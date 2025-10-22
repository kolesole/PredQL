import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, BASE_DIR)

from sqlalchemy import *
from antlr4 import *
from antlr4_parser.Lexer_PQL import Lexer_PQL
from antlr4_parser.Parser_PQL import Parser_PQL 
from pql_visitor.PQLVisitor import PQLVisitor

class PQLConverter:
    def __init__(self, eng_url : str, start_time):
        self.engine = create_engine(eng_url)
        self.metadata = MetaData(bind=self.engine)
        self.metadata.reflect()

        self.start_time = start_time

        self.pql_visitor = PQLVisitor()


    def parse_query(self, query : str):
        input_stream = InputStream(query)
        lexer = Lexer_PQL(input_stream)
        token_stream = CommonTokenStream(lexer)
        
        parser = Parser_PQL(token_stream)
        tree = parser.query()

        query_dict = self.pql_visitor.visit(tree)
        return query_dict 
      
    
    def convert(self, query : str):
        query_dict = self.parse_query(query)

        stmt = None
        for qpart in query_dict["Qparts"]:
            qtype = qpart["QType"]
 
            match qtype:
                case "assuming":
                    stmt_part = self._build_assuming_query(qpart)    
                case "for_each":
                    stmt_part = self._build_for_each_query(qpart)
                case "predict":
                    stmt_part = self._build_predict_query(qpart)
                case "where":
                    stmt_part = self._build_where_query(qpart)
                case _:
                    pass
            stmt = stmt_part if stmt == None else stmt.where(and_(stmt._whereclause, stmt_part._whereclause))

        with engine.connect() as conn:
            res = conn.execute(stmt).mappings().all()

        return res 
    

    def _build_assuming_query(self, query_dict : dict):
        conditions = query_dict["Conditions"]
        logicalOps = query_dict["LogicalOps"]

        exprs = [self._build_condition(cond) for cond in conditions]
        if not logicalOps:
            return exprs[0]
        
        res = exprs[0]
        for op, expr in zip(logicalOps, exprs[1:]):
            match op.lower():
                case "and":
                    res = and_(res, expr)
                case "or":
                    res = or_(res, expr)
                case _:
                    pass

        return res
    

    def _build_for_each_query(self, query_dict : dict):
        table_name = query_dict["Table"]
        column_name = query_dict["Column"]

        table = self.metadata.tables[table_name]
        column = table.c[column_name] if column_name != "*" else table.c[list(table.c.keys())[0]]

        return column
    

    def _build_predict_query(self, query_dict : dict):
        pred_type = query_dict["PredType"]

        expr = None
        match pred_type:
            case "aggregation":
                expr = self._build_aggregation(query_dict["Aggregation"])
            case "condition":
                expr = self._build_condition(query_dict["Condition"])
            case "id_dot_id":
                expr = self._build_id_dot_id(query_dict)
            case _:
                pass




    def _build_where_query(self, query_dict : dict):
        conditions = query_dict["Conditions"]
        logicalOps = query_dict["LogicalOps"]

        exprs = [self._build_condition(cond) for cond in conditions]
        if not logicalOps:
            return exprs[0]
        
        res = exprs[0]
        for op, expr in zip(logicalOps, exprs[1:]):
            match op.lower():
                case "and":
                    res = and_(res, expr)
                case "or":
                    res = or_(res, expr)
                case _:
                    pass

        return res
    

    def _build_condition(self, cond_dict : dict):
        ctype = cond_dict["CType"]
        cond_type = cond_dict["CondType"]

        expr = None
        match cond_type:
            case "aggregation":
                expr = self._build_aggregation(cond_dict["Aggregation"])
            case "id_dot_id":
                expr = self._build_id_dot_id(cond_dict)
            case _:
                pass
        
        cond = None
        match ctype:
            case "num":
                cond = self._build_num_condition(cond_dict)
            case "str":
                cond = self._build_str_condition(cond_dict)
            case "null":
                cond = self._build_null_check_condition(cond_dict)
            case _:
                pass
        
        return cond(expr)
    

    def _build_num_condition(self, cond_dict : dict):
        tmp = cond_dict["N"]
        N = float(tmp) if "." in tmp else int(tmp)

        comp_op = cond_dict["CompOp"]
        match comp_op:
            case "!=":
                return lambda expr : expr != N
            case "<":
                return lambda expr : expr < N
            case "<=":
                return lambda expr : expr <= N
            case "==":
                return lambda expr : expr == N
            case ">":
                return lambda expr : expr > N
            case ">=":
                return lambda expr : expr >= N
            case _:
                pass


    def _build_str_condition(self, cond_dict : dict):
        string = cond_dict["String"]

        comp_op = cond_dict["CompOp"].lower()
        match comp_op:
            case "not like":
                return lambda expr : expr.not_like(string)
            case "not contains":
                return lambda expr : ~expr.contains(string)
            case "ends with":
                return lambda expr : expr.endswith(string)
            case "starts with":
                return lambda expr : expr.startswith(string)
            case "like":
                return lambda expr : expr.like(string)
            case "contains":
                return lambda expr : expr.contains(string)
            case "=":
                return lambda expr : expr == string
            case _:
                pass

    def _build_null_check_condition(self, cond_dict : dict):
        check_op = cond_dict["CheckOp"].lower()
        match check_op:
            case "is not null":
                return lambda expr : expr.is_not(None)
            case "is null":
                return lambda expr : expr.is_(None)
            case _:
                pass


    def _build_aggregation(self, aggr_dict : dict):
        aggr_type = aggr_dict["AggrType"].lower()
        table_name = aggr_dict["Table"]
        column_name = aggr_dict["Column"]

        table = self.metadata.tables[table_name]

        where = aggr_dict["Where"]
        if where:
            where_expr = self._build_where_query(where)
            table = select(table).where(where_expr).subquery()

        column = table.c[column_name] if column_name != "*" else table.c[list(table.c.keys())[0]]
      
        match aggr_type:
            case "avg":
                return func.avg(column)
            case "count":
                return func.count(column)
            case "count_distinct":
                return func.count(column.distinct())
            case "first":
                pass
            case "last":
                pass
            case "list_distinct":
                return func.array_agg(column.distinct())
            case "max":
                return func.max(column)
            case "min":
                return func.min(column)
            case "sum":
                return func.sum(column)
            case _:
                pass

    
    def _build_id_dot_id(self, some_dict : dict):
        table_name = some_dict["Table"]
        column_name = some_dict["Column"]
        table = self.metadata.tables[table_name]
        expr = table.c[column_name] if column_name != "*" else table.c[list(table.c.keys())[0]]
        
        return expr


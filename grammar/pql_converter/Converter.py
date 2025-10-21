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
    def __init__(self, eng_url, start_time):
        self.engine = create_engine(eng_url)
        self.metadata = MetaData(bind=self.engine)
        self.metadata.reflect()

        self.start_time = start_time

        self.pql_visitor = PQLVisitor()

    def parse_query(self, query):
        input_stream = InputStream(query)
        lexer = Lexer_PQL(input_stream)
        token_stream = CommonTokenStream(lexer)
        
        parser = Parser_PQL(token_stream)
        tree = parser.query()

        query_dict = self.pql_visitor.visit(tree)
        return query_dict   
    
    def convert(self, query):
        query_dict = self.parse_query(query)

        stmt = None
        for qpart in query_dict["Qparts"]:
            qtype = qpart["QType"]
 
            match qtype:
                case "assuming":
                    stmt_part = self._build_assuming_query(qpart)    
                case "for_each":
                    stmt_part = self._build_for_each_query(qpart)
                case "predict" if qpart["PredType"] == "aggregation":
                    stmt_part = self._build_predict_aggr_query(qpart)
                case "predict" if qpart["PredType"] == "condition":
                    stmt_part = self._build_predict_cond_query(qpart)
                case "predict" if qpart["PredType"] == "id_dot_id":
                    stmt_part = self._build_predict_idi_query(qpart)
                case "where":
                    stmt_part = self._build_where_query(qpart)
                case _:
                    pass
            stmt = stmt_part if stmt == None else stmt.where(and_(stmt._whereclause, stmt_part._whereclause))

        with engine.connect() as conn:
            res = conn.execute(stmt).mappings().all()

        return res 

    def _build_assuming_query(self, query_dict):
        pass

    def _build_for_each_query(self, query_dict):
        pass

    def _build_predict_aggr_query(self, query_dict):
        pass

    def _build_predict_cond_query(self, query_dict):
        pass

    def _build_predict_idi_query(self, query__dict):
        pass

    def _build_where_query(self, query_dict):
        pass

    def _build_condition(self, cond_dict):
        ctype = cond_dict["CType"]
        match ctype:
            case "num":
                return self._build_num_condition(cond_dict)
            case "str":
                return self._build_str_condition(cond_dict)
            case "null":
                return self._build_null_check_condition(cond_dict)
            case _:
                pass

    def _build_num_condition(self, cond_dict):
        pass

    def _build_str_condition(self, cond_dict):
        pass

    def _build_null_check_condition(self, cond_dict):
        pass

    def _build_aggregation(self, aggr_dict):
        aggr_type = aggr_dict["AggrType"].lower()
        table_name = aggr_dict["Table"]
        column_name = aggr_dict["Column"]

        table = self.metadata.tables[table_name]

        where = aggr_dict["Where"]
        if where:
            where_expr = self._build_where_query(where)
            table = select(table).where(where_expr).subquery()

        column = table.c[column_name] if column_name != "*" else table.c[list(table.c.keys())[0]]
        # ???????????????????????????????????????????????
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








    
    


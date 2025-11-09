import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, BASE_DIR)

from sqlalchemy import *
from relbench.base import *
from datetime import datetime
import pandas as pd
import duckdb
from typing import Tuple

from antlr4 import *
from grammar.antlr4_parser.Lexer_PQL import Lexer_PQL
from grammar.antlr4_parser.Parser_PQL import Parser_PQL 
from utils import *
from grammar.pql_visitor.PQLVisitor import PQLVisitor

class PQLConverter:
    def __init__(self, db : Database):
        self.db = db
        self.timestamps = None
        self.pql_visitor = PQLVisitor()

        # self.conn = duckdb.connect()
        # for name, table in db.table_dict.items():
        #     self.conn.register(name, table.df)

        # self.engine = create_engine(eng_url)
        # self.metadata = MetaData(bind=self.engine)
        # self.metadata.reflect()

        # self.cur_time = cur_time


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

        query_parts = query_dict["Qparts"]

        # find for each(we need this to "group by" something)

        for_each_dict = None
        for qpart in query_parts:
            if qpart["QType"] == "for_each":
                for_each_dict = qpart
                break

        ptable_name = for_each_dict["Table"]
        ppk_name = for_each_dict["Column"]
        ptable = self.db.table_dict[ptable_name]
        ptable_df = ptable.df

    
        if for_each_dict["Where"]:
            ptable_df = self.apply_where(for_each_dict["Where"], ptable_name, ptable_df, ppk_name)

        for qpart in query_parts:
            match qpart["QType"]:
                case "for_each":
                    continue
                case "assuming":
                    ptable_df = self.apply_assuming(qpart, ptable_name, ptable_df, ppk_name)
                case "predict":
                    ptable_df = self.apply_predict(qpart, ptable_name, ptable_df, ppk_name)
                case "where":
                    ptable_df = self.apply_where(qpart, ptable_name, ptable_df, ppk_name)
                case _:
                    pass
        
        return Table(
            df=ptable_df,
            fkey_col_to_pkey_table=None,
            pkey_col=None,
            time_col="timestamp",
            )
    

    def apply_assuming(self, 
                       query_dict : dict,
                       ptable_name : str, 
                       ptable_df : pd.DataFrame, 
                       ppk_name : str) -> pd.DataFrame:
        # vyfiltruje tablku a vrati ji
        conditions = query_dict["Conditions"]
        logicalOps = query_dict["LogicalOps"]

        filtered_tables = [
            self.apply_condition(cond, ptable_name, ptable_df, ppk_name)
            for cond in conditions
        ]

        fks = [
            self.find_fk_name(ftable_name, self.db.table_dict[ftable_name], ptable_name, ppk_name)
            for ftable_name, ftable_df in filtered_tables  
        ]

        if len(filtered_tables) == 1:
            return pd.merge(ptable_df, filtered_tables[0][1], left_on=ppk_name, right_on=fks[0], how="left")
        
        
        # TODO for several conditions

        # res_query = subqueries[0]
        # for op, subq in zip(logicalOps, subqueries[1:]):
        #     match op.lower():
        #         case "and":
        #             res_query = select(res_query.c[0]).intersect(select(subq.c[0])).subquery()
        #         case "or":
        #             res_query = select(res_query.c[0]).union(select(subq.c[0])).subquery()
        #         case _:
        #             pass
        
        # return res_query
    

    def apply_predict(self, 
                      query_dict : dict,
                      ptable_name : str, 
                      ptable_df : pd.DataFrame, 
                      ppk_name : str) -> pd.DataFrame:
        
        pass
        
        # pred_type = query_dict["PredType"]

        # subquery = None
        # subquery_fk = None
        # table_name = None
        # match pred_type:
        #     case "aggregation":
        #         subquery, subquery_fk = self._build_aggregation(query_dict["Aggregation"], 
        #                                        parent_table_name, 
        #                                        parent_pk_name, 
        #                                        time_column_name)
        #         table_name = query_dict["Aggregation"]["Table"]
        #     case "condition":
        #         subquery, subquery_fk = self._build_condition(query_dict["Condition"], 
        #                                      parent_table_name, 
        #                                      parent_pk_name, 
        #                                      time_column_name)
        #         table_name = query_dict["Condition"]["Table"]
        #     case "id_dot_id":
        #         subquery = self._build_id_dot_id(query_dict)
        #         table_name = query_dict["Table"]
        #     case _:
        #         pass
        
        # table = self.metadata.tables(table_name)
        # table_pk_name = self._find_child_column_name(table_name, parent_table_name, parent_pk_name)
        # table_pk = table.c[table_pk_name]
        # res_query = (
        #     select(
        #         table,
        #         case(
        #             (exists(select(1).select_from(subquery)
        #                     .where(subquery_fk == table_pk)), True),
        #             else_=False).label("label")
        #         )
        # )

        # return res_query


    def apply_where(self, 
                    query_dict : dict,
                    ptable_name : str, 
                    ptable_df : pd.DataFrame, 
                    ppk_name : str) -> pd.DataFrame:
        conditions = query_dict["Conditions"]
        logicalOps = query_dict["LogicalOps"]

        filtered_tables = [
            self.apply_condition(cond, ptable_name, ptable_df, ppk_name)
            for cond in conditions
        ]

        fks = [
            self.find_fk_name(ftable_name, self.db.table_dict[ftable_name], ptable_name, ppk_name)
            for ftable_name, ftable_df in filtered_tables  
        ]

        if len(filtered_tables) == 1:
            # filtered = pd.merge(ptable_df, filtered_tables[0][1], left_on=ppk_name, right_on=fks[0], how="left", indicator=True)
            # filtered = filtered[filtered["_merge"] == "both"]
            # filtered = filtered[ptable_df.columns]

            valid_keys = filtered_tables[0][1][fks[0]].unique()
            filtered = ptable_df[ptable_df[ppk_name].isin(valid_keys)]
            return filtered
        
        # TODO for several conditions
        # for op, subq in zip(logicalOps, filtered_tables[1:]):
        #     match op.lower():
        #         case "and":
        #             res_query = (
        #                 select(res_query.c[0])
        #                 .intersect(select(subq.c[0]))
        #             ).subquery()
        #         case "or":
        #             res_query = (
        #                 select(res_query.c[0])
        #                 .union(select(subq.c[0]))
        #             ).subquery()
        #         case _:
        #             pass
        
        # return res_query

        # subqueries = [
        #     self._build_condition(cond, parent_table_name, parent_pk_name, time_column_name)[0] 
        #     for cond in conditions
        # ]

        # if len(subqueries) == 1:
        #     return subqueries[0]
        
        # parent_table = self.metadata.tables[parent_table_name]
        # parent_pk = parent_table.c[parent_pk_name]
        
        # res_query = subqueries[0]
        # for op, subq in zip(logicalOps, subqueries[1:]):
        #     match op.lower():
        #         case "and":
        #             res_query = (
        #                 select(res_query.c[0])
        #                 .intersect(select(subq.c[0]))
        #             ).subquery()
        #         case "or":
        #             res_query = (
        #                 select(res_query.c[0])
        #                 .union(select(subq.c[0]))
        #             ).subquery()
        #         case _:
        #             pass
        
        # return res_query
    

    def apply_condition(self, 
                       cond_dict : dict,
                       ptable_name : str, 
                       ptable_df : pd.DataFrame, 
                       ppk_name : str) -> Tuple[str, pd.DataFrame]:
        ctype = cond_dict["CType"]
        cond_type = cond_dict["CondType"]
        
        table_name = None
        filter_col = None
        match cond_type:
            case "aggregation":
                table_name = cond_dict["Aggregation"]["Table"]
                filter_col = self.apply_aggregation(cond_dict["Aggregation"], ptable_name, ptable_df, ppk_name)
            case "id_dot_id":
                table_name = cond_dict["Table"]
                # TODO can be "*"
                filter_col_name = cond_dict["Column"]
                filter_col = self.db.table_dict[table_name].df[filter_col_name]
            case _:
                pass
        table = self.db.table_dict[table_name]
        table_df = table.df
        
        cond_filter = None
        match ctype:
            case "num":
                cond_filter = gen_num_filter(cond_dict)
            case "str":
                cond_filter = gen_str_filter(cond_dict)
            case "null":
                cond_filter = gen_null_filter(cond_dict)
            case _:
                pass
        
        ex = filter_col[0]
        if type(ex) == str:
            mask = filter_col.str.contains(r"\s", regex=True)
            # print(table_df[table_df[filter_col_name] == 'Max'])
        mask = cond_filter(table_df, filter_col_name)
        print(mask, table_df[mask])
        return table_name, table_df[mask]

        # expr = None
        # table_name = None
        # match cond_type:
        #     case "aggregation":
        #         aggr_table = self._build_aggregation(cond_dict["Aggregation"], 
        #                                              parent_table_name, 
        #                                              parent_pk_name, 
        #                                              time_column_name)[0]
        #         expr = aggr_table.c["aggr_value"]
        #         table_name = cond_dict["Aggregation"]["Table"]
        #     case "id_dot_id":
        #         expr = self._build_id_dot_id(cond_dict)
        #         table_name = cond_dict["Table"]
        #     case _:
        #         pass
        
        # cond = None
        # match ctype:
        #     case "num":
        #         cond = gen_num_condition(cond_dict)
        #     case "str":
        #         cond = gen_str_condition(cond_dict)
        #     case "null":
        #         cond = gen_null_check_condition(cond_dict)
        #     case _:
        #         pass
        
        # table = self.metadata.tables[table_name]
        # parent_table = self.metadata.tables[parent_table_name]
        # parent_pk = parent_table.c[parent_pk_name]
        # time_column = table.c[time_column_name]

        # stmt = None
        # if table is parent_table:
        #     stmt = (
        #         select(table)
        #         .where(and_(cond(expr), time_column <= self.cur_time))
        #     ).subquery()
        # else:
        #     child_fk_name = self._find_child_column_name(table_name, parent_table_name, parent_pk_name)
        #     child_fk = table.c[child_fk_name]
        #     stmt = (
        #         select(table)
        #         .select_from(
        #             parent_table.join(table, parent_pk == child_fk)
        #         )
        #         .where(and_(cond(expr), time_column <= self.cur_time))
        #     ).subquery()

        # return stmt, child_fk
    

    def apply_aggregation(self, 
                          aggr_dict : dict,
                          ptable_name : str, 
                          ptable_df : pd.DataFrame, 
                          ppk_name : str) -> pd.Series:
        aggr_type = aggr_dict["AggrType"].lower()
        table_name = aggr_dict["Table"]
        column_name = aggr_dict["Column"]

        table = self.db.table_dict[table_name]
        table_df = table.df.copy()
        fk = self.find_fk_name(table_name, table, ptable_name, ppk_name)

        aggr_func = gen_aggr_func(aggr_type)

        # TODO where in aggregation
        # where = aggr_dict["Where"]
        # if where:
        #     table = 

        # TODO column_name can be "*"

        aggr_col = table_df.groupby(fk)[column_name].transform(aggr_func)

        return aggr_col


    def find_fk_name(self, 
                     ctable_name : str, 
                     ctable : Table, 
                     ptable_name : str,
                     ppk_name) -> str:
        if ctable_name == ptable_name:
            return ppk_name
        
        for k, v in ctable.fkey_col_to_pkey_table.items():
            if v == ptable_name:
                return k
        
        return ""


        # column = table.c[column_name] if column_name != "*" else table.c[list(table.c.keys())[0]]
        
        # aggr_op = gen_aggr_op(aggr_type)
        # time_column = table.c[time_column_name]

        # parent_table = self.metadata.tables[parent_table_name]
        # parent_pk = parent_table.c[parent_pk_name]

        # child_fk_name = self._find_child_column_name(table, parent_table_name, parent_pk_name)
        # child_fk = table.c[child_fk_name]

        # aggregation = aggr_op(column).label("aggr_value")

        # stmt = select(child_fk, aggregation).select_from(table)
        
        # # time filter

        # start = aggr_dict["Start"]
        # end = aggr_dict["End"]
        # time_unit = aggr_dict["MeasureUnit"]

        # if start is not None and end is not None and time_unit is not None:
        #     time_unit = time_unit.lower()
        #     time_filter = and_(
        #             time_column >= self.cur_time + text(f"interval '{start} {time_unit}'"),
        #             time_column <= self.cur_time + text(f"interval '{end} {time_unit}'")
        #     )
        #     stmt = stmt.where(time_filter)

        # stmt = stmt.group_by(child_fk)


        # return (stmt.subquery(), child_fk)

    
    # def apply_id_dot_id(self, some_dict : dict):
    #     #TODO
    #     table_name = some_dict["Table"]
    #     column_name = some_dict["Column"]
    #     table = self.metadata.tables[table_name]
    #     expr = table.c[column_name] if column_name != "*" else table.c[list(table.c.keys())[0]]
        
    #     #time filtering

    #     return expr

        
    

    # def _find_child_column_name(self, child_table_name, parent_table_name, parent_pk_name):
    #     child_table = self.metadata.tables[child_table_name]
    #     parent_table = self.metadata.tables[parent_table_name]

    #     parent_pk = parent_table.c[parent_pk_name]

    #     for fk in child_table.foreign_keys:
    #         if fk.column is parent_pk:
    #             return fk.parent.name
        

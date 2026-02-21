"""Visitor implementation for traversing PredQL parse trees."""

from predql.parser import ParserPredQL, ParserPredQLVisitor
from predql.visitor.parsed_value import ParsedValue


class Visitor(ParserPredQLVisitor):
    """Visitor class for converting PredQL parse trees to dictionaries."""
    
    # Visit a parse tree produced by ParserPredQL#query.
    def visitQuery(self, ctx:ParserPredQL.QueryContext):
        query_tmp = self._rule2value(ctx.query_tmp())
        query_stat = self._rule2value(ctx.query_stat())
        
        query_dict = {"QueryTmp" : query_tmp,
                      "QueryStat": query_stat
                     }
        return query_dict


    # Visit a parse tree produced by ParserPredQL#query_tmp.
    def visitQuery_tmp(self, ctx:ParserPredQL.Query_tmpContext):
        predict = self._rule2value(ctx.predict_tmp())
        for_each = self._rule2value(ctx.for_each())
        assuming = self._rule2value(ctx.assuming())
        where = self._rule2value(ctx.where_tmp())   

        query_dict = {"Predict" : predict,
                      "ForEach" : for_each,
                      "Assuming": assuming,
                      "Where"   : where
                     }
        return query_dict


    # Visit a parse tree produced by ParserPredQL#query_stat.
    def visitQuery_stat(self, ctx:ParserPredQL.Query_statContext):
        predict = self._rule2value(ctx.predict_stat())
        for_each = self._rule2value(ctx.for_each())
        where = self._rule2value(ctx.where_stat())

        query_dict = {"Predict": predict,
                      "ForEach": for_each,
                      "Where"  : where
                     }
        return query_dict


    # Visit a parse tree produced by ParserPredQL#for_each.
    def visitFor_each(self, ctx:ParserPredQL.For_eachContext):
        table = self._node2value(ctx.ID(0))
        column = self._node2value(ctx.ID(1))
        where = self._rule2value(ctx.where_stat())
        
        for_each_dict = {"Table" : table,
                         "Column": column,
                         "Where" : where
                        }
        return for_each_dict


    # Visit a parse tree produced by ParserPredQL#predict_tmp.
    def visitPredict_tmp(self, ctx:ParserPredQL.Predict_tmpContext):
        if ctx.aggregation_tmp():
            pred_type = "aggregation"
        elif ctx.expr_or_tmp():
            pred_type = "expr"
        
        aggregation = self._rule2value(ctx.aggregation_tmp())
        expr = self._rule2value(ctx.expr_or_tmp())

        rank_top = self._node2value(ctx.RANK_TOP())
        K = self._node2value(ctx.INT())
        classify = self._node2value(ctx.CLASSIFY())

        predict_dict = {"PredType"   : pred_type,
                        "Aggregation": aggregation,
                        "Expr"       : expr,
                        "RankTop"    : rank_top,
                        "K"          : K,
                        "Classify"   : classify
                       }
        return predict_dict


    # Visit a parse tree produced by ParserPredQL#predict_stat.
    def visitPredict_stat(self, ctx:ParserPredQL.Predict_statContext):
        if ctx.aggregation_stat():
            pred_type = "aggregation"
        elif ctx.expr_or_stat():
            pred_type = "expr"
        else:
            pred_type = "id_dot_id"
        
        aggregation = self._rule2value(ctx.aggregation_stat())
        expr = self._rule2value(ctx.expr_or_stat())
        table = self._node2value(ctx.ID(0))
        column = self._node2value(ctx.STAR() if ctx.STAR() else ctx.ID(1))

        rank_top = self._node2value(ctx.RANK_TOP())
        K = self._node2value(ctx.INT())
        classify = self._node2value(ctx.CLASSIFY())

        predict_dict = {"PredType"   : pred_type,
                        "Aggregation": aggregation,
                        "Expr"       : expr,
                        "Table"      : table,
                        "Column"     : column,
                        "RankTop"    : rank_top,
                        "K"          : K,
                        "Classify"   : classify
                       }
        return predict_dict


    # Visit a parse tree produced by ParserPredQL#assuming.
    def visitAssuming(self, ctx:ParserPredQL.AssumingContext):
        expr = self._rule2value(ctx.expr_or_tmp())

        assuming_dict = {"Expr": expr}
        return assuming_dict


    # Visit a parse tree produced by ParserPredQL#where_tmp.
    def visitWhere_tmp(self, ctx:ParserPredQL.Where_tmpContext):
        expr = self._rule2value(ctx.expr_or_tmp())
        
        where_dict = {"Expr": expr}
        return where_dict


    # Visit a parse tree produced by ParserPredQL#where_stat.
    def visitWhere_stat(self, ctx:ParserPredQL.Where_statContext):
        expr = self._rule2value(ctx.expr_or_stat())
        
        where_dict = {"Expr": expr}
        return where_dict


    # Visit a parse tree produced by ParserPredQL#expr_or_tmp.
    def visitExpr_or_tmp(self, ctx:ParserPredQL.Expr_or_tmpContext):
        if len(ctx.expr_and_tmp()) == 1:
            return self.visit(ctx.expr_and_tmp(0))

        expr_dict = self.visit(ctx.expr_and_tmp(0))
        for i in range(1, len(ctx.expr_and_tmp())):
            right = self.visit(ctx.expr_and_tmp(i))
            expr_dict = {"Op"       : self._node2value(ctx.OR(i-1)),
                         "LeftExpr" : expr_dict,
                         "RightExpr": right
                     }
            
        return expr_dict


    # Visit a parse tree produced by ParserPredQL#expr_or_stat.
    def visitExpr_or_stat(self, ctx:ParserPredQL.Expr_or_statContext):
        if len(ctx.expr_and_stat()) == 1:
            return self.visit(ctx.expr_and_stat(0))

        expr_dict = self.visit(ctx.expr_and_stat(0))
        for i in range(1, len(ctx.expr_and_stat())):
            right = self.visit(ctx.expr_and_stat(i))
            expr_dict = {"Op"       : self._node2value(ctx.OR(i-1)),
                         "LeftExpr" : expr_dict,
                         "RightExpr": right
                     }
            
        return expr_dict


    # Visit a parse tree produced by ParserPredQL#expr_and_tmp.
    def visitExpr_and_tmp(self, ctx:ParserPredQL.Expr_and_tmpContext):
        if len(ctx.expr_term_tmp()) == 1:
            return self.visit(ctx.expr_term_tmp(0))

        expr_dict = self.visit(ctx.expr_term_tmp(0))
        for i in range(1, len(ctx.expr_term_tmp())):
            right = self.visit(ctx.expr_term_tmp(i))
            expr_dict = {"Op"       : self._node2value(ctx.AND(i-1)),
                         "LeftExpr" : expr_dict,
                         "RightExpr": right
                        }

        return expr_dict


    # Visit a parse tree produced by ParserPredQL#expr_and_stat.
    def visitExpr_and_stat(self, ctx:ParserPredQL.Expr_and_statContext):
        if len(ctx.expr_term_stat()) == 1:
            return self.visit(ctx.expr_term_stat(0))

        expr_dict = self.visit(ctx.expr_term_stat(0))
        for i in range(1, len(ctx.expr_term_stat())):
            right = self.visit(ctx.expr_term_stat(i))
            expr_dict = {"Op"       : self._node2value(ctx.AND(i-1)),
                         "LeftExpr" : expr_dict,
                         "RightExpr": right
                        }

        return expr_dict


    # Visit a parse tree produced by ParserPredQL#expr_term_tmp.
    def visitExpr_term_tmp(self, ctx:ParserPredQL.Expr_term_tmpContext):
        if ctx.condition_tmp():
            return self._rule2value(ctx.condition_tmp())
        elif ctx.expr_or_tmp():
            return self.visit(ctx.expr_or_tmp())


    # Visit a parse tree produced by ParserPredQL#expr_term_stat.
    def visitExpr_term_stat(self, ctx:ParserPredQL.Expr_term_statContext):
        if ctx.condition_stat():
            return self._rule2value(ctx.condition_stat())
        elif ctx.expr_or_stat():
            return self.visit(ctx.expr_or_stat())


    # Visit a parse tree produced by ParserPredQL#condition_tmp.
    def visitCondition_tmp(self, ctx:ParserPredQL.Condition_tmpContext):
        if ctx.num_condition():
            cond_dict = self.visit(ctx.num_condition())
        elif ctx.str_condition():
            cond_dict = self.visit(ctx.str_condition())
        elif ctx.null_check_condition():
            cond_dict = self.visit(ctx.null_check_condition())

        cond_dict["CondType"] = "aggregation"
        cond_dict["NOT"] = self._node2value(ctx.NOT())
        cond_dict["Aggregation"] = self._rule2value(ctx.aggregation_tmp())
        return cond_dict


    # Visit a parse tree produced by ParserPredQL#condition_stat.
    def visitCondition_stat(self, ctx:ParserPredQL.Condition_statContext):
        if ctx.aggregation_stat():
            cond_type = "aggregation"
        else:
            cond_type = "id_dot_id"

        if ctx.num_condition():
            cond_dict = self.visit(ctx.num_condition())
        elif ctx.str_condition():
            cond_dict = self.visit(ctx.str_condition())
        elif ctx.null_check_condition():
            cond_dict = self.visit(ctx.null_check_condition())

        cond_dict["CondType"] = cond_type
        cond_dict["NOT"] = self._node2value(ctx.NOT())
        cond_dict["Aggregation"] = self._rule2value(ctx.aggregation_stat())
        cond_dict["Table"] = self._node2value(ctx.ID(0))
        cond_dict["Column"] = self._node2value(ctx.STAR() if ctx.STAR() else ctx.ID(1))
        return cond_dict


    # Visit a parse tree produced by ParserPredQL#num_condition.
    def visitNum_condition(self, ctx:ParserPredQL.Num_conditionContext):
        ctype = "num"
        comp_op = self._node2value(ctx.NUM_COMP_OP())

        if ctx.DATETIME():
            N = self._node2value(ctx.DATETIME())
        elif ctx.FLOAT():
            N = self._node2value(ctx.FLOAT())
        elif ctx.INT():
            N = self._node2value(ctx.INT())

        num_cond_dict = {"CType"  : ctype,
                         "CompOp" : comp_op,
                         "N"      : N
                        }
        return num_cond_dict


    # Visit a parse tree produced by ParserPredQL#str_condition.
    def visitStr_condition(self, ctx:ParserPredQL.Str_conditionContext):
        ctype = "str"
        comp_op = self._node2value(ctx.STR_COMP_OP())
        string = self._node2value(ctx.STRING())

        string_cond_dict = {"CType"  : ctype,
                            "CompOp" : comp_op,
                            "String" : string
                           }
        return string_cond_dict


    # Visit a parse tree produced by ParserPredQL#null_check_condition.
    def visitNull_check_condition(self, ctx:ParserPredQL.Null_check_conditionContext):
        ctype = "null"
        check_op = self._node2value(ctx.NULL_CHECK_OP())

        null_cond_dict = {"CType"   : ctype,
                          "CheckOp" : check_op
                         }
        return null_cond_dict


    # Visit a parse tree produced by ParserPredQL#aggregation_tmp.
    def visitAggregation_tmp(self, ctx:ParserPredQL.Aggregation_tmpContext):
        aggr_type = self._node2value(ctx.AGGR_FUNC())
        table = self._node2value(ctx.ID(0))
        column = self._node2value(ctx.STAR() if ctx.STAR() else ctx.ID(1))
        where = self._rule2value(ctx.where_stat())
        start = self._node2value(ctx.INT(0))
        end = self._node2value(ctx.INT(1))
        measure_unit = self._node2value(ctx.TIME_MEASURE_UNIT())

        aggr_dict = {"AggrType"    : aggr_type,
                     "Table"       : table,
                     "Column"      : column,
                     "Where"       : where,
                     "Start"       : start,
                     "End"         : end,
                     "MeasureUnit" : measure_unit
                    }
        return aggr_dict


    # Visit a parse tree produced by ParserPredQL#aggregation_stat.
    def visitAggregation_stat(self, ctx:ParserPredQL.Aggregation_statContext):
        aggr_type = self._node2value(ctx.AGGR_FUNC())
        table = self._node2value(ctx.ID(0))
        column = self._node2value(ctx.STAR() if ctx.STAR() else ctx.ID(1))
        where = self._rule2value(ctx.where_stat())

        aggr_dict = {"AggrType"    : aggr_type,
                     "Table"       : table,
                     "Column"      : column,
                     "Where"       : where,
                    }
        return aggr_dict



    def _node2value(self, node) -> ParsedValue:
        
        if not node:
            return None

        token = node.getSymbol()
        return ParsedValue(value=token.text, 
                           line=token.line, 
                           column=token.column)


    def _rule2value(self, ctx) -> ParsedValue:

        if not ctx:
            return None
        
        return ParsedValue(value=self.visit(ctx),
                           line=ctx.start.line,
                           column=ctx.start.column)

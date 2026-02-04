"""Visitor implementation for traversing PredQL parse trees."""

from predql.parser import ParserPredQL, ParserPredQLVisitor
from predql.visitor.parsed_value import ParsedValue


class Visitor(ParserPredQLVisitor):
    """Visitor class for converting PredQL parse trees to dictionaries."""
    
    # Visit a parse tree produced by ParserPredQL#query.
    def visitQuery(self, ctx:ParserPredQL.QueryContext):
        predict = self._rule2value(ctx.predict())
        for_each = self._rule2value(ctx.for_each())
        assuming = self._rule2value(ctx.assuming())
        where = self._rule2value(ctx.where())

        query_dict = {"Predict" : predict,
                      "ForEach" : for_each,
                      "Assuming": assuming,
                      "Where"   : where
                     }
        return query_dict


    # Visit a parse tree produced by ParserPredQL#assuming.
    def visitAssuming(self, ctx:ParserPredQL.AssumingContext):
        qtype = "assuming"
        expr = self._rule2value(ctx.expr_or())

        assuming_dict = {"QType" : qtype,
                         "Expr"  : expr
                        }
        return assuming_dict


    # Visit a parse tree produced by ParserPredQL#for_each.
    def visitFor_each(self, ctx:ParserPredQL.For_eachContext):
        qtype = "for_each"

        table = self._node2value(ctx.ID(0))
        column = self._node2value(ctx.ID(1))
        where = self._rule2value(ctx.where())

        for_each_dict = {"QType" : qtype,
                         "Table" : table,
                         "Column": column,
                         "Where" : where
                        }
        return for_each_dict


    # Visit a parse tree produced by ParserPredQL#predict.
    def visitPredict(self, ctx:ParserPredQL.PredictContext):
        qtype = "predict"
        pred_type = None
        aggregation = None
        expr = None
        table = None
        column = None

        if ctx.aggregation():
            pred_type = "aggregation"
            aggregation = self._rule2value(ctx.aggregation())
        elif ctx.expr_or():
            pred_type = "expr"
            expr = self._rule2value(ctx.expr_or())
        else:
            pred_type = "id_dot_id"
            table = self._node2value(ctx.ID(0))
            column = self._node2value(ctx.STAR() if ctx.STAR() else ctx.ID(1))
        
        rank_top = self._node2value(ctx.RANK_TOP())
        K = self._node2value(ctx.INT())
        classify = self._node2value(ctx.CLASSIFY())

        predict_dict = {"QType"       : qtype,
                        "PredType"    : pred_type,
                        "Aggregation" : aggregation,
                        "Expr"        : expr,
                        "Table"       : table,
                        "Column"      : column,
                        "RankTop"     : rank_top,
                        "K"           : K,
                        "Classify"    : classify
                       }
        return predict_dict


    # Visit a parse tree produced by ParserPredQL#where.
    def visitWhere(self, ctx:ParserPredQL.WhereContext):
        qtype = "where"
        expr = self._rule2value(ctx.expr_or())

        where_dict = {"QType" : qtype,
                      "Expr"  : expr
                     }
        return where_dict

    # Visit a parse tree produced by ParserPredQL#expr_or.
    def visitExpr_or(self, ctx:ParserPredQL.Expr_orContext):
        expr_dict = None
        if len(ctx.expr_and()) == 1:
            return self.visit(ctx.expr_and(0))

        expr_dict = self.visit(ctx.expr_and(0))
        for i in range(1, len(ctx.expr_and())):
            right = self.visit(ctx.expr_and(i))
            expr_dict = {"Op"   : self._node2value(ctx.OR(i-1)),
                         "Left" : expr_dict,
                         "Right": right
                     }

        return expr_dict


    # Visit a parse tree produced by ParserPredQL#expr_and.
    def visitExpr_and(self, ctx:ParserPredQL.Expr_andContext):
        if len(ctx.expr_term()) == 1:
            return self.visit(ctx.expr_term(0))

        expr_dict = self.visit(ctx.expr_term(0))
        for i in range(1, len(ctx.expr_term())):
            right = self.visit(ctx.expr_term(i))
            expr_dict = {"Op"   : self._node2value(ctx.AND(i-1)),
                         "Left" : expr_dict,
                         "Right": right
                        }

        return expr_dict


    # Visit a parse tree produced by ParserPredQL#expr_term.
    def visitExpr_term(self, ctx:ParserPredQL.Expr_termContext):
        if ctx.condition():
            return self._rule2value(ctx.condition())
        elif ctx.expr_or():
            return self.visit(ctx.expr_or())


    # Visit a parse tree produced by ParserPredQL#condition.
    def visitCondition(self, ctx:ParserPredQL.ConditionContext):
        cond_dict = None
        cond_type = None
        NOT = self._node2value(ctx.NOT())
        aggregation = None
        table = None
        column = None

        if ctx.aggregation():
            cond_type = "aggregation"
            aggregation = self._rule2value(ctx.aggregation())
        else:
            cond_type = "id_dot_id"
            table = self._node2value(ctx.ID(0))
            column = self._node2value(ctx.STAR() if ctx.STAR() else ctx.ID(1))


        if ctx.num_condition():
            cond_dict = self.visit(ctx.num_condition())
        elif ctx.str_condition():
            cond_dict = self.visit(ctx.str_condition())
        elif ctx.null_check_condition():
            cond_dict = self.visit(ctx.null_check_condition())
        else:
            pass

        cond_dict["CondType"] = cond_type
        cond_dict["NOT"] = NOT
        cond_dict["Aggregation"] = aggregation
        cond_dict["Table"] = table
        cond_dict["Column"] = column

        return cond_dict


    # Visit a parse tree produced by ParserPredQL#num_condition.
    def visitNum_condition(self, ctx:ParserPredQL.Num_conditionContext):
        ctype = "num"
        comp_op = self._node2value(ctx.NUM_COMP_OP())

        N = None
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


    # Visit a parse tree produced by ParserPredQL#aggregation.
    def visitAggregation(self, ctx:ParserPredQL.AggregationContext):
        aggr_type = self._node2value(ctx.AGGR_FUNC())
        table = self._node2value(ctx.ID(0))
        column = self._node2value(ctx.STAR() if ctx.STAR() else ctx.ID(1))
        where = self._rule2value(ctx.where())
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

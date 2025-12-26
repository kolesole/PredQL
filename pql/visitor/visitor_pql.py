from pql.parser.gen.ParserPQL import ParserPQL
from pql.parser.gen.ParserPQLVisitor import ParserPQLVisitor

class VisitorPQL(ParserPQLVisitor):
    # Visit a parse tree produced by ParserPQL#query.
    def visitQuery(self, ctx:ParserPQL.QueryContext):
        predict = self.visit(ctx.predict())
        for_each = self.visit(ctx.for_each())
        assuming = self.visit(ctx.assuming()) if ctx.assuming() else None
        where = self.visit(ctx.where()) if ctx.where() else None
        
        query_dict = {"Predict" : predict,
                      "ForEach" : for_each,
                      "Assuming": assuming,
                      "Where"   : where 
                     }
        return query_dict


    # Visit a parse tree produced by ParserPQL#assuming.
    def visitAssuming(self, ctx:ParserPQL.AssumingContext):
        qtype = "assuming"
        expr = self.visit(ctx.expr_or())
        
        assuming_dict = {"QType" : qtype,
                         "Expr"  : expr    
                        }
        return assuming_dict


    # Visit a parse tree produced by ParserPQL#for_each.
    def visitFor_each(self, ctx:ParserPQL.For_eachContext):
        qtype = "for_each"
        table = ctx.ID(0).getText()
        column = ctx.ID(1).getText()   
        where = self.visit(ctx.where()) if ctx.where() else None
        
        for_each_dict = {"QType" : qtype,
                         "Table" : table,
                         "Column": column,
                         "Where" : where
                        }
        return for_each_dict


    # Visit a parse tree produced by ParserPQL#predict.
    def visitPredict(self, ctx:ParserPQL.PredictContext):
        qtype = "predict"
        pred_type = None
        aggregation = None
        expr = None
        table = None
        column = None

        if ctx.aggregation():
            pred_type = "aggregation"
            aggregation = self.visit(ctx.aggregation())
        elif ctx.expr_or():
            pred_type = "expr"
            expr = self.visit(ctx.expr_or())
        else:
            pred_type = "id_dot_id"
            table = ctx.ID(0).getText()
            column = "*" if ctx.STAR() else ctx.ID(1).getText()     

        rank_top = True if ctx.RANK_TOP() else False 
        K = ctx.INT().getText() if rank_top else None        
        classify = True if ctx.CLASSIFY() else False

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


    # Visit a parse tree produced by ParserPQL#where.
    def visitWhere(self, ctx:ParserPQL.WhereContext):
        qtype = "where"
        expr = self.visit(ctx.expr_or())    

        where_dict = {"QType" : qtype,
                      "Expr"  : expr
                     }
        return where_dict
    
     # Visit a parse tree produced by ParserPQL#expr_or.
    def visitExpr_or(self, ctx:ParserPQL.Expr_orContext):
        expr_dict = None
        if len(ctx.expr_and()) == 1:
            return self.visit(ctx.expr_and(0))
        
        expr_dict = self.visit(ctx.expr_and(0))
        for i in range(1, len(ctx.expr_and())):
            right = self.visit(ctx.expr_and(i))
            expr_dict = {"Op"   : "OR", 
                         "Left" : expr_dict, 
                         "Right": right
                     }

        return expr_dict


    # Visit a parse tree produced by ParserPQL#expr_and.
    def visitExpr_and(self, ctx:ParserPQL.Expr_andContext):
        if len(ctx.expr_term()) == 1:
            return self.visit(ctx.expr_term(0))
        
        expr_dict = self.visit(ctx.expr_term(0))
        for i in range(1, len(ctx.expr_term())):
            right = self.visit(ctx.expr_term(i))
            expr_dict = {"Op"   : "AND", 
                         "Left" : expr_dict, 
                         "Right": right
                        }

        return expr_dict


    # Visit a parse tree produced by ParserPQL#expr_term.
    def visitExpr_term(self, ctx:ParserPQL.Expr_termContext):
        if ctx.condition():
            return self.visit(ctx.condition())
        elif ctx.expr_or():
            return self.visit(ctx.expr_or())


    # Visit a parse tree produced by ParserPQL#condition.
    def visitCondition(self, ctx:ParserPQL.ConditionContext):
        cond_dict = None
        cond_type = None
        NOT = True if ctx.NOT() else False
        aggregation = None
        table = None
        column = None

        if ctx.aggregation():
            cond_type = "aggregation"
            aggregation = self.visit(ctx.aggregation()) 
        else:
            cond_type = "id_dot_id"
            table = ctx.ID(0).getText()
            column = "*" if ctx.STAR() else ctx.ID(1).getText()

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


    # Visit a parse tree produced by ParserPQL#num_condition.
    def visitNum_condition(self, ctx:ParserPQL.Num_conditionContext):
        ctype = "num"
        comp_op = ctx.NUM_COMP_OP().getText()
    
        N = None
        if ctx.DATETIME():
            N = ctx.DATETIME().getText()
        elif ctx.FLOAT():
            N = ctx.FLOAT().getText()
        elif ctx.INT():
            N = ctx.INT().getText()

        num_cond_dict = {"CType"  : ctype,
                         "CompOp" : comp_op,
                         "N"      : N
                        }
        return num_cond_dict


    # Visit a parse tree produced by ParserPQL#str_condition.
    def visitStr_condition(self, ctx:ParserPQL.Str_conditionContext):
        ctype = "str"
        comp_op = ctx.STR_COMP_OP().getText()
        string = ctx.STRING().getText() 

        string_cond_dict = {"CType"  : ctype,
                            "CompOp" : comp_op,
                            "String" : string
                           }
        return string_cond_dict


    # Visit a parse tree produced by Parser_PQL#null_check_condition.
    def visitNull_check_condition(self, ctx:ParserPQL.Null_check_conditionContext):
        ctype = "null"
        check_op = ctx.NULL_CHECK_OP().getText()

        null_cond_dict = {"CType"   : ctype,
                          "CheckOp" : check_op
                         }
        return null_cond_dict


    # Visit a parse tree produced by Parser_PQL#aggregation.
    def visitAggregation(self, ctx:ParserPQL.AggregationContext):
        aggr_type = ctx.AGGR_FUNC().getText()
        table = ctx.ID(0).getText()
        column = "*" if ctx.STAR() else ctx.ID(1).getText()
        where = self.visit(ctx.where()) if ctx.where() else None
        start = ctx.INT(0).getText() if ctx.INT() else None
        end = ctx.INT(1).getText() if ctx.INT() else None
        measure_unit = ctx.TIME_MEASURE_UNIT().getText() if ctx.TIME_MEASURE_UNIT() else None
        
        aggr_dict = {"AggrType"    : aggr_type,
                     "Table"       : table,
                     "Column"      : column,
                     "Where"       : where,
                     "Start"       : start,
                     "End"         : end,
                     "MeasureUnit" : measure_unit
                    }
        return aggr_dict

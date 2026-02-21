# Generated from ParserPredQL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ParserPredQL import ParserPredQL
else:
    from ParserPredQL import ParserPredQL

# This class defines a complete listener for a parse tree produced by ParserPredQL.
class ParserPredQLListener(ParseTreeListener):

    # Enter a parse tree produced by ParserPredQL#query.
    def enterQuery(self, ctx:ParserPredQL.QueryContext):
        pass

    # Exit a parse tree produced by ParserPredQL#query.
    def exitQuery(self, ctx:ParserPredQL.QueryContext):
        pass


    # Enter a parse tree produced by ParserPredQL#query_tmp.
    def enterQuery_tmp(self, ctx:ParserPredQL.Query_tmpContext):
        pass

    # Exit a parse tree produced by ParserPredQL#query_tmp.
    def exitQuery_tmp(self, ctx:ParserPredQL.Query_tmpContext):
        pass


    # Enter a parse tree produced by ParserPredQL#query_stat.
    def enterQuery_stat(self, ctx:ParserPredQL.Query_statContext):
        pass

    # Exit a parse tree produced by ParserPredQL#query_stat.
    def exitQuery_stat(self, ctx:ParserPredQL.Query_statContext):
        pass


    # Enter a parse tree produced by ParserPredQL#for_each.
    def enterFor_each(self, ctx:ParserPredQL.For_eachContext):
        pass

    # Exit a parse tree produced by ParserPredQL#for_each.
    def exitFor_each(self, ctx:ParserPredQL.For_eachContext):
        pass


    # Enter a parse tree produced by ParserPredQL#predict_tmp.
    def enterPredict_tmp(self, ctx:ParserPredQL.Predict_tmpContext):
        pass

    # Exit a parse tree produced by ParserPredQL#predict_tmp.
    def exitPredict_tmp(self, ctx:ParserPredQL.Predict_tmpContext):
        pass


    # Enter a parse tree produced by ParserPredQL#predict_stat.
    def enterPredict_stat(self, ctx:ParserPredQL.Predict_statContext):
        pass

    # Exit a parse tree produced by ParserPredQL#predict_stat.
    def exitPredict_stat(self, ctx:ParserPredQL.Predict_statContext):
        pass


    # Enter a parse tree produced by ParserPredQL#assuming.
    def enterAssuming(self, ctx:ParserPredQL.AssumingContext):
        pass

    # Exit a parse tree produced by ParserPredQL#assuming.
    def exitAssuming(self, ctx:ParserPredQL.AssumingContext):
        pass


    # Enter a parse tree produced by ParserPredQL#where_tmp.
    def enterWhere_tmp(self, ctx:ParserPredQL.Where_tmpContext):
        pass

    # Exit a parse tree produced by ParserPredQL#where_tmp.
    def exitWhere_tmp(self, ctx:ParserPredQL.Where_tmpContext):
        pass


    # Enter a parse tree produced by ParserPredQL#where_stat.
    def enterWhere_stat(self, ctx:ParserPredQL.Where_statContext):
        pass

    # Exit a parse tree produced by ParserPredQL#where_stat.
    def exitWhere_stat(self, ctx:ParserPredQL.Where_statContext):
        pass


    # Enter a parse tree produced by ParserPredQL#expr_or_tmp.
    def enterExpr_or_tmp(self, ctx:ParserPredQL.Expr_or_tmpContext):
        pass

    # Exit a parse tree produced by ParserPredQL#expr_or_tmp.
    def exitExpr_or_tmp(self, ctx:ParserPredQL.Expr_or_tmpContext):
        pass


    # Enter a parse tree produced by ParserPredQL#expr_or_stat.
    def enterExpr_or_stat(self, ctx:ParserPredQL.Expr_or_statContext):
        pass

    # Exit a parse tree produced by ParserPredQL#expr_or_stat.
    def exitExpr_or_stat(self, ctx:ParserPredQL.Expr_or_statContext):
        pass


    # Enter a parse tree produced by ParserPredQL#expr_and_tmp.
    def enterExpr_and_tmp(self, ctx:ParserPredQL.Expr_and_tmpContext):
        pass

    # Exit a parse tree produced by ParserPredQL#expr_and_tmp.
    def exitExpr_and_tmp(self, ctx:ParserPredQL.Expr_and_tmpContext):
        pass


    # Enter a parse tree produced by ParserPredQL#expr_and_stat.
    def enterExpr_and_stat(self, ctx:ParserPredQL.Expr_and_statContext):
        pass

    # Exit a parse tree produced by ParserPredQL#expr_and_stat.
    def exitExpr_and_stat(self, ctx:ParserPredQL.Expr_and_statContext):
        pass


    # Enter a parse tree produced by ParserPredQL#expr_term_tmp.
    def enterExpr_term_tmp(self, ctx:ParserPredQL.Expr_term_tmpContext):
        pass

    # Exit a parse tree produced by ParserPredQL#expr_term_tmp.
    def exitExpr_term_tmp(self, ctx:ParserPredQL.Expr_term_tmpContext):
        pass


    # Enter a parse tree produced by ParserPredQL#expr_term_stat.
    def enterExpr_term_stat(self, ctx:ParserPredQL.Expr_term_statContext):
        pass

    # Exit a parse tree produced by ParserPredQL#expr_term_stat.
    def exitExpr_term_stat(self, ctx:ParserPredQL.Expr_term_statContext):
        pass


    # Enter a parse tree produced by ParserPredQL#condition_tmp.
    def enterCondition_tmp(self, ctx:ParserPredQL.Condition_tmpContext):
        pass

    # Exit a parse tree produced by ParserPredQL#condition_tmp.
    def exitCondition_tmp(self, ctx:ParserPredQL.Condition_tmpContext):
        pass


    # Enter a parse tree produced by ParserPredQL#condition_stat.
    def enterCondition_stat(self, ctx:ParserPredQL.Condition_statContext):
        pass

    # Exit a parse tree produced by ParserPredQL#condition_stat.
    def exitCondition_stat(self, ctx:ParserPredQL.Condition_statContext):
        pass


    # Enter a parse tree produced by ParserPredQL#num_condition.
    def enterNum_condition(self, ctx:ParserPredQL.Num_conditionContext):
        pass

    # Exit a parse tree produced by ParserPredQL#num_condition.
    def exitNum_condition(self, ctx:ParserPredQL.Num_conditionContext):
        pass


    # Enter a parse tree produced by ParserPredQL#str_condition.
    def enterStr_condition(self, ctx:ParserPredQL.Str_conditionContext):
        pass

    # Exit a parse tree produced by ParserPredQL#str_condition.
    def exitStr_condition(self, ctx:ParserPredQL.Str_conditionContext):
        pass


    # Enter a parse tree produced by ParserPredQL#null_check_condition.
    def enterNull_check_condition(self, ctx:ParserPredQL.Null_check_conditionContext):
        pass

    # Exit a parse tree produced by ParserPredQL#null_check_condition.
    def exitNull_check_condition(self, ctx:ParserPredQL.Null_check_conditionContext):
        pass


    # Enter a parse tree produced by ParserPredQL#aggregation_tmp.
    def enterAggregation_tmp(self, ctx:ParserPredQL.Aggregation_tmpContext):
        pass

    # Exit a parse tree produced by ParserPredQL#aggregation_tmp.
    def exitAggregation_tmp(self, ctx:ParserPredQL.Aggregation_tmpContext):
        pass


    # Enter a parse tree produced by ParserPredQL#aggregation_stat.
    def enterAggregation_stat(self, ctx:ParserPredQL.Aggregation_statContext):
        pass

    # Exit a parse tree produced by ParserPredQL#aggregation_stat.
    def exitAggregation_stat(self, ctx:ParserPredQL.Aggregation_statContext):
        pass



del ParserPredQL
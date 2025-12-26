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


    # Enter a parse tree produced by ParserPredQL#assuming.
    def enterAssuming(self, ctx:ParserPredQL.AssumingContext):
        pass

    # Exit a parse tree produced by ParserPredQL#assuming.
    def exitAssuming(self, ctx:ParserPredQL.AssumingContext):
        pass


    # Enter a parse tree produced by ParserPredQL#for_each.
    def enterFor_each(self, ctx:ParserPredQL.For_eachContext):
        pass

    # Exit a parse tree produced by ParserPredQL#for_each.
    def exitFor_each(self, ctx:ParserPredQL.For_eachContext):
        pass


    # Enter a parse tree produced by ParserPredQL#predict.
    def enterPredict(self, ctx:ParserPredQL.PredictContext):
        pass

    # Exit a parse tree produced by ParserPredQL#predict.
    def exitPredict(self, ctx:ParserPredQL.PredictContext):
        pass


    # Enter a parse tree produced by ParserPredQL#where.
    def enterWhere(self, ctx:ParserPredQL.WhereContext):
        pass

    # Exit a parse tree produced by ParserPredQL#where.
    def exitWhere(self, ctx:ParserPredQL.WhereContext):
        pass


    # Enter a parse tree produced by ParserPredQL#expr_or.
    def enterExpr_or(self, ctx:ParserPredQL.Expr_orContext):
        pass

    # Exit a parse tree produced by ParserPredQL#expr_or.
    def exitExpr_or(self, ctx:ParserPredQL.Expr_orContext):
        pass


    # Enter a parse tree produced by ParserPredQL#expr_and.
    def enterExpr_and(self, ctx:ParserPredQL.Expr_andContext):
        pass

    # Exit a parse tree produced by ParserPredQL#expr_and.
    def exitExpr_and(self, ctx:ParserPredQL.Expr_andContext):
        pass


    # Enter a parse tree produced by ParserPredQL#expr_term.
    def enterExpr_term(self, ctx:ParserPredQL.Expr_termContext):
        pass

    # Exit a parse tree produced by ParserPredQL#expr_term.
    def exitExpr_term(self, ctx:ParserPredQL.Expr_termContext):
        pass


    # Enter a parse tree produced by ParserPredQL#condition.
    def enterCondition(self, ctx:ParserPredQL.ConditionContext):
        pass

    # Exit a parse tree produced by ParserPredQL#condition.
    def exitCondition(self, ctx:ParserPredQL.ConditionContext):
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


    # Enter a parse tree produced by ParserPredQL#aggregation.
    def enterAggregation(self, ctx:ParserPredQL.AggregationContext):
        pass

    # Exit a parse tree produced by ParserPredQL#aggregation.
    def exitAggregation(self, ctx:ParserPredQL.AggregationContext):
        pass



del ParserPredQL
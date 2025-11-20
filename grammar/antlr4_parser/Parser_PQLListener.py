# Generated from Parser_PQL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .Parser_PQL import Parser_PQL
else:
    from Parser_PQL import Parser_PQL

# This class defines a complete listener for a parse tree produced by Parser_PQL.
class Parser_PQLListener(ParseTreeListener):

    # Enter a parse tree produced by Parser_PQL#query.
    def enterQuery(self, ctx:Parser_PQL.QueryContext):
        pass

    # Exit a parse tree produced by Parser_PQL#query.
    def exitQuery(self, ctx:Parser_PQL.QueryContext):
        pass


    # Enter a parse tree produced by Parser_PQL#assuming.
    def enterAssuming(self, ctx:Parser_PQL.AssumingContext):
        pass

    # Exit a parse tree produced by Parser_PQL#assuming.
    def exitAssuming(self, ctx:Parser_PQL.AssumingContext):
        pass


    # Enter a parse tree produced by Parser_PQL#for_each.
    def enterFor_each(self, ctx:Parser_PQL.For_eachContext):
        pass

    # Exit a parse tree produced by Parser_PQL#for_each.
    def exitFor_each(self, ctx:Parser_PQL.For_eachContext):
        pass


    # Enter a parse tree produced by Parser_PQL#predict.
    def enterPredict(self, ctx:Parser_PQL.PredictContext):
        pass

    # Exit a parse tree produced by Parser_PQL#predict.
    def exitPredict(self, ctx:Parser_PQL.PredictContext):
        pass


    # Enter a parse tree produced by Parser_PQL#where.
    def enterWhere(self, ctx:Parser_PQL.WhereContext):
        pass

    # Exit a parse tree produced by Parser_PQL#where.
    def exitWhere(self, ctx:Parser_PQL.WhereContext):
        pass


    # Enter a parse tree produced by Parser_PQL#expr_or.
    def enterExpr_or(self, ctx:Parser_PQL.Expr_orContext):
        pass

    # Exit a parse tree produced by Parser_PQL#expr_or.
    def exitExpr_or(self, ctx:Parser_PQL.Expr_orContext):
        pass


    # Enter a parse tree produced by Parser_PQL#expr_and.
    def enterExpr_and(self, ctx:Parser_PQL.Expr_andContext):
        pass

    # Exit a parse tree produced by Parser_PQL#expr_and.
    def exitExpr_and(self, ctx:Parser_PQL.Expr_andContext):
        pass


    # Enter a parse tree produced by Parser_PQL#expr_term.
    def enterExpr_term(self, ctx:Parser_PQL.Expr_termContext):
        pass

    # Exit a parse tree produced by Parser_PQL#expr_term.
    def exitExpr_term(self, ctx:Parser_PQL.Expr_termContext):
        pass


    # Enter a parse tree produced by Parser_PQL#condition.
    def enterCondition(self, ctx:Parser_PQL.ConditionContext):
        pass

    # Exit a parse tree produced by Parser_PQL#condition.
    def exitCondition(self, ctx:Parser_PQL.ConditionContext):
        pass


    # Enter a parse tree produced by Parser_PQL#num_condition.
    def enterNum_condition(self, ctx:Parser_PQL.Num_conditionContext):
        pass

    # Exit a parse tree produced by Parser_PQL#num_condition.
    def exitNum_condition(self, ctx:Parser_PQL.Num_conditionContext):
        pass


    # Enter a parse tree produced by Parser_PQL#str_condition.
    def enterStr_condition(self, ctx:Parser_PQL.Str_conditionContext):
        pass

    # Exit a parse tree produced by Parser_PQL#str_condition.
    def exitStr_condition(self, ctx:Parser_PQL.Str_conditionContext):
        pass


    # Enter a parse tree produced by Parser_PQL#null_check_condition.
    def enterNull_check_condition(self, ctx:Parser_PQL.Null_check_conditionContext):
        pass

    # Exit a parse tree produced by Parser_PQL#null_check_condition.
    def exitNull_check_condition(self, ctx:Parser_PQL.Null_check_conditionContext):
        pass


    # Enter a parse tree produced by Parser_PQL#aggregation.
    def enterAggregation(self, ctx:Parser_PQL.AggregationContext):
        pass

    # Exit a parse tree produced by Parser_PQL#aggregation.
    def exitAggregation(self, ctx:Parser_PQL.AggregationContext):
        pass



del Parser_PQL
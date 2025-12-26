# Generated from ParserPQL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ParserPQL import ParserPQL
else:
    from ParserPQL import ParserPQL

# This class defines a complete listener for a parse tree produced by ParserPQL.
class ParserPQLListener(ParseTreeListener):

    # Enter a parse tree produced by ParserPQL#query.
    def enterQuery(self, ctx:ParserPQL.QueryContext):
        pass

    # Exit a parse tree produced by ParserPQL#query.
    def exitQuery(self, ctx:ParserPQL.QueryContext):
        pass


    # Enter a parse tree produced by ParserPQL#assuming.
    def enterAssuming(self, ctx:ParserPQL.AssumingContext):
        pass

    # Exit a parse tree produced by ParserPQL#assuming.
    def exitAssuming(self, ctx:ParserPQL.AssumingContext):
        pass


    # Enter a parse tree produced by ParserPQL#for_each.
    def enterFor_each(self, ctx:ParserPQL.For_eachContext):
        pass

    # Exit a parse tree produced by ParserPQL#for_each.
    def exitFor_each(self, ctx:ParserPQL.For_eachContext):
        pass


    # Enter a parse tree produced by ParserPQL#predict.
    def enterPredict(self, ctx:ParserPQL.PredictContext):
        pass

    # Exit a parse tree produced by ParserPQL#predict.
    def exitPredict(self, ctx:ParserPQL.PredictContext):
        pass


    # Enter a parse tree produced by ParserPQL#where.
    def enterWhere(self, ctx:ParserPQL.WhereContext):
        pass

    # Exit a parse tree produced by ParserPQL#where.
    def exitWhere(self, ctx:ParserPQL.WhereContext):
        pass


    # Enter a parse tree produced by ParserPQL#expr_or.
    def enterExpr_or(self, ctx:ParserPQL.Expr_orContext):
        pass

    # Exit a parse tree produced by ParserPQL#expr_or.
    def exitExpr_or(self, ctx:ParserPQL.Expr_orContext):
        pass


    # Enter a parse tree produced by ParserPQL#expr_and.
    def enterExpr_and(self, ctx:ParserPQL.Expr_andContext):
        pass

    # Exit a parse tree produced by ParserPQL#expr_and.
    def exitExpr_and(self, ctx:ParserPQL.Expr_andContext):
        pass


    # Enter a parse tree produced by ParserPQL#expr_term.
    def enterExpr_term(self, ctx:ParserPQL.Expr_termContext):
        pass

    # Exit a parse tree produced by ParserPQL#expr_term.
    def exitExpr_term(self, ctx:ParserPQL.Expr_termContext):
        pass


    # Enter a parse tree produced by ParserPQL#condition.
    def enterCondition(self, ctx:ParserPQL.ConditionContext):
        pass

    # Exit a parse tree produced by ParserPQL#condition.
    def exitCondition(self, ctx:ParserPQL.ConditionContext):
        pass


    # Enter a parse tree produced by ParserPQL#num_condition.
    def enterNum_condition(self, ctx:ParserPQL.Num_conditionContext):
        pass

    # Exit a parse tree produced by ParserPQL#num_condition.
    def exitNum_condition(self, ctx:ParserPQL.Num_conditionContext):
        pass


    # Enter a parse tree produced by ParserPQL#str_condition.
    def enterStr_condition(self, ctx:ParserPQL.Str_conditionContext):
        pass

    # Exit a parse tree produced by ParserPQL#str_condition.
    def exitStr_condition(self, ctx:ParserPQL.Str_conditionContext):
        pass


    # Enter a parse tree produced by ParserPQL#null_check_condition.
    def enterNull_check_condition(self, ctx:ParserPQL.Null_check_conditionContext):
        pass

    # Exit a parse tree produced by ParserPQL#null_check_condition.
    def exitNull_check_condition(self, ctx:ParserPQL.Null_check_conditionContext):
        pass


    # Enter a parse tree produced by ParserPQL#aggregation.
    def enterAggregation(self, ctx:ParserPQL.AggregationContext):
        pass

    # Exit a parse tree produced by ParserPQL#aggregation.
    def exitAggregation(self, ctx:ParserPQL.AggregationContext):
        pass



del ParserPQL
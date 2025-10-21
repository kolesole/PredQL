# Generated from Parser_PQL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Parser_PQL import Parser_PQL
else:
    from Parser_PQL import Parser_PQL

# This class defines a complete generic visitor for a parse tree produced by Parser_PQL.

class Parser_PQLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by Parser_PQL#query.
    def visitQuery(self, ctx:Parser_PQL.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser_PQL#help_query.
    def visitHelp_query(self, ctx:Parser_PQL.Help_queryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser_PQL#assuming.
    def visitAssuming(self, ctx:Parser_PQL.AssumingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser_PQL#for_each.
    def visitFor_each(self, ctx:Parser_PQL.For_eachContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser_PQL#predict.
    def visitPredict(self, ctx:Parser_PQL.PredictContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser_PQL#where.
    def visitWhere(self, ctx:Parser_PQL.WhereContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser_PQL#condition.
    def visitCondition(self, ctx:Parser_PQL.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser_PQL#num_condition.
    def visitNum_condition(self, ctx:Parser_PQL.Num_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser_PQL#str_condition.
    def visitStr_condition(self, ctx:Parser_PQL.Str_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser_PQL#null_check_condition.
    def visitNull_check_condition(self, ctx:Parser_PQL.Null_check_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser_PQL#aggregation.
    def visitAggregation(self, ctx:Parser_PQL.AggregationContext):
        return self.visitChildren(ctx)



del Parser_PQL
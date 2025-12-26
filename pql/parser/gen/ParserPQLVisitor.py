# Generated from ParserPQL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ParserPQL import ParserPQL
else:
    from ParserPQL import ParserPQL

# This class defines a complete generic visitor for a parse tree produced by ParserPQL.

class ParserPQLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ParserPQL#query.
    def visitQuery(self, ctx:ParserPQL.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPQL#assuming.
    def visitAssuming(self, ctx:ParserPQL.AssumingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPQL#for_each.
    def visitFor_each(self, ctx:ParserPQL.For_eachContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPQL#predict.
    def visitPredict(self, ctx:ParserPQL.PredictContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPQL#where.
    def visitWhere(self, ctx:ParserPQL.WhereContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPQL#expr_or.
    def visitExpr_or(self, ctx:ParserPQL.Expr_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPQL#expr_and.
    def visitExpr_and(self, ctx:ParserPQL.Expr_andContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPQL#expr_term.
    def visitExpr_term(self, ctx:ParserPQL.Expr_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPQL#condition.
    def visitCondition(self, ctx:ParserPQL.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPQL#num_condition.
    def visitNum_condition(self, ctx:ParserPQL.Num_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPQL#str_condition.
    def visitStr_condition(self, ctx:ParserPQL.Str_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPQL#null_check_condition.
    def visitNull_check_condition(self, ctx:ParserPQL.Null_check_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPQL#aggregation.
    def visitAggregation(self, ctx:ParserPQL.AggregationContext):
        return self.visitChildren(ctx)



del ParserPQL
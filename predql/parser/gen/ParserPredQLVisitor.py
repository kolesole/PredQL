# Generated from ParserPredQL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ParserPredQL import ParserPredQL
else:
    from ParserPredQL import ParserPredQL

# This class defines a complete generic visitor for a parse tree produced by ParserPredQL.

class ParserPredQLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ParserPredQL#query.
    def visitQuery(self, ctx:ParserPredQL.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPredQL#assuming.
    def visitAssuming(self, ctx:ParserPredQL.AssumingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPredQL#for_each.
    def visitFor_each(self, ctx:ParserPredQL.For_eachContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPredQL#predict.
    def visitPredict(self, ctx:ParserPredQL.PredictContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPredQL#where.
    def visitWhere(self, ctx:ParserPredQL.WhereContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPredQL#expr_or.
    def visitExpr_or(self, ctx:ParserPredQL.Expr_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPredQL#expr_and.
    def visitExpr_and(self, ctx:ParserPredQL.Expr_andContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPredQL#expr_term.
    def visitExpr_term(self, ctx:ParserPredQL.Expr_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPredQL#condition.
    def visitCondition(self, ctx:ParserPredQL.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPredQL#num_condition.
    def visitNum_condition(self, ctx:ParserPredQL.Num_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPredQL#str_condition.
    def visitStr_condition(self, ctx:ParserPredQL.Str_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPredQL#null_check_condition.
    def visitNull_check_condition(self, ctx:ParserPredQL.Null_check_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPredQL#aggregation.
    def visitAggregation(self, ctx:ParserPredQL.AggregationContext):
        return self.visitChildren(ctx)



del ParserPredQL
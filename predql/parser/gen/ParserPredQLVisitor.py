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


    # Visit a parse tree produced by ParserPredQL#query_tmp.
    def visitQuery_tmp(self, ctx:ParserPredQL.Query_tmpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPredQL#query_stat.
    def visitQuery_stat(self, ctx:ParserPredQL.Query_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPredQL#for_each.
    def visitFor_each(self, ctx:ParserPredQL.For_eachContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPredQL#predict_tmp.
    def visitPredict_tmp(self, ctx:ParserPredQL.Predict_tmpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPredQL#predict_stat.
    def visitPredict_stat(self, ctx:ParserPredQL.Predict_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPredQL#assuming.
    def visitAssuming(self, ctx:ParserPredQL.AssumingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPredQL#where_tmp.
    def visitWhere_tmp(self, ctx:ParserPredQL.Where_tmpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPredQL#where_stat.
    def visitWhere_stat(self, ctx:ParserPredQL.Where_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPredQL#expr_or_tmp.
    def visitExpr_or_tmp(self, ctx:ParserPredQL.Expr_or_tmpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPredQL#expr_or_stat.
    def visitExpr_or_stat(self, ctx:ParserPredQL.Expr_or_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPredQL#expr_and_tmp.
    def visitExpr_and_tmp(self, ctx:ParserPredQL.Expr_and_tmpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPredQL#expr_and_stat.
    def visitExpr_and_stat(self, ctx:ParserPredQL.Expr_and_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPredQL#expr_term_tmp.
    def visitExpr_term_tmp(self, ctx:ParserPredQL.Expr_term_tmpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPredQL#expr_term_stat.
    def visitExpr_term_stat(self, ctx:ParserPredQL.Expr_term_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPredQL#condition_tmp.
    def visitCondition_tmp(self, ctx:ParserPredQL.Condition_tmpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPredQL#condition_stat.
    def visitCondition_stat(self, ctx:ParserPredQL.Condition_statContext):
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


    # Visit a parse tree produced by ParserPredQL#aggregation_tmp.
    def visitAggregation_tmp(self, ctx:ParserPredQL.Aggregation_tmpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ParserPredQL#aggregation_stat.
    def visitAggregation_stat(self, ctx:ParserPredQL.Aggregation_statContext):
        return self.visitChildren(ctx)



del ParserPredQL
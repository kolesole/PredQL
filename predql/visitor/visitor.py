"""Visitor implementation for traversing PredQL parse trees."""

from antlr4 import ParserRuleContext, TerminalNode

from predql.parser import ParserPredQL, ParserPredQLVisitor

from predql.visitor.parsed_value import ParsedValue


class Visitor(ParserPredQLVisitor):
    r"""Visitor class for converting PredQL parse trees to dictionaries.
    
    Implements the visitor pattern to traverse ANTLR-generated parse trees  
    and convert them into structured Python dictionaries. Each visit method  
    corresponds to a grammar rule and extracts relevant information while  
    preserving source location data for error reporting.  
    
    The visitor wraps parsed values in ParsedValue objects that track  
    their line and column positions in the source query.  
    """
    
    def visitQuery(self, 
                   ctx : ParserPredQL.QueryContext) -> dict:
        r"""Visits the top-level query rule.

        Extracts both temporal and static query components (only one will be non-None).
        
        Args:
            ctx (ParserPredQL.QueryContext): Parse tree context.
        
        Returns:
            query_dict (dict): Dictionary with 'QueryTmp' and 'QueryStat' keys.
        """
        query_tmp = self._rule2value(ctx.query_tmp())
        query_stat = self._rule2value(ctx.query_stat())
        
        query_dict = {"QueryTmp" : query_tmp,
                      "QueryStat": query_stat
                     }
        return query_dict


    def visitQuery_tmp(self, 
                       ctx : ParserPredQL.Query_tmpContext) -> dict:
        r"""Visits a temporal query rule.
        
        Args:
            ctx (ParserPredQL.Query_tmpContext): Parse tree context.
        
        Returns:
            query_dict (dict): Dictionary with temporal query components.
        """
        predict = self._rule2value(ctx.predict_tmp())
        for_each = self._rule2value(ctx.for_each())
        assuming = self._rule2value(ctx.assuming())
        where = self._rule2value(ctx.where_tmp())   

        query_dict = {"Predict" : predict,
                      "ForEach" : for_each,
                      "Assuming": assuming,
                      "Where"   : where
                     }
        return query_dict


    def visitQuery_stat(self, 
                        ctx : ParserPredQL.Query_statContext) -> dict:
        r"""Visits a static query rule.
        
        Args:
            ctx (ParserPredQL.Query_statContext): Parse tree context.
        
        Returns:
            query_dict (dict): Dictionary with static query components.
        """
        predict = self._rule2value(ctx.predict_stat())
        for_each = self._rule2value(ctx.for_each())
        where = self._rule2value(ctx.where_stat())

        query_dict = {"Predict": predict,
                      "ForEach": for_each,
                      "Where"  : where
                     }
        return query_dict


    def visitFor_each(self, 
                      ctx : ParserPredQL.For_eachContext) -> dict:
        r"""Visits FOR EACH clause.
        
        Args:
            ctx (ParserPredQL.For_eachContext): Parse tree context.
        
        Returns:
            for_each_dict (dict): Dictionary with FOR EACH components.
        """
        table = self._node2value(ctx.ID(0))
        column = self._node2value(ctx.ID(1))
        where = self._rule2value(ctx.where_stat())
        
        for_each_dict = {"Table" : table,
                         "Column": column,
                         "Where" : where
                        }
        return for_each_dict


    def visitPredict_tmp(self, 
                         ctx : ParserPredQL.Predict_tmpContext) -> dict:
        r"""Visits temporal PREDICT clause.
        
        Args:
            ctx (ParserPredQL.Predict_tmpContext): Parse tree context.
        
        Returns:
            predict_dict (dict): Dictionary with temporal PREDICT components.
        """
        if ctx.aggregation_tmp():
            pred_type = "aggregation"
        elif ctx.expr_or_tmp():
            pred_type = "expr"
        
        aggregation = self._rule2value(ctx.aggregation_tmp())
        expr = self._rule2value(ctx.expr_or_tmp())

        rank_top = self._node2value(ctx.RANK_TOP())
        K = self._node2value(ctx.INT())
        classify = self._node2value(ctx.CLASSIFY())

        predict_dict = {"PredType"   : pred_type,
                        "Aggregation": aggregation,
                        "Expr"       : expr,
                        "RankTop"    : rank_top,
                        "K"          : K,
                        "Classify"   : classify
                       }
        return predict_dict


    def visitPredict_stat(self, 
                          ctx : ParserPredQL.Predict_statContext) -> dict:
        r"""Visits static PREDICT clause.
        
        Args:
            ctx (ParserPredQL.Predict_statContext): Parse tree context.
        
        Returns:
            predict_dict (dict): Dictionary with static PREDICT components.
        """
        if ctx.aggregation_stat():
            pred_type = "aggregation"
        elif ctx.expr_or_stat():
            pred_type = "expr"
        else:
            pred_type = "id_dot_id"
        
        aggregation = self._rule2value(ctx.aggregation_stat())
        expr = self._rule2value(ctx.expr_or_stat())
        table = self._node2value(ctx.ID(0))
        column = self._node2value(ctx.STAR() if ctx.STAR() else ctx.ID(1))

        rank_top = self._node2value(ctx.RANK_TOP())
        K = self._node2value(ctx.INT())
        classify = self._node2value(ctx.CLASSIFY())

        predict_dict = {"PredType"   : pred_type,
                        "Aggregation": aggregation,
                        "Expr"       : expr,
                        "Table"      : table,
                        "Column"     : column,
                        "RankTop"    : rank_top,
                        "K"          : K,
                        "Classify"   : classify
                       }
        return predict_dict


    def visitAssuming(self, 
                      ctx : ParserPredQL.AssumingContext) -> dict:
        r"""Visits ASSUMING clause.
        
        Args:
            ctx (ctx:ParserPredQL.AssumingContext): Parse tree context.
        
        Returns:
            assuming_dict (dict): Dictionary with ASSUMING components.
        """
        expr = self._rule2value(ctx.expr_or_tmp())

        assuming_dict = {"Expr": expr}
        return assuming_dict


    def visitWhere_tmp(self, 
                       ctx : ParserPredQL.Where_tmpContext) -> dict:
        r"""Visits temporal WHERE clause.
        
        Args:
            ctx (ctx:ParserPredQL.Where_tmpContext): Parse tree context.
        
        Returns:
            where_dict (dict): Dictionary with temporal WHERE components.
        """
        expr = self._rule2value(ctx.expr_or_tmp())
        
        where_dict = {"Expr": expr}
        return where_dict


    def visitWhere_stat(self, 
                        ctx : ParserPredQL.Where_statContext) -> dict:
        r"""Visits static WHERE clause.
        
        Args:
            ctx (ctx:ParserPredQL.Where_statContext): Parse tree context.
        
        Returns:
            where_dict (dict): Dictionary with static WHERE components.
        """
        expr = self._rule2value(ctx.expr_or_stat())
        
        where_dict = {"Expr": expr}
        return where_dict


    def visitExpr_or_tmp(self, 
                         ctx : ParserPredQL.Expr_or_tmpContext) -> dict | ParsedValue:
        r"""Visits a temporal OR expression.  

        Builds a left-associative tree of OR operations.  
        For single expressions, returns the expression directly.  
        For multiple OR expressions, creates a nested dictionary structure.  
        
        Args:
            ctx (ParserPredQL.Expr_or_tmpContext): Parse tree context.
        
        Returns:
            expr_dict (dict | ParsedValue): Expression tree or single expression.
        """
        # base case: only one AND expression, return it directly
        if len(ctx.expr_and_tmp()) == 1:
            return self.visit(ctx.expr_and_tmp(0))

        # build left-associative OR tree
        expr_dict = self.visit(ctx.expr_and_tmp(0))
        for i in range(1, len(ctx.expr_and_tmp())):
            right = self.visit(ctx.expr_and_tmp(i))
            expr_dict = {"Op"       : self._node2value(ctx.OR(i-1)),
                         "LeftExpr" : expr_dict,
                         "RightExpr": right
                     }
            
        return expr_dict


    def visitExpr_or_stat(self, ctx:ParserPredQL.Expr_or_statContext):
        r"""Visits a static OR expression.  

        Builds a left-associative tree of OR operations.  
        For single expressions, returns the expression directly.  
        For multiple OR expressions, creates a nested dictionary structure.  
        
        Args:
            ctx (ParserPredQL.Expr_or_statContext): Parse tree context.
        
        Returns:
            expr_dict (dict | ParsedValue): Expression tree or single expression.
        """
        # base case: only one AND expression, return it directly
        if len(ctx.expr_and_stat()) == 1:
            return self.visit(ctx.expr_and_stat(0))

        # build left-associative OR tree
        expr_dict = self.visit(ctx.expr_and_stat(0))
        for i in range(1, len(ctx.expr_and_stat())):
            right = self.visit(ctx.expr_and_stat(i))
            expr_dict = {"Op"       : self._node2value(ctx.OR(i-1)),
                         "LeftExpr" : expr_dict,
                         "RightExpr": right
                     }
            
        return expr_dict


    def visitExpr_and_tmp(self, 
                          ctx : ParserPredQL.Expr_and_tmpContext) -> dict | ParsedValue:
        r"""Visits a temporal AND expression.  

        Builds a left-associative tree of AND operations.  
        For single expressions, returns the expression directly.  
        For multiple AND expressions, creates a nested dictionary structure.  
        
        Args:
            ctx (ParserPredQL.Expr_and_tmpContext): Parse tree context.
        
        Returns:
            expr_dict (dict | ParsedValue): Expression tree or single expression.
        """
        # base case: only one AND expression, return it directly
        if len(ctx.expr_term_tmp()) == 1:
            return self.visit(ctx.expr_term_tmp(0))

        # build left-associative AND tree
        expr_dict = self.visit(ctx.expr_term_tmp(0))
        for i in range(1, len(ctx.expr_term_tmp())):
            right = self.visit(ctx.expr_term_tmp(i))
            expr_dict = {"Op"       : self._node2value(ctx.AND(i-1)),
                         "LeftExpr" : expr_dict,
                         "RightExpr": right
                        }

        return expr_dict


    def visitExpr_and_stat(self, 
                           ctx : ParserPredQL.Expr_and_statContext) -> dict | ParsedValue:
        r"""Visits a static AND expression.  

        Builds a left-associative tree of AND operations.  
        For single expressions, returns the expression directly.  
        For multiple AND expressions, creates a nested dictionary structure.  
        
        Args:
            ctx (ParserPredQL.Expr_and_statContext): Parse tree context.
        
        Returns:
            expr_dict (dict | ParsedValue): Expression tree or single expression.
        """
        # base case: only one AND expression, return it directly
        if len(ctx.expr_term_stat()) == 1:
            return self.visit(ctx.expr_term_stat(0))

        # build left-associative AND tree
        expr_dict = self.visit(ctx.expr_term_stat(0))
        for i in range(1, len(ctx.expr_term_stat())):
            right = self.visit(ctx.expr_term_stat(i))
            expr_dict = {"Op"       : self._node2value(ctx.AND(i-1)),
                         "LeftExpr" : expr_dict,
                         "RightExpr": right
                        }

        return expr_dict


    def visitExpr_term_tmp(self, 
                           ctx : ParserPredQL.Expr_term_tmpContext) -> dict | ParsedValue:
        """Visits a temporal term expression (base case or parenthesized expr).
        
        Args:
            ctx (ParserPredQL.Expr_term_tmpContext): Parse tree context.
        
        Returns:
            expr_dict (dict | ParsedValue): Expression tree or single expression.
        """
        if ctx.condition_tmp():
            return self._rule2value(ctx.condition_tmp())
        elif ctx.expr_or_tmp():
            return self.visit(ctx.expr_or_tmp())


    def visitExpr_term_stat(self, 
                            ctx : ParserPredQL.Expr_term_statContext) -> dict | ParsedValue:
        """Visits a static term expression (base case or parenthesized expr).
        
        Args:
            ctx (ParserPredQL.Expr_term_statContext): Parse tree context.
        
        Returns:
            expr_dict (dict | ParsedValue): Expression tree or single expression.
        """
        if ctx.condition_stat():
            return self._rule2value(ctx.condition_stat())
        elif ctx.expr_or_stat():
            return self.visit(ctx.expr_or_stat())


    def visitCondition_tmp(self, 
                           ctx:ParserPredQL.Condition_tmpContext) -> dict:
        r"""Visits a temporal condition.    
        
        Args:
            ctx (ParserPredQL.Condition_tmpContext): Parse tree context.
        
        Returns:
            condition_dict (dict): Dictionary with temporal condition components.
        """
        if ctx.num_condition():
            cond_dict = self.visit(ctx.num_condition())
        elif ctx.str_condition():
            cond_dict = self.visit(ctx.str_condition())
        elif ctx.null_check_condition():
            cond_dict = self.visit(ctx.null_check_condition())

        cond_dict["CondType"] = "aggregation"
        cond_dict["NOT"] = self._node2value(ctx.NOT())
        cond_dict["Aggregation"] = self._rule2value(ctx.aggregation_tmp())
        return cond_dict


    def visitCondition_stat(self, ctx:ParserPredQL.Condition_statContext):
        r"""Visits a static condition.    
        
        Args:
            ctx (ParserPredQL.Condition_statContext): Parse tree context.
        
        Returns:
            condition_dict (dict): Dictionary with static condition components.
        """
        if ctx.aggregation_stat():
            cond_type = "aggregation"
        else:
            cond_type = "id_dot_id"

        if ctx.num_condition():
            cond_dict = self.visit(ctx.num_condition())
        elif ctx.str_condition():
            cond_dict = self.visit(ctx.str_condition())
        elif ctx.null_check_condition():
            cond_dict = self.visit(ctx.null_check_condition())

        cond_dict["CondType"] = cond_type
        cond_dict["NOT"] = self._node2value(ctx.NOT())
        cond_dict["Aggregation"] = self._rule2value(ctx.aggregation_stat())
        cond_dict["Table"] = self._node2value(ctx.ID(0))
        cond_dict["Column"] = self._node2value(ctx.STAR() if ctx.STAR() else ctx.ID(1))
        return cond_dict


    def visitNum_condition(self, 
                           ctx : ParserPredQL.Num_conditionContext) -> dict:
        r"""Visits a numerical condition.    
        
        Args:
            ctx (ParserPredQL.Num_conditionContext): Parse tree context.
        
        Returns:
            num_cond_dict (dict): Dictionary with numerical condition components.
        """
        ctype = "num"
        comp_op = self._node2value(ctx.NUM_COMP_OP())

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


    def visitStr_condition(self, 
                           ctx : ParserPredQL.Str_conditionContext) -> dict:
        r"""Visits a string condition.    
        
        Args:
            ctx (ParserPredQL.Str_conditionContext): Parse tree context.
        
        Returns:
            str_cond_dict (dict): Dictionary with string condition components.
        """
        ctype = "str"
        comp_op = self._node2value(ctx.STR_COMP_OP())
        string = self._node2value(ctx.STRING())

        str_cond_dict = {"CType"  : ctype,
                            "CompOp" : comp_op,
                            "String" : string
                           }
        return str_cond_dict


    def visitNull_check_condition(self, 
                                  ctx : ParserPredQL.Null_check_conditionContext) -> dict:
        r"""Visits a null check condition.    
        
        Args:
            ctx (ParserPredQL.Null_check_conditionContext): Parse tree context.
        
        Returns:
            null_cond_dict (dict): Dictionary with null check condition components.
        """
        ctype = "null"
        check_op = self._node2value(ctx.NULL_CHECK_OP())

        null_cond_dict = {"CType"   : ctype,
                          "CheckOp" : check_op
                         }
        return null_cond_dict


    def visitAggregation_tmp(self, ctx:ParserPredQL.Aggregation_tmpContext):
        r"""Visits a temporal aggregation.    
        
        Args:
            ctx (ParserPredQL.Aggregation_tmpContext): Parse tree context.
        
        Returns:
            aggr_dict (dict): Dictionary with temporal aggregation components.
        """
        aggr_type = self._node2value(ctx.AGGR_FUNC())
        table = self._node2value(ctx.ID(0))
        column = self._node2value(ctx.STAR() if ctx.STAR() else ctx.ID(1))
        where = self._rule2value(ctx.where_stat())
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


    def visitAggregation_stat(self, 
                              ctx : ParserPredQL.Aggregation_statContext) -> dict:
        r"""Visits a stat aggregation.    
        
        Args:
            ctx (ParserPredQL.Aggregation_statContext): Parse tree context.
        
        Returns:
            aggr_dict (dict): Dictionary with static aggregation components.
        """
        aggr_type = self._node2value(ctx.AGGR_FUNC())
        table = self._node2value(ctx.ID(0))
        column = self._node2value(ctx.STAR() if ctx.STAR() else ctx.ID(1))
        where = self._rule2value(ctx.where_stat())

        aggr_dict = {"AggrType"    : aggr_type,
                     "Table"       : table,
                     "Column"      : column,
                     "Where"       : where,
                    }
        return aggr_dict

    ################## Helper methods ##################

    def _node2value(self, 
                    node : TerminalNode | None) -> ParsedValue | None:
        r"""Converts a terminal node (token) to *`ParsedValue`*.  

        Extracts the text and position information from an ANTLR terminal node.
        
        Args:
            node (TerminalNode | None): ANTLR terminal node, or None.
        
        Returns:
            out (ParsedValue | None): Wrapped value with location, or None if node is None.
        """
        if not node:
            return None

        token = node.getSymbol()
        return ParsedValue(value=token.text, 
                           line=token.line, 
                           column=token.column)


    def _rule2value(self, 
                    ctx : ParserRuleContext | None) -> ParsedValue | None:
        r"""Converts a rule context to *`ParsedValue`*.  
        
        Visits the rule context and wraps the result with location info.
        
        Args:
            ctx (ParserRuleContext | None): ANTLR rule context, or None.
        
        Returns:
            out (ParsedValue | None): Wrapped visit result with location, or None if ctx is None.
        """
        if not ctx:
            return None
        
        return ParsedValue(value=self.visit(ctx),
                           line=ctx.start.line,
                           column=ctx.start.column)

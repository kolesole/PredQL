# Generated from ParserPQL.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,44,140,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        1,0,3,0,30,8,0,1,0,3,0,33,8,0,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,
        2,1,2,3,2,45,8,2,1,3,1,3,1,3,1,3,1,3,3,3,52,8,3,1,3,1,3,1,3,1,3,
        1,3,3,3,59,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,68,8,3,3,3,70,8,3,
        1,4,1,4,1,4,1,5,1,5,1,5,5,5,78,8,5,10,5,12,5,81,9,5,1,6,1,6,1,6,
        5,6,86,8,6,10,6,12,6,89,9,6,1,7,1,7,1,7,1,7,1,7,3,7,96,8,7,1,8,3,
        8,99,8,8,1,8,1,8,1,8,1,8,3,8,105,8,8,1,8,1,8,1,8,3,8,110,8,8,1,9,
        1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,3,
        12,126,8,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,134,8,12,3,12,136,
        8,12,1,12,1,12,1,12,0,0,13,0,2,4,6,8,10,12,14,16,18,20,22,24,0,2,
        2,0,38,38,42,42,1,0,31,33,147,0,26,1,0,0,0,2,36,1,0,0,0,4,39,1,0,
        0,0,6,69,1,0,0,0,8,71,1,0,0,0,10,74,1,0,0,0,12,82,1,0,0,0,14,95,
        1,0,0,0,16,98,1,0,0,0,18,111,1,0,0,0,20,114,1,0,0,0,22,117,1,0,0,
        0,24,119,1,0,0,0,26,27,3,6,3,0,27,29,3,4,2,0,28,30,3,2,1,0,29,28,
        1,0,0,0,29,30,1,0,0,0,30,32,1,0,0,0,31,33,3,8,4,0,32,31,1,0,0,0,
        32,33,1,0,0,0,33,34,1,0,0,0,34,35,5,39,0,0,35,1,1,0,0,0,36,37,5,
        1,0,0,37,38,3,10,5,0,38,3,1,0,0,0,39,40,5,2,0,0,40,41,5,42,0,0,41,
        42,5,34,0,0,42,44,5,42,0,0,43,45,3,8,4,0,44,43,1,0,0,0,44,45,1,0,
        0,0,45,5,1,0,0,0,46,47,5,3,0,0,47,51,3,24,12,0,48,49,5,6,0,0,49,
        52,5,33,0,0,50,52,5,5,0,0,51,48,1,0,0,0,51,50,1,0,0,0,51,52,1,0,
        0,0,52,70,1,0,0,0,53,54,5,3,0,0,54,58,3,10,5,0,55,56,5,6,0,0,56,
        59,5,33,0,0,57,59,5,5,0,0,58,55,1,0,0,0,58,57,1,0,0,0,58,59,1,0,
        0,0,59,70,1,0,0,0,60,61,5,3,0,0,61,62,5,42,0,0,62,63,5,34,0,0,63,
        67,7,0,0,0,64,65,5,6,0,0,65,68,5,33,0,0,66,68,5,5,0,0,67,64,1,0,
        0,0,67,66,1,0,0,0,67,68,1,0,0,0,68,70,1,0,0,0,69,46,1,0,0,0,69,53,
        1,0,0,0,69,60,1,0,0,0,70,7,1,0,0,0,71,72,5,4,0,0,72,73,3,10,5,0,
        73,9,1,0,0,0,74,79,3,12,6,0,75,76,5,29,0,0,76,78,3,12,6,0,77,75,
        1,0,0,0,78,81,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,11,1,0,0,0,
        81,79,1,0,0,0,82,87,3,14,7,0,83,84,5,28,0,0,84,86,3,14,7,0,85,83,
        1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,13,1,0,0,0,
        89,87,1,0,0,0,90,96,3,16,8,0,91,92,5,36,0,0,92,93,3,10,5,0,93,94,
        5,37,0,0,94,96,1,0,0,0,95,90,1,0,0,0,95,91,1,0,0,0,96,15,1,0,0,0,
        97,99,5,30,0,0,98,97,1,0,0,0,98,99,1,0,0,0,99,104,1,0,0,0,100,105,
        3,24,12,0,101,102,5,42,0,0,102,103,5,34,0,0,103,105,7,0,0,0,104,
        100,1,0,0,0,104,101,1,0,0,0,105,109,1,0,0,0,106,110,3,18,9,0,107,
        110,3,20,10,0,108,110,3,22,11,0,109,106,1,0,0,0,109,107,1,0,0,0,
        109,108,1,0,0,0,110,17,1,0,0,0,111,112,5,17,0,0,112,113,7,1,0,0,
        113,19,1,0,0,0,114,115,5,18,0,0,115,116,5,41,0,0,116,21,1,0,0,0,
        117,118,5,25,0,0,118,23,1,0,0,0,119,120,5,7,0,0,120,121,5,36,0,0,
        121,122,5,42,0,0,122,123,5,34,0,0,123,125,7,0,0,0,124,126,3,8,4,
        0,125,124,1,0,0,0,125,126,1,0,0,0,126,135,1,0,0,0,127,128,5,35,0,
        0,128,129,5,33,0,0,129,130,5,35,0,0,130,133,5,33,0,0,131,132,5,35,
        0,0,132,134,5,40,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,136,1,0,
        0,0,135,127,1,0,0,0,135,136,1,0,0,0,136,137,1,0,0,0,137,138,5,37,
        0,0,138,25,1,0,0,0,16,29,32,44,51,58,67,69,79,87,95,98,104,109,125,
        133,135
    ]

class ParserPQL ( Parser ):

    grammarFileName = "ParserPQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'.'", "','", "'('", "')'", 
                     "'*'", "';'" ]

    symbolicNames = [ "<INVALID>", "ASSUMING", "FOR_EACH", "PREDICT", "WHERE", 
                      "CLASSIFY", "RANK_TOP", "AGGR_FUNC", "AVG", "COUNT", 
                      "COUNT_DISTINCT", "FIRST", "LAST", "LIST_DISTINCT", 
                      "MAX", "MIN", "SUM", "NUM_COMP_OP", "STR_COMP_OP", 
                      "NOT_LIKE", "NOT_CONTAINS", "ENDS_WITH", "STARTS_WITH", 
                      "LIKE", "CONTAINS", "NULL_CHECK_OP", "IS_NOT_NULL", 
                      "IS_NULL", "AND", "OR", "NOT", "DATETIME", "FLOAT", 
                      "INT", "DOT", "COMMA", "OPEN_PAREN", "CLOSE_PAREN", 
                      "STAR", "SEMI_COLUMN", "TIME_MEASURE_UNIT", "STRING", 
                      "ID", "WS_SKIP", "ANY" ]

    RULE_query = 0
    RULE_assuming = 1
    RULE_for_each = 2
    RULE_predict = 3
    RULE_where = 4
    RULE_expr_or = 5
    RULE_expr_and = 6
    RULE_expr_term = 7
    RULE_condition = 8
    RULE_num_condition = 9
    RULE_str_condition = 10
    RULE_null_check_condition = 11
    RULE_aggregation = 12

    ruleNames =  [ "query", "assuming", "for_each", "predict", "where", 
                   "expr_or", "expr_and", "expr_term", "condition", "num_condition", 
                   "str_condition", "null_check_condition", "aggregation" ]

    EOF = Token.EOF
    ASSUMING=1
    FOR_EACH=2
    PREDICT=3
    WHERE=4
    CLASSIFY=5
    RANK_TOP=6
    AGGR_FUNC=7
    AVG=8
    COUNT=9
    COUNT_DISTINCT=10
    FIRST=11
    LAST=12
    LIST_DISTINCT=13
    MAX=14
    MIN=15
    SUM=16
    NUM_COMP_OP=17
    STR_COMP_OP=18
    NOT_LIKE=19
    NOT_CONTAINS=20
    ENDS_WITH=21
    STARTS_WITH=22
    LIKE=23
    CONTAINS=24
    NULL_CHECK_OP=25
    IS_NOT_NULL=26
    IS_NULL=27
    AND=28
    OR=29
    NOT=30
    DATETIME=31
    FLOAT=32
    INT=33
    DOT=34
    COMMA=35
    OPEN_PAREN=36
    CLOSE_PAREN=37
    STAR=38
    SEMI_COLUMN=39
    TIME_MEASURE_UNIT=40
    STRING=41
    ID=42
    WS_SKIP=43
    ANY=44

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def predict(self):
            return self.getTypedRuleContext(ParserPQL.PredictContext,0)


        def for_each(self):
            return self.getTypedRuleContext(ParserPQL.For_eachContext,0)


        def SEMI_COLUMN(self):
            return self.getToken(ParserPQL.SEMI_COLUMN, 0)

        def assuming(self):
            return self.getTypedRuleContext(ParserPQL.AssumingContext,0)


        def where(self):
            return self.getTypedRuleContext(ParserPQL.WhereContext,0)


        def getRuleIndex(self):
            return ParserPQL.RULE_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuery" ):
                return visitor.visitQuery(self)
            else:
                return visitor.visitChildren(self)




    def query(self):

        localctx = ParserPQL.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_query)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.predict()
            self.state = 27
            self.for_each()
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 28
                self.assuming()


            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 31
                self.where()


            self.state = 34
            self.match(ParserPQL.SEMI_COLUMN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssumingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSUMING(self):
            return self.getToken(ParserPQL.ASSUMING, 0)

        def expr_or(self):
            return self.getTypedRuleContext(ParserPQL.Expr_orContext,0)


        def getRuleIndex(self):
            return ParserPQL.RULE_assuming

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssuming" ):
                listener.enterAssuming(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssuming" ):
                listener.exitAssuming(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssuming" ):
                return visitor.visitAssuming(self)
            else:
                return visitor.visitChildren(self)




    def assuming(self):

        localctx = ParserPQL.AssumingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_assuming)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(ParserPQL.ASSUMING)
            self.state = 37
            self.expr_or()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_eachContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR_EACH(self):
            return self.getToken(ParserPQL.FOR_EACH, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ParserPQL.ID)
            else:
                return self.getToken(ParserPQL.ID, i)

        def DOT(self):
            return self.getToken(ParserPQL.DOT, 0)

        def where(self):
            return self.getTypedRuleContext(ParserPQL.WhereContext,0)


        def getRuleIndex(self):
            return ParserPQL.RULE_for_each

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_each" ):
                listener.enterFor_each(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_each" ):
                listener.exitFor_each(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_each" ):
                return visitor.visitFor_each(self)
            else:
                return visitor.visitChildren(self)




    def for_each(self):

        localctx = ParserPQL.For_eachContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_for_each)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(ParserPQL.FOR_EACH)
            self.state = 40
            self.match(ParserPQL.ID)
            self.state = 41
            self.match(ParserPQL.DOT)
            self.state = 42
            self.match(ParserPQL.ID)
            self.state = 44
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 43
                self.where()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PredictContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREDICT(self):
            return self.getToken(ParserPQL.PREDICT, 0)

        def aggregation(self):
            return self.getTypedRuleContext(ParserPQL.AggregationContext,0)


        def RANK_TOP(self):
            return self.getToken(ParserPQL.RANK_TOP, 0)

        def INT(self):
            return self.getToken(ParserPQL.INT, 0)

        def CLASSIFY(self):
            return self.getToken(ParserPQL.CLASSIFY, 0)

        def expr_or(self):
            return self.getTypedRuleContext(ParserPQL.Expr_orContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ParserPQL.ID)
            else:
                return self.getToken(ParserPQL.ID, i)

        def DOT(self):
            return self.getToken(ParserPQL.DOT, 0)

        def STAR(self):
            return self.getToken(ParserPQL.STAR, 0)

        def getRuleIndex(self):
            return ParserPQL.RULE_predict

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredict" ):
                listener.enterPredict(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredict" ):
                listener.exitPredict(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPredict" ):
                return visitor.visitPredict(self)
            else:
                return visitor.visitChildren(self)




    def predict(self):

        localctx = ParserPQL.PredictContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_predict)
        self._la = 0 # Token type
        try:
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.match(ParserPQL.PREDICT)
                self.state = 47
                self.aggregation()
                self.state = 51
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6]:
                    self.state = 48
                    self.match(ParserPQL.RANK_TOP)
                    self.state = 49
                    self.match(ParserPQL.INT)
                    pass
                elif token in [5]:
                    self.state = 50
                    self.match(ParserPQL.CLASSIFY)
                    pass
                elif token in [2]:
                    pass
                else:
                    pass
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.match(ParserPQL.PREDICT)
                self.state = 54
                self.expr_or()
                self.state = 58
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6]:
                    self.state = 55
                    self.match(ParserPQL.RANK_TOP)
                    self.state = 56
                    self.match(ParserPQL.INT)
                    pass
                elif token in [5]:
                    self.state = 57
                    self.match(ParserPQL.CLASSIFY)
                    pass
                elif token in [2]:
                    pass
                else:
                    pass
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 60
                self.match(ParserPQL.PREDICT)
                self.state = 61
                self.match(ParserPQL.ID)
                self.state = 62
                self.match(ParserPQL.DOT)
                self.state = 63
                _la = self._input.LA(1)
                if not(_la==38 or _la==42):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 67
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6]:
                    self.state = 64
                    self.match(ParserPQL.RANK_TOP)
                    self.state = 65
                    self.match(ParserPQL.INT)
                    pass
                elif token in [5]:
                    self.state = 66
                    self.match(ParserPQL.CLASSIFY)
                    pass
                elif token in [2]:
                    pass
                else:
                    pass
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhereContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(ParserPQL.WHERE, 0)

        def expr_or(self):
            return self.getTypedRuleContext(ParserPQL.Expr_orContext,0)


        def getRuleIndex(self):
            return ParserPQL.RULE_where

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhere" ):
                listener.enterWhere(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhere" ):
                listener.exitWhere(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhere" ):
                return visitor.visitWhere(self)
            else:
                return visitor.visitChildren(self)




    def where(self):

        localctx = ParserPQL.WhereContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_where)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(ParserPQL.WHERE)
            self.state = 72
            self.expr_or()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_orContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_and(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserPQL.Expr_andContext)
            else:
                return self.getTypedRuleContext(ParserPQL.Expr_andContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(ParserPQL.OR)
            else:
                return self.getToken(ParserPQL.OR, i)

        def getRuleIndex(self):
            return ParserPQL.RULE_expr_or

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_or" ):
                listener.enterExpr_or(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_or" ):
                listener.exitExpr_or(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_or" ):
                return visitor.visitExpr_or(self)
            else:
                return visitor.visitChildren(self)




    def expr_or(self):

        localctx = ParserPQL.Expr_orContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expr_or)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.expr_and()
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 75
                self.match(ParserPQL.OR)
                self.state = 76
                self.expr_and()
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_andContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserPQL.Expr_termContext)
            else:
                return self.getTypedRuleContext(ParserPQL.Expr_termContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(ParserPQL.AND)
            else:
                return self.getToken(ParserPQL.AND, i)

        def getRuleIndex(self):
            return ParserPQL.RULE_expr_and

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_and" ):
                listener.enterExpr_and(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_and" ):
                listener.exitExpr_and(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_and" ):
                return visitor.visitExpr_and(self)
            else:
                return visitor.visitChildren(self)




    def expr_and(self):

        localctx = ParserPQL.Expr_andContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expr_and)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.expr_term()
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 83
                self.match(ParserPQL.AND)
                self.state = 84
                self.expr_term()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_termContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(ParserPQL.ConditionContext,0)


        def OPEN_PAREN(self):
            return self.getToken(ParserPQL.OPEN_PAREN, 0)

        def expr_or(self):
            return self.getTypedRuleContext(ParserPQL.Expr_orContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(ParserPQL.CLOSE_PAREN, 0)

        def getRuleIndex(self):
            return ParserPQL.RULE_expr_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_term" ):
                listener.enterExpr_term(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_term" ):
                listener.exitExpr_term(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_term" ):
                return visitor.visitExpr_term(self)
            else:
                return visitor.visitChildren(self)




    def expr_term(self):

        localctx = ParserPQL.Expr_termContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expr_term)
        try:
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 30, 42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.condition()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.match(ParserPQL.OPEN_PAREN)
                self.state = 92
                self.expr_or()
                self.state = 93
                self.match(ParserPQL.CLOSE_PAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def aggregation(self):
            return self.getTypedRuleContext(ParserPQL.AggregationContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ParserPQL.ID)
            else:
                return self.getToken(ParserPQL.ID, i)

        def DOT(self):
            return self.getToken(ParserPQL.DOT, 0)

        def num_condition(self):
            return self.getTypedRuleContext(ParserPQL.Num_conditionContext,0)


        def str_condition(self):
            return self.getTypedRuleContext(ParserPQL.Str_conditionContext,0)


        def null_check_condition(self):
            return self.getTypedRuleContext(ParserPQL.Null_check_conditionContext,0)


        def NOT(self):
            return self.getToken(ParserPQL.NOT, 0)

        def STAR(self):
            return self.getToken(ParserPQL.STAR, 0)

        def getRuleIndex(self):
            return ParserPQL.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = ParserPQL.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 97
                self.match(ParserPQL.NOT)


            self.state = 104
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.state = 100
                self.aggregation()
                pass
            elif token in [42]:
                self.state = 101
                self.match(ParserPQL.ID)
                self.state = 102
                self.match(ParserPQL.DOT)
                self.state = 103
                _la = self._input.LA(1)
                if not(_la==38 or _la==42):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.state = 106
                self.num_condition()
                pass
            elif token in [18]:
                self.state = 107
                self.str_condition()
                pass
            elif token in [25]:
                self.state = 108
                self.null_check_condition()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Num_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_COMP_OP(self):
            return self.getToken(ParserPQL.NUM_COMP_OP, 0)

        def DATETIME(self):
            return self.getToken(ParserPQL.DATETIME, 0)

        def FLOAT(self):
            return self.getToken(ParserPQL.FLOAT, 0)

        def INT(self):
            return self.getToken(ParserPQL.INT, 0)

        def getRuleIndex(self):
            return ParserPQL.RULE_num_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNum_condition" ):
                listener.enterNum_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNum_condition" ):
                listener.exitNum_condition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum_condition" ):
                return visitor.visitNum_condition(self)
            else:
                return visitor.visitChildren(self)




    def num_condition(self):

        localctx = ParserPQL.Num_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_num_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(ParserPQL.NUM_COMP_OP)
            self.state = 112
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15032385536) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Str_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STR_COMP_OP(self):
            return self.getToken(ParserPQL.STR_COMP_OP, 0)

        def STRING(self):
            return self.getToken(ParserPQL.STRING, 0)

        def getRuleIndex(self):
            return ParserPQL.RULE_str_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStr_condition" ):
                listener.enterStr_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStr_condition" ):
                listener.exitStr_condition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStr_condition" ):
                return visitor.visitStr_condition(self)
            else:
                return visitor.visitChildren(self)




    def str_condition(self):

        localctx = ParserPQL.Str_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_str_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(ParserPQL.STR_COMP_OP)
            self.state = 115
            self.match(ParserPQL.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Null_check_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NULL_CHECK_OP(self):
            return self.getToken(ParserPQL.NULL_CHECK_OP, 0)

        def getRuleIndex(self):
            return ParserPQL.RULE_null_check_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNull_check_condition" ):
                listener.enterNull_check_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNull_check_condition" ):
                listener.exitNull_check_condition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNull_check_condition" ):
                return visitor.visitNull_check_condition(self)
            else:
                return visitor.visitChildren(self)




    def null_check_condition(self):

        localctx = ParserPQL.Null_check_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_null_check_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(ParserPQL.NULL_CHECK_OP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggregationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AGGR_FUNC(self):
            return self.getToken(ParserPQL.AGGR_FUNC, 0)

        def OPEN_PAREN(self):
            return self.getToken(ParserPQL.OPEN_PAREN, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ParserPQL.ID)
            else:
                return self.getToken(ParserPQL.ID, i)

        def DOT(self):
            return self.getToken(ParserPQL.DOT, 0)

        def CLOSE_PAREN(self):
            return self.getToken(ParserPQL.CLOSE_PAREN, 0)

        def STAR(self):
            return self.getToken(ParserPQL.STAR, 0)

        def where(self):
            return self.getTypedRuleContext(ParserPQL.WhereContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ParserPQL.COMMA)
            else:
                return self.getToken(ParserPQL.COMMA, i)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(ParserPQL.INT)
            else:
                return self.getToken(ParserPQL.INT, i)

        def TIME_MEASURE_UNIT(self):
            return self.getToken(ParserPQL.TIME_MEASURE_UNIT, 0)

        def getRuleIndex(self):
            return ParserPQL.RULE_aggregation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregation" ):
                listener.enterAggregation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregation" ):
                listener.exitAggregation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregation" ):
                return visitor.visitAggregation(self)
            else:
                return visitor.visitChildren(self)




    def aggregation(self):

        localctx = ParserPQL.AggregationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_aggregation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(ParserPQL.AGGR_FUNC)
            self.state = 120
            self.match(ParserPQL.OPEN_PAREN)
            self.state = 121
            self.match(ParserPQL.ID)
            self.state = 122
            self.match(ParserPQL.DOT)
            self.state = 123
            _la = self._input.LA(1)
            if not(_la==38 or _la==42):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 124
                self.where()


            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 127
                self.match(ParserPQL.COMMA)
                self.state = 128
                self.match(ParserPQL.INT)
                self.state = 129
                self.match(ParserPQL.COMMA)
                self.state = 130
                self.match(ParserPQL.INT)
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==35:
                    self.state = 131
                    self.match(ParserPQL.COMMA)
                    self.state = 132
                    self.match(ParserPQL.TIME_MEASURE_UNIT)




            self.state = 137
            self.match(ParserPQL.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






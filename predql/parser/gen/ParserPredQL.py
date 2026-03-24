# Generated from ParserPredQL.g4 by ANTLR 4.13.2
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
        4,1,44,211,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,1,0,3,0,47,8,0,1,1,1,1,1,1,3,1,52,8,1,1,1,3,1,
        55,8,1,1,1,1,1,1,2,1,2,1,2,3,2,62,8,2,1,2,1,2,1,3,1,3,1,3,1,3,1,
        3,3,3,71,8,3,1,4,1,4,1,4,1,4,1,4,3,4,78,8,4,1,4,1,4,3,4,82,8,4,1,
        5,1,5,1,5,1,5,1,5,3,5,89,8,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,97,8,5,
        1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,5,9,111,8,9,10,9,
        12,9,114,9,9,1,10,1,10,1,10,5,10,119,8,10,10,10,12,10,122,9,10,1,
        11,1,11,1,11,5,11,127,8,11,10,11,12,11,130,9,11,1,12,1,12,1,12,5,
        12,135,8,12,10,12,12,12,138,9,12,1,13,1,13,1,13,1,13,1,13,3,13,145,
        8,13,1,14,1,14,1,14,1,14,1,14,3,14,152,8,14,1,15,3,15,155,8,15,1,
        15,1,15,1,15,1,15,3,15,161,8,15,1,16,3,16,164,8,16,1,16,1,16,1,16,
        1,16,3,16,170,8,16,1,16,1,16,1,16,3,16,175,8,16,1,17,1,17,1,17,1,
        18,1,18,1,18,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,3,20,191,8,
        20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,
        21,1,21,3,21,207,8,21,1,21,1,21,1,21,0,0,22,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,0,2,2,0,32,32,42,42,1,0,37,
        39,215,0,46,1,0,0,0,2,48,1,0,0,0,4,58,1,0,0,0,6,65,1,0,0,0,8,81,
        1,0,0,0,10,96,1,0,0,0,12,98,1,0,0,0,14,101,1,0,0,0,16,104,1,0,0,
        0,18,107,1,0,0,0,20,115,1,0,0,0,22,123,1,0,0,0,24,131,1,0,0,0,26,
        144,1,0,0,0,28,151,1,0,0,0,30,154,1,0,0,0,32,163,1,0,0,0,34,176,
        1,0,0,0,36,179,1,0,0,0,38,182,1,0,0,0,40,184,1,0,0,0,42,200,1,0,
        0,0,44,47,3,2,1,0,45,47,3,4,2,0,46,44,1,0,0,0,46,45,1,0,0,0,47,1,
        1,0,0,0,48,49,3,8,4,0,49,51,3,6,3,0,50,52,3,12,6,0,51,50,1,0,0,0,
        51,52,1,0,0,0,52,54,1,0,0,0,53,55,3,14,7,0,54,53,1,0,0,0,54,55,1,
        0,0,0,55,56,1,0,0,0,56,57,5,33,0,0,57,3,1,0,0,0,58,59,3,10,5,0,59,
        61,3,6,3,0,60,62,3,16,8,0,61,60,1,0,0,0,61,62,1,0,0,0,62,63,1,0,
        0,0,63,64,5,33,0,0,64,5,1,0,0,0,65,66,5,2,0,0,66,67,5,42,0,0,67,
        68,5,28,0,0,68,70,7,0,0,0,69,71,3,16,8,0,70,69,1,0,0,0,70,71,1,0,
        0,0,71,7,1,0,0,0,72,73,5,3,0,0,73,77,3,40,20,0,74,75,5,6,0,0,75,
        78,5,39,0,0,76,78,5,5,0,0,77,74,1,0,0,0,77,76,1,0,0,0,77,78,1,0,
        0,0,78,82,1,0,0,0,79,80,5,3,0,0,80,82,3,18,9,0,81,72,1,0,0,0,81,
        79,1,0,0,0,82,9,1,0,0,0,83,84,5,3,0,0,84,88,3,42,21,0,85,86,5,6,
        0,0,86,89,5,39,0,0,87,89,5,5,0,0,88,85,1,0,0,0,88,87,1,0,0,0,88,
        89,1,0,0,0,89,97,1,0,0,0,90,91,5,3,0,0,91,97,3,20,10,0,92,93,5,3,
        0,0,93,94,5,42,0,0,94,95,5,28,0,0,95,97,7,0,0,0,96,83,1,0,0,0,96,
        90,1,0,0,0,96,92,1,0,0,0,97,11,1,0,0,0,98,99,5,1,0,0,99,100,3,18,
        9,0,100,13,1,0,0,0,101,102,5,4,0,0,102,103,3,18,9,0,103,15,1,0,0,
        0,104,105,5,4,0,0,105,106,3,20,10,0,106,17,1,0,0,0,107,112,3,22,
        11,0,108,109,5,35,0,0,109,111,3,22,11,0,110,108,1,0,0,0,111,114,
        1,0,0,0,112,110,1,0,0,0,112,113,1,0,0,0,113,19,1,0,0,0,114,112,1,
        0,0,0,115,120,3,24,12,0,116,117,5,35,0,0,117,119,3,24,12,0,118,116,
        1,0,0,0,119,122,1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,21,1,
        0,0,0,122,120,1,0,0,0,123,128,3,26,13,0,124,125,5,34,0,0,125,127,
        3,26,13,0,126,124,1,0,0,0,127,130,1,0,0,0,128,126,1,0,0,0,128,129,
        1,0,0,0,129,23,1,0,0,0,130,128,1,0,0,0,131,136,3,28,14,0,132,133,
        5,34,0,0,133,135,3,28,14,0,134,132,1,0,0,0,135,138,1,0,0,0,136,134,
        1,0,0,0,136,137,1,0,0,0,137,25,1,0,0,0,138,136,1,0,0,0,139,145,3,
        30,15,0,140,141,5,30,0,0,141,142,3,18,9,0,142,143,5,31,0,0,143,145,
        1,0,0,0,144,139,1,0,0,0,144,140,1,0,0,0,145,27,1,0,0,0,146,152,3,
        32,16,0,147,148,5,30,0,0,148,149,3,20,10,0,149,150,5,31,0,0,150,
        152,1,0,0,0,151,146,1,0,0,0,151,147,1,0,0,0,152,29,1,0,0,0,153,155,
        5,36,0,0,154,153,1,0,0,0,154,155,1,0,0,0,155,156,1,0,0,0,156,160,
        3,40,20,0,157,161,3,34,17,0,158,161,3,36,18,0,159,161,3,38,19,0,
        160,157,1,0,0,0,160,158,1,0,0,0,160,159,1,0,0,0,161,31,1,0,0,0,162,
        164,5,36,0,0,163,162,1,0,0,0,163,164,1,0,0,0,164,169,1,0,0,0,165,
        170,3,42,21,0,166,167,5,42,0,0,167,168,5,28,0,0,168,170,7,0,0,0,
        169,165,1,0,0,0,169,166,1,0,0,0,170,174,1,0,0,0,171,175,3,34,17,
        0,172,175,3,36,18,0,173,175,3,38,19,0,174,171,1,0,0,0,174,172,1,
        0,0,0,174,173,1,0,0,0,175,33,1,0,0,0,176,177,5,17,0,0,177,178,7,
        1,0,0,178,35,1,0,0,0,179,180,5,18,0,0,180,181,5,41,0,0,181,37,1,
        0,0,0,182,183,5,25,0,0,183,39,1,0,0,0,184,185,5,7,0,0,185,186,5,
        30,0,0,186,187,5,42,0,0,187,188,5,28,0,0,188,190,7,0,0,0,189,191,
        3,16,8,0,190,189,1,0,0,0,190,191,1,0,0,0,191,192,1,0,0,0,192,193,
        5,29,0,0,193,194,5,39,0,0,194,195,5,29,0,0,195,196,5,39,0,0,196,
        197,5,29,0,0,197,198,5,40,0,0,198,199,5,31,0,0,199,41,1,0,0,0,200,
        201,5,7,0,0,201,202,5,30,0,0,202,203,5,42,0,0,203,204,5,28,0,0,204,
        206,7,0,0,0,205,207,3,16,8,0,206,205,1,0,0,0,206,207,1,0,0,0,207,
        208,1,0,0,0,208,209,5,31,0,0,209,43,1,0,0,0,22,46,51,54,61,70,77,
        81,88,96,112,120,128,136,144,151,154,160,163,169,174,190,206
    ]

class ParserPredQL ( Parser ):

    grammarFileName = "ParserPredQL.g4"

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
                     "'.'", "','", "'('", "')'", "'*'", "';'" ]

    symbolicNames = [ "<INVALID>", "ASSUMING", "FOR_EACH", "PREDICT", "WHERE", 
                      "CLASSIFY", "RANK_TOP", "AGGR_FUNC", "AVG", "COUNT", 
                      "COUNT_DISTINCT", "FIRST", "LAST", "LIST_DISTINCT", 
                      "MAX", "MIN", "SUM", "NUM_COMP_OP", "STR_COMP_OP", 
                      "NOT_LIKE", "NOT_CONTAINS", "ENDS_WITH", "STARTS_WITH", 
                      "LIKE", "CONTAINS", "NULL_CHECK_OP", "IS_NOT_NULL", 
                      "IS_NULL", "DOT", "COMMA", "OPEN_PAREN", "CLOSE_PAREN", 
                      "STAR", "SEMICOLON", "AND", "OR", "NOT", "DATETIME", 
                      "FLOAT", "INT", "TIME_MEASURE_UNIT", "STRING", "ID", 
                      "WS_SKIP", "ANY" ]

    RULE_query = 0
    RULE_query_tmp = 1
    RULE_query_stat = 2
    RULE_for_each = 3
    RULE_predict_tmp = 4
    RULE_predict_stat = 5
    RULE_assuming = 6
    RULE_where_tmp = 7
    RULE_where_stat = 8
    RULE_expr_or_tmp = 9
    RULE_expr_or_stat = 10
    RULE_expr_and_tmp = 11
    RULE_expr_and_stat = 12
    RULE_expr_term_tmp = 13
    RULE_expr_term_stat = 14
    RULE_condition_tmp = 15
    RULE_condition_stat = 16
    RULE_num_condition = 17
    RULE_str_condition = 18
    RULE_null_check_condition = 19
    RULE_aggregation_tmp = 20
    RULE_aggregation_stat = 21

    ruleNames =  [ "query", "query_tmp", "query_stat", "for_each", "predict_tmp", 
                   "predict_stat", "assuming", "where_tmp", "where_stat", 
                   "expr_or_tmp", "expr_or_stat", "expr_and_tmp", "expr_and_stat", 
                   "expr_term_tmp", "expr_term_stat", "condition_tmp", "condition_stat", 
                   "num_condition", "str_condition", "null_check_condition", 
                   "aggregation_tmp", "aggregation_stat" ]

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
    DOT=28
    COMMA=29
    OPEN_PAREN=30
    CLOSE_PAREN=31
    STAR=32
    SEMICOLON=33
    AND=34
    OR=35
    NOT=36
    DATETIME=37
    FLOAT=38
    INT=39
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

        def query_tmp(self):
            return self.getTypedRuleContext(ParserPredQL.Query_tmpContext,0)


        def query_stat(self):
            return self.getTypedRuleContext(ParserPredQL.Query_statContext,0)


        def getRuleIndex(self):
            return ParserPredQL.RULE_query

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

        localctx = ParserPredQL.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_query)
        try:
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.query_tmp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.query_stat()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Query_tmpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def predict_tmp(self):
            return self.getTypedRuleContext(ParserPredQL.Predict_tmpContext,0)


        def for_each(self):
            return self.getTypedRuleContext(ParserPredQL.For_eachContext,0)


        def SEMICOLON(self):
            return self.getToken(ParserPredQL.SEMICOLON, 0)

        def assuming(self):
            return self.getTypedRuleContext(ParserPredQL.AssumingContext,0)


        def where_tmp(self):
            return self.getTypedRuleContext(ParserPredQL.Where_tmpContext,0)


        def getRuleIndex(self):
            return ParserPredQL.RULE_query_tmp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery_tmp" ):
                listener.enterQuery_tmp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery_tmp" ):
                listener.exitQuery_tmp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuery_tmp" ):
                return visitor.visitQuery_tmp(self)
            else:
                return visitor.visitChildren(self)




    def query_tmp(self):

        localctx = ParserPredQL.Query_tmpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_query_tmp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.predict_tmp()
            self.state = 49
            self.for_each()
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 50
                self.assuming()


            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 53
                self.where_tmp()


            self.state = 56
            self.match(ParserPredQL.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Query_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def predict_stat(self):
            return self.getTypedRuleContext(ParserPredQL.Predict_statContext,0)


        def for_each(self):
            return self.getTypedRuleContext(ParserPredQL.For_eachContext,0)


        def SEMICOLON(self):
            return self.getToken(ParserPredQL.SEMICOLON, 0)

        def where_stat(self):
            return self.getTypedRuleContext(ParserPredQL.Where_statContext,0)


        def getRuleIndex(self):
            return ParserPredQL.RULE_query_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery_stat" ):
                listener.enterQuery_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery_stat" ):
                listener.exitQuery_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuery_stat" ):
                return visitor.visitQuery_stat(self)
            else:
                return visitor.visitChildren(self)




    def query_stat(self):

        localctx = ParserPredQL.Query_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_query_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.predict_stat()
            self.state = 59
            self.for_each()
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 60
                self.where_stat()


            self.state = 63
            self.match(ParserPredQL.SEMICOLON)
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
            return self.getToken(ParserPredQL.FOR_EACH, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ParserPredQL.ID)
            else:
                return self.getToken(ParserPredQL.ID, i)

        def DOT(self):
            return self.getToken(ParserPredQL.DOT, 0)

        def STAR(self):
            return self.getToken(ParserPredQL.STAR, 0)

        def where_stat(self):
            return self.getTypedRuleContext(ParserPredQL.Where_statContext,0)


        def getRuleIndex(self):
            return ParserPredQL.RULE_for_each

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

        localctx = ParserPredQL.For_eachContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_for_each)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(ParserPredQL.FOR_EACH)
            self.state = 66
            self.match(ParserPredQL.ID)
            self.state = 67
            self.match(ParserPredQL.DOT)
            self.state = 68
            _la = self._input.LA(1)
            if not(_la==32 or _la==42):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 69
                self.where_stat()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Predict_tmpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREDICT(self):
            return self.getToken(ParserPredQL.PREDICT, 0)

        def aggregation_tmp(self):
            return self.getTypedRuleContext(ParserPredQL.Aggregation_tmpContext,0)


        def RANK_TOP(self):
            return self.getToken(ParserPredQL.RANK_TOP, 0)

        def INT(self):
            return self.getToken(ParserPredQL.INT, 0)

        def CLASSIFY(self):
            return self.getToken(ParserPredQL.CLASSIFY, 0)

        def expr_or_tmp(self):
            return self.getTypedRuleContext(ParserPredQL.Expr_or_tmpContext,0)


        def getRuleIndex(self):
            return ParserPredQL.RULE_predict_tmp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredict_tmp" ):
                listener.enterPredict_tmp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredict_tmp" ):
                listener.exitPredict_tmp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPredict_tmp" ):
                return visitor.visitPredict_tmp(self)
            else:
                return visitor.visitChildren(self)




    def predict_tmp(self):

        localctx = ParserPredQL.Predict_tmpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_predict_tmp)
        try:
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.match(ParserPredQL.PREDICT)
                self.state = 73
                self.aggregation_tmp()
                self.state = 77
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6]:
                    self.state = 74
                    self.match(ParserPredQL.RANK_TOP)
                    self.state = 75
                    self.match(ParserPredQL.INT)
                    pass
                elif token in [5]:
                    self.state = 76
                    self.match(ParserPredQL.CLASSIFY)
                    pass
                elif token in [2]:
                    pass
                else:
                    pass
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.match(ParserPredQL.PREDICT)
                self.state = 80
                self.expr_or_tmp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Predict_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREDICT(self):
            return self.getToken(ParserPredQL.PREDICT, 0)

        def aggregation_stat(self):
            return self.getTypedRuleContext(ParserPredQL.Aggregation_statContext,0)


        def RANK_TOP(self):
            return self.getToken(ParserPredQL.RANK_TOP, 0)

        def INT(self):
            return self.getToken(ParserPredQL.INT, 0)

        def CLASSIFY(self):
            return self.getToken(ParserPredQL.CLASSIFY, 0)

        def expr_or_stat(self):
            return self.getTypedRuleContext(ParserPredQL.Expr_or_statContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ParserPredQL.ID)
            else:
                return self.getToken(ParserPredQL.ID, i)

        def DOT(self):
            return self.getToken(ParserPredQL.DOT, 0)

        def STAR(self):
            return self.getToken(ParserPredQL.STAR, 0)

        def getRuleIndex(self):
            return ParserPredQL.RULE_predict_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredict_stat" ):
                listener.enterPredict_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredict_stat" ):
                listener.exitPredict_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPredict_stat" ):
                return visitor.visitPredict_stat(self)
            else:
                return visitor.visitChildren(self)




    def predict_stat(self):

        localctx = ParserPredQL.Predict_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_predict_stat)
        self._la = 0 # Token type
        try:
            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.match(ParserPredQL.PREDICT)
                self.state = 84
                self.aggregation_stat()
                self.state = 88
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6]:
                    self.state = 85
                    self.match(ParserPredQL.RANK_TOP)
                    self.state = 86
                    self.match(ParserPredQL.INT)
                    pass
                elif token in [5]:
                    self.state = 87
                    self.match(ParserPredQL.CLASSIFY)
                    pass
                elif token in [2]:
                    pass
                else:
                    pass
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.match(ParserPredQL.PREDICT)
                self.state = 91
                self.expr_or_stat()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 92
                self.match(ParserPredQL.PREDICT)
                self.state = 93
                self.match(ParserPredQL.ID)
                self.state = 94
                self.match(ParserPredQL.DOT)
                self.state = 95
                _la = self._input.LA(1)
                if not(_la==32 or _la==42):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass


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
            return self.getToken(ParserPredQL.ASSUMING, 0)

        def expr_or_tmp(self):
            return self.getTypedRuleContext(ParserPredQL.Expr_or_tmpContext,0)


        def getRuleIndex(self):
            return ParserPredQL.RULE_assuming

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

        localctx = ParserPredQL.AssumingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assuming)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(ParserPredQL.ASSUMING)
            self.state = 99
            self.expr_or_tmp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Where_tmpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(ParserPredQL.WHERE, 0)

        def expr_or_tmp(self):
            return self.getTypedRuleContext(ParserPredQL.Expr_or_tmpContext,0)


        def getRuleIndex(self):
            return ParserPredQL.RULE_where_tmp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhere_tmp" ):
                listener.enterWhere_tmp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhere_tmp" ):
                listener.exitWhere_tmp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhere_tmp" ):
                return visitor.visitWhere_tmp(self)
            else:
                return visitor.visitChildren(self)




    def where_tmp(self):

        localctx = ParserPredQL.Where_tmpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_where_tmp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(ParserPredQL.WHERE)
            self.state = 102
            self.expr_or_tmp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Where_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(ParserPredQL.WHERE, 0)

        def expr_or_stat(self):
            return self.getTypedRuleContext(ParserPredQL.Expr_or_statContext,0)


        def getRuleIndex(self):
            return ParserPredQL.RULE_where_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhere_stat" ):
                listener.enterWhere_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhere_stat" ):
                listener.exitWhere_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhere_stat" ):
                return visitor.visitWhere_stat(self)
            else:
                return visitor.visitChildren(self)




    def where_stat(self):

        localctx = ParserPredQL.Where_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_where_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(ParserPredQL.WHERE)
            self.state = 105
            self.expr_or_stat()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_or_tmpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_and_tmp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserPredQL.Expr_and_tmpContext)
            else:
                return self.getTypedRuleContext(ParserPredQL.Expr_and_tmpContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(ParserPredQL.OR)
            else:
                return self.getToken(ParserPredQL.OR, i)

        def getRuleIndex(self):
            return ParserPredQL.RULE_expr_or_tmp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_or_tmp" ):
                listener.enterExpr_or_tmp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_or_tmp" ):
                listener.exitExpr_or_tmp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_or_tmp" ):
                return visitor.visitExpr_or_tmp(self)
            else:
                return visitor.visitChildren(self)




    def expr_or_tmp(self):

        localctx = ParserPredQL.Expr_or_tmpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expr_or_tmp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.expr_and_tmp()
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 108
                self.match(ParserPredQL.OR)
                self.state = 109
                self.expr_and_tmp()
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_or_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_and_stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserPredQL.Expr_and_statContext)
            else:
                return self.getTypedRuleContext(ParserPredQL.Expr_and_statContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(ParserPredQL.OR)
            else:
                return self.getToken(ParserPredQL.OR, i)

        def getRuleIndex(self):
            return ParserPredQL.RULE_expr_or_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_or_stat" ):
                listener.enterExpr_or_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_or_stat" ):
                listener.exitExpr_or_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_or_stat" ):
                return visitor.visitExpr_or_stat(self)
            else:
                return visitor.visitChildren(self)




    def expr_or_stat(self):

        localctx = ParserPredQL.Expr_or_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expr_or_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.expr_and_stat()
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 116
                self.match(ParserPredQL.OR)
                self.state = 117
                self.expr_and_stat()
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_and_tmpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_term_tmp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserPredQL.Expr_term_tmpContext)
            else:
                return self.getTypedRuleContext(ParserPredQL.Expr_term_tmpContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(ParserPredQL.AND)
            else:
                return self.getToken(ParserPredQL.AND, i)

        def getRuleIndex(self):
            return ParserPredQL.RULE_expr_and_tmp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_and_tmp" ):
                listener.enterExpr_and_tmp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_and_tmp" ):
                listener.exitExpr_and_tmp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_and_tmp" ):
                return visitor.visitExpr_and_tmp(self)
            else:
                return visitor.visitChildren(self)




    def expr_and_tmp(self):

        localctx = ParserPredQL.Expr_and_tmpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expr_and_tmp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.expr_term_tmp()
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 124
                self.match(ParserPredQL.AND)
                self.state = 125
                self.expr_term_tmp()
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_and_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_term_stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserPredQL.Expr_term_statContext)
            else:
                return self.getTypedRuleContext(ParserPredQL.Expr_term_statContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(ParserPredQL.AND)
            else:
                return self.getToken(ParserPredQL.AND, i)

        def getRuleIndex(self):
            return ParserPredQL.RULE_expr_and_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_and_stat" ):
                listener.enterExpr_and_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_and_stat" ):
                listener.exitExpr_and_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_and_stat" ):
                return visitor.visitExpr_and_stat(self)
            else:
                return visitor.visitChildren(self)




    def expr_and_stat(self):

        localctx = ParserPredQL.Expr_and_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expr_and_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.expr_term_stat()
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 132
                self.match(ParserPredQL.AND)
                self.state = 133
                self.expr_term_stat()
                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_term_tmpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition_tmp(self):
            return self.getTypedRuleContext(ParserPredQL.Condition_tmpContext,0)


        def OPEN_PAREN(self):
            return self.getToken(ParserPredQL.OPEN_PAREN, 0)

        def expr_or_tmp(self):
            return self.getTypedRuleContext(ParserPredQL.Expr_or_tmpContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(ParserPredQL.CLOSE_PAREN, 0)

        def getRuleIndex(self):
            return ParserPredQL.RULE_expr_term_tmp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_term_tmp" ):
                listener.enterExpr_term_tmp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_term_tmp" ):
                listener.exitExpr_term_tmp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_term_tmp" ):
                return visitor.visitExpr_term_tmp(self)
            else:
                return visitor.visitChildren(self)




    def expr_term_tmp(self):

        localctx = ParserPredQL.Expr_term_tmpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expr_term_tmp)
        try:
            self.state = 144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.condition_tmp()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.match(ParserPredQL.OPEN_PAREN)
                self.state = 141
                self.expr_or_tmp()
                self.state = 142
                self.match(ParserPredQL.CLOSE_PAREN)
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


    class Expr_term_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition_stat(self):
            return self.getTypedRuleContext(ParserPredQL.Condition_statContext,0)


        def OPEN_PAREN(self):
            return self.getToken(ParserPredQL.OPEN_PAREN, 0)

        def expr_or_stat(self):
            return self.getTypedRuleContext(ParserPredQL.Expr_or_statContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(ParserPredQL.CLOSE_PAREN, 0)

        def getRuleIndex(self):
            return ParserPredQL.RULE_expr_term_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_term_stat" ):
                listener.enterExpr_term_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_term_stat" ):
                listener.exitExpr_term_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_term_stat" ):
                return visitor.visitExpr_term_stat(self)
            else:
                return visitor.visitChildren(self)




    def expr_term_stat(self):

        localctx = ParserPredQL.Expr_term_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expr_term_stat)
        try:
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 36, 42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.condition_stat()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.match(ParserPredQL.OPEN_PAREN)
                self.state = 148
                self.expr_or_stat()
                self.state = 149
                self.match(ParserPredQL.CLOSE_PAREN)
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


    class Condition_tmpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def aggregation_tmp(self):
            return self.getTypedRuleContext(ParserPredQL.Aggregation_tmpContext,0)


        def num_condition(self):
            return self.getTypedRuleContext(ParserPredQL.Num_conditionContext,0)


        def str_condition(self):
            return self.getTypedRuleContext(ParserPredQL.Str_conditionContext,0)


        def null_check_condition(self):
            return self.getTypedRuleContext(ParserPredQL.Null_check_conditionContext,0)


        def NOT(self):
            return self.getToken(ParserPredQL.NOT, 0)

        def getRuleIndex(self):
            return ParserPredQL.RULE_condition_tmp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition_tmp" ):
                listener.enterCondition_tmp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition_tmp" ):
                listener.exitCondition_tmp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition_tmp" ):
                return visitor.visitCondition_tmp(self)
            else:
                return visitor.visitChildren(self)




    def condition_tmp(self):

        localctx = ParserPredQL.Condition_tmpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_condition_tmp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 153
                self.match(ParserPredQL.NOT)


            self.state = 156
            self.aggregation_tmp()
            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.state = 157
                self.num_condition()
                pass
            elif token in [18]:
                self.state = 158
                self.str_condition()
                pass
            elif token in [25]:
                self.state = 159
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


    class Condition_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def aggregation_stat(self):
            return self.getTypedRuleContext(ParserPredQL.Aggregation_statContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ParserPredQL.ID)
            else:
                return self.getToken(ParserPredQL.ID, i)

        def DOT(self):
            return self.getToken(ParserPredQL.DOT, 0)

        def num_condition(self):
            return self.getTypedRuleContext(ParserPredQL.Num_conditionContext,0)


        def str_condition(self):
            return self.getTypedRuleContext(ParserPredQL.Str_conditionContext,0)


        def null_check_condition(self):
            return self.getTypedRuleContext(ParserPredQL.Null_check_conditionContext,0)


        def NOT(self):
            return self.getToken(ParserPredQL.NOT, 0)

        def STAR(self):
            return self.getToken(ParserPredQL.STAR, 0)

        def getRuleIndex(self):
            return ParserPredQL.RULE_condition_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition_stat" ):
                listener.enterCondition_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition_stat" ):
                listener.exitCondition_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition_stat" ):
                return visitor.visitCondition_stat(self)
            else:
                return visitor.visitChildren(self)




    def condition_stat(self):

        localctx = ParserPredQL.Condition_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_condition_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 162
                self.match(ParserPredQL.NOT)


            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.state = 165
                self.aggregation_stat()
                pass
            elif token in [42]:
                self.state = 166
                self.match(ParserPredQL.ID)
                self.state = 167
                self.match(ParserPredQL.DOT)
                self.state = 168
                _la = self._input.LA(1)
                if not(_la==32 or _la==42):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 174
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.state = 171
                self.num_condition()
                pass
            elif token in [18]:
                self.state = 172
                self.str_condition()
                pass
            elif token in [25]:
                self.state = 173
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
            return self.getToken(ParserPredQL.NUM_COMP_OP, 0)

        def DATETIME(self):
            return self.getToken(ParserPredQL.DATETIME, 0)

        def FLOAT(self):
            return self.getToken(ParserPredQL.FLOAT, 0)

        def INT(self):
            return self.getToken(ParserPredQL.INT, 0)

        def getRuleIndex(self):
            return ParserPredQL.RULE_num_condition

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

        localctx = ParserPredQL.Num_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_num_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(ParserPredQL.NUM_COMP_OP)
            self.state = 177
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 962072674304) != 0)):
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
            return self.getToken(ParserPredQL.STR_COMP_OP, 0)

        def STRING(self):
            return self.getToken(ParserPredQL.STRING, 0)

        def getRuleIndex(self):
            return ParserPredQL.RULE_str_condition

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

        localctx = ParserPredQL.Str_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_str_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(ParserPredQL.STR_COMP_OP)
            self.state = 180
            self.match(ParserPredQL.STRING)
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
            return self.getToken(ParserPredQL.NULL_CHECK_OP, 0)

        def getRuleIndex(self):
            return ParserPredQL.RULE_null_check_condition

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

        localctx = ParserPredQL.Null_check_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_null_check_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(ParserPredQL.NULL_CHECK_OP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Aggregation_tmpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AGGR_FUNC(self):
            return self.getToken(ParserPredQL.AGGR_FUNC, 0)

        def OPEN_PAREN(self):
            return self.getToken(ParserPredQL.OPEN_PAREN, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ParserPredQL.ID)
            else:
                return self.getToken(ParserPredQL.ID, i)

        def DOT(self):
            return self.getToken(ParserPredQL.DOT, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ParserPredQL.COMMA)
            else:
                return self.getToken(ParserPredQL.COMMA, i)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(ParserPredQL.INT)
            else:
                return self.getToken(ParserPredQL.INT, i)

        def TIME_MEASURE_UNIT(self):
            return self.getToken(ParserPredQL.TIME_MEASURE_UNIT, 0)

        def CLOSE_PAREN(self):
            return self.getToken(ParserPredQL.CLOSE_PAREN, 0)

        def STAR(self):
            return self.getToken(ParserPredQL.STAR, 0)

        def where_stat(self):
            return self.getTypedRuleContext(ParserPredQL.Where_statContext,0)


        def getRuleIndex(self):
            return ParserPredQL.RULE_aggregation_tmp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregation_tmp" ):
                listener.enterAggregation_tmp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregation_tmp" ):
                listener.exitAggregation_tmp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregation_tmp" ):
                return visitor.visitAggregation_tmp(self)
            else:
                return visitor.visitChildren(self)




    def aggregation_tmp(self):

        localctx = ParserPredQL.Aggregation_tmpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_aggregation_tmp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(ParserPredQL.AGGR_FUNC)
            self.state = 185
            self.match(ParserPredQL.OPEN_PAREN)
            self.state = 186
            self.match(ParserPredQL.ID)
            self.state = 187
            self.match(ParserPredQL.DOT)
            self.state = 188
            _la = self._input.LA(1)
            if not(_la==32 or _la==42):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 189
                self.where_stat()


            self.state = 192
            self.match(ParserPredQL.COMMA)
            self.state = 193
            self.match(ParserPredQL.INT)
            self.state = 194
            self.match(ParserPredQL.COMMA)
            self.state = 195
            self.match(ParserPredQL.INT)
            self.state = 196
            self.match(ParserPredQL.COMMA)
            self.state = 197
            self.match(ParserPredQL.TIME_MEASURE_UNIT)
            self.state = 198
            self.match(ParserPredQL.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Aggregation_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AGGR_FUNC(self):
            return self.getToken(ParserPredQL.AGGR_FUNC, 0)

        def OPEN_PAREN(self):
            return self.getToken(ParserPredQL.OPEN_PAREN, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ParserPredQL.ID)
            else:
                return self.getToken(ParserPredQL.ID, i)

        def DOT(self):
            return self.getToken(ParserPredQL.DOT, 0)

        def CLOSE_PAREN(self):
            return self.getToken(ParserPredQL.CLOSE_PAREN, 0)

        def STAR(self):
            return self.getToken(ParserPredQL.STAR, 0)

        def where_stat(self):
            return self.getTypedRuleContext(ParserPredQL.Where_statContext,0)


        def getRuleIndex(self):
            return ParserPredQL.RULE_aggregation_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregation_stat" ):
                listener.enterAggregation_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregation_stat" ):
                listener.exitAggregation_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregation_stat" ):
                return visitor.visitAggregation_stat(self)
            else:
                return visitor.visitChildren(self)




    def aggregation_stat(self):

        localctx = ParserPredQL.Aggregation_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_aggregation_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(ParserPredQL.AGGR_FUNC)
            self.state = 201
            self.match(ParserPredQL.OPEN_PAREN)
            self.state = 202
            self.match(ParserPredQL.ID)
            self.state = 203
            self.match(ParserPredQL.DOT)
            self.state = 204
            _la = self._input.LA(1)
            if not(_la==32 or _la==42):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 205
                self.where_stat()


            self.state = 208
            self.match(ParserPredQL.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






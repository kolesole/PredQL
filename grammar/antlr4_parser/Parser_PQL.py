# Generated from Parser_PQL.g4 by ANTLR 4.13.1
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
        4,1,45,128,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,4,0,24,8,0,11,0,12,0,25,
        1,0,1,0,1,1,1,1,1,1,1,1,3,1,34,8,1,1,2,1,2,1,2,1,2,5,2,40,8,2,10,
        2,12,2,43,9,2,1,3,1,3,1,3,1,3,1,3,3,3,50,8,3,1,4,1,4,1,4,1,4,1,4,
        3,4,57,8,4,1,4,1,4,1,4,1,4,1,4,3,4,64,8,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,3,4,73,8,4,3,4,75,8,4,1,5,1,5,1,5,1,5,5,5,81,8,5,10,5,12,5,
        84,9,5,1,6,1,6,1,6,1,6,3,6,90,8,6,1,6,1,6,1,6,3,6,95,8,6,1,7,1,7,
        1,7,1,7,3,7,101,8,7,1,8,1,8,1,8,1,9,1,9,1,10,1,10,1,10,1,10,1,10,
        1,10,3,10,114,8,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,122,8,10,3,
        10,124,8,10,1,10,1,10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,20,0,
        3,2,0,39,39,43,43,1,0,33,34,1,0,32,34,138,0,23,1,0,0,0,2,33,1,0,
        0,0,4,35,1,0,0,0,6,44,1,0,0,0,8,74,1,0,0,0,10,76,1,0,0,0,12,89,1,
        0,0,0,14,100,1,0,0,0,16,102,1,0,0,0,18,105,1,0,0,0,20,107,1,0,0,
        0,22,24,3,2,1,0,23,22,1,0,0,0,24,25,1,0,0,0,25,23,1,0,0,0,25,26,
        1,0,0,0,26,27,1,0,0,0,27,28,5,40,0,0,28,1,1,0,0,0,29,34,3,4,2,0,
        30,34,3,6,3,0,31,34,3,8,4,0,32,34,3,10,5,0,33,29,1,0,0,0,33,30,1,
        0,0,0,33,31,1,0,0,0,33,32,1,0,0,0,34,3,1,0,0,0,35,36,5,1,0,0,36,
        41,3,12,6,0,37,38,5,28,0,0,38,40,3,12,6,0,39,37,1,0,0,0,40,43,1,
        0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,5,1,0,0,0,43,41,1,0,0,0,44,
        45,5,2,0,0,45,46,5,43,0,0,46,47,5,35,0,0,47,49,5,43,0,0,48,50,3,
        10,5,0,49,48,1,0,0,0,49,50,1,0,0,0,50,7,1,0,0,0,51,52,5,3,0,0,52,
        56,3,20,10,0,53,54,5,6,0,0,54,57,5,34,0,0,55,57,5,5,0,0,56,53,1,
        0,0,0,56,55,1,0,0,0,56,57,1,0,0,0,57,75,1,0,0,0,58,59,5,3,0,0,59,
        63,3,12,6,0,60,61,5,6,0,0,61,64,5,34,0,0,62,64,5,5,0,0,63,60,1,0,
        0,0,63,62,1,0,0,0,63,64,1,0,0,0,64,75,1,0,0,0,65,66,5,3,0,0,66,67,
        5,43,0,0,67,68,5,35,0,0,68,72,7,0,0,0,69,70,5,6,0,0,70,73,5,34,0,
        0,71,73,5,5,0,0,72,69,1,0,0,0,72,71,1,0,0,0,72,73,1,0,0,0,73,75,
        1,0,0,0,74,51,1,0,0,0,74,58,1,0,0,0,74,65,1,0,0,0,75,9,1,0,0,0,76,
        77,5,4,0,0,77,82,3,12,6,0,78,79,5,28,0,0,79,81,3,12,6,0,80,78,1,
        0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,11,1,0,0,0,84,
        82,1,0,0,0,85,90,3,20,10,0,86,87,5,43,0,0,87,88,5,35,0,0,88,90,7,
        0,0,0,89,85,1,0,0,0,89,86,1,0,0,0,90,94,1,0,0,0,91,95,3,14,7,0,92,
        95,3,16,8,0,93,95,3,18,9,0,94,91,1,0,0,0,94,92,1,0,0,0,94,93,1,0,
        0,0,95,13,1,0,0,0,96,97,5,17,0,0,97,101,7,1,0,0,98,99,5,17,0,0,99,
        101,7,2,0,0,100,96,1,0,0,0,100,98,1,0,0,0,101,15,1,0,0,0,102,103,
        5,18,0,0,103,104,5,42,0,0,104,17,1,0,0,0,105,106,5,25,0,0,106,19,
        1,0,0,0,107,108,5,7,0,0,108,109,5,37,0,0,109,110,5,43,0,0,110,111,
        5,35,0,0,111,113,7,0,0,0,112,114,3,10,5,0,113,112,1,0,0,0,113,114,
        1,0,0,0,114,123,1,0,0,0,115,116,5,36,0,0,116,117,5,34,0,0,117,118,
        5,36,0,0,118,121,5,34,0,0,119,120,5,36,0,0,120,122,5,41,0,0,121,
        119,1,0,0,0,121,122,1,0,0,0,122,124,1,0,0,0,123,115,1,0,0,0,123,
        124,1,0,0,0,124,125,1,0,0,0,125,126,5,38,0,0,126,21,1,0,0,0,15,25,
        33,41,49,56,63,72,74,82,89,94,100,113,121,123
    ]

class Parser_PQL ( Parser ):

    grammarFileName = "Parser_PQL.g4"

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
                     "<INVALID>", "<INVALID>", "<INVALID>", "'.'", "','", 
                     "'('", "')'", "'*'", "';'" ]

    symbolicNames = [ "<INVALID>", "ASSUMING", "FOR_EACH", "PREDICT", "WHERE", 
                      "CLASSIFY", "RANK_TOP", "AGGR_FUNC", "AVG", "COUNT", 
                      "COUNT_DISTINCT", "FIRST", "LAST", "LIST_DISTINCT", 
                      "MAX", "MIN", "SUM", "NUM_COMP_OP", "STR_COMP_OP", 
                      "NOT_LIKE", "NOT_CONTAINS", "ENDS_WITH", "STARTS_WITH", 
                      "LIKE", "CONTAINS", "NULL_CHECK_OP", "IS_NOT_NULL", 
                      "IS_NULL", "LOGICAL_OP", "AND", "OR", "NOT", "DATETIME", 
                      "FLOAT", "INT", "DOT", "COMMA", "OPEN_PAREN", "CLOSE_PAREN", 
                      "STAR", "SEMI_COLUMN", "TIME_MEASURE_UNIT", "STRING", 
                      "ID", "WS_SKIP", "ANY" ]

    RULE_query = 0
    RULE_help_query = 1
    RULE_assuming = 2
    RULE_for_each = 3
    RULE_predict = 4
    RULE_where = 5
    RULE_condition = 6
    RULE_num_condition = 7
    RULE_str_condition = 8
    RULE_null_check_condition = 9
    RULE_aggregation = 10

    ruleNames =  [ "query", "help_query", "assuming", "for_each", "predict", 
                   "where", "condition", "num_condition", "str_condition", 
                   "null_check_condition", "aggregation" ]

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
    LOGICAL_OP=28
    AND=29
    OR=30
    NOT=31
    DATETIME=32
    FLOAT=33
    INT=34
    DOT=35
    COMMA=36
    OPEN_PAREN=37
    CLOSE_PAREN=38
    STAR=39
    SEMI_COLUMN=40
    TIME_MEASURE_UNIT=41
    STRING=42
    ID=43
    WS_SKIP=44
    ANY=45

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI_COLUMN(self):
            return self.getToken(Parser_PQL.SEMI_COLUMN, 0)

        def help_query(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Parser_PQL.Help_queryContext)
            else:
                return self.getTypedRuleContext(Parser_PQL.Help_queryContext,i)


        def getRuleIndex(self):
            return Parser_PQL.RULE_query

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

        localctx = Parser_PQL.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_query)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.help_query()
                self.state = 25 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0)):
                    break

            self.state = 27
            self.match(Parser_PQL.SEMI_COLUMN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Help_queryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assuming(self):
            return self.getTypedRuleContext(Parser_PQL.AssumingContext,0)


        def for_each(self):
            return self.getTypedRuleContext(Parser_PQL.For_eachContext,0)


        def predict(self):
            return self.getTypedRuleContext(Parser_PQL.PredictContext,0)


        def where(self):
            return self.getTypedRuleContext(Parser_PQL.WhereContext,0)


        def getRuleIndex(self):
            return Parser_PQL.RULE_help_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHelp_query" ):
                listener.enterHelp_query(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHelp_query" ):
                listener.exitHelp_query(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHelp_query" ):
                return visitor.visitHelp_query(self)
            else:
                return visitor.visitChildren(self)




    def help_query(self):

        localctx = Parser_PQL.Help_queryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_help_query)
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.assuming()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.for_each()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.predict()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 32
                self.where()
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


    class AssumingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSUMING(self):
            return self.getToken(Parser_PQL.ASSUMING, 0)

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Parser_PQL.ConditionContext)
            else:
                return self.getTypedRuleContext(Parser_PQL.ConditionContext,i)


        def LOGICAL_OP(self, i:int=None):
            if i is None:
                return self.getTokens(Parser_PQL.LOGICAL_OP)
            else:
                return self.getToken(Parser_PQL.LOGICAL_OP, i)

        def getRuleIndex(self):
            return Parser_PQL.RULE_assuming

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

        localctx = Parser_PQL.AssumingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assuming)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(Parser_PQL.ASSUMING)
            self.state = 36
            self.condition()
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 37
                self.match(Parser_PQL.LOGICAL_OP)
                self.state = 38
                self.condition()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            return self.getToken(Parser_PQL.FOR_EACH, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(Parser_PQL.ID)
            else:
                return self.getToken(Parser_PQL.ID, i)

        def DOT(self):
            return self.getToken(Parser_PQL.DOT, 0)

        def where(self):
            return self.getTypedRuleContext(Parser_PQL.WhereContext,0)


        def getRuleIndex(self):
            return Parser_PQL.RULE_for_each

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

        localctx = Parser_PQL.For_eachContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_for_each)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(Parser_PQL.FOR_EACH)
            self.state = 45
            self.match(Parser_PQL.ID)
            self.state = 46
            self.match(Parser_PQL.DOT)
            self.state = 47
            self.match(Parser_PQL.ID)
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 48
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
            return self.getToken(Parser_PQL.PREDICT, 0)

        def aggregation(self):
            return self.getTypedRuleContext(Parser_PQL.AggregationContext,0)


        def RANK_TOP(self):
            return self.getToken(Parser_PQL.RANK_TOP, 0)

        def INT(self):
            return self.getToken(Parser_PQL.INT, 0)

        def CLASSIFY(self):
            return self.getToken(Parser_PQL.CLASSIFY, 0)

        def condition(self):
            return self.getTypedRuleContext(Parser_PQL.ConditionContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(Parser_PQL.ID)
            else:
                return self.getToken(Parser_PQL.ID, i)

        def DOT(self):
            return self.getToken(Parser_PQL.DOT, 0)

        def STAR(self):
            return self.getToken(Parser_PQL.STAR, 0)

        def getRuleIndex(self):
            return Parser_PQL.RULE_predict

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

        localctx = Parser_PQL.PredictContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_predict)
        self._la = 0 # Token type
        try:
            self.state = 74
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.match(Parser_PQL.PREDICT)
                self.state = 52
                self.aggregation()
                self.state = 56
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6]:
                    self.state = 53
                    self.match(Parser_PQL.RANK_TOP)
                    self.state = 54
                    self.match(Parser_PQL.INT)
                    pass
                elif token in [5]:
                    self.state = 55
                    self.match(Parser_PQL.CLASSIFY)
                    pass
                elif token in [1, 2, 3, 4, 40]:
                    pass
                else:
                    pass
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.match(Parser_PQL.PREDICT)
                self.state = 59
                self.condition()
                self.state = 63
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6]:
                    self.state = 60
                    self.match(Parser_PQL.RANK_TOP)
                    self.state = 61
                    self.match(Parser_PQL.INT)
                    pass
                elif token in [5]:
                    self.state = 62
                    self.match(Parser_PQL.CLASSIFY)
                    pass
                elif token in [1, 2, 3, 4, 40]:
                    pass
                else:
                    pass
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 65
                self.match(Parser_PQL.PREDICT)
                self.state = 66
                self.match(Parser_PQL.ID)
                self.state = 67
                self.match(Parser_PQL.DOT)
                self.state = 68
                _la = self._input.LA(1)
                if not(_la==39 or _la==43):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 72
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6]:
                    self.state = 69
                    self.match(Parser_PQL.RANK_TOP)
                    self.state = 70
                    self.match(Parser_PQL.INT)
                    pass
                elif token in [5]:
                    self.state = 71
                    self.match(Parser_PQL.CLASSIFY)
                    pass
                elif token in [1, 2, 3, 4, 40]:
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
            return self.getToken(Parser_PQL.WHERE, 0)

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Parser_PQL.ConditionContext)
            else:
                return self.getTypedRuleContext(Parser_PQL.ConditionContext,i)


        def LOGICAL_OP(self, i:int=None):
            if i is None:
                return self.getTokens(Parser_PQL.LOGICAL_OP)
            else:
                return self.getToken(Parser_PQL.LOGICAL_OP, i)

        def getRuleIndex(self):
            return Parser_PQL.RULE_where

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

        localctx = Parser_PQL.WhereContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_where)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(Parser_PQL.WHERE)
            self.state = 77
            self.condition()
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 78
                self.match(Parser_PQL.LOGICAL_OP)
                self.state = 79
                self.condition()
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            return self.getTypedRuleContext(Parser_PQL.AggregationContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(Parser_PQL.ID)
            else:
                return self.getToken(Parser_PQL.ID, i)

        def DOT(self):
            return self.getToken(Parser_PQL.DOT, 0)

        def num_condition(self):
            return self.getTypedRuleContext(Parser_PQL.Num_conditionContext,0)


        def str_condition(self):
            return self.getTypedRuleContext(Parser_PQL.Str_conditionContext,0)


        def null_check_condition(self):
            return self.getTypedRuleContext(Parser_PQL.Null_check_conditionContext,0)


        def STAR(self):
            return self.getToken(Parser_PQL.STAR, 0)

        def getRuleIndex(self):
            return Parser_PQL.RULE_condition

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

        localctx = Parser_PQL.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.state = 85
                self.aggregation()
                pass
            elif token in [43]:
                self.state = 86
                self.match(Parser_PQL.ID)
                self.state = 87
                self.match(Parser_PQL.DOT)
                self.state = 88
                _la = self._input.LA(1)
                if not(_la==39 or _la==43):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 94
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.state = 91
                self.num_condition()
                pass
            elif token in [18]:
                self.state = 92
                self.str_condition()
                pass
            elif token in [25]:
                self.state = 93
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
            return self.getToken(Parser_PQL.NUM_COMP_OP, 0)

        def FLOAT(self):
            return self.getToken(Parser_PQL.FLOAT, 0)

        def INT(self):
            return self.getToken(Parser_PQL.INT, 0)

        def DATETIME(self):
            return self.getToken(Parser_PQL.DATETIME, 0)

        def getRuleIndex(self):
            return Parser_PQL.RULE_num_condition

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

        localctx = Parser_PQL.Num_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_num_condition)
        self._la = 0 # Token type
        try:
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.match(Parser_PQL.NUM_COMP_OP)
                self.state = 97
                _la = self._input.LA(1)
                if not(_la==33 or _la==34):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
                self.match(Parser_PQL.NUM_COMP_OP)
                self.state = 99
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30064771072) != 0)):
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


    class Str_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STR_COMP_OP(self):
            return self.getToken(Parser_PQL.STR_COMP_OP, 0)

        def STRING(self):
            return self.getToken(Parser_PQL.STRING, 0)

        def getRuleIndex(self):
            return Parser_PQL.RULE_str_condition

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

        localctx = Parser_PQL.Str_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_str_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(Parser_PQL.STR_COMP_OP)
            self.state = 103
            self.match(Parser_PQL.STRING)
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
            return self.getToken(Parser_PQL.NULL_CHECK_OP, 0)

        def getRuleIndex(self):
            return Parser_PQL.RULE_null_check_condition

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

        localctx = Parser_PQL.Null_check_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_null_check_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(Parser_PQL.NULL_CHECK_OP)
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
            return self.getToken(Parser_PQL.AGGR_FUNC, 0)

        def OPEN_PAREN(self):
            return self.getToken(Parser_PQL.OPEN_PAREN, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(Parser_PQL.ID)
            else:
                return self.getToken(Parser_PQL.ID, i)

        def DOT(self):
            return self.getToken(Parser_PQL.DOT, 0)

        def CLOSE_PAREN(self):
            return self.getToken(Parser_PQL.CLOSE_PAREN, 0)

        def STAR(self):
            return self.getToken(Parser_PQL.STAR, 0)

        def where(self):
            return self.getTypedRuleContext(Parser_PQL.WhereContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(Parser_PQL.COMMA)
            else:
                return self.getToken(Parser_PQL.COMMA, i)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(Parser_PQL.INT)
            else:
                return self.getToken(Parser_PQL.INT, i)

        def TIME_MEASURE_UNIT(self):
            return self.getToken(Parser_PQL.TIME_MEASURE_UNIT, 0)

        def getRuleIndex(self):
            return Parser_PQL.RULE_aggregation

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

        localctx = Parser_PQL.AggregationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_aggregation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(Parser_PQL.AGGR_FUNC)
            self.state = 108
            self.match(Parser_PQL.OPEN_PAREN)
            self.state = 109
            self.match(Parser_PQL.ID)
            self.state = 110
            self.match(Parser_PQL.DOT)
            self.state = 111
            _la = self._input.LA(1)
            if not(_la==39 or _la==43):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 112
                self.where()


            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 115
                self.match(Parser_PQL.COMMA)
                self.state = 116
                self.match(Parser_PQL.INT)
                self.state = 117
                self.match(Parser_PQL.COMMA)
                self.state = 118
                self.match(Parser_PQL.INT)
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==36:
                    self.state = 119
                    self.match(Parser_PQL.COMMA)
                    self.state = 120
                    self.match(Parser_PQL.TIME_MEASURE_UNIT)




            self.state = 125
            self.match(Parser_PQL.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






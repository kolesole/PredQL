// Generated from /home/kolesiko/CTU/BT/PredQL/predql/parser/ParserPredQL.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class ParserPredQL extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		ASSUMING=1, FOR_EACH=2, PREDICT=3, WHERE=4, CLASSIFY=5, RANK_TOP=6, AGGR_FUNC=7, 
		AVG=8, COUNT=9, COUNT_DISTINCT=10, FIRST=11, LAST=12, LIST_DISTINCT=13, 
		MAX=14, MIN=15, SUM=16, NUM_COMP_OP=17, STR_COMP_OP=18, NOT_LIKE=19, NOT_CONTAINS=20, 
		ENDS_WITH=21, STARTS_WITH=22, LIKE=23, CONTAINS=24, NULL_CHECK_OP=25, 
		IS_NOT_NULL=26, IS_NULL=27, DOT=28, COMMA=29, OPEN_PAREN=30, CLOSE_PAREN=31, 
		STAR=32, SEMICOLON=33, AND=34, OR=35, NOT=36, DATETIME=37, FLOAT=38, INT=39, 
		TIME_MEASURE_UNIT=40, STRING=41, ID=42, WS_SKIP=43, ANY=44;
	public static final int
		RULE_query = 0, RULE_query_tmp = 1, RULE_query_stat = 2, RULE_for_each = 3, 
		RULE_predict_tmp = 4, RULE_predict_stat = 5, RULE_assuming = 6, RULE_where_tmp = 7, 
		RULE_where_stat = 8, RULE_expr_or_tmp = 9, RULE_expr_or_stat = 10, RULE_expr_and_tmp = 11, 
		RULE_expr_and_stat = 12, RULE_expr_term_tmp = 13, RULE_expr_term_stat = 14, 
		RULE_condition_tmp = 15, RULE_condition_stat = 16, RULE_num_condition = 17, 
		RULE_str_condition = 18, RULE_null_check_condition = 19, RULE_aggregation_tmp = 20, 
		RULE_aggregation_stat = 21;
	private static String[] makeRuleNames() {
		return new String[] {
			"query", "query_tmp", "query_stat", "for_each", "predict_tmp", "predict_stat", 
			"assuming", "where_tmp", "where_stat", "expr_or_tmp", "expr_or_stat", 
			"expr_and_tmp", "expr_and_stat", "expr_term_tmp", "expr_term_stat", "condition_tmp", 
			"condition_stat", "num_condition", "str_condition", "null_check_condition", 
			"aggregation_tmp", "aggregation_stat"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, "'.'", "','", "'('", "')'", "'*'", "';'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "ASSUMING", "FOR_EACH", "PREDICT", "WHERE", "CLASSIFY", "RANK_TOP", 
			"AGGR_FUNC", "AVG", "COUNT", "COUNT_DISTINCT", "FIRST", "LAST", "LIST_DISTINCT", 
			"MAX", "MIN", "SUM", "NUM_COMP_OP", "STR_COMP_OP", "NOT_LIKE", "NOT_CONTAINS", 
			"ENDS_WITH", "STARTS_WITH", "LIKE", "CONTAINS", "NULL_CHECK_OP", "IS_NOT_NULL", 
			"IS_NULL", "DOT", "COMMA", "OPEN_PAREN", "CLOSE_PAREN", "STAR", "SEMICOLON", 
			"AND", "OR", "NOT", "DATETIME", "FLOAT", "INT", "TIME_MEASURE_UNIT", 
			"STRING", "ID", "WS_SKIP", "ANY"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "ParserPredQL.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ParserPredQL(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class QueryContext extends ParserRuleContext {
		public Query_tmpContext query_tmp() {
			return getRuleContext(Query_tmpContext.class,0);
		}
		public Query_statContext query_stat() {
			return getRuleContext(Query_statContext.class,0);
		}
		public QueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_query; }
	}

	public final QueryContext query() throws RecognitionException {
		QueryContext _localctx = new QueryContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_query);
		try {
			setState(46);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(44);
				query_tmp();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(45);
				query_stat();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Query_tmpContext extends ParserRuleContext {
		public Predict_tmpContext predict_tmp() {
			return getRuleContext(Predict_tmpContext.class,0);
		}
		public For_eachContext for_each() {
			return getRuleContext(For_eachContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(ParserPredQL.SEMICOLON, 0); }
		public AssumingContext assuming() {
			return getRuleContext(AssumingContext.class,0);
		}
		public Where_tmpContext where_tmp() {
			return getRuleContext(Where_tmpContext.class,0);
		}
		public Query_tmpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_query_tmp; }
	}

	public final Query_tmpContext query_tmp() throws RecognitionException {
		Query_tmpContext _localctx = new Query_tmpContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_query_tmp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			predict_tmp();
			setState(49);
			for_each();
			setState(51);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ASSUMING) {
				{
				setState(50);
				assuming();
				}
			}

			setState(54);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WHERE) {
				{
				setState(53);
				where_tmp();
				}
			}

			setState(56);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Query_statContext extends ParserRuleContext {
		public Predict_statContext predict_stat() {
			return getRuleContext(Predict_statContext.class,0);
		}
		public For_eachContext for_each() {
			return getRuleContext(For_eachContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(ParserPredQL.SEMICOLON, 0); }
		public Where_statContext where_stat() {
			return getRuleContext(Where_statContext.class,0);
		}
		public Query_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_query_stat; }
	}

	public final Query_statContext query_stat() throws RecognitionException {
		Query_statContext _localctx = new Query_statContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_query_stat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(58);
			predict_stat();
			setState(59);
			for_each();
			setState(61);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WHERE) {
				{
				setState(60);
				where_stat();
				}
			}

			setState(63);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class For_eachContext extends ParserRuleContext {
		public TerminalNode FOR_EACH() { return getToken(ParserPredQL.FOR_EACH, 0); }
		public List<TerminalNode> ID() { return getTokens(ParserPredQL.ID); }
		public TerminalNode ID(int i) {
			return getToken(ParserPredQL.ID, i);
		}
		public TerminalNode DOT() { return getToken(ParserPredQL.DOT, 0); }
		public TerminalNode STAR() { return getToken(ParserPredQL.STAR, 0); }
		public Where_statContext where_stat() {
			return getRuleContext(Where_statContext.class,0);
		}
		public For_eachContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_each; }
	}

	public final For_eachContext for_each() throws RecognitionException {
		For_eachContext _localctx = new For_eachContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_for_each);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(65);
			match(FOR_EACH);
			setState(66);
			match(ID);
			setState(67);
			match(DOT);
			setState(68);
			_la = _input.LA(1);
			if ( !(_la==STAR || _la==ID) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(70);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				{
				setState(69);
				where_stat();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Predict_tmpContext extends ParserRuleContext {
		public TerminalNode PREDICT() { return getToken(ParserPredQL.PREDICT, 0); }
		public Aggregation_tmpContext aggregation_tmp() {
			return getRuleContext(Aggregation_tmpContext.class,0);
		}
		public TerminalNode RANK_TOP() { return getToken(ParserPredQL.RANK_TOP, 0); }
		public TerminalNode INT() { return getToken(ParserPredQL.INT, 0); }
		public TerminalNode CLASSIFY() { return getToken(ParserPredQL.CLASSIFY, 0); }
		public Expr_or_tmpContext expr_or_tmp() {
			return getRuleContext(Expr_or_tmpContext.class,0);
		}
		public Predict_tmpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_predict_tmp; }
	}

	public final Predict_tmpContext predict_tmp() throws RecognitionException {
		Predict_tmpContext _localctx = new Predict_tmpContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_predict_tmp);
		try {
			setState(81);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(72);
				match(PREDICT);
				setState(73);
				aggregation_tmp();
				setState(77);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case RANK_TOP:
					{
					setState(74);
					match(RANK_TOP);
					setState(75);
					match(INT);
					}
					break;
				case CLASSIFY:
					{
					setState(76);
					match(CLASSIFY);
					}
					break;
				case FOR_EACH:
					break;
				default:
					break;
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(79);
				match(PREDICT);
				setState(80);
				expr_or_tmp();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Predict_statContext extends ParserRuleContext {
		public TerminalNode PREDICT() { return getToken(ParserPredQL.PREDICT, 0); }
		public Aggregation_statContext aggregation_stat() {
			return getRuleContext(Aggregation_statContext.class,0);
		}
		public TerminalNode RANK_TOP() { return getToken(ParserPredQL.RANK_TOP, 0); }
		public TerminalNode INT() { return getToken(ParserPredQL.INT, 0); }
		public TerminalNode CLASSIFY() { return getToken(ParserPredQL.CLASSIFY, 0); }
		public Expr_or_statContext expr_or_stat() {
			return getRuleContext(Expr_or_statContext.class,0);
		}
		public List<TerminalNode> ID() { return getTokens(ParserPredQL.ID); }
		public TerminalNode ID(int i) {
			return getToken(ParserPredQL.ID, i);
		}
		public TerminalNode DOT() { return getToken(ParserPredQL.DOT, 0); }
		public TerminalNode STAR() { return getToken(ParserPredQL.STAR, 0); }
		public Predict_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_predict_stat; }
	}

	public final Predict_statContext predict_stat() throws RecognitionException {
		Predict_statContext _localctx = new Predict_statContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_predict_stat);
		int _la;
		try {
			setState(96);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(83);
				match(PREDICT);
				setState(84);
				aggregation_stat();
				setState(88);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case RANK_TOP:
					{
					setState(85);
					match(RANK_TOP);
					setState(86);
					match(INT);
					}
					break;
				case CLASSIFY:
					{
					setState(87);
					match(CLASSIFY);
					}
					break;
				case FOR_EACH:
					break;
				default:
					break;
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(90);
				match(PREDICT);
				setState(91);
				expr_or_stat();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(92);
				match(PREDICT);
				setState(93);
				match(ID);
				setState(94);
				match(DOT);
				setState(95);
				_la = _input.LA(1);
				if ( !(_la==STAR || _la==ID) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssumingContext extends ParserRuleContext {
		public TerminalNode ASSUMING() { return getToken(ParserPredQL.ASSUMING, 0); }
		public Expr_or_tmpContext expr_or_tmp() {
			return getRuleContext(Expr_or_tmpContext.class,0);
		}
		public AssumingContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assuming; }
	}

	public final AssumingContext assuming() throws RecognitionException {
		AssumingContext _localctx = new AssumingContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_assuming);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(98);
			match(ASSUMING);
			setState(99);
			expr_or_tmp();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Where_tmpContext extends ParserRuleContext {
		public TerminalNode WHERE() { return getToken(ParserPredQL.WHERE, 0); }
		public Expr_or_tmpContext expr_or_tmp() {
			return getRuleContext(Expr_or_tmpContext.class,0);
		}
		public Where_tmpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_where_tmp; }
	}

	public final Where_tmpContext where_tmp() throws RecognitionException {
		Where_tmpContext _localctx = new Where_tmpContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_where_tmp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(101);
			match(WHERE);
			setState(102);
			expr_or_tmp();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Where_statContext extends ParserRuleContext {
		public TerminalNode WHERE() { return getToken(ParserPredQL.WHERE, 0); }
		public Expr_or_statContext expr_or_stat() {
			return getRuleContext(Expr_or_statContext.class,0);
		}
		public Where_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_where_stat; }
	}

	public final Where_statContext where_stat() throws RecognitionException {
		Where_statContext _localctx = new Where_statContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_where_stat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(104);
			match(WHERE);
			setState(105);
			expr_or_stat();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr_or_tmpContext extends ParserRuleContext {
		public List<Expr_and_tmpContext> expr_and_tmp() {
			return getRuleContexts(Expr_and_tmpContext.class);
		}
		public Expr_and_tmpContext expr_and_tmp(int i) {
			return getRuleContext(Expr_and_tmpContext.class,i);
		}
		public List<TerminalNode> OR() { return getTokens(ParserPredQL.OR); }
		public TerminalNode OR(int i) {
			return getToken(ParserPredQL.OR, i);
		}
		public Expr_or_tmpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr_or_tmp; }
	}

	public final Expr_or_tmpContext expr_or_tmp() throws RecognitionException {
		Expr_or_tmpContext _localctx = new Expr_or_tmpContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_expr_or_tmp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(107);
			expr_and_tmp();
			setState(112);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OR) {
				{
				{
				setState(108);
				match(OR);
				setState(109);
				expr_and_tmp();
				}
				}
				setState(114);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr_or_statContext extends ParserRuleContext {
		public List<Expr_and_statContext> expr_and_stat() {
			return getRuleContexts(Expr_and_statContext.class);
		}
		public Expr_and_statContext expr_and_stat(int i) {
			return getRuleContext(Expr_and_statContext.class,i);
		}
		public List<TerminalNode> OR() { return getTokens(ParserPredQL.OR); }
		public TerminalNode OR(int i) {
			return getToken(ParserPredQL.OR, i);
		}
		public Expr_or_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr_or_stat; }
	}

	public final Expr_or_statContext expr_or_stat() throws RecognitionException {
		Expr_or_statContext _localctx = new Expr_or_statContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_expr_or_stat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(115);
			expr_and_stat();
			setState(120);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OR) {
				{
				{
				setState(116);
				match(OR);
				setState(117);
				expr_and_stat();
				}
				}
				setState(122);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr_and_tmpContext extends ParserRuleContext {
		public List<Expr_term_tmpContext> expr_term_tmp() {
			return getRuleContexts(Expr_term_tmpContext.class);
		}
		public Expr_term_tmpContext expr_term_tmp(int i) {
			return getRuleContext(Expr_term_tmpContext.class,i);
		}
		public List<TerminalNode> AND() { return getTokens(ParserPredQL.AND); }
		public TerminalNode AND(int i) {
			return getToken(ParserPredQL.AND, i);
		}
		public Expr_and_tmpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr_and_tmp; }
	}

	public final Expr_and_tmpContext expr_and_tmp() throws RecognitionException {
		Expr_and_tmpContext _localctx = new Expr_and_tmpContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_expr_and_tmp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(123);
			expr_term_tmp();
			setState(128);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AND) {
				{
				{
				setState(124);
				match(AND);
				setState(125);
				expr_term_tmp();
				}
				}
				setState(130);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr_and_statContext extends ParserRuleContext {
		public List<Expr_term_statContext> expr_term_stat() {
			return getRuleContexts(Expr_term_statContext.class);
		}
		public Expr_term_statContext expr_term_stat(int i) {
			return getRuleContext(Expr_term_statContext.class,i);
		}
		public List<TerminalNode> AND() { return getTokens(ParserPredQL.AND); }
		public TerminalNode AND(int i) {
			return getToken(ParserPredQL.AND, i);
		}
		public Expr_and_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr_and_stat; }
	}

	public final Expr_and_statContext expr_and_stat() throws RecognitionException {
		Expr_and_statContext _localctx = new Expr_and_statContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_expr_and_stat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(131);
			expr_term_stat();
			setState(136);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AND) {
				{
				{
				setState(132);
				match(AND);
				setState(133);
				expr_term_stat();
				}
				}
				setState(138);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr_term_tmpContext extends ParserRuleContext {
		public Condition_tmpContext condition_tmp() {
			return getRuleContext(Condition_tmpContext.class,0);
		}
		public TerminalNode OPEN_PAREN() { return getToken(ParserPredQL.OPEN_PAREN, 0); }
		public Expr_or_tmpContext expr_or_tmp() {
			return getRuleContext(Expr_or_tmpContext.class,0);
		}
		public TerminalNode CLOSE_PAREN() { return getToken(ParserPredQL.CLOSE_PAREN, 0); }
		public Expr_term_tmpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr_term_tmp; }
	}

	public final Expr_term_tmpContext expr_term_tmp() throws RecognitionException {
		Expr_term_tmpContext _localctx = new Expr_term_tmpContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_expr_term_tmp);
		try {
			setState(144);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case AGGR_FUNC:
			case NOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(139);
				condition_tmp();
				}
				break;
			case OPEN_PAREN:
				enterOuterAlt(_localctx, 2);
				{
				setState(140);
				match(OPEN_PAREN);
				setState(141);
				expr_or_tmp();
				setState(142);
				match(CLOSE_PAREN);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr_term_statContext extends ParserRuleContext {
		public Condition_statContext condition_stat() {
			return getRuleContext(Condition_statContext.class,0);
		}
		public TerminalNode OPEN_PAREN() { return getToken(ParserPredQL.OPEN_PAREN, 0); }
		public Expr_or_statContext expr_or_stat() {
			return getRuleContext(Expr_or_statContext.class,0);
		}
		public TerminalNode CLOSE_PAREN() { return getToken(ParserPredQL.CLOSE_PAREN, 0); }
		public Expr_term_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr_term_stat; }
	}

	public final Expr_term_statContext expr_term_stat() throws RecognitionException {
		Expr_term_statContext _localctx = new Expr_term_statContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_expr_term_stat);
		try {
			setState(151);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case AGGR_FUNC:
			case NOT:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(146);
				condition_stat();
				}
				break;
			case OPEN_PAREN:
				enterOuterAlt(_localctx, 2);
				{
				setState(147);
				match(OPEN_PAREN);
				setState(148);
				expr_or_stat();
				setState(149);
				match(CLOSE_PAREN);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Condition_tmpContext extends ParserRuleContext {
		public Aggregation_tmpContext aggregation_tmp() {
			return getRuleContext(Aggregation_tmpContext.class,0);
		}
		public Num_conditionContext num_condition() {
			return getRuleContext(Num_conditionContext.class,0);
		}
		public Str_conditionContext str_condition() {
			return getRuleContext(Str_conditionContext.class,0);
		}
		public Null_check_conditionContext null_check_condition() {
			return getRuleContext(Null_check_conditionContext.class,0);
		}
		public TerminalNode NOT() { return getToken(ParserPredQL.NOT, 0); }
		public Condition_tmpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition_tmp; }
	}

	public final Condition_tmpContext condition_tmp() throws RecognitionException {
		Condition_tmpContext _localctx = new Condition_tmpContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_condition_tmp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(154);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NOT) {
				{
				setState(153);
				match(NOT);
				}
			}

			setState(156);
			aggregation_tmp();
			setState(160);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUM_COMP_OP:
				{
				setState(157);
				num_condition();
				}
				break;
			case STR_COMP_OP:
				{
				setState(158);
				str_condition();
				}
				break;
			case NULL_CHECK_OP:
				{
				setState(159);
				null_check_condition();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Condition_statContext extends ParserRuleContext {
		public Aggregation_statContext aggregation_stat() {
			return getRuleContext(Aggregation_statContext.class,0);
		}
		public List<TerminalNode> ID() { return getTokens(ParserPredQL.ID); }
		public TerminalNode ID(int i) {
			return getToken(ParserPredQL.ID, i);
		}
		public TerminalNode DOT() { return getToken(ParserPredQL.DOT, 0); }
		public Num_conditionContext num_condition() {
			return getRuleContext(Num_conditionContext.class,0);
		}
		public Str_conditionContext str_condition() {
			return getRuleContext(Str_conditionContext.class,0);
		}
		public Null_check_conditionContext null_check_condition() {
			return getRuleContext(Null_check_conditionContext.class,0);
		}
		public TerminalNode NOT() { return getToken(ParserPredQL.NOT, 0); }
		public TerminalNode STAR() { return getToken(ParserPredQL.STAR, 0); }
		public Condition_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition_stat; }
	}

	public final Condition_statContext condition_stat() throws RecognitionException {
		Condition_statContext _localctx = new Condition_statContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_condition_stat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(163);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NOT) {
				{
				setState(162);
				match(NOT);
				}
			}

			setState(169);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case AGGR_FUNC:
				{
				setState(165);
				aggregation_stat();
				}
				break;
			case ID:
				{
				setState(166);
				match(ID);
				setState(167);
				match(DOT);
				setState(168);
				_la = _input.LA(1);
				if ( !(_la==STAR || _la==ID) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(174);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUM_COMP_OP:
				{
				setState(171);
				num_condition();
				}
				break;
			case STR_COMP_OP:
				{
				setState(172);
				str_condition();
				}
				break;
			case NULL_CHECK_OP:
				{
				setState(173);
				null_check_condition();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Num_conditionContext extends ParserRuleContext {
		public TerminalNode NUM_COMP_OP() { return getToken(ParserPredQL.NUM_COMP_OP, 0); }
		public TerminalNode DATETIME() { return getToken(ParserPredQL.DATETIME, 0); }
		public TerminalNode FLOAT() { return getToken(ParserPredQL.FLOAT, 0); }
		public TerminalNode INT() { return getToken(ParserPredQL.INT, 0); }
		public Num_conditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_num_condition; }
	}

	public final Num_conditionContext num_condition() throws RecognitionException {
		Num_conditionContext _localctx = new Num_conditionContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_num_condition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(176);
			match(NUM_COMP_OP);
			setState(177);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 962072674304L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Str_conditionContext extends ParserRuleContext {
		public TerminalNode STR_COMP_OP() { return getToken(ParserPredQL.STR_COMP_OP, 0); }
		public TerminalNode STRING() { return getToken(ParserPredQL.STRING, 0); }
		public Str_conditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_str_condition; }
	}

	public final Str_conditionContext str_condition() throws RecognitionException {
		Str_conditionContext _localctx = new Str_conditionContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_str_condition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(179);
			match(STR_COMP_OP);
			setState(180);
			match(STRING);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Null_check_conditionContext extends ParserRuleContext {
		public TerminalNode NULL_CHECK_OP() { return getToken(ParserPredQL.NULL_CHECK_OP, 0); }
		public Null_check_conditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_null_check_condition; }
	}

	public final Null_check_conditionContext null_check_condition() throws RecognitionException {
		Null_check_conditionContext _localctx = new Null_check_conditionContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_null_check_condition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(182);
			match(NULL_CHECK_OP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Aggregation_tmpContext extends ParserRuleContext {
		public TerminalNode AGGR_FUNC() { return getToken(ParserPredQL.AGGR_FUNC, 0); }
		public TerminalNode OPEN_PAREN() { return getToken(ParserPredQL.OPEN_PAREN, 0); }
		public List<TerminalNode> ID() { return getTokens(ParserPredQL.ID); }
		public TerminalNode ID(int i) {
			return getToken(ParserPredQL.ID, i);
		}
		public TerminalNode DOT() { return getToken(ParserPredQL.DOT, 0); }
		public List<TerminalNode> COMMA() { return getTokens(ParserPredQL.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(ParserPredQL.COMMA, i);
		}
		public List<TerminalNode> INT() { return getTokens(ParserPredQL.INT); }
		public TerminalNode INT(int i) {
			return getToken(ParserPredQL.INT, i);
		}
		public TerminalNode TIME_MEASURE_UNIT() { return getToken(ParserPredQL.TIME_MEASURE_UNIT, 0); }
		public TerminalNode CLOSE_PAREN() { return getToken(ParserPredQL.CLOSE_PAREN, 0); }
		public TerminalNode STAR() { return getToken(ParserPredQL.STAR, 0); }
		public Where_statContext where_stat() {
			return getRuleContext(Where_statContext.class,0);
		}
		public Aggregation_tmpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_aggregation_tmp; }
	}

	public final Aggregation_tmpContext aggregation_tmp() throws RecognitionException {
		Aggregation_tmpContext _localctx = new Aggregation_tmpContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_aggregation_tmp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(184);
			match(AGGR_FUNC);
			setState(185);
			match(OPEN_PAREN);
			setState(186);
			match(ID);
			setState(187);
			match(DOT);
			setState(188);
			_la = _input.LA(1);
			if ( !(_la==STAR || _la==ID) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(190);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WHERE) {
				{
				setState(189);
				where_stat();
				}
			}

			setState(192);
			match(COMMA);
			setState(193);
			match(INT);
			setState(194);
			match(COMMA);
			setState(195);
			match(INT);
			setState(196);
			match(COMMA);
			setState(197);
			match(TIME_MEASURE_UNIT);
			setState(198);
			match(CLOSE_PAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Aggregation_statContext extends ParserRuleContext {
		public TerminalNode AGGR_FUNC() { return getToken(ParserPredQL.AGGR_FUNC, 0); }
		public TerminalNode OPEN_PAREN() { return getToken(ParserPredQL.OPEN_PAREN, 0); }
		public List<TerminalNode> ID() { return getTokens(ParserPredQL.ID); }
		public TerminalNode ID(int i) {
			return getToken(ParserPredQL.ID, i);
		}
		public TerminalNode DOT() { return getToken(ParserPredQL.DOT, 0); }
		public TerminalNode CLOSE_PAREN() { return getToken(ParserPredQL.CLOSE_PAREN, 0); }
		public TerminalNode STAR() { return getToken(ParserPredQL.STAR, 0); }
		public Where_statContext where_stat() {
			return getRuleContext(Where_statContext.class,0);
		}
		public Aggregation_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_aggregation_stat; }
	}

	public final Aggregation_statContext aggregation_stat() throws RecognitionException {
		Aggregation_statContext _localctx = new Aggregation_statContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_aggregation_stat);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(200);
			match(AGGR_FUNC);
			setState(201);
			match(OPEN_PAREN);
			setState(202);
			match(ID);
			setState(203);
			match(DOT);
			setState(204);
			_la = _input.LA(1);
			if ( !(_la==STAR || _la==ID) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(206);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WHERE) {
				{
				setState(205);
				where_stat();
				}
			}

			setState(208);
			match(CLOSE_PAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001,\u00d3\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0001\u0000\u0001\u0000\u0003\u0000/\b\u0000\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0003\u00014\b\u0001\u0001\u0001\u0003\u00017\b\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002>\b"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0003\u0003G\b\u0003\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0003\u0004N\b\u0004\u0001\u0004\u0001"+
		"\u0004\u0003\u0004R\b\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0003\u0005Y\b\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0003\u0005a\b\u0005\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0005\to\b\t\n\t\f\tr\t\t\u0001"+
		"\n\u0001\n\u0001\n\u0005\nw\b\n\n\n\f\nz\t\n\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0005\u000b\u007f\b\u000b\n\u000b\f\u000b\u0082\t\u000b\u0001\f"+
		"\u0001\f\u0001\f\u0005\f\u0087\b\f\n\f\f\f\u008a\t\f\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0003\r\u0091\b\r\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0003\u000e\u0098\b\u000e\u0001\u000f\u0003\u000f"+
		"\u009b\b\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0003\u000f"+
		"\u00a1\b\u000f\u0001\u0010\u0003\u0010\u00a4\b\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0003\u0010\u00aa\b\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0003\u0010\u00af\b\u0010\u0001\u0011\u0001\u0011\u0001"+
		"\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001"+
		"\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0003"+
		"\u0014\u00bf\b\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001"+
		"\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015\u0001"+
		"\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0003\u0015\u00cf\b\u0015\u0001"+
		"\u0015\u0001\u0015\u0001\u0015\u0000\u0000\u0016\u0000\u0002\u0004\u0006"+
		"\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*\u0000"+
		"\u0002\u0002\u0000  **\u0001\u0000%\'\u00d7\u0000.\u0001\u0000\u0000\u0000"+
		"\u00020\u0001\u0000\u0000\u0000\u0004:\u0001\u0000\u0000\u0000\u0006A"+
		"\u0001\u0000\u0000\u0000\bQ\u0001\u0000\u0000\u0000\n`\u0001\u0000\u0000"+
		"\u0000\fb\u0001\u0000\u0000\u0000\u000ee\u0001\u0000\u0000\u0000\u0010"+
		"h\u0001\u0000\u0000\u0000\u0012k\u0001\u0000\u0000\u0000\u0014s\u0001"+
		"\u0000\u0000\u0000\u0016{\u0001\u0000\u0000\u0000\u0018\u0083\u0001\u0000"+
		"\u0000\u0000\u001a\u0090\u0001\u0000\u0000\u0000\u001c\u0097\u0001\u0000"+
		"\u0000\u0000\u001e\u009a\u0001\u0000\u0000\u0000 \u00a3\u0001\u0000\u0000"+
		"\u0000\"\u00b0\u0001\u0000\u0000\u0000$\u00b3\u0001\u0000\u0000\u0000"+
		"&\u00b6\u0001\u0000\u0000\u0000(\u00b8\u0001\u0000\u0000\u0000*\u00c8"+
		"\u0001\u0000\u0000\u0000,/\u0003\u0002\u0001\u0000-/\u0003\u0004\u0002"+
		"\u0000.,\u0001\u0000\u0000\u0000.-\u0001\u0000\u0000\u0000/\u0001\u0001"+
		"\u0000\u0000\u000001\u0003\b\u0004\u000013\u0003\u0006\u0003\u000024\u0003"+
		"\f\u0006\u000032\u0001\u0000\u0000\u000034\u0001\u0000\u0000\u000046\u0001"+
		"\u0000\u0000\u000057\u0003\u000e\u0007\u000065\u0001\u0000\u0000\u0000"+
		"67\u0001\u0000\u0000\u000078\u0001\u0000\u0000\u000089\u0005!\u0000\u0000"+
		"9\u0003\u0001\u0000\u0000\u0000:;\u0003\n\u0005\u0000;=\u0003\u0006\u0003"+
		"\u0000<>\u0003\u0010\b\u0000=<\u0001\u0000\u0000\u0000=>\u0001\u0000\u0000"+
		"\u0000>?\u0001\u0000\u0000\u0000?@\u0005!\u0000\u0000@\u0005\u0001\u0000"+
		"\u0000\u0000AB\u0005\u0002\u0000\u0000BC\u0005*\u0000\u0000CD\u0005\u001c"+
		"\u0000\u0000DF\u0007\u0000\u0000\u0000EG\u0003\u0010\b\u0000FE\u0001\u0000"+
		"\u0000\u0000FG\u0001\u0000\u0000\u0000G\u0007\u0001\u0000\u0000\u0000"+
		"HI\u0005\u0003\u0000\u0000IM\u0003(\u0014\u0000JK\u0005\u0006\u0000\u0000"+
		"KN\u0005\'\u0000\u0000LN\u0005\u0005\u0000\u0000MJ\u0001\u0000\u0000\u0000"+
		"ML\u0001\u0000\u0000\u0000MN\u0001\u0000\u0000\u0000NR\u0001\u0000\u0000"+
		"\u0000OP\u0005\u0003\u0000\u0000PR\u0003\u0012\t\u0000QH\u0001\u0000\u0000"+
		"\u0000QO\u0001\u0000\u0000\u0000R\t\u0001\u0000\u0000\u0000ST\u0005\u0003"+
		"\u0000\u0000TX\u0003*\u0015\u0000UV\u0005\u0006\u0000\u0000VY\u0005\'"+
		"\u0000\u0000WY\u0005\u0005\u0000\u0000XU\u0001\u0000\u0000\u0000XW\u0001"+
		"\u0000\u0000\u0000XY\u0001\u0000\u0000\u0000Ya\u0001\u0000\u0000\u0000"+
		"Z[\u0005\u0003\u0000\u0000[a\u0003\u0014\n\u0000\\]\u0005\u0003\u0000"+
		"\u0000]^\u0005*\u0000\u0000^_\u0005\u001c\u0000\u0000_a\u0007\u0000\u0000"+
		"\u0000`S\u0001\u0000\u0000\u0000`Z\u0001\u0000\u0000\u0000`\\\u0001\u0000"+
		"\u0000\u0000a\u000b\u0001\u0000\u0000\u0000bc\u0005\u0001\u0000\u0000"+
		"cd\u0003\u0012\t\u0000d\r\u0001\u0000\u0000\u0000ef\u0005\u0004\u0000"+
		"\u0000fg\u0003\u0012\t\u0000g\u000f\u0001\u0000\u0000\u0000hi\u0005\u0004"+
		"\u0000\u0000ij\u0003\u0014\n\u0000j\u0011\u0001\u0000\u0000\u0000kp\u0003"+
		"\u0016\u000b\u0000lm\u0005#\u0000\u0000mo\u0003\u0016\u000b\u0000nl\u0001"+
		"\u0000\u0000\u0000or\u0001\u0000\u0000\u0000pn\u0001\u0000\u0000\u0000"+
		"pq\u0001\u0000\u0000\u0000q\u0013\u0001\u0000\u0000\u0000rp\u0001\u0000"+
		"\u0000\u0000sx\u0003\u0018\f\u0000tu\u0005#\u0000\u0000uw\u0003\u0018"+
		"\f\u0000vt\u0001\u0000\u0000\u0000wz\u0001\u0000\u0000\u0000xv\u0001\u0000"+
		"\u0000\u0000xy\u0001\u0000\u0000\u0000y\u0015\u0001\u0000\u0000\u0000"+
		"zx\u0001\u0000\u0000\u0000{\u0080\u0003\u001a\r\u0000|}\u0005\"\u0000"+
		"\u0000}\u007f\u0003\u001a\r\u0000~|\u0001\u0000\u0000\u0000\u007f\u0082"+
		"\u0001\u0000\u0000\u0000\u0080~\u0001\u0000\u0000\u0000\u0080\u0081\u0001"+
		"\u0000\u0000\u0000\u0081\u0017\u0001\u0000\u0000\u0000\u0082\u0080\u0001"+
		"\u0000\u0000\u0000\u0083\u0088\u0003\u001c\u000e\u0000\u0084\u0085\u0005"+
		"\"\u0000\u0000\u0085\u0087\u0003\u001c\u000e\u0000\u0086\u0084\u0001\u0000"+
		"\u0000\u0000\u0087\u008a\u0001\u0000\u0000\u0000\u0088\u0086\u0001\u0000"+
		"\u0000\u0000\u0088\u0089\u0001\u0000\u0000\u0000\u0089\u0019\u0001\u0000"+
		"\u0000\u0000\u008a\u0088\u0001\u0000\u0000\u0000\u008b\u0091\u0003\u001e"+
		"\u000f\u0000\u008c\u008d\u0005\u001e\u0000\u0000\u008d\u008e\u0003\u0012"+
		"\t\u0000\u008e\u008f\u0005\u001f\u0000\u0000\u008f\u0091\u0001\u0000\u0000"+
		"\u0000\u0090\u008b\u0001\u0000\u0000\u0000\u0090\u008c\u0001\u0000\u0000"+
		"\u0000\u0091\u001b\u0001\u0000\u0000\u0000\u0092\u0098\u0003 \u0010\u0000"+
		"\u0093\u0094\u0005\u001e\u0000\u0000\u0094\u0095\u0003\u0014\n\u0000\u0095"+
		"\u0096\u0005\u001f\u0000\u0000\u0096\u0098\u0001\u0000\u0000\u0000\u0097"+
		"\u0092\u0001\u0000\u0000\u0000\u0097\u0093\u0001\u0000\u0000\u0000\u0098"+
		"\u001d\u0001\u0000\u0000\u0000\u0099\u009b\u0005$\u0000\u0000\u009a\u0099"+
		"\u0001\u0000\u0000\u0000\u009a\u009b\u0001\u0000\u0000\u0000\u009b\u009c"+
		"\u0001\u0000\u0000\u0000\u009c\u00a0\u0003(\u0014\u0000\u009d\u00a1\u0003"+
		"\"\u0011\u0000\u009e\u00a1\u0003$\u0012\u0000\u009f\u00a1\u0003&\u0013"+
		"\u0000\u00a0\u009d\u0001\u0000\u0000\u0000\u00a0\u009e\u0001\u0000\u0000"+
		"\u0000\u00a0\u009f\u0001\u0000\u0000\u0000\u00a1\u001f\u0001\u0000\u0000"+
		"\u0000\u00a2\u00a4\u0005$\u0000\u0000\u00a3\u00a2\u0001\u0000\u0000\u0000"+
		"\u00a3\u00a4\u0001\u0000\u0000\u0000\u00a4\u00a9\u0001\u0000\u0000\u0000"+
		"\u00a5\u00aa\u0003*\u0015\u0000\u00a6\u00a7\u0005*\u0000\u0000\u00a7\u00a8"+
		"\u0005\u001c\u0000\u0000\u00a8\u00aa\u0007\u0000\u0000\u0000\u00a9\u00a5"+
		"\u0001\u0000\u0000\u0000\u00a9\u00a6\u0001\u0000\u0000\u0000\u00aa\u00ae"+
		"\u0001\u0000\u0000\u0000\u00ab\u00af\u0003\"\u0011\u0000\u00ac\u00af\u0003"+
		"$\u0012\u0000\u00ad\u00af\u0003&\u0013\u0000\u00ae\u00ab\u0001\u0000\u0000"+
		"\u0000\u00ae\u00ac\u0001\u0000\u0000\u0000\u00ae\u00ad\u0001\u0000\u0000"+
		"\u0000\u00af!\u0001\u0000\u0000\u0000\u00b0\u00b1\u0005\u0011\u0000\u0000"+
		"\u00b1\u00b2\u0007\u0001\u0000\u0000\u00b2#\u0001\u0000\u0000\u0000\u00b3"+
		"\u00b4\u0005\u0012\u0000\u0000\u00b4\u00b5\u0005)\u0000\u0000\u00b5%\u0001"+
		"\u0000\u0000\u0000\u00b6\u00b7\u0005\u0019\u0000\u0000\u00b7\'\u0001\u0000"+
		"\u0000\u0000\u00b8\u00b9\u0005\u0007\u0000\u0000\u00b9\u00ba\u0005\u001e"+
		"\u0000\u0000\u00ba\u00bb\u0005*\u0000\u0000\u00bb\u00bc\u0005\u001c\u0000"+
		"\u0000\u00bc\u00be\u0007\u0000\u0000\u0000\u00bd\u00bf\u0003\u0010\b\u0000"+
		"\u00be\u00bd\u0001\u0000\u0000\u0000\u00be\u00bf\u0001\u0000\u0000\u0000"+
		"\u00bf\u00c0\u0001\u0000\u0000\u0000\u00c0\u00c1\u0005\u001d\u0000\u0000"+
		"\u00c1\u00c2\u0005\'\u0000\u0000\u00c2\u00c3\u0005\u001d\u0000\u0000\u00c3"+
		"\u00c4\u0005\'\u0000\u0000\u00c4\u00c5\u0005\u001d\u0000\u0000\u00c5\u00c6"+
		"\u0005(\u0000\u0000\u00c6\u00c7\u0005\u001f\u0000\u0000\u00c7)\u0001\u0000"+
		"\u0000\u0000\u00c8\u00c9\u0005\u0007\u0000\u0000\u00c9\u00ca\u0005\u001e"+
		"\u0000\u0000\u00ca\u00cb\u0005*\u0000\u0000\u00cb\u00cc\u0005\u001c\u0000"+
		"\u0000\u00cc\u00ce\u0007\u0000\u0000\u0000\u00cd\u00cf\u0003\u0010\b\u0000"+
		"\u00ce\u00cd\u0001\u0000\u0000\u0000\u00ce\u00cf\u0001\u0000\u0000\u0000"+
		"\u00cf\u00d0\u0001\u0000\u0000\u0000\u00d0\u00d1\u0005\u001f\u0000\u0000"+
		"\u00d1+\u0001\u0000\u0000\u0000\u0016.36=FMQX`px\u0080\u0088\u0090\u0097"+
		"\u009a\u00a0\u00a3\u00a9\u00ae\u00be\u00ce";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
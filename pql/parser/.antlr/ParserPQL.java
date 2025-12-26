// Generated from /home/kolesiko/CTU/BT/PQL/pql/parser/ParserPQL.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class ParserPQL extends Parser {
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
		STAR=32, SEMI_COLUMN=33, AND=34, OR=35, NOT=36, DATETIME=37, FLOAT=38, 
		INT=39, TIME_MEASURE_UNIT=40, STRING=41, ID=42, WS_SKIP=43, ANY=44;
	public static final int
		RULE_query = 0, RULE_assuming = 1, RULE_for_each = 2, RULE_predict = 3, 
		RULE_where = 4, RULE_expr_or = 5, RULE_expr_and = 6, RULE_expr_term = 7, 
		RULE_condition = 8, RULE_num_condition = 9, RULE_str_condition = 10, RULE_null_check_condition = 11, 
		RULE_aggregation = 12;
	private static String[] makeRuleNames() {
		return new String[] {
			"query", "assuming", "for_each", "predict", "where", "expr_or", "expr_and", 
			"expr_term", "condition", "num_condition", "str_condition", "null_check_condition", 
			"aggregation"
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
			"IS_NULL", "DOT", "COMMA", "OPEN_PAREN", "CLOSE_PAREN", "STAR", "SEMI_COLUMN", 
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
	public String getGrammarFileName() { return "ParserPQL.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ParserPQL(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class QueryContext extends ParserRuleContext {
		public PredictContext predict() {
			return getRuleContext(PredictContext.class,0);
		}
		public For_eachContext for_each() {
			return getRuleContext(For_eachContext.class,0);
		}
		public TerminalNode SEMI_COLUMN() { return getToken(ParserPQL.SEMI_COLUMN, 0); }
		public AssumingContext assuming() {
			return getRuleContext(AssumingContext.class,0);
		}
		public WhereContext where() {
			return getRuleContext(WhereContext.class,0);
		}
		public QueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_query; }
	}

	public final QueryContext query() throws RecognitionException {
		QueryContext _localctx = new QueryContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_query);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(26);
			predict();
			setState(27);
			for_each();
			setState(29);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ASSUMING) {
				{
				setState(28);
				assuming();
				}
			}

			setState(32);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WHERE) {
				{
				setState(31);
				where();
				}
			}

			setState(34);
			match(SEMI_COLUMN);
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
		public TerminalNode ASSUMING() { return getToken(ParserPQL.ASSUMING, 0); }
		public Expr_orContext expr_or() {
			return getRuleContext(Expr_orContext.class,0);
		}
		public AssumingContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assuming; }
	}

	public final AssumingContext assuming() throws RecognitionException {
		AssumingContext _localctx = new AssumingContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_assuming);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(36);
			match(ASSUMING);
			setState(37);
			expr_or();
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
		public TerminalNode FOR_EACH() { return getToken(ParserPQL.FOR_EACH, 0); }
		public List<TerminalNode> ID() { return getTokens(ParserPQL.ID); }
		public TerminalNode ID(int i) {
			return getToken(ParserPQL.ID, i);
		}
		public TerminalNode DOT() { return getToken(ParserPQL.DOT, 0); }
		public WhereContext where() {
			return getRuleContext(WhereContext.class,0);
		}
		public For_eachContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_each; }
	}

	public final For_eachContext for_each() throws RecognitionException {
		For_eachContext _localctx = new For_eachContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_for_each);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(39);
			match(FOR_EACH);
			setState(40);
			match(ID);
			setState(41);
			match(DOT);
			setState(42);
			match(ID);
			setState(44);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				{
				setState(43);
				where();
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
	public static class PredictContext extends ParserRuleContext {
		public TerminalNode PREDICT() { return getToken(ParserPQL.PREDICT, 0); }
		public AggregationContext aggregation() {
			return getRuleContext(AggregationContext.class,0);
		}
		public TerminalNode RANK_TOP() { return getToken(ParserPQL.RANK_TOP, 0); }
		public TerminalNode INT() { return getToken(ParserPQL.INT, 0); }
		public TerminalNode CLASSIFY() { return getToken(ParserPQL.CLASSIFY, 0); }
		public Expr_orContext expr_or() {
			return getRuleContext(Expr_orContext.class,0);
		}
		public List<TerminalNode> ID() { return getTokens(ParserPQL.ID); }
		public TerminalNode ID(int i) {
			return getToken(ParserPQL.ID, i);
		}
		public TerminalNode DOT() { return getToken(ParserPQL.DOT, 0); }
		public TerminalNode STAR() { return getToken(ParserPQL.STAR, 0); }
		public PredictContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_predict; }
	}

	public final PredictContext predict() throws RecognitionException {
		PredictContext _localctx = new PredictContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_predict);
		int _la;
		try {
			setState(64);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(46);
				match(PREDICT);
				setState(47);
				aggregation();
				setState(51);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case RANK_TOP:
					{
					setState(48);
					match(RANK_TOP);
					setState(49);
					match(INT);
					}
					break;
				case CLASSIFY:
					{
					setState(50);
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
				setState(53);
				match(PREDICT);
				setState(54);
				expr_or();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(55);
				match(PREDICT);
				setState(56);
				match(ID);
				setState(57);
				match(DOT);
				setState(58);
				_la = _input.LA(1);
				if ( !(_la==STAR || _la==ID) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(62);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case RANK_TOP:
					{
					setState(59);
					match(RANK_TOP);
					setState(60);
					match(INT);
					}
					break;
				case CLASSIFY:
					{
					setState(61);
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
	public static class WhereContext extends ParserRuleContext {
		public TerminalNode WHERE() { return getToken(ParserPQL.WHERE, 0); }
		public Expr_orContext expr_or() {
			return getRuleContext(Expr_orContext.class,0);
		}
		public WhereContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_where; }
	}

	public final WhereContext where() throws RecognitionException {
		WhereContext _localctx = new WhereContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_where);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(66);
			match(WHERE);
			setState(67);
			expr_or();
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
	public static class Expr_orContext extends ParserRuleContext {
		public List<Expr_andContext> expr_and() {
			return getRuleContexts(Expr_andContext.class);
		}
		public Expr_andContext expr_and(int i) {
			return getRuleContext(Expr_andContext.class,i);
		}
		public List<TerminalNode> OR() { return getTokens(ParserPQL.OR); }
		public TerminalNode OR(int i) {
			return getToken(ParserPQL.OR, i);
		}
		public Expr_orContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr_or; }
	}

	public final Expr_orContext expr_or() throws RecognitionException {
		Expr_orContext _localctx = new Expr_orContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_expr_or);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(69);
			expr_and();
			setState(74);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OR) {
				{
				{
				setState(70);
				match(OR);
				setState(71);
				expr_and();
				}
				}
				setState(76);
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
	public static class Expr_andContext extends ParserRuleContext {
		public List<Expr_termContext> expr_term() {
			return getRuleContexts(Expr_termContext.class);
		}
		public Expr_termContext expr_term(int i) {
			return getRuleContext(Expr_termContext.class,i);
		}
		public List<TerminalNode> AND() { return getTokens(ParserPQL.AND); }
		public TerminalNode AND(int i) {
			return getToken(ParserPQL.AND, i);
		}
		public Expr_andContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr_and; }
	}

	public final Expr_andContext expr_and() throws RecognitionException {
		Expr_andContext _localctx = new Expr_andContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_expr_and);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(77);
			expr_term();
			setState(82);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AND) {
				{
				{
				setState(78);
				match(AND);
				setState(79);
				expr_term();
				}
				}
				setState(84);
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
	public static class Expr_termContext extends ParserRuleContext {
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public TerminalNode OPEN_PAREN() { return getToken(ParserPQL.OPEN_PAREN, 0); }
		public Expr_orContext expr_or() {
			return getRuleContext(Expr_orContext.class,0);
		}
		public TerminalNode CLOSE_PAREN() { return getToken(ParserPQL.CLOSE_PAREN, 0); }
		public Expr_termContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr_term; }
	}

	public final Expr_termContext expr_term() throws RecognitionException {
		Expr_termContext _localctx = new Expr_termContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_expr_term);
		try {
			setState(90);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case AGGR_FUNC:
			case NOT:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(85);
				condition();
				}
				break;
			case OPEN_PAREN:
				enterOuterAlt(_localctx, 2);
				{
				setState(86);
				match(OPEN_PAREN);
				setState(87);
				expr_or();
				setState(88);
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
	public static class ConditionContext extends ParserRuleContext {
		public AggregationContext aggregation() {
			return getRuleContext(AggregationContext.class,0);
		}
		public List<TerminalNode> ID() { return getTokens(ParserPQL.ID); }
		public TerminalNode ID(int i) {
			return getToken(ParserPQL.ID, i);
		}
		public TerminalNode DOT() { return getToken(ParserPQL.DOT, 0); }
		public Num_conditionContext num_condition() {
			return getRuleContext(Num_conditionContext.class,0);
		}
		public Str_conditionContext str_condition() {
			return getRuleContext(Str_conditionContext.class,0);
		}
		public Null_check_conditionContext null_check_condition() {
			return getRuleContext(Null_check_conditionContext.class,0);
		}
		public TerminalNode NOT() { return getToken(ParserPQL.NOT, 0); }
		public TerminalNode STAR() { return getToken(ParserPQL.STAR, 0); }
		public ConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition; }
	}

	public final ConditionContext condition() throws RecognitionException {
		ConditionContext _localctx = new ConditionContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_condition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(93);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NOT) {
				{
				setState(92);
				match(NOT);
				}
			}

			setState(99);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case AGGR_FUNC:
				{
				setState(95);
				aggregation();
				}
				break;
			case ID:
				{
				setState(96);
				match(ID);
				setState(97);
				match(DOT);
				setState(98);
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
			setState(104);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUM_COMP_OP:
				{
				setState(101);
				num_condition();
				}
				break;
			case STR_COMP_OP:
				{
				setState(102);
				str_condition();
				}
				break;
			case NULL_CHECK_OP:
				{
				setState(103);
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
		public TerminalNode NUM_COMP_OP() { return getToken(ParserPQL.NUM_COMP_OP, 0); }
		public TerminalNode DATETIME() { return getToken(ParserPQL.DATETIME, 0); }
		public TerminalNode FLOAT() { return getToken(ParserPQL.FLOAT, 0); }
		public TerminalNode INT() { return getToken(ParserPQL.INT, 0); }
		public Num_conditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_num_condition; }
	}

	public final Num_conditionContext num_condition() throws RecognitionException {
		Num_conditionContext _localctx = new Num_conditionContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_num_condition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(106);
			match(NUM_COMP_OP);
			setState(107);
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
		public TerminalNode STR_COMP_OP() { return getToken(ParserPQL.STR_COMP_OP, 0); }
		public TerminalNode STRING() { return getToken(ParserPQL.STRING, 0); }
		public Str_conditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_str_condition; }
	}

	public final Str_conditionContext str_condition() throws RecognitionException {
		Str_conditionContext _localctx = new Str_conditionContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_str_condition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(109);
			match(STR_COMP_OP);
			setState(110);
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
		public TerminalNode NULL_CHECK_OP() { return getToken(ParserPQL.NULL_CHECK_OP, 0); }
		public Null_check_conditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_null_check_condition; }
	}

	public final Null_check_conditionContext null_check_condition() throws RecognitionException {
		Null_check_conditionContext _localctx = new Null_check_conditionContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_null_check_condition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(112);
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
	public static class AggregationContext extends ParserRuleContext {
		public TerminalNode AGGR_FUNC() { return getToken(ParserPQL.AGGR_FUNC, 0); }
		public TerminalNode OPEN_PAREN() { return getToken(ParserPQL.OPEN_PAREN, 0); }
		public List<TerminalNode> ID() { return getTokens(ParserPQL.ID); }
		public TerminalNode ID(int i) {
			return getToken(ParserPQL.ID, i);
		}
		public TerminalNode DOT() { return getToken(ParserPQL.DOT, 0); }
		public TerminalNode CLOSE_PAREN() { return getToken(ParserPQL.CLOSE_PAREN, 0); }
		public TerminalNode STAR() { return getToken(ParserPQL.STAR, 0); }
		public WhereContext where() {
			return getRuleContext(WhereContext.class,0);
		}
		public List<TerminalNode> COMMA() { return getTokens(ParserPQL.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(ParserPQL.COMMA, i);
		}
		public List<TerminalNode> INT() { return getTokens(ParserPQL.INT); }
		public TerminalNode INT(int i) {
			return getToken(ParserPQL.INT, i);
		}
		public TerminalNode TIME_MEASURE_UNIT() { return getToken(ParserPQL.TIME_MEASURE_UNIT, 0); }
		public AggregationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_aggregation; }
	}

	public final AggregationContext aggregation() throws RecognitionException {
		AggregationContext _localctx = new AggregationContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_aggregation);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(114);
			match(AGGR_FUNC);
			setState(115);
			match(OPEN_PAREN);
			setState(116);
			match(ID);
			setState(117);
			match(DOT);
			setState(118);
			_la = _input.LA(1);
			if ( !(_la==STAR || _la==ID) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(120);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WHERE) {
				{
				setState(119);
				where();
				}
			}

			setState(130);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(122);
				match(COMMA);
				setState(123);
				match(INT);
				setState(124);
				match(COMMA);
				setState(125);
				match(INT);
				setState(128);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==COMMA) {
					{
					setState(126);
					match(COMMA);
					setState(127);
					match(TIME_MEASURE_UNIT);
					}
				}

				}
			}

			setState(132);
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
		"\u0004\u0001,\u0087\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0001\u0000\u0001\u0000\u0001\u0000\u0003\u0000\u001e\b\u0000"+
		"\u0001\u0000\u0003\u0000!\b\u0000\u0001\u0000\u0001\u0000\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0003\u0002-\b\u0002\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0003\u00034\b\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0003\u0003?\b\u0003\u0003\u0003A\b\u0003\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0005\u0005I\b"+
		"\u0005\n\u0005\f\u0005L\t\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0005"+
		"\u0006Q\b\u0006\n\u0006\f\u0006T\t\u0006\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0003\u0007[\b\u0007\u0001\b\u0003\b^\b"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0003\bd\b\b\u0001\b\u0001\b\u0001"+
		"\b\u0003\bi\b\b\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001"+
		"\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0003"+
		"\fy\b\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0003\f\u0081"+
		"\b\f\u0003\f\u0083\b\f\u0001\f\u0001\f\u0001\f\u0000\u0000\r\u0000\u0002"+
		"\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u0000\u0002\u0002"+
		"\u0000  **\u0001\u0000%\'\u008c\u0000\u001a\u0001\u0000\u0000\u0000\u0002"+
		"$\u0001\u0000\u0000\u0000\u0004\'\u0001\u0000\u0000\u0000\u0006@\u0001"+
		"\u0000\u0000\u0000\bB\u0001\u0000\u0000\u0000\nE\u0001\u0000\u0000\u0000"+
		"\fM\u0001\u0000\u0000\u0000\u000eZ\u0001\u0000\u0000\u0000\u0010]\u0001"+
		"\u0000\u0000\u0000\u0012j\u0001\u0000\u0000\u0000\u0014m\u0001\u0000\u0000"+
		"\u0000\u0016p\u0001\u0000\u0000\u0000\u0018r\u0001\u0000\u0000\u0000\u001a"+
		"\u001b\u0003\u0006\u0003\u0000\u001b\u001d\u0003\u0004\u0002\u0000\u001c"+
		"\u001e\u0003\u0002\u0001\u0000\u001d\u001c\u0001\u0000\u0000\u0000\u001d"+
		"\u001e\u0001\u0000\u0000\u0000\u001e \u0001\u0000\u0000\u0000\u001f!\u0003"+
		"\b\u0004\u0000 \u001f\u0001\u0000\u0000\u0000 !\u0001\u0000\u0000\u0000"+
		"!\"\u0001\u0000\u0000\u0000\"#\u0005!\u0000\u0000#\u0001\u0001\u0000\u0000"+
		"\u0000$%\u0005\u0001\u0000\u0000%&\u0003\n\u0005\u0000&\u0003\u0001\u0000"+
		"\u0000\u0000\'(\u0005\u0002\u0000\u0000()\u0005*\u0000\u0000)*\u0005\u001c"+
		"\u0000\u0000*,\u0005*\u0000\u0000+-\u0003\b\u0004\u0000,+\u0001\u0000"+
		"\u0000\u0000,-\u0001\u0000\u0000\u0000-\u0005\u0001\u0000\u0000\u0000"+
		"./\u0005\u0003\u0000\u0000/3\u0003\u0018\f\u000001\u0005\u0006\u0000\u0000"+
		"14\u0005\'\u0000\u000024\u0005\u0005\u0000\u000030\u0001\u0000\u0000\u0000"+
		"32\u0001\u0000\u0000\u000034\u0001\u0000\u0000\u00004A\u0001\u0000\u0000"+
		"\u000056\u0005\u0003\u0000\u00006A\u0003\n\u0005\u000078\u0005\u0003\u0000"+
		"\u000089\u0005*\u0000\u00009:\u0005\u001c\u0000\u0000:>\u0007\u0000\u0000"+
		"\u0000;<\u0005\u0006\u0000\u0000<?\u0005\'\u0000\u0000=?\u0005\u0005\u0000"+
		"\u0000>;\u0001\u0000\u0000\u0000>=\u0001\u0000\u0000\u0000>?\u0001\u0000"+
		"\u0000\u0000?A\u0001\u0000\u0000\u0000@.\u0001\u0000\u0000\u0000@5\u0001"+
		"\u0000\u0000\u0000@7\u0001\u0000\u0000\u0000A\u0007\u0001\u0000\u0000"+
		"\u0000BC\u0005\u0004\u0000\u0000CD\u0003\n\u0005\u0000D\t\u0001\u0000"+
		"\u0000\u0000EJ\u0003\f\u0006\u0000FG\u0005#\u0000\u0000GI\u0003\f\u0006"+
		"\u0000HF\u0001\u0000\u0000\u0000IL\u0001\u0000\u0000\u0000JH\u0001\u0000"+
		"\u0000\u0000JK\u0001\u0000\u0000\u0000K\u000b\u0001\u0000\u0000\u0000"+
		"LJ\u0001\u0000\u0000\u0000MR\u0003\u000e\u0007\u0000NO\u0005\"\u0000\u0000"+
		"OQ\u0003\u000e\u0007\u0000PN\u0001\u0000\u0000\u0000QT\u0001\u0000\u0000"+
		"\u0000RP\u0001\u0000\u0000\u0000RS\u0001\u0000\u0000\u0000S\r\u0001\u0000"+
		"\u0000\u0000TR\u0001\u0000\u0000\u0000U[\u0003\u0010\b\u0000VW\u0005\u001e"+
		"\u0000\u0000WX\u0003\n\u0005\u0000XY\u0005\u001f\u0000\u0000Y[\u0001\u0000"+
		"\u0000\u0000ZU\u0001\u0000\u0000\u0000ZV\u0001\u0000\u0000\u0000[\u000f"+
		"\u0001\u0000\u0000\u0000\\^\u0005$\u0000\u0000]\\\u0001\u0000\u0000\u0000"+
		"]^\u0001\u0000\u0000\u0000^c\u0001\u0000\u0000\u0000_d\u0003\u0018\f\u0000"+
		"`a\u0005*\u0000\u0000ab\u0005\u001c\u0000\u0000bd\u0007\u0000\u0000\u0000"+
		"c_\u0001\u0000\u0000\u0000c`\u0001\u0000\u0000\u0000dh\u0001\u0000\u0000"+
		"\u0000ei\u0003\u0012\t\u0000fi\u0003\u0014\n\u0000gi\u0003\u0016\u000b"+
		"\u0000he\u0001\u0000\u0000\u0000hf\u0001\u0000\u0000\u0000hg\u0001\u0000"+
		"\u0000\u0000i\u0011\u0001\u0000\u0000\u0000jk\u0005\u0011\u0000\u0000"+
		"kl\u0007\u0001\u0000\u0000l\u0013\u0001\u0000\u0000\u0000mn\u0005\u0012"+
		"\u0000\u0000no\u0005)\u0000\u0000o\u0015\u0001\u0000\u0000\u0000pq\u0005"+
		"\u0019\u0000\u0000q\u0017\u0001\u0000\u0000\u0000rs\u0005\u0007\u0000"+
		"\u0000st\u0005\u001e\u0000\u0000tu\u0005*\u0000\u0000uv\u0005\u001c\u0000"+
		"\u0000vx\u0007\u0000\u0000\u0000wy\u0003\b\u0004\u0000xw\u0001\u0000\u0000"+
		"\u0000xy\u0001\u0000\u0000\u0000y\u0082\u0001\u0000\u0000\u0000z{\u0005"+
		"\u001d\u0000\u0000{|\u0005\'\u0000\u0000|}\u0005\u001d\u0000\u0000}\u0080"+
		"\u0005\'\u0000\u0000~\u007f\u0005\u001d\u0000\u0000\u007f\u0081\u0005"+
		"(\u0000\u0000\u0080~\u0001\u0000\u0000\u0000\u0080\u0081\u0001\u0000\u0000"+
		"\u0000\u0081\u0083\u0001\u0000\u0000\u0000\u0082z\u0001\u0000\u0000\u0000"+
		"\u0082\u0083\u0001\u0000\u0000\u0000\u0083\u0084\u0001\u0000\u0000\u0000"+
		"\u0084\u0085\u0005\u001f\u0000\u0000\u0085\u0019\u0001\u0000\u0000\u0000"+
		"\u000f\u001d ,3>@JRZ]chx\u0080\u0082";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
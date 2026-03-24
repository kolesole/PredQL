"""Error handling and collection for PredQL parsing and validation."""

from typing import override

from antlr4.error.ErrorListener import ErrorListener


class Colors:
    r"""ANSI color codes for terminal output formatting."""

    DEFAULT = "\033[0m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class Error:
    r"""Represents a single syntax or validation error.

    Stores the location and message of an error that occurred during
    parsing or validation of a PredQL query.
    """

    def __init__(self, line: int, column: int, message: str) -> None:
        r"""Initializes an *`Error`* object.

        Args:
            line (int): Line number of the error.
            column (int): Column number of the error.
            message (str): Error message.

        Returns:
            out (None):
        """
        self.line = line
        self.column = column
        self.message = message

    def __str__(self) -> str:
        r"""Formats the error as a colored string for terminal output.

        Returns:
            out (str): Formatted error string with ANSI color codes.
        """
        return (
            f"{Colors.RED}{Colors.BOLD}ERROR{Colors.DEFAULT} at line {self.line}:{self.column} - "
            f"{Colors.UNDERLINE}{self.message}{Colors.DEFAULT}"
        )


class ErrorCollector(ErrorListener):
    r"""Collects syntax and validation errors during parsing.

    Implements ANTLR ErrorListener interface to capture syntax errors during
    parsing, and provides additional methods for collecting validation errors.
    """

    def __init__(self) -> None:
        r"""Initializes the *`ErrorCollector`* with an empty error list.

        Returns:
            out (None):
        """
        super().__init__()
        self.errors = []

    def __repr__(self) -> str:
        r"""Formats all collected errors as a numbered list.

        Returns:
            out (str): Multi-line string with all errors, numbered sequentially.
        """
        return "\n".join(f"{i + 1}. " + str(error) for i, error in enumerate(self.errors))

    def __len__(self) -> int:
        r"""Returns the number of collected errors.

        Returns:
            out (int): Total count of errors.
        """
        return len(self.errors)

    @override
    def syntaxError(self, recognizer: any, offendingSymbol: any, line: int, column: int, msg: str, e: any) -> None:
        r"""ANTLR callback invoked when a syntax error is encountered.

        This method is automatically called by the ANTLR parser when it
        encounters a syntax error during parsing.

        Args:
            recognizer (any): The parser instance.
            offendingSymbol (any): The token that caused the error.
            line (int): Line number of the error.
            column (int): Column number of the error.
            msg (str): Error message from ANTLR.
            e (any): The recognition exception (if any).

        Returns:
            out (None):
        """
        self.errors.append(Error(line, column, msg))

    def val_error(self, line: int, column: int, msg: str) -> None:
        r"""Add a validation error to the collection.

        Used by validators to report semantic errors (e.g., referencing non-existent tables or columns).

        Args:
            line (int): Line number of the error.
            column (int): Column number of the error.
            msg (str): Error message.

        Returns:
            out (None):
        """
        self.errors.append(Error(line, column, msg))

    def clear(self) -> None:
        r"""Clears all collected errors from the collector.

        Returns:
            out (None):
        """
        self.errors.clear()

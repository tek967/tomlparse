"""
A lexer for TOML. divide the file into individual tokens for the parser to run.
"""

from enum import Enum

TokenType = Enum(
    'IDENTIFIER',
    'SEPERATOR',
    'LITERAL',
    'COMMENT'
)

class IdentifierToken(Enum):
    TOKEN_PLUS = "+"
    TOKEN_MINUS = "-"
    TOKEN_HEX = "0x"
    TOKEN_OCT = "0o"
    TOKEN_BIN = "0b"
    TOKEN_UNDERSCORE = "_"
    TOKEN_EQUAL = "="
    TOKEN_COMMENT = "#"

class SeperatorToken(Enum):
    TOKEN_COMMA = ","
    TOKEN_START_SQUARE_BRACKET = "["
    TOKEN_END_SQUARE_BRACKET = "]"
    TOKEN_START_CURLY_BRACE = "{"
    TOKEN_END_CURLY_BRACE = "}"

LiteralToken = Enum (
    'STRING',
    'INTEGER',
    'FLOAT',
    'NOTANUMBER',
    'BOOLEAN',
    'LIST',
    'INLINETABLE',
    'TABLE'
)
class Token:
    innerName = None
    innerType = None
    innerValue = None

class Lexer:
    def __init__(self, expression) -> None:
        self.expr = expression.split()

    def tokenise(self) -> Token:
        pass

    def lex(self) -> list:
        pass
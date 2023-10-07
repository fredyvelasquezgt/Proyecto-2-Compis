from antlr4 import *
from antlr4.error.ErrorListener import *

class yaplErrorListener(ErrorListener):

    def __init__(self) -> None:
        self.errors = []
        super().__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append({
            "msg": msg,
            "line": line,
            "column": column,
            "offendingSymbol": offendingSymbol
        })

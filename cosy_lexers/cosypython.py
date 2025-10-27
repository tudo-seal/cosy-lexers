from functools import partial

from pygments.lexers.python import PythonLexer
from pygments.token import Keyword, Name


__all__ = ("CosyPythonLexer",)


class CosyPythonLexer(PythonLexer):
    name = "CosyPythonLexer"
    aliases = ["cosy-py"]
    mimetypes = []
    filenames = []

    EXTRA_PSEUDO_KEYWORDS = {
        "parameter",
        "argument",
        "constraint",
        "parameter_constraint",
        "suffix",
        "DSL",
        "Constructor",
        "CoSy",
        "Component",
        "Group",
        "DataGroup",
        "Arrow",
        "Intersection",
        "Tree",
        "Inspector",
        "Container",
        "SolutionSpace",
        "Taxonomy",
        "Subtypes",
        "Tree",
        "Literal"
    }

    def get_tokens_unprocessed(self, text):
        for index, token, value in \
                PythonLexer.get_tokens_unprocessed(self, text):
            if token is Name and value in self.EXTRA_PSEUDO_KEYWORDS:
                yield index, Keyword.Pseudo, value
            else:
                yield index, token, value

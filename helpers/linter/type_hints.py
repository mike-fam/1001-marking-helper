"""
Type hints helpers
"""
from dataclasses import dataclass

from helpers.linter.utils.tree import SyntaxTree
from helpers.linter.utils.violation import BaseViolation


CriteriaConfig = dict[str, list]

Config = dict[str, CriteriaConfig]

AnalyserResults = dict[str, BaseViolation]

CheckOutput = dict[str, AnalyserResults]


@dataclass
class AnalyserHelper:
    tree: SyntaxTree
    source: list[str]
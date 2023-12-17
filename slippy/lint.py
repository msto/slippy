
from dataclasses import dataclass
from enum import Enum, unique

from snakemake.rules import Rule


@unique
class LintCode(Enum):
    SLE101 = "No docstring"


@dataclass
class Lint:
    """"""
    code: LintCode
    filename: str



def lint(rule: Rule) -> list[Lint]:
    pass
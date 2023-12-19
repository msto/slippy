from dataclasses import dataclass
from enum import Enum
from enum import unique

from snakemake.rules import Rule


@unique
class LintCode(Enum):
    SLE101 = "No docstring"


@dataclass
class Lint:
    """"""

    code: LintCode
    filename: str


def lint_rule(rule: Rule) -> list[Lint]:
    return []

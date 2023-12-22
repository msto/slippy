#!/usr/bin/env python

import sys
from pathlib import Path
from typing import Optional

import defopt
from snakemake.workflow import Workflow

from slippy.diagnostic import SlippyDiagnostic
from slippy.lint import lint_rule


def slippy(
    *,
    snakefile: Path,
    include_all: bool = False,
) -> None:
    """
    Slippy is a simple snakemake linter.

    Args:
        snakefile: Snakefile to lint.
        include_all: Lint the `all` rule.
    """

    workflow = Workflow(snakefile=snakefile)
    workflow.include(snakefile)

    # Lint each rule, collecting as we go
    diagnostics: list[SlippyDiagnostic] = []
    for rule in workflow.rules:
        diagnostics += lint_rule(rule)


def main(argv: Optional[list[str]] = None) -> None:
    argv = sys.argv[1:] if argv is None else argv
    defopt.run(slippy, argv=argv)

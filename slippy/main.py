#!/usr/bin/env python

from pathlib import Path

import defopt
from snakemake.rules import Rule
from snakemake.workflow import Workflow


def main(
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

    import pdb
    pdb.set_trace()

    # Lint each rule, collecting as we go
    lints: list[Lint] = []
    for rule in workflow.rules:
        # workflow.main_snakefile
        pass


if __name__ == "__main__":
    defopt.run(main)

from pathlib import Path

from snakemake.rules import Rule
from snakemake.workflow import Workflow


def load_workflow(snakefile: Path) -> Workflow:
    """
    Load a workflow from a snakefile.

    Simply creating a `Workflow` object from a snakefile does not parse the workflow - it is
    necssary to explicitly include the snakefile as well.

    This function is just a simple helper to avoid repetition and safeguard against forgetting the
    `include`.

    Args:
        snakefile: The snakefile to load.

    Returns:
        The workflow.
    """

    workflow = Workflow(snakefile=snakefile)
    workflow.include(snakefile)

    return workflow


def get_rule_lineno(rule: Rule) -> int:
    """
    Get the line number of a rule in a workflow.

    Each `Rule` has an associated `lineno` attribute. However, this attribute does not contain the
    actual line number the rule is defined on, but rather contains the index of the rule's *token*.
    The actual line number can be found in the `linemaps` attribute of the rule's associated
    `Workflow`.  `linemaps` is a dict of dicts, where the parent `dict` contains one `dict` per
    snakefile included in the workflow, and each nested `dict` maps token indexes to line numbers.

    Args:
        rule: The rule to get the line number of.

    Returns:
        The line number of the rule.
    """

    return rule.workflow.linemaps[rule.snakefile][rule.lineno]

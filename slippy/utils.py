import linecache
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


# TODO: use enum instead of str?
def get_directive_lineno(rule: Rule, directive: str) -> int:
    """
    Get the line number of a specific directive.

    This function obtains the line number at which the rule definition begins, which is cached in
    each `Rule` object. It then uses linecache to find the next instance of the desired directive.
    If the directive cannot be found before the end of the rule declaration, a `ValueError` is
    raised.

    Note that this function assumes that all rules are defined in the main Snakefile, with no
    subworkflows or rule imports.

    Args:
        rule: A parsed rule declaration
        directive: The directive in question

    Returns:
        The line number of the directive in the main Snakefile.

    Raises:
        ValueError: if the directive cannot be found within the rule declaration.
    """

    # TODO: verify the rule is defined in the main Snakefile
    snakefile = rule.workflow.main_snakefile
    lineno = get_rule_lineno(rule)

    while True:
        lineno += 1
        line = linecache.getline(snakefile, lineno)

        # Either we've reached a gap between rules or we've reached the end of the file.
        if line == "":
            raise ValueError(f"Directive {directive} could not be found in rule {rule.name}")

        # Cover the unlikely case where the user didn't include a blank line between rule names
        if line.startswith("rule"):
            new_rule_name = line.rstrip(":").split()[-1]
            raise ValueError(
                f"Encountered new rule {new_rule_name} before finding "
                f"directive {directive} in rule {rule.name}"
            )

        if line.strip() == f"{directive}:":
            return lineno

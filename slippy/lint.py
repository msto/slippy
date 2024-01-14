from snakemake.rules import Rule

from .codes import SlippyCode
from .diagnostic import CodeRange
from .diagnostic import SlippyDiagnostic
from .utils import get_directive_range
from .utils import get_rule_lineno


def lint_rule(rule: Rule) -> list[SlippyDiagnostic]:
    """
    Lint a snakemake rule.
    """
    errs: list[SlippyDiagnostic | None] = [
        _check_rule_has_docstring(rule),
    ]

    return [e for e in errs if e is not None]


def _check_rule_has_docstring(rule: Rule) -> SlippyDiagnostic | None:
    """
    Check that a rule has a docstring.
    """

    if rule.docstring is not None:
        return None

    lineno = get_rule_lineno(rule)

    # Taking a shortcut for now to avoid parsing the line in question, but this should be
    # refactored to use `linecache`.
    # A rule declaration includes "rule " (5 characters), the name of the rule, and a trailing
    # colon (1 character).
    line_length = len(rule.name) + 6

    return SlippyDiagnostic(
        range=CodeRange(
            start_line=lineno,
            start_character=1,
            end_line=lineno,
            end_character=line_length,
        ),
        message=f"rule {rule} has no docstring",
        code=SlippyCode.NO_DOCSTRING.value,
    )


def _check_rule_has_shell(rule: Rule) -> SlippyDiagnostic | None:
    """
    Check that a rule has a `shell` block, and does not define a `run` or `script` block instead.
    """

    if rule.shellcmd is not None:
        return None

    if rule.script is not None:
        directive = "script"
    elif rule.run_func is not None:
        directive = "run"
    else:
        raise ValueError(f"Rule {rule.name} does not declare a `shell`, `run`, or `script` block.")

    return SlippyDiagnostic(
        range=get_directive_range(rule=rule, directive=directive),
        message=f"rule {rule} declares a `{directive}` block instead of a `shell` block",
        code=SlippyCode.NO_SHELL.value,
    )


def _check_rule_has_log(rule: Rule) -> SlippyDiagnostic | None:
    """
    Check that a rule declares a log.
    """

    # We only run this lint on rules with a shell block - other rules fail `_check_rule_has_shell()`
    if rule.shellcmd is None:
        return None

    # TODO: flag multiple logs? I don't know why this is declared as a namedlist
    if len(rule.log) > 0:
        return None

    return SlippyDiagnostic(
        range=get_directive_range(rule=rule, directive="shell"),
        message=f"rule {rule} has no log",
        code=SlippyCode.NO_LOG.value,
    )


def _check_rule_inputs_are_named(rule: Rule) -> SlippyDiagnostic | None:
    """
    Check that all rule inputs are named.
    """

    # TODO
    # if len(rule.ruleinfo.input.paths) > 0:
    #     return SlippyDiagnostic(
    #         # TODO: get range
    #         range=CodeRange(
    #             start_line=0,
    #             start_character=0,
    #             end_line=0,
    #             end_character=0,
    #         ),
    #         message=SlippyCode.INPUTS_NOT_NAMED.format(rule.name),
    #         code=SlippyCode.INPUTS_NOT_NAMED.value,
    #     )
    # else:
    #     return None

    return None


def _check_rule_inputs_are_referenced_by_name(rule: Rule) -> SlippyDiagnostic | None:
    """
    Check that inputs are referenced by name, not index, within the shell block.
    """

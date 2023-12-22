from snakemake.rules import Rule

from .codes import SlippyCode
from .diagnostic import CodeRange
from .diagnostic import SlippyDiagnostic


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

    if rule.docstring is None:
        # TODO: add constructor from SlippyCode and rule
        return SlippyDiagnostic(
            # TODO: get range
            range=CodeRange(
                start_line=0,
                start_character=0,
                end_line=0,
                end_character=0,
            ),
            message=SlippyCode.NO_DOCSTRING.value.format(rule.name),
            code=SlippyCode.NO_DOCSTRING.name,
        )
    else:
        return None


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

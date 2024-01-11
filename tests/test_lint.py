from snakemake.workflow import Workflow

from slippy.codes import SlippyCode
from slippy.diagnostic import CodeRange
from slippy.diagnostic import SlippyDiagnostic
from slippy.lint import _check_rule_has_docstring


def test_check_rule_has_docstring(
    test_workflow: Workflow,
) -> None:
    """Test that we can report the absence of a docstring."""

    good_rule = test_workflow.get_rule("good_rule")
    assert _check_rule_has_docstring(good_rule) is None

    diagnostic = SlippyDiagnostic(
        range=CodeRange(start_line=23, start_character=1, end_line=23, end_character=28),
        message="rule rule_with_no_docstring has no docstring",
        code=SlippyCode.NO_DOCSTRING.value,
    )
    bad_rule = test_workflow.get_rule("rule_with_no_docstring")
    assert _check_rule_has_docstring(bad_rule) == diagnostic

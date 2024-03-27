from snakemake.workflow import Workflow

from slippy.codes import SlippyCode
from slippy.diagnostic import CodeRange
from slippy.diagnostic import SlippyDiagnostic
from slippy.lint import _check_rule_has_docstring
from slippy.lint import _check_rule_has_log
from slippy.lint import _check_rule_has_log_redirection
from slippy.lint import _check_rule_has_shell


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


def test_check_rule_has_shell(
    test_workflow: Workflow,
) -> None:
    """Test that we enforce the use of `shell` over `run` or `script`."""

    good_rule = test_workflow.get_rule("good_rule")
    assert _check_rule_has_shell(good_rule) is None

    diagnostic = SlippyDiagnostic(
        range=CodeRange(start_line=45, start_character=5, end_line=45, end_character=8),
        message="rule rule_with_run_block declares a `run` block instead of a `shell` block",
        code=SlippyCode.NO_SHELL.value,
    )
    bad_rule = test_workflow.get_rule("rule_with_run_block")
    assert _check_rule_has_shell(bad_rule) == diagnostic

    diagnostic = SlippyDiagnostic(
        range=CodeRange(start_line=56, start_character=5, end_line=56, end_character=11),
        message="rule rule_with_script_block declares a `script` block instead of a `shell` block",
        code=SlippyCode.NO_SHELL.value,
    )
    bad_rule = test_workflow.get_rule("rule_with_script_block")
    assert _check_rule_has_shell(bad_rule) == diagnostic


def test_check_rule_has_log(
    test_workflow: Workflow,
) -> None:
    """Test that we can report the absence of a log directive."""

    good_rule = test_workflow.get_rule("good_rule")
    assert _check_rule_has_log(good_rule) is None

    diagnostic = SlippyDiagnostic(
        range=CodeRange(start_line=65, start_character=5, end_line=65, end_character=10),
        message="rule rule_with_no_log has no log",
        code=SlippyCode.NO_LOG.value,
    )
    bad_rule = test_workflow.get_rule("rule_with_no_log")
    assert _check_rule_has_log(bad_rule) == diagnostic


def test_check_rule_has_log_redirection(
    test_workflow: Workflow,
) -> None:
    """Test that we can report when the shell command does not redirect stdout/stderr to log."""

    good_rule = test_workflow.get_rule("good_rule")
    import pdb
    pdb.set_trace()
    assert _check_rule_has_log_redirection(good_rule) is None

    diagnostic = SlippyDiagnostic(
        range=CodeRange(start_line=65, start_character=5, end_line=65, end_character=10),
        message="rule rule_with_no_log_redirection has no log redirection",
        code=SlippyCode.NO_LOG_REDIRECTION.value,
    )
    bad_rule = test_workflow.get_rule("rule_with_no_log_redirection")
    assert _check_rule_has_log_redirection(bad_rule) == diagnostic
from pathlib import Path

from snakemake.workflow import Workflow

from slippy.utils import get_directive_lineno
from slippy.utils import get_rule_lineno
from slippy.utils import load_workflow


def test_load_workflow(smk_dir: Path) -> None:
    """Test that we can load a workflow and its constituent rules."""

    workflow = load_workflow(smk_dir / "test.smk")
    assert workflow.is_rule("all")
    assert workflow.is_rule("good_rule")


def test_get_rule_lineno(test_workflow: Workflow) -> None:
    """Test that we can accurately parse the line number on which a rule's declaration begins."""

    rules = {r.name: r for r in test_workflow.rules}

    assert get_rule_lineno(rules["all"]) == 2
    assert get_rule_lineno(rules["good_rule"]) == 7
    assert get_rule_lineno(rules["rule_with_no_docstring"]) == 23


def test_get_directive_lineno(test_workflow: Workflow) -> None:
    """Test that we can obtain the line number on which a directive begins."""

    rule = test_workflow.get_rule("good_rule")

    assert get_directive_lineno(rule, "input") == 9
    assert get_directive_lineno(rule, "output") == 11
    assert get_directive_lineno(rule, "log") == 13
    assert get_directive_lineno(rule, "shell") == 15

from pathlib import Path

from snakemake.workflow import Workflow

from slippy.utils import get_rule_lineno, load_workflow


def test_get_rule_lineno(smk_dir: Path) -> None:
    snakefile = smk_dir / "test.smk"
    workflow = load_workflow(snakefile)

    rules = {r.name: r for r in workflow.rules}

    assert get_rule_lineno(rules["all"]) == 2
    assert get_rule_lineno(rules["make_test"]) == 7
    assert get_rule_lineno(rules["make_test2"]) == 18

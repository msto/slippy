from pathlib import Path

import pytest
from snakemake.workflow import Workflow

from slippy.utils import load_workflow


@pytest.fixture
def smk_dir() -> Path:
    """The directory containing the test snakefiles."""

    return Path(__file__).parent / "snakefiles"


@pytest.fixture
def test_workflow(smk_dir: Path) -> Workflow:
    """A workflow with rules representing the various test cases."""

    return load_workflow(smk_dir / "test.smk")

"""
Define the set of error codes reported by `slippy`.
"""

from enum import Enum
from enum import unique


@unique
class SlippyCode(Enum):
    NO_DOCSTRING = "no_docstring"
    NO_SHELL = "no_shell"

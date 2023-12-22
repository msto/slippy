"""
Define the set of error codes reported by `slippy`.
"""

from enum import Enum
from enum import unique


@unique
class SlippyCode(Enum):
    NO_DOCSTRING = "rule {0} has no docstring"

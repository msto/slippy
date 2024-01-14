"""
Define the set of error codes reported by `slippy`.
"""

from enum import Enum
from enum import unique


@unique
class SlippyCode(Enum):
    NO_DOCSTRING = "no_docstring"
    NO_SHELL = "no_shell"
    NO_LOG = "no_log"
    NO_LOG_REDIRECTION = "no_log_redirection"

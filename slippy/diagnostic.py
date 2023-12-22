"""
Define classes to support publishing diagnostics to LSP in VS Code.

https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#diagnostic
"""

from dataclasses import dataclass
from enum import IntEnum
from enum import unique


@dataclass(frozen=True)
class CodeRange:
    """
    Represent a range of code.

    https://code.visualstudio.com/api/references/vscode-api#Range
    """

    start_line: int
    start_character: int
    end_line: int
    end_character: int

    def __post_init__(self) -> None:
        """
        Enforce the requirement on `Range` that `start` <= `end`.
        """
        msg = (
            f"Start line number ({self.start_line}) must be less than or equal to end line number "
            f"({self.end_line})."
        )
        assert self.start_line <= self.end_line, msg

        if self.start_line == self.end_line:
            msg = (
                f"Start character position ({self.start_character}) must be less than or equal to "
                f"end character position ({self.end_character})."
            )
            assert self.start_character <= self.end_character, msg


@unique
class DiagnosticSeverity(IntEnum):
    """
    Enumeration of the diagnostic severity levels supported by LSP.

    https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#diagnostic
    """

    Error = 1
    Warning = 2
    Information = 3
    Hint = 4


@dataclass(frozen=True)
class SlippyDiagnostic:
    """
    Representation of a diagnostic, compatible with the LSP API.

    https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/#diagnostic

    The LSP `Diagnostic` class has two required fields: `range` and `message.` This class also
    reports the diagnostic's `source` ("slippy"), and a default `severity` level of `Warning`.

    Attributes:
        `range`: The range of code in which the diagnostic occurred.
        `message`: A human-readable message describing the diagnostic.
        `code`: The diagnostic's code.
        `severity`: The diagnostic's severity level.
        `source`: The diagnostic's source.
    """

    range: CodeRange
    message: str
    code: int | str | None

    @property
    def source(self) -> str:
        """
        Describe the source of this diagnostic (always `slippy`).
        """
        return "slippy"

    @property
    def severity(self) -> DiagnosticSeverity:
        """
        The diagnostic's severity level.
        """

        # TODO: Add support for other severity levels.
        return DiagnosticSeverity.Warning

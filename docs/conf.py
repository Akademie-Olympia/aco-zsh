"""Sphinx configuration. Shared settings live in the ACO docs kit (docs/_aco)."""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))

from _aco.base import configure  # noqa: E402

configure(
    globals(),
    slug="aco-zsh",
    title="Zsh",
)

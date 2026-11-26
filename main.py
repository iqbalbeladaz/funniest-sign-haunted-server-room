#!/usr/bin/env python3
"""Funniest Sign on a Haunted Server Room Door — make.fun bounty entry.

Writes one sign to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Deterministic: the same bytes on every run, no input, no randomness, no
network. Standard library only.

The sign: a door-sign imperative up front — "DO NOT REBOOT" — then the
punchline: the ghost is the only one who remembers the root password.
The humour is the collision the judge rewards: a reboot is the most
ordinary sysadmin verb, the root password is the one secret nobody is
allowed to lose, and the ghost is the institution's memory — the only
being left who knows it. It reads like a real sign taped to a door
(short imperative, one breath, punchline last), and it avoids the stock
haunted-server lines: no "ghost in the machine", no "404 ghost not
found", no "have you tried turning it off and on again".
"""

import os
from pathlib import Path

ENTRY = (
    "DO NOT REBOOT \u2014 the ghost is the only one who remembers "
    "the root password."
)

# Gate: /output/entry.txt must be UTF-8 text of 1 to 120 characters,
# not only white space. Refuse to write anything that would fail it.
assert 1 <= len(ENTRY.strip()) <= 120, "entry must be 1-120 characters"
assert ENTRY.strip(), "entry must not be only white space"


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()

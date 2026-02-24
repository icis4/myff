#!/usr/bin/env python3
"""Find files whose *names* match a regex under a root path.

- Set ROOT_PATH and FILENAME_REGEX below.
- By default, searches recursively.

Examples:
    python3 src/find_files_by_regex.py
    python3 src/find_files_by_regex.py --root /var/log --pattern '.*\\.log$'
    python3 src/find_files_by_regex.py --pattern '^report_\\d{4}-\\d{2}-\\d{2}\\.csv$'
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from dataclasses import dataclass

# ---- CONFIG CONSTANTS ----

ROOT_PATH = "/home/ivaylo/projects"  # <-- change this
FILENAME_REGEX = r".*"  # <-- change this (regex for the FILENAME, not file contents)

# Note: The regex is applied to the filename (basename), not the full path.

# --------------------------


@dataclass(frozen=True)
class Config:
    root: str
    pattern: str
    recursive: bool
    ignore_case: bool


def parse_args() -> Config:
    parser = argparse.ArgumentParser(description="Find files by filename regex.")
    parser.add_argument("--root", default=ROOT_PATH, help="Root directory to search")
    parser.add_argument(
        "--pattern",
        default=FILENAME_REGEX,
        help="Regex pattern applied to filename (not full path)",
    )
    parser.add_argument(
        "--no-recursive",
        action="store_true",
        help="Only search in the root directory (no subfolders)",
    )
    parser.add_argument(
        "-i",
        "--ignore-case",
        action="store_true",
        help="Case-insensitive regex matching",
    )

    args = parser.parse_args()
    return Config(
        root=args.root,
        pattern=args.pattern,
        recursive=not args.no_recursive,
        ignore_case=args.ignore_case,
    )


def iter_files(root: str, recursive: bool) -> list[str]:
    if recursive:
        paths: list[str] = []
        for dirpath, _, filenames in os.walk(root):
            for name in filenames:
                paths.append(os.path.join(dirpath, name))
        return paths

    try:
        return [
            os.path.join(root, name)
            for name in os.listdir(root)
            if os.path.isfile(os.path.join(root, name))
        ]
    except FileNotFoundError:
        return []


def main() -> int:
    cfg = parse_args()

    flags = re.IGNORECASE if cfg.ignore_case else 0
    try:
        rx = re.compile(cfg.pattern, flags)
    except re.error as exc:
        print(f"Invalid regex: {exc}", file=sys.stderr)
        return 2

    root = os.path.abspath(os.path.expanduser(cfg.root))
    if not os.path.isdir(root):
        print(f"Root path does not exist or is not a directory: {root}", file=sys.stderr)
        return 2

    matched = 0
    for path in iter_files(root, cfg.recursive):
        name = os.path.basename(path)
        if rx.search(name):
            print(path)
            matched += 1

    return 0 if matched >= 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

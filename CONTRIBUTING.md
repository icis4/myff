# Contributing

Thanks for your interest in contributing to **myff**.

Before you get started, please follow [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md).

## Ways to Contribute
There are a few easy ways to help:
- Report a bug or suggest an improvement via an Issue.
- Open a Pull Request (PR) with a fix or a new feature.
- Improve documentation (README examples, clarifications, edge cases).

## Requirements
- Python 3.9+.
- No additional dependencies (standard library only).

## Running Locally
The script is a single standalone file.

Example (CLI arguments):

```bash
python3 find_files_by_regex.py --root . --pattern '.*\\.py$'
```

Case-insensitive:

```bash
python3 find_files_by_regex.py --root . --pattern 'readme\\.md$' -i
```

Non-recursive:

```bash
python3 find_files_by_regex.py --root . --pattern '.*' --no-recursive
```

## Reporting a Problem (Issue)
When opening an issue, please include:
- What you expected to happen.
- What actually happened (including terminal output/errors).
- The exact command/arguments you used.
- Your Python version (`python3 --version`) and OS.

## Pull Requests

### Process
1. Fork the project.
2. Create a new branch (e.g. `fix/…` or `feature/…`).
3. Make your change.
4. Make sure the script works and the README is up to date (if you change behavior/interface).
5. Open a PR with a clear description.

### What to Include in the PR Description
- Brief context: why the change is needed.
- What exactly is changing.
- How to test it manually (example commands).

### Scope and Focus
- Small, focused PRs are preferred.
- If you add a new flag/option, add a corresponding example in the README.
- Try not to add dependencies unless there is a strong reason.

## Code Style
- Follow PEP 8 and the existing style in the codebase.
- Keep things readable (clear names, small functions, clear error messages).
- Preserve backwards compatibility unless the change is explicitly documented.

## Compatibility and Behavior
- The regex is applied to the **filename**, not the full path.
- Exit codes:
  - `0` – successful execution
  - `2` – invalid regex or invalid root path

## Security
If you discover a security issue, avoid filing a public issue with sensitive details. Prefer responsible disclosure to the maintainers (contact info is in the Code of Conduct).

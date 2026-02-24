# AGENTS.md

This document provides guidance for AI agents and automated tooling working in this repository.

# Language
Use English for comments and documentation

## Project overview
- **Goal:** Find files whose **names** match a regex under a given root directory.
- **Language:** Python (standard library only).
- **Entry point:** `find_files_by_regex.py`.

## How to run
Use CLI flags (preferred):

```bash
python3 find_files_by_regex.py --root . --pattern '.*\\.py$'
```

Helpful variants:

```bash
python3 find_files_by_regex.py --root . --pattern 'readme\\.md$' -i
python3 find_files_by_regex.py --root . --pattern '.*' --no-recursive
```

Expected exit codes:
- `0` – successful execution
- `2` – invalid regex or invalid root path

## What agents may change
Agents are welcome to:
- Fix bugs and edge cases.
- Improve CLI UX (help text, flags) when it stays backward-compatible.
- Improve docs (`README.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`).
- Add lightweight tests **only** if a test harness is introduced deliberately and kept simple.

Agents should avoid:
- Adding non-standard dependencies unless explicitly requested.
- Changing behavior that users rely on without updating docs and providing a clear migration note.
- Unrelated refactors or formatting-only PRs.

## Behavioral contract (important)
- The regex is applied to the **filename** (`os.path.basename(path)`), not the full path.
- Recursive search is the default; `--no-recursive` limits to the root folder.

## Code style
- Keep changes small and readable.
- Prefer clear variable names and straightforward control flow.
- Use type hints where they improve clarity (the project already uses them).
- Maintain the existing error-handling pattern and exit codes.

## Documentation updates
If you add/modify flags or change output behavior, update:
- `README.md` usage examples
- `CONTRIBUTING.md` if contribution workflow changes

## Security & privacy
- Do not log or leak sensitive paths beyond what the tool already prints.
- If a change touches potentially sensitive behavior, document it.

## Contact
For conduct or enforcement topics, see `CODE_OF_CONDUCT.md`.

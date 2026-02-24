# myff

Small Python script for finding files whose **names** match a regex under a given directory.

## Documentation

- [CONTRIBUTING.md](./CONTRIBUTING.md)
- [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)

## What it does

- Walks a directory (`root`) and by default searches **recursively** through all subfolders.
- Applies the regex to the **basename** (the filename itself), not the full path.
- Prints the full paths of all matched files.

## Requirements

- Python 3.9+ (works with newer versions as well)

## Usage

### 1) Via CLI arguments (recommended)

```bash
python3 src/find_files_by_regex.py --root /home/ivaylo --pattern 'index\.html$'
```

Case-insensitive:

```bash
python3 src/find_files_by_regex.py --root /home/ivaylo --pattern 'readme\.md$' -i
```

Current directory only (no subfolders):

```bash
python3 src/find_files_by_regex.py --root . --pattern '.*\.py$' --no-recursive
```

### 2) Via constants in the script

Open `src/find_files_by_regex.py` and change:

- `ROOT_PATH` – the root directory
- `FILENAME_REGEX` – regex for the filename

Then run:

```bash
python3 src/find_files_by_regex.py
```

## Notes

- The regex is applied to the filename (`os.path.basename(path)`), not the full path.
- If you want to match against the **full path**, tell me and I can add it as an option.

## Exit codes

- `0` – successful execution (regardless of whether there are 0 or more matches)
- `2` – invalid regex or invalid root path

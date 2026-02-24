# myff

Малък Python скрипт за търсене на файлове, чиито **имена** съвпадат с regex, в зададена директория.

## Какво прави

- Обхожда директория (`root`) и по подразбиране **рекурсивно** търси във всички подпапки.
- Прилага regex върху **basename** (самото име на файла), а не върху целия път.
- Печата пълните пътища на всички намерени файлове.

## Изисквания

- Python 3.9+ (работи и с по-нови версии)

## Ползване

### 1) Чрез CLI аргументи (препоръчително)

```bash
python3 find_files_by_regex.py --root /home/ivaylo --pattern 'index\.html$'
```

Case-insensitive:

```bash
python3 find_files_by_regex.py --root /home/ivaylo --pattern 'readme\.md$' -i
```

Само текущата директория (без подпапки):

```bash
python3 find_files_by_regex.py --root . --pattern '.*\.py$' --no-recursive
```

### 2) Чрез константи в скрипта

Отвори `find_files_by_regex.py` и промени:

- `ROOT_PATH` – root директорията
- `FILENAME_REGEX` – regex за името на файла

После пусни:

```bash
python3 find_files_by_regex.py
```

## Бележки

- Regex-ът се прилага върху името на файла (`os.path.basename(path)`), не върху целия път.
- Ако искаш да мачваш regex върху **целия път** (full path), кажи и ще го добавя като опция.

## Exit codes

- `0` – успешно изпълнение (независимо дали има 0 или повече съвпадения)
- `2` – невалиден regex или невалиден root path

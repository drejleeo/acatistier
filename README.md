# acatistier

This repo is a scraper for doxologia romanian website.

Its purpose is to gather multiple prayers called "acatiste" and output them to a `.docx` file.
Using calibre, I then transformed it to a `.mobi` file to work nicely on kindle.

# Run

Install dependencies

```bash
uv sync
```

```bash
python collect_prayers.py

# Important: edit your catalog.json to customize your selection.

python save_book.py
```

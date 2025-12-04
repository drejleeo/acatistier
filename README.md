# acatistier

This repo is a scraper for doxologia romanian website.

Its purpose is to gather multiple prayers called "acatiste" and output them to a `.docx` file.
Using calibre, I then transformed it to a `.mobi` file to work nicely on kindle.

# Run

If you want to experiment with the code, you can use the included jupyter notebook to keep the downloaded soups locally and avoid unnecessary network calls, as rate limiting might be applied to the website in the future.

```bash
# Install dependencies
uv sync

# Activate virtual env
source .venv/bin/activate

# Download catalog into json file
# Important: edit your catalog.json to customize your selection
python collect_prayers.py

# Save selection to docx
python save_book.py
```

# Octave forge gentoo package generator

## Usage

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install requirements.txt
python3 octave-gentoo-package.py
```

Then all packages shoud in ``dev-octave`` directory.
If you want to use it in your own overlay, you need to add categorie ``dev-octave`` into ``profiles/categories``.

## Overlay

If you want use it out of the box, this is my overlay.

[::vowstar-overlay: https://github.com/vowstar/vowstar-overlay](https://github.com/vowstar/vowstar-overlay)

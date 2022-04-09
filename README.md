# german-freeval

## Installation

To install German FREEVAL you'll need Python (>= 3.10). Clone this repository and install a virtual environment.

```bash
python -m venv venv --upgrade-deps
pip install -r requirements.txt
```

If you want to contribute to German FREEVAl you should consider using [VS Code](https://code.visualstudio.com/) and installing additional requirements.

```bash
pip install -r requirements_dev.txt 
```

Windows users can use `/venv_setup/venv_install.bat` for convenience.

## Documentation

The documentation is powered by the awesome projects [mkdocs](https://www.mkdocs.org/), [material-theme](https://squidfunk.github.io/mkdocs-material/), and [mkdocstrings](https://mkdocstrings.github.io/usage/).

To run mkdocs locally:

```bash
pip install -r requirements_docs.txt
mkdocs serve
```

Open [127.0.0.1:8000](http://127.0.0.1:8000) in your browser and watch the documentation autoupdating while you work on the documentation in `/docs`.

## Acknowlegement

[German FREEVAL](https://www.bast.de/DE/Publikationen/Daten/Verkehrstechnik/v1-FREEVAL/FREEVAL-start_node.html) was initially implemented by [KIT-Institute for Transport Studie](https://ifv.kit.edu)
and was funded by the [German Federal Highway Research Institute (BASt)](https://www.bast.de/).
It was initially implemented in VisualBasic and data handling was done in Excel.
German FREEVAL is based on the [US FREEVAL](http://freeval.org/).

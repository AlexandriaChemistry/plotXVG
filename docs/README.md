# The plotXVG manual

The manual is written in reStructuredText and built with Sphinx. The
workflow `.github/workflows/docs.yml` builds it for every pull request and
publishes it at https://alexandriachemistry.github.io/plotXVG/ for every push
to main.

To build it locally (Python 3.11 or newer), from the top of the repository:

    python -m pip install -r docs/requirements.txt .
    sphinx-build -b html docs docs/_build/html

and open `docs/_build/html/index.html`.

- The options in `options.rst` come from the argument parser of plotxvg
  (`build_parser()` in `plotxvg/plotxvg.py`), so they are always up to date.
- The chapter `examples.rst` is made by `generate_examples.py`, which runs all
  examples of `tests/test.py` and therefore needs plotxvg to be installed.
  Sphinx runs it when `examples.rst` does not exist yet; after changing the
  examples, delete `examples.rst` or run `python docs/generate_examples.py`.

# Reference images

PNG plots of all examples in `tests/test.py`, used by `tests/compare_images.py`
in the `images` job of the GitHub workflow.

The images are made on the reference platform of that job (ubuntu-latest,
Python 3.12, the versions in `tests/requirements-images.txt`). Plots made on
other platforms differ, mainly in fonts, so do not generate them locally.

To create or update the references after an intended change of the plots:

1. Run the workflow, e.g. by pushing to a pull request.
2. Download the `images-actual` artifact of the run.
3. Inspect the plots, then copy the PNG files (not the `*-failed-diff.png`
   files) into this directory and commit them.

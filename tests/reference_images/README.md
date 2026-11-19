# Reference images

PNG plots of all examples in `tests/test.py`, used by `tests/compare_images.py`
in the `images` job of the GitHub workflow.

In PNG mode `test.py` draws all text with DejaVu Sans, which comes with
matplotlib, so the plots do not depend on the fonts installed. With the
package versions in `tests/requirements-images.txt` the plots are then
pixel-identical on Linux and macOS (checked on ubuntu-latest and Apple
silicon). Other versions of matplotlib, numpy or scipy can change them.

To check or update the references locally, from the top of the repository:

    python -m venv venv-images
    . venv-images/bin/activate
    pip install -r tests/requirements-images.txt .
    cd tests
    python test.py png-output -format png
    python compare_images.py png-output

After an intended change of the plots, inspect the plots and the
`*-failed-diff.png` difference images in `png-output`, then copy the plots
(not the difference images) here and commit them:

    find png-output -name '*.png' ! -name '*-failed-diff.png' -exec cp {} reference_images/ \;

Alternatively, download the `images-actual` artifact of a workflow run,
which holds the same files.

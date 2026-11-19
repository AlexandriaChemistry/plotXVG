#!/usr/bin/env python3
"""Compare the PNG plots made by test.py with the reference images.

Usage:
    python test.py png-output -format png
    python compare_images.py png-output

The plots must be made with the package versions in
requirements-images.txt, since other versions can change the rendering.
In PNG mode test.py uses a font that comes with matplotlib, so the
installed fonts do not matter. See reference_images/README.md for how to
create or update the reference images.

For each plot that differs, matplotlib writes a difference image next
to the plot, named <plot>-failed-diff.png.
"""
import argparse, sys
from pathlib import Path
from matplotlib.testing.compare import compare_images
from matplotlib.testing.exceptions import ImageComparisonFailure

def main():
    scriptdir = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description="Compare plots with reference images")
    parser.add_argument("actualdir", help="Directory with the PNG plots made by test.py")
    parser.add_argument("-refdir", "--refdir", default=str(scriptdir / "reference_images"),
                        help="Directory with the reference images, default reference_images next to this script")
    parser.add_argument("-tol", "--tol", type=float, default=1.0,
                        help="Tolerance for the RMS pixel difference (255 is the maximum), default 1.0")
    args = parser.parse_args()

    actualdir = Path(args.actualdir)
    refdir = Path(args.refdir)
    actuals = sorted(p for p in actualdir.glob("*.png") if not p.name.endswith("-failed-diff.png"))
    if not actuals:
        sys.exit(f"No PNG plots found in {actualdir}")

    failed = []
    for actual in actuals:
        expected = refdir / actual.name
        if not expected.is_file():
            print(f"{actual.name}: no reference image")
            failed.append(actual.name)
            continue
        try:
            result = compare_images(str(expected), str(actual), tol=args.tol)
        except ImageComparisonFailure as e:
            # For example, the images do not have the same size
            result = str(e)
        if result is None:
            print(f"{actual.name}: OK")
        else:
            print(f"{actual.name}: DIFFERENT\n{result}")
            failed.append(actual.name)

    # References without a plot mean that an example was removed or renamed
    names = {p.name for p in actuals}
    for expected in sorted(refdir.glob("*.png")):
        if expected.name not in names and not expected.name.endswith("-failed-diff.png"):
            print(f"{expected.name}: reference image without a plot")
            failed.append(expected.name)

    if failed:
        print(f"{len(failed)} image(s) do not match the references: {', '.join(failed)}")
        sys.exit(1)
    print(f"All {len(actuals)} images match the references.")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Make the chapter examples.rst of the manual from the examples in
tests/test.py: run them all with PNG output into docs/examples/, then write
one section per example with its description, command and plot.
plotxvg must be installed, since test.py runs the plotxvg command.
"""
import re, subprocess, sys
from pathlib import Path

docsdir = Path(__file__).resolve().parent
plotdir = docsdir / "examples"
testdir = docsdir.parent / "tests"

# test.py adds this font to every command for PNG output, such that the
# plots do not depend on the fonts installed; it is not part of the example
FONTFLAG = ' -font "DejaVu Sans"'

INTRO = """\
.. This file is made by generate_examples.py, do not edit it.

.. _examples:

Example plots
=============

This chapter shows how plotXVG can be used, with the examples of the script
``tests/test.py`` in the plotXVG repository. Each plot comes with the exact
plotXVG command that made it. To run the commands yourself, go to the
``tests`` directory of the repository, where the input files are.
"""

def rst_text(text: str) -> str:
    """Collapse white space and escape the characters that rst interprets."""
    text = " ".join(text.split())
    return re.sub(r"([*`|\\])", r"\\\1", text)

def read_command_file(path: Path):
    content = path.read_text()
    description = content.split("Description:", 1)[1].split("File(s) used:", 1)[0]
    command = content.split("Command:", 1)[1].strip()
    return description, command

def clean_command(command: str, plotfile: str) -> str:
    """Remove the font of test.py and show the plot without its directory."""
    command = command.replace(FONTFLAG, "")
    return re.sub(r"-save \S+", f"-save {plotfile}", command)

def main():
    plotdir.mkdir(exist_ok=True)
    for old in plotdir.glob("*"):
        old.unlink()
    subprocess.run([sys.executable, str(testdir / "test.py"), str(plotdir), "-format", "png"],
                   check=True)
    sections = [INTRO]
    for png in sorted(plotdir.glob("[0-9]*.png")):
        name = re.sub(r"^\d+", "", png.stem)
        description, command = read_command_file(plotdir / f"{png.stem}_command.txt")
        title = name.replace("_", " ")
        sections.append(f"""
.. _example-{name}:

{title}
{"-" * len(title)}

{rst_text(description)}

.. code-block:: shell

   {clean_command(command, png.name)}

.. image:: examples/{png.name}
   :width: 90%
   :alt: Plot of the example {title}
""")
    (docsdir / "examples.rst").write_text("".join(sections))
    print(f"Wrote examples.rst with {len(sections) - 1} examples")

if __name__ == "__main__":
    main()

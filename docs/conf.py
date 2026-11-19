# Configuration of the Sphinx manual of plotXVG, see README.md in this
# directory.
import datetime
import os
import subprocess
import sys
import tomllib

docsdir = os.path.dirname(os.path.abspath(__file__))
topdir = os.path.dirname(docsdir)
# Use the plotxvg of this source tree for the options
sys.path.insert(0, topdir)

with open(os.path.join(topdir, "pyproject.toml"), "rb") as f:
    release = tomllib.load(f)["project"]["version"]
version = release

project = "plotXVG"
author = "Måns Rosenbaum and David van der Spoel"
copyright = f"{datetime.date.today().year}, {author}"

extensions = [
    "sphinx.ext.mathjax",
    "sphinx.ext.extlinks",
    "sphinxarg.ext",
    "sphinx_copybutton",
]
extlinks = {"issue": ("https://github.com/AlexandriaChemistry/plotXVG/issues/%s", "issue %s")}

html_theme = "sphinx_rtd_theme"
html_title = f"plotXVG {release} manual"
html_theme_options = {"navigation_depth": 3}
exclude_patterns = ["_build", "README.md"]
# Do not copy the prompt of shell examples
copybutton_prompt_text = "$ "

# The example chapter is made from the plots of tests/test.py, which takes
# about a minute. It is only made if it does not exist yet; delete
# examples.rst or run generate_examples.py to make it again.
if not os.path.exists(os.path.join(docsdir, "examples.rst")):
    subprocess.run([sys.executable, os.path.join(docsdir, "generate_examples.py")], check=True)

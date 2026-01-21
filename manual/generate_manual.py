import os
from pathlib import Path
import subprocess
import textwrap
import shutil, sys
#Check if the user has installed pdflatex first
if shutil.which("pdflatex") == None:
   sys.exit("You need to install pdflatex first.")

OUTPUT_PLOTS = Path("../tests/plotxvg_tests-output") 
INFILE = Path("chapters/temp_plots.tex")
OUTFILE = Path("chapters/example_plots.tex")
outputdir = Path("plotXVG_manual")
outputdir.mkdir(parents=True, exist_ok=True)

def collect_examples():
    examples_latex = ""
    setcount = 0
    # Loop through all PDF images
    for pdf_file in sorted(OUTPUT_PLOTS.glob("*.pdf")):
        
        # To find txt file
        txt_file = pdf_file.with_suffix("")  # remove .pdf
        txt_file = Path(str(txt_file) + "_command.txt")

        # fig labeling in manual
        label = f"{setcount:02d}"

        description = ""
        command = ""
        if txt_file.exists():
            content = txt_file.read_text()
            marker_desc = "File(s) used:"
            marker_cmd = "Command:"

            if marker_desc in content:
                description = content.split(marker_desc, 1)[0].rstrip()
                description = description.split("Description:", 1)[-1].lstrip() #Removes "Description: " in the beginning.
            else:
                description = ""

            if marker_cmd in content:
                command = content.split(marker_cmd, 1)[1].lstrip()
            else:
                command = ""

            wrapped = textwrap.fill(command, width=60,
                                    break_long_words=False,
                                    break_on_hyphens=False)
            wrapped = wrapped.replace("\n", " \\\n\t\t")

        examples_latex += rf"""
Command for Fig. \ref{{fig:{label}}}:
\begin{{verbatim}}
{wrapped}
\end{{verbatim}}
\begin{{figure}}[H]
    \centering
    \includegraphics[width=0.9\textwidth]{{{pdf_file.as_posix()}}}
    \caption{{{description}}}
    \label{{fig:{label}}}
\end{{figure}}

"""
        setcount +=1
    return examples_latex


def build_plotchapter():
    template = INFILE.read_text()
    examples = collect_examples()

    final_tex = template.replace(f"% EXAMPLES %", examples)

    OUTFILE.write_text(final_tex)
    print("plots insterted. Generating manual...")

build_plotchapter()
subprocess.run([
"pdflatex",
"-output-directory=plotXVG_manual",
"-jobname=plotXVG_manual",
"main.tex"
]) #Run twice because pdflatex requests that time to time
subprocess.run([
"pdflatex",
"-output-directory=plotXVG_manual",
"-jobname=plotXVG_manual",
"main.tex"
])
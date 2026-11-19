Preface
=======

This manual is a work in progress, describing the current functions and
utilities of plotXVG version |release| and how to install and use this tool.

Command lines are shown ``like this``, or as a block:

.. code-block:: shell

   plotxvg -f file.xvg

Enhancements, reports of issues and overall suggestions for improvements are
very welcome, either by e-mail to mans.rosenbaum@icm.uu.se or as an issue on
GitHub at https://github.com/AlexandriaChemistry/plotXVG/issues.

plotXVG is free and open-source software, available from
https://github.com/AlexandriaChemistry/plotXVG.

Citing plotXVG
--------------

We kindly request that you cite the paper about plotXVG if you use the tool
for a publication of your own:

   Måns K. Rosenbaum and David van der Spoel, *plotXVG: Batch Generation of
   Publication-Quality Graphs from GROMACS Output*, J. Chem. Inf. Model.
   **66** (2026) 2955-2959, https://doi.org/10.1021/acs.jcim.5c02998

About plotXVG
-------------

plotXVG is a command-line tool based on the Matplotlib library and NumPy,
meant in part to replace the Grace software for quickly making plots from
xvg files written by GROMACS. It supports csv and dat files as well. It
consists of about 1200 lines of Python code, plus a test script.

The following chapters give an installation guide and the practical usage of
plotXVG, including descriptions of all options.

We hope this tool suits your needs!

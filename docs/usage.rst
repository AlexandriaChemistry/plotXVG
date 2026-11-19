Using plotXVG
=============

plotXVG can be used both from the command line and from Python, for instance
in a script or a Jupyter notebook. The command line is useful for quickly
plotting new output files and opens a Matplotlib window in which you can
interact with the plot. The Python interface is suitable for analysis in, for
example, a Jupyter notebook, and makes it easy to plot many files with
control over styles, labels and more. Both are easy to use, with some small
differences.

Command line
------------

The general command for using plotXVG on the command line is:

.. code-block:: shell

   plotxvg -f file(s) [options]

There is only one required argument, namely one or more input files in xvg,
csv or dat format. This produces a scatter plot of the data. Matplotlib
opens a window with an interactive plot, from which you can save it with the
buttons of the window. Alternatively, the ``-save`` option saves the plot
after the layout of the plot has been adjusted; the interactive window might
not show the final image. If you do not want a window to be opened, add
``-noshow``:

.. code-block:: shell

   plotxvg -f file(s) -save output.pdf -noshow

To make a line plot instead, add the option ``-ls`` (short for line style)
with a line style:

.. code-block:: shell

   plotxvg -f file(s) -ls solid

This makes a plot with a solid line. The supported line styles are solid,
dashed, dashdot and dotted. Lines and markers can be combined by giving both
options:

.. code-block:: shell

   plotxvg -f file(s) -ls dashed -mk +

which gives a dashed line with a cross at each data point. All options are
described in :doc:`options`.

Python
------

To use plotXVG in a Python script or a notebook, first import it:

.. code-block:: python

   import plotxvg

Then call the function ``plot()``:

.. code-block:: python

   plotxvg.plot("file.xvg")

To plot several files, put them in a list:

.. code-block:: python

   plotxvg.plot(["file1.xvg", "file2.xvg"])

Options are given as keyword arguments named after the option, with the
values as strings, or lists of strings for options that take several values:

.. code-block:: python

   plotxvg.plot(["file1.xvg", "file2.xvg"],
                linestyle=["solid", "dashed"],
                panels=True,
                save="plot.pdf")

Both the long and the short option names are supported, just like on the
command line. Options that are switched on or off take ``True`` or
``False``, not strings.

Heatmaps and contour plots
--------------------------

plotXVG can also make heatmaps, for instance to study probability densities
and free energy landscapes. Use the option ``-heatmap`` for this:

.. code-block:: shell

   plotxvg -f file.xvg -heatmap

In Python, set ``heatmap`` to ``True``:

.. code-block:: python

   plotxvg.plot("file.xvg", heatmap=True)

The input file can either contain two columns of raw data, from which a
probability density is computed on a grid of bins, or three columns of 2D
data, with the third column holding the values for the color scale. Use
``-contour`` instead of ``-heatmap`` to make a plot with contour lines.

The option ``-gibbs`` turns the probability density into the Gibbs free
energy:

.. math::

   G = -k_\mathrm{B}T \ln \frac{P}{P_0}

where :math:`P_0` is the probability of the most populated bin, which
therefore has :math:`G = 0`, :math:`k_\mathrm{B}` is Boltzmann's constant
and :math:`T` the absolute temperature, which can be set with
``-temp`` (default 298.15 K). The free energy is given in kJ/mol.

With ``-kde`` the probability density is instead estimated by kernel density
estimation, using ``stats.gaussian_kde`` of SciPy. This can be beneficial if
there are very few data points. Adding ``-showdots`` also draws the data
points on top of the density.

Other options for heatmaps and contour plots are the colormap ``-cmap``
(default *viridis*), the number of bins ``-bins`` for computing the density
(default 50), and the number of contour levels ``-levels`` (default 15). See
the examples :ref:`example-heatmap` and :ref:`example-contour_kde`.

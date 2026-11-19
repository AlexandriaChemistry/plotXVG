Installation
============

plotXVG is written in Python and needs only a few other packages.

Prerequisites
-------------

The following software is required for plotXVG to work:

#. Python, version 3.10 or higher (3.11 or higher with conda).
#. Matplotlib version 3.7.0 or higher.
#. NumPy version 1.24.1 or higher.
#. SciPy version 1.15.3 or higher, used for the kernel density estimation
   (``-kde``).
#. Optionally, XQuartz or similar, for opening windows when working on a
   remote server.

When installing with conda or pip, the required packages are installed
automatically.

With conda
----------

plotXVG is available from the channel ``alexandriachemistry`` on anaconda.org.
Install it into a new or existing environment with conda or mamba:

.. code-block:: shell

   conda install -c alexandriachemistry -c conda-forge plotxvg

With pip
--------

plotXVG is also available on PyPI. Install it into your **current** Python
environment with:

.. code-block:: shell

   python -m pip install plotxvg

From the source
---------------

Alternatively, clone the repository from GitHub:

.. code-block:: shell

   git clone https://github.com/AlexandriaChemistry/plotXVG

Then go into that directory and, while being in your Python environment,
install plotXVG with pip:

.. code-block:: shell

   python -m pip install .

The benefit of cloning the repository is that the example files of the
:ref:`examples` and the test script are available, but it is not a
requirement.

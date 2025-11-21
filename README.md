# plotXVG

Molecular simulation tools such as [GROMACS](https://www.gromacs.org) routinely produce 
time-series of energies and other observables. To turn this data into
publication quality figures a user can either use a (commercial) software package with a graphical user interface,
often offering fine control and high-quality output, or write their own
code to make plots using a scripting language. In the age of big data and machine
learning it is often necessary to generate many graphs, be able to rapidly inspect
them, and to make plots for manuscripts. 
This repository provides a simple Python tool, *plotxvg*, built on the well-known [matplotlib](https://matplotlib.org/) plotting library that will generate a graphcs file from, for instance, an energy calculation. 
This will allow users to rapidly and reproducibly generate series of graphics files without programming.
Obviously, the tool is applicable to any kind of line graph data, not just that from molecular simulations. 


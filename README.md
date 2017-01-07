PRISM_interface
========

Interface to generate input files automatically for model checker PRISM 

-----
Description
-----
This package contains the implementation for generating input files, particularly, MDP model, LTL/DRA model for the [PRISM model checker](http://www.prismmodelchecker.org).

Creating by hand these modules is simply tedious, particularly so since PRISM does not allow non-integer identifier for each mode of a state. 




-----
Features
-----
* Generate MDP model in [PRISM language](http://www.prismmodelchecker.org/manual/ThePRISMLanguage/Example1) from MDP that are created as [NetworkX](https://networkx.github.io) graph objects.

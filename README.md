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
* Generate product MDP model in [PRISM language](http://www.prismmodelchecker.org/manual/ThePRISMLanguage/Example1) from MDP that are created as [NetworkX](https://networkx.github.io) graph objects.

 Specifically, check the [P_MDP_TG](https://github.com/MengGuo/P_MDP_TG/blob/master/case_study_data_to_prism.py) to generate the product automaton from a (probabilistically-labeled) MDP and a LTL formula.

 Then this PRISM module ([size5_all_base_nx2prism.nm](https://github.com/MengGuo/PRISM_interface/blob/master/data/size5_all_base_nx2prism.nm)) along with a trivia LTL formula ([size5_all_base_nx2prism.nm.props](https://github.com/MengGuo/PRISM_interface/blob/master/data/size5_all_base_nx2prism.nm.props)) can be fed directly to PRISM. 

*

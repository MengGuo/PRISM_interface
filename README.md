PRISM_interface
========

Generate input files automatically for model checker PRISM, from NetworkX graph objects.

```
@ARTICLE{8272366,
  author={M. {Guo} and M. M. {Zavlanos}},
  journal={IEEE Transactions on Automatic Control}, 
  title={Probabilistic Motion Planning Under Temporal Tasks and Soft Constraints}, 
  year={2018},
  volume={63},
  number={12},
  pages={4051-4066},
  doi={10.1109/TAC.2018.2799561}}
```

-----
Description
-----
This package contains the implementation for generating input files, particularly, MDP model, LTL/DRA model for the [PRISM model checker](http://www.prismmodelchecker.org), from [NetworkX](https://networkx.github.io) graph objects.

Creating by hand these modules is simply **tedious**, particularly so since PRISM does **not** allow non-integer identifier for each mode of a state. 




-----
Features
-----
* Generate product MDP model in [PRISM language](http://www.prismmodelchecker.org/manual/ThePRISMLanguage/Example1) from MDP that are created as [NetworkX](https://networkx.github.io) graph objects.

 Specifically, check the [P_MDP_TG package ](https://github.com/MengGuo/P_MDP_TG/tree/master/pickle_for_prism) to generate the product automaton from a (probabilistically-labeled) MDP and a LTL formula.

 Then this PRISM module (example [size5_all_base_nx2prism.nm](https://github.com/MengGuo/PRISM_interface/blob/master/data/size5_all_base_nx2prism.nm)) along with a trivia LTL formula (example [size5_all_base_nx2prism.nm.props](https://github.com/MengGuo/PRISM_interface/blob/master/data/size5_all_base_nx2prism.nm.props)) can be fed directly to PRISM.

<p align="center">  
  <img src="https://github.com/MengGuo/PRISM_interface/blob/master/data/prism_prod_mdp.png" width="700"/>
</p>

* Generate DRA model as MDP module in PRISM language.

 Given a LTL formula, [P_MDP_TG package ](https://github.com/MengGuo/P_MDP_TG) provides automated translation to a NetworkX graph, via LTL2BA and LTL2DSTAR. Then the equivalent PRISM module as a MDP can be generated here.

 Note that the DRA (example [dra_all_base_nx2prism.nm](https://github.com/MengGuo/PRISM_interface/blob/master/data/dra_all_base_nx2prism.nm)) is encoded as a PRISM module to allow action-based LTL model checking (i.e., synchronized game between a MDP and a DRA), since PRISM only supports state-based LTL currently. 


<p align="center">  
  <img src="https://github.com/MengGuo/PRISM_interface/blob/master/data/prism_dra.png" width="700"/>
</p>

* Generate labeled MDP module in PRISM language, from NetworkX graph object.

 Given a labeled MDP digraph, [P_MDP_TG package ](https://github.com/MengGuo/P_MDP_TG/tree/master/pickle_for_prism) generates the corresponding mdp module in PRISM language, see example [size5_motion_mdp_nx2prism.nm](https://github.com/MengGuo/PRISM_interface/blob/master/data/size5_motion_mdp_nx2prism.nm)

<p align="center">  
  <img src="https://github.com/MengGuo/PRISM_interface/blob/master/data/prism_mdp.png" width="700"/>
</p>

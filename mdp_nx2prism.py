# -*- coding: utf-8 -*-

import pickle


# networkx digraph object
mdp = pickle.load(open('mdp_model.p','rb'))

# create mdp module file
# official example: http://www.prismmodelchecker.org/manual/ThePRISMLanguage/Example1

mdp_file = open("mdp_nx2prism.nm", "w")

mdp_file.write('//mdp in PRISM language, generated from networkx digraph model \n')

mdp_file.write('mdp \n')

mdp_file.write('module test_mdp \n')

# converts state names to integers 
states_list = list(mdp.nodes())
no_of_states = len(states_list)
init_state = mdp.graph[initial_node]
idx_init_state = states_list.index(init_state)

mdp_file.write('x: [0..%d] init %d;\n' %(no_of_states, idx_init_state))

for f_s in mdp.nodes():






mdp_file.close()




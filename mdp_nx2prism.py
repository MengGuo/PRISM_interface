# -*- coding: utf-8 -*-

import pickle

def mdp_module_nx2prism(nx_mdp):
    # create mdp module file
    # official example: http://www.prismmodelchecker.org/manual/ThePRISMLanguage/Example1
    if 'name' in nx_mdp.graph:
        name = nx_mdp.graph['name']
    else:
        name = 'mdp'
    mdp_nm_file = open("%s_nx2prism.nm" %name, "w")

    mdp_nm_file.write('//mdp in PRISM language, generated from networkx digraph model \n')

    mdp_nm_file.write('mdp \n')
    mdp_nm_file.write('\n')
    mdp_nm_file.write('\n')

    #----------------------------------------
    # Module part
    mdp_nm_file.write('module test_mdp \n')

    # converts state names to integers 
    states_list = list(nx_mdp.nodes())
    no_of_states = len(states_list)
    init_state = nx_mdp.graph['initial_node']
    idx_init_state = states_list.index(init_state)

    mdp_nm_file.write('x: [0..%d] init %d;\n' %(no_of_states, idx_init_state))

    # example : [act] x=0 -> 0.8:(x'=0) + 0.2:(x'=1);
    act_cost = dict()
    state_label = dict()
    for f_s in nx_mdp.nodes():
        idx_f_s = states_list.index(f_s)
        if label in nx_mdp.node[f_s]:
            label = nx_mdp.node[f_s]['label']
            # node label ['label'],
            # set of atomic propositions fulfilled at a state
            # optional
            for l in label:
                if l not in state_label:
                    state_label[l] = set([idx_f_s,])
                else:
                    state_label[l].add(idx_f_s)
        for act in nx_mdp.node[f_s]['actions']:
            mdp_nm_file.write('[%s] x=%d -> ' %(str(act), idx_f_s))
            k = 0
            for t_s in nx_mdp.successors_iter(f_s):
                idx_t_s = states_list.index(t_s)
                prob_cost = nx_mdp.edge[f_s][t_s]['prop']
                # edge label ['prop'],
                # dict of trans. prob and cost over different actions
                # fixed
                if act in prob_cost:
                    prob, cost = prob_cost[act]
                    if act not in act_cost:
                        act_cost[act] = cost
                    if k == 0:
                        mdp_nm_file.write("%f:(x'= %d)" %(prob,idx_t_s))
                    else:
                        mdp_nm_file.write("+ %f:(x'= %d)" %(prob,idx_t_s))
                    k += 1
            mdp_nm_file.write(';\n')

    mdp_nm_file.write('endmodule\n')
    #----------------------------------------

    #----------------------------------------
    # label part
    mdp_nm_file.write('\n')
    mdp_nm_file.write('\n')
    for label,states in state_label.items():    
        mdp_nm_file.write('label "%s" = '%label)
        k = 0
        for state in states:
            if k == 0:
                mdp_nm_file.write('s = %d'%state)
            else:
                mdp_nm_file.write('| s = %d'%state)
            k += 1
        mdp_nm_file.write(';\n')

    #----------------------------------------
    # cost part
    mdp_nm_file.write('\n')
    mdp_nm_file.write('\n')

    mdp_nm_file.write('rewards\n')
    for act,cost in act_cost.items():    
        mdp_nm_file.write('[%s] true : %f;\n' %(act,cost))
    mdp_nm_file.write('endrewards\n')

    #----------------------------------------
    mdp_nm_file.close()
    print('PRISM mdp module saved at %s_nx2prism.nm' %name)


# networkx digraph object
nx_mdp = pickle.load(open('nx_mdp_model.p','rb'))
mdp_module_nx2prism(nx_mdp)






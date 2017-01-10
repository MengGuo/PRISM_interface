# -*- coding: utf-8 -*-

import pickle

def dra_module_nx2prism(nx_dra):
    # create dra module file
    # toy example: https://github.com/prismmodelchecker/prism-tests/blob/master/functionality/verify/mdps/ltl/running-ltl.nm

    if 'name' in nx_dra.graph:
        name = nx_dra.graph['name']
    else:
        name = 'dra'
    dra_nm_file = open("%s_nx2prism.nm" %name, "w")

    dra_nm_file.write('//dra in PRISM language, generated from  networkx digraph model \n')

    dra_nm_file.write('// This is encoded as a PRISM module to allow action-based LTL \n')
    
    dra_nm_file.write('// model checking: PRISM only supports state-based LTL currently module\n')

    dra_nm_file.write('dra \n')
    dra_nm_file.write('\n')
    dra_nm_file.write('\n')

    #----------------------------------------
    # Module part
    dra_nm_file.write('module test_dra \n')

    # converts state names to integers 
    states_list = list(nx_dra.nodes())
    no_of_states = len(states_list)
    init_state = list(nx_dra.graph['initial'])[0]
    idx_init_state = states_list.index(init_state)

    dra_nm_file.write('x: [0..%d] init %d;\n' %(no_of_states, idx_init_state))

    # example : [go] q=0 -> (q'=1);
    act_cost = dict()
    state_label = dict()
    for f_s in nx_dra.nodes():
        idx_f_s = states_list.index(f_s)
        if label in nx_dra.node[f_s]:
            label = nx_dra.node[f_s]['label']
            # node label ['label'],
            # set of atomic propositions fulfilled at a state
            # optional
            for l in label:
                if l not in state_label:
                    state_label[l] = set([idx_f_s,])
                else:
                    state_label[l].add(idx_f_s)
        for act in nx_dra.node[f_s]['actions']:
            dra_nm_file.write('[%s] x=%d -> ' %(str(act), idx_f_s))
            k = 0
            for t_s in nx_dra.successors_iter(f_s):
                idx_t_s = states_list.index(t_s)
                prob_cost = nx_dra.edge[f_s][t_s]['prop']
                # edge label ['prop'],
                # dict of trans. prob and cost over different actions
                # fixed
                if act in prob_cost:
                    prob, cost = prob_cost[act]
                    if act not in act_cost:
                        act_cost[act] = cost
                    if k == 0:
                        dra_nm_file.write("%f:(x'= %d)" %(prob,idx_t_s))
                    else:
                        dra_nm_file.write("+ %f:(x'= %d)" %(prob,idx_t_s))
                    k += 1
            dra_nm_file.write(';\n')

    dra_nm_file.write('endmodule\n')
    #----------------------------------------

    #----------------------------------------
    # label part
    dra_nm_file.write('\n')
    dra_nm_file.write('\n')
    for label,states in state_label.items():    
        dra_nm_file.write('label "%s" = '%label)
        k = 0
        for state in states:
            if k == 0:
                dra_nm_file.write('s = %d'%state)
            else:
                dra_nm_file.write('| s = %d'%state)
            k += 1
        dra_nm_file.write(';\n')

    #----------------------------------------
    # cost part
    dra_nm_file.write('\n')
    dra_nm_file.write('\n')

    dra_nm_file.write('rewards\n')
    for act,cost in act_cost.items():    
        dra_nm_file.write('[%s] true : %f;\n' %(act,cost))
    dra_nm_file.write('endrewards\n')

    #----------------------------------------
    dra_nm_file.close()
    print('PRISM dra module saved at dra_nx2prism.nm')


# networkx digraph object
nx_dra = pickle.load(open('nx_dra_model.p','rb'))
dra_module_nx2prism(nx_dra)






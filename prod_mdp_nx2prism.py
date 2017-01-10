# -*- coding: utf-8 -*-

import pickle

def prod_mdp_module_nx2prism(nx_prod_mdp):
    # create product mdp module file
    # product between mdp and dra
    # PRISM mdp module official example: http://www.prismmodelchecker.org/manual/ThePRISMLanguage/Example1
    if 'name' in nx_prod_mdp.graph:
        name = nx_prod_mdp.graph['name']
    else:
        name = 'prod_mdp'
    prod_mdp_nm_file = open("%s_nx2prism.nm" %name, "w")

    prod_mdp_nm_file.write('//product mdp in PRISM language, generated from networkx digraph model \n')

    prod_mdp_nm_file.write('mdp \n')
    prod_mdp_nm_file.write('\n')
    prod_mdp_nm_file.write('\n')

    #----------------------------------------
    # Module part
    prod_mdp_nm_file.write('module test_product_mdp \n')

    # converts state names to integers 
    states_list = list(nx_prod_mdp.nodes())
    no_of_states = len(states_list)
    init_state = list(nx_prod_mdp.graph['initial'])[0]
    idx_init_state = states_list.index(init_state)

    prod_mdp_nm_file.write('x: [0..%d] init %d;\n' %(no_of_states, idx_init_state))

    act_cost = dict()
    # example : [act] x=0 -> 0.8:(x'=0) + 0.2:(x'=1);
    for f_s in nx_prod_mdp.nodes():
        idx_f_s = states_list.index(f_s)
        for act in nx_prod_mdp.node[f_s]['act']:
            prod_mdp_nm_file.write('[%s] x=%d -> ' %(str(act), idx_f_s))
            k = 0
            for t_s in nx_prod_mdp.successors_iter(f_s):
                idx_t_s = states_list.index(t_s)
                prob_cost = nx_prod_mdp.edge[f_s][t_s]['prop']
                # edge label ['prop'],
                # dict of trans. prob and cost over different actions
                # fixed
                if act in prob_cost:
                    prob, cost = prob_cost[act]
                    if act not in act_cost:
                        act_cost[act] = cost
                    if k == 0:
                        prod_mdp_nm_file.write("%f:(x'= %d)" %(prob,idx_t_s))
                    else:
                        prod_mdp_nm_file.write("+ %f:(x'= %d)" %(prob,idx_t_s))
                    k += 1
            prod_mdp_nm_file.write(';\n')

    prod_mdp_nm_file.write('endmodule\n')
    #----------------------------------------

    #----------------------------------------
    # label part, for accepting pairs
    prod_mdp_nm_file.write('\n')
    prod_mdp_nm_file.write('\n')
    for acc_pair in nx_prod_mdp.graph['accept']:
        k = 0
        Ip, Hp = acc_pair
        # Ip
        prod_mdp_nm_file.write('label "K%d" = '%k)
        j_Ip = 0
        for s in Ip:
            idx_s = states_list.index(s)
            if j_Ip == 0:
                prod_mdp_nm_file.write('s = %d'%idx_s)
            else:
                prod_mdp_nm_file.write('| s = %d'%idx_s)
                j_Ip += 1
        prod_mdp_nm_file.write(';\n')
        # Hp
        prod_mdp_nm_file.write('label "L%d" = '%k)
        j_Hp = 0
        for s in Hp:
            idx_s = states_list.index(s)
            if j_Hp == 0:
                prod_mdp_nm_file.write('s = %d'%idx_s)
            else:
                prod_mdp_nm_file.write('| s = %d'%idx_s)
                j_Hp += 1
        prod_mdp_nm_file.write(';\n')
        k += 1
    print('%d accepting pairs in the product automaton' %k)
    #----------------------------------------
    # cost part
    prod_mdp_nm_file.write('\n')
    prod_mdp_nm_file.write('\n')

    prod_mdp_nm_file.write('rewards\n')
    for act,cost in act_cost.items():    
        prod_mdp_nm_file.write('[%s] true : %f;\n' %(act,cost))
    prod_mdp_nm_file.write('endrewards\n')

    #----------------------------------------
    prod_mdp_nm_file.close()
    print('PRISM mdp module saved at %s_nx2prism.nm' %name)


# networkx digraph object
nx_prod_mdp = pickle.load(open('nx_prod_mdp_model.p','rb'))
prod_mdp_module_nx2prism(nx_prod_mdp)






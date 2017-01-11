# -*- coding: utf-8 -*-

import pickle

def prod_mdp_module_nx2prism(nx_prod_mdp):
    # create product mdp module file
    # product between mdp and dra
    # PRISM mdp module official example: http://www.prismmodelchecker.org/manual/ThePRISMLanguage/Example1
    name = nx_prod_mdp['name']
    prod_mdp_nm_file = open("data/%s_nx2prism.nm" %name, "w")

    prod_mdp_nm_file.write('//product mdp in PRISM language, generated from networkx digraph model \n')
    prod_mdp_nm_file.write('\n')
    
    prod_mdp_nm_file.write('mdp \n')
    prod_mdp_nm_file.write('\n')
    prod_mdp_nm_file.write('\n')

    #----------------------------------------
    # Module part
    prod_mdp_nm_file.write('module test_product_mdp \n')
    prod_mdp_nm_file.write('\n')

    # converts state names to integers 
    states_list = list(nx_prod_mdp['states'])
    no_of_states = len(states_list)
    init_state = list(nx_prod_mdp['init'])[0]
    idx_init_state = states_list.index(init_state)

    prod_mdp_nm_file.write('x: [0..%d] init %d;\n' %(no_of_states, idx_init_state))
    prod_mdp_nm_file.write('\n')
    prod_mdp_nm_file.write('\n')
    
    act_cost = dict()
    # example : [act] x=0 -> 0.8:(x'=0) + 0.2:(x'=1);
    for f_s, acts in nx_prod_mdp['state_act'].iteritems():
        idx_f_s = states_list.index(f_s)
        for act in acts:
            prod_mdp_nm_file.write('[%s] x=%d -> ' %(str(''.join(act)), idx_f_s))
            k = 0
            f_s_successors = [e[1] for e in nx_prod_mdp['edge_prop'].iterkeys() if e[0] == f_s]
            for t_s in f_s_successors:
                idx_t_s = states_list.index(t_s)
                prob_cost = nx_prod_mdp['edge_prop'][(f_s, t_s)]
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

    prod_mdp_nm_file.write('\n')
    prod_mdp_nm_file.write('\n')
    prod_mdp_nm_file.write('endmodule\n')
    #----------------------------------------

    #----------------------------------------
    # label part, for accepting pairs
    prod_mdp_nm_file.write('\n')
    prod_mdp_nm_file.write('\n')
    k = 0
    for acc_pair in nx_prod_mdp['accept']:
        Ip, Hp = acc_pair
        # Ip
        if Ip:
            prod_mdp_nm_file.write('label "K%d" = '%k)
            j_Ip = 0
            for s in Ip:
                idx_s = states_list.index(s)
                if j_Ip == 0:
                    prod_mdp_nm_file.write('x = %d'%idx_s)
                else:
                    prod_mdp_nm_file.write('| x = %d'%idx_s)
                j_Ip += 1
            prod_mdp_nm_file.write(';\n')
        # Hp
        if Hp:
            prod_mdp_nm_file.write('label "L%d" = '%k)
            j_Hp = 0
            for s in Hp:
                idx_s = states_list.index(s)
                if j_Hp == 0:
                    prod_mdp_nm_file.write('x = %d'%idx_s)
                else:
                    prod_mdp_nm_file.write('| x = %d'%idx_s)
                j_Hp += 1
            prod_mdp_nm_file.write(';\n')
        k += 1
    print('--------------------')
    print('%d accepting pairs in the product automaton' %k)
    #----------------------------------------
    # cost part
    prod_mdp_nm_file.write('\n')
    prod_mdp_nm_file.write('\n')

    prod_mdp_nm_file.write('rewards\n')
    prod_mdp_nm_file.write('\n')
    for act,cost in act_cost.items():    
        prod_mdp_nm_file.write('[%s] true : %f;\n' %(''.join(act),cost))
    prod_mdp_nm_file.write('\n')
    prod_mdp_nm_file.write('\n')
    prod_mdp_nm_file.write('endrewards\n')
    prod_mdp_nm_file.write('\n')

    #----------------------------------------
    prod_mdp_nm_file.close()
    print('PRISM mdp module saved at data/%s_nx2prism.nm' %name)


# networkx digraph object
nx_prod_mdp = pickle.load(open('data/nx_prod_mdp_model.p','rb'))
prod_mdp_module_nx2prism(nx_prod_mdp)






# -*- coding: utf-8 -*-

import pickle

def dra_module_nx2prism(nx_dra):
    # create product mdp module file
    # product between mdp and dra
    # PRISM mdp module official example: https://github.com/prismmodelchecker/prism-tests/blob/master/functionality/verify/mdps/ltl/running-ltl2.nm
    
    name = nx_dra['name']
    dra_nm_file = open("data/%s_nx2prism.nm" %name, "w")

    dra_nm_file.write('//dra in PRISM language, generated from networkx digraph model \n')
    dra_nm_file.write('// This is encoded as a PRISM module to allow action-based LTL \n')
    dra_nm_file.write('// model checking: PRISM only supports state-based LTL currently \n')
    dra_nm_file.write('\n')
    
    dra_nm_file.write('mdp \n')
    dra_nm_file.write('\n')
    dra_nm_file.write('\n')

    #----------------------------------------
    # Module part
    dra_nm_file.write('module test_dra \n')
    dra_nm_file.write('\n')

    # converts state names to integers 
    states_list = list(nx_dra['states'])
    no_of_states = len(states_list)
    init_state = list(nx_dra['init'])[0]
    idx_init_state = states_list.index(init_state)

    dra_nm_file.write('q: [0..%d] init %d;\n' %(no_of_states, idx_init_state))
    dra_nm_file.write('\n')
    dra_nm_file.write('\n')
    
    # example : [go] q=0 -> (q'=0);
    symbols = nx_dra['symbols']
    for e,guard in nx_dra['edge_guard'].iteritems():
        f_s, t_s = e
        idx_f_s = states_list.index(f_s)
        idx_t_s = states_list.index(t_s)
        for guard_string in guard:
            act_string = ''
            for k, ap in enumerate(symbols):
                if guard_string[k] == '1':
                    act_string +='%s_1_'%str(ap)
                elif guard_string[k] == '0':
                    act_string += '%s_0_'%str(ap)
            dra_nm_file.write("[%s] q=%d -> (q'=%d);\n" %(str(''.join(act_string)), idx_f_s, idx_t_s))

    dra_nm_file.write('\n')
    dra_nm_file.write('\n')
    dra_nm_file.write('endmodule\n')
    #----------------------------------------


    #----------------------------------------
    # label part, for accepting pairs
    dra_nm_file.write('\n')
    dra_nm_file.write('\n')
    k = 0
    for acc_pair in nx_dra['accept']:
        Ip, Hp = acc_pair
        # Ip
        if Ip:
            dra_nm_file.write('label "K%d" = '%k)
            j_Ip = 0
            for s in Ip:
                idx_s = states_list.index(s)
                if j_Ip == 0:
                    dra_nm_file.write('q = %d'%idx_s)
                else:
                    dra_nm_file.write('| q = %d'%idx_s)
                j_Ip += 1
            dra_nm_file.write(';\n')
        # Hp
        if Hp:
            dra_nm_file.write('label "L%d" = '%k)
            j_Hp = 0
            for s in Hp:
                idx_s = states_list.index(s)
                if j_Hp == 0:
                    dra_nm_file.write('q = %d'%idx_s)
                else:
                    dra_nm_file.write('| q = %d'%idx_s)
                j_Hp += 1
            dra_nm_file.write(';\n')
        k += 1
    print('--------------------')
    print('%d accepting pairs in the product automaton' %k)
    
    dra_nm_file.close()
    print('PRISM mdp module saved at data/%s_nx2prism.nm' %name)


# networkx digraph object
nx_dra = pickle.load(open('data/nx_dra_model.p','rb'))
dra_module_nx2prism(nx_dra)






# Bouchacourt and Buschman 2019
# A Flexible Model of Working Memory

from FlexibleWM import *
for curr_iter in range(2):
    dictionnary = {'specific_load': True, 'Number_of_trials': 256*3, 'name_simu': 'Sim{}'.format(curr_iter+1)} # Add here any parameter you want to change from default. Defaults values are at the beginning of FlexibleWM.py
    MyModel = FlexibleWM(dictionnary)
    MyModel.run_a_trial() 
    gcPython.collect() 

# dictionnary = {'specific_load': True, 'Number_of_trials': 2, 'name_simu': 'tmp'} # Add here any parameter you want to change from default. Defaults values are at the beginning of FlexibleWM.py
# 'create_a_specific_network':True
# MyModel = FlexibleWM(dictionnary)
# MyModel.run_a_trial() 
# gcPython.collect() 
# if you want to create a specific network first, you can call MyModel.initialize_weights() with a dictionnary including 'create_a_specific_network':True ; then calling MyModel.run_a_trial() using a dictionnary including 'same_network_to_use':True 


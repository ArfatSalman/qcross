import os
from json import loads

PATH = 'data/qmt-cirq-permutations/exec-metadata'

files = os.listdir(PATH)

for file in files:
    f = file.split('.')[0]
    content = loads( open( 'data/qmt-cirq-permutations/exec-metadata/' + file ).read() )
    div = content['divergence']
    if div['ks_qiskit_cirq']['statistic'] == 0:
        continue
    print(f'python search_GA.py --prog {f} --max_eval 4000 --pop_size 20 --offspring_size 40')
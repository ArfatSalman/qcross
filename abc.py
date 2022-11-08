import os

from transpiler import CirqCircuit

path = "data/qmt_v55/programs/source/"
cirq_folder_path = "data/qmt_v55/programs/cirq/"

files = os.listdir(path)

for file_path in files:
    with open(path + file_path) as file:
        print(f'opening {file_path}')
        content = file.read()
        cirq_filepath = cirq_folder_path + f"{file_path.split('.')[0]}_cirq.py"
        with open(cirq_filepath, 'w') as cirq_file:
            cirq_file.write(CirqCircuit.from_qiskit_source(content))


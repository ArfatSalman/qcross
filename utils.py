import os

paths = [
    'data/qmt_v52/programs/source',
    'data/qmt_v53/programs/source',
    'data/qmt_v54/programs/source',
    'data/qmt_v55/programs/source',
    'data/qmt_v56/programs/source'
]

def get_qiskit_content_by_program_id(prog_id):
    for folder in paths:
        files = os.listdir(folder)
        filename = prog_id + '.py'
        if filename in files:
            return open(folder + '/' + filename , encoding='ascii').read()

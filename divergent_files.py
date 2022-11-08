from json import loads
from termcolor import colored
import os


exec_metadata_path = "data/qmt-cirq/exec-metadata/"

def scan_for_divergence(
    alpha_level: float = 0.05,
    method="holm",
):
    files = os.listdir(exec_metadata_path)
    for filename in files:
        fullpath = exec_metadata_path + filename
        data = loads(open(fullpath).read())
        if data['divergence']['ks']['p-value'] < alpha_level:
            print(colored(filename, 'red'))

if __name__ == '__main__':
    scan_for_divergence()
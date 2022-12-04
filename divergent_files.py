from json import loads
from termcolor import colored
import os


exec_metadata_path = "data/qmt-cirq/exec-metadata/"
# exec_metadata_path = "data/qmt-cirq-old-pre-transform/exec-metadata/"


def scan_for_divergence(
    alpha_level: float = 0.05,
    method="holm",
):
    files = os.listdir(exec_metadata_path)
    result = { "subset": [], "generic": []}
    count = 0
    for filename in files:
        fullpath = exec_metadata_path + filename
        data = loads(open(fullpath).read())
        for key in data["divergence"]:
            if key == "js":
                print(fullpath)
            if data["divergence"][key]["p-value"] < alpha_level:
                # print(colored(filename, "red"))
                count += 1
                result["generic"].append(filename)
        if data.get('subset_metadata'):
            # print(colored(f"SUBSET {filename}", "blue"))
            result["subset"].append(filename)
    return result


if __name__ == "__main__":
    print(colored(f"PATH = {exec_metadata_path}", "green", attrs=["bold"]))
    res = scan_for_divergence()
    for r in res['subset']:
        print(r)
    print(colored(f"Divergent Files = {len(res['subset'])}", "yellow", attrs=["bold"]))
    print(colored(f"Total Files = {len(os.listdir(exec_metadata_path))}", "red", attrs=["bold"]))

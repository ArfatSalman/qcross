import os

folders = os.listdir("qcross-data/completed-execs")

for folder in folders:
    if os.path.exists(
        os.path.join("qcross-data/completed-execs", folder, "exec-metadata.json")
    ):
        continue
    print("Removing ", folder)
    os.system("rm -rf qcross-data/completed-execs/" + folder)

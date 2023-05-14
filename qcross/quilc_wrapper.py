import subprocess

QUILC = None


def restart_quilc():
    global QUILC
    if QUILC is not None:
        print("Killing QUILC")
        QUILC.kill()
        QUILC.terminate()
        QUILC.wait()
    print("Creating a new QUILC")
    QUILC = subprocess.Popen(
        [
            "quilc",
            "-S",
            "--quiet",
            "--prefer-gate-ladders",
            "--log-level",
            "notice",
            "--protoquil",
            "--enable-state-prep-reductions",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT,
    )
    return QUILC

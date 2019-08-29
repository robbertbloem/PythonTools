"""
This script is a roundabout way of installing updates to modules.

Without this script, use `pip list --outdated` to see the outdated modules and then upgrade using `python -m pip install Package --upgrade`. This automates that process. 




"""

import subprocess

freeze = subprocess.check_output(["pip", "freeze"])
list = subprocess.check_output(["pip", "list", "--outdated"])

list = str(list)
freeze = str(freeze)
freeze = str.split(freeze[2:-1], r"\r\n")
packages = []
for f in freeze[:-1]:
    packages.append(str.split(f, "==")[0])

for p in packages:
    if p in list:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', p, "--upgrade"])


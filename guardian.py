import subprocess
import sys

result = subprocess.run([
    sys.executable, "-m", "checkov.main",
    "-f", sys.argv[1],
    "--framework", "terraform",
    "--check", "CKV_AWS_20,CKV2_AWS_6"
])

if result.returncode == 0:
    print("Safe to deploy")
else:
    print("Deployment blocked: fix the issues first")
# my_pinterest.py
import subprocess

try:
    subprocess.run(["google-chrome", "--version"], check=True)
except subprocess.CalledProcessError:
    print("Google Chrome not found - Install Google Chrome to run!")
else:
    subprocess.run(["node", "server.js"])

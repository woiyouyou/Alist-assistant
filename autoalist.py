#  encoding = 'utf-8'
import subprocess
import win32process
from subprocess import Popen
from win32process import CREATE_NO_WINDOW

p1 = subprocess.Popen('I:\\Alist\\alist server')  # 打开Alist server
p2 = subprocess.Popen('I:\\RaiDrive\\RaiDrive.exe')  # 打开RaiDrive
win32process.CREATE_NO_WINDOW('I:\\RaiDrive\\RaiDrive.exe')

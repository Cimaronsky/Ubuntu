#!/usr/bin/python
# Author @nu11secur1ty
import os
os.system("apt update -y")
os.system("apt upgrade -y")
os.system("apt dist-upgrade -y")
os.system("apt --fix-broken install -y")
os.system("apt autoremove -y")
os.system("do-release-upgrade")

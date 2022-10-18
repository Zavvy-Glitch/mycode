#!/usr/bin/env python3
""" DocString """

import shutil
import os

# moves location into the working directory
os.chdir("/home/student/mycode/")

# copies fileX to fileY
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

# copies entire directoryX to directoryY
os.system("rm -rf /home/student/mycode/5g_research_backup/")
shutil.copytree("5g_research/", "5g_research_backup/")



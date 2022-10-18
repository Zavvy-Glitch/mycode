#!/usr/bin/env python3

""" TLG Cohort D23 | CChea
    DocString """

import shutil
import os


def main():
    
    # sets the present working directory
    os.chdir('/home/student/mycode/')

    # will move source object into chosen directory
    shutil.move('raynor.obj', 'ceph_storage/')
    
    # this line will pause the execution for user input and store it into xname variable
    xname = input('What is the new name for kerrigan.obj? ')
    
    # will move kerrigan.obj into directory ceph_storage/ with name from xname variable
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main()

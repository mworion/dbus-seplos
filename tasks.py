############################################################
# -*- coding: utf-8 -*-
#
#  o-o   o--o  o   o  o-o
#  |  \  |   | |   | |
#  |   O O--o  |   |  o-o
#  |  /  |   | |   |     |
#  o-o   o--o   o-o  o--o
#
#
#   o-o  o--o o--o  o     o-o   o-o
#  |     |    |   | |    o   o |
#   o-o  O-o  O--o  |    |   |  o-o
#      | |    |     |    o   o     |
#  o--o  o--o o     O---o o-o  o--o
#
# python-based service for victron cerbo > v3.00
#
# (c) 2024 by mworion
# Licence MIT
#
###########################################################

from invoke import task
from PIL import Image
import glob
import time
import os
import zipapp
import zipfile

rn = ''
#
# defining all necessary virtual client login for building over all platforms
#

def runMW(c, param):
    c.run(param)


def printMW(param):
    print(param)


@task
def log(c):
    runMW(c, 'python3 logViewer.py')

@task
def image_res(c):
    printMW('changing image resolution for docs to 150 dpi')
    files = glob.glob('./doc/source/**/*.png', recursive=True)
    for file in files:
        print(file)
        im = Image.open(file)
        im.save(file, dpi=(150, 150))
    printMW('changing image resolution for docs to 150 dpi finished\n')


@task
def version_doc(c):
    printMW('changing the version number to setup.py')

    # getting version of desired package
    with open('./dbus-seplos/src/seplos_utils.py', 'r') as setup:
        text = setup.readlines()

    for line in text:
        if line.strip().startswith('DRIVER_VERSION'):
            _, number, _ = line.split("'")

    # reading configuration file
    with open('./doc/source/conf.py', 'r') as conf:
        text = conf.readlines()
    textNew = list()

    print(f'version is >{number}<')

    # replacing the version number
    for line in text:
        if line.startswith('version'):
            line = f"version = '{number}'\n"
        if line.startswith('release'):
            line = f"release = '{number}'\n"
        textNew.append(line)

    # writing configuration file
    with open('./doc/source/conf.py', 'w+') as conf:
        conf.writelines(textNew)
    printMW('changing the version number to setup.py finished\n')


@task(pre=[version_doc])
def make_pdf(c):
    drawio = '/Applications/draw.io.app/Contents/MacOS/draw.io'
    printMW('Generate PDF for distro')
    for fullFilePath in glob.glob('./doc/**/**.drawio', recursive=True):
        output = fullFilePath[:-6] + 'png'
        command = f'{drawio} -x -f png -o {output} {fullFilePath}'
        runMW(c, command)
    with c.cd('doc'):
        runMW(c, 'make latexpdf')
    printMW('Generation finished\n')


@task(pre=[version_doc])
def make_html(c):
    drawio = '/Applications/draw.io.app/Contents/MacOS/draw.io'
    printMW('Generate HTML for distro')
    for fullFilePath in glob.glob('./doc/**/**.drawio', recursive=True):
        output = fullFilePath[:-6] + 'png'
        command = f'{drawio} -x -f png -o {output} {fullFilePath}'
        runMW(c, command)
    with c.cd('doc'):
        runMW(c, 'make html')
    with c.cd('docs'):
        runMW(c, 'rm -rf *')
        runMW(c, 'rm -rf .nojekyll')
        runMW(c, 'rm -rf .buildinfo')
    with c.cd('doc/build'):
        runMW(c, 'mv html/* ../../docs')
        runMW(c, 'mv html/.nojekyll ../../docs')
        runMW(c, 'mv html/.buildinfo ../../docs')
    printMW('Generation finished\n')


@task(pre=[make_pdf, make_html])
def show_doc(c):
    with c.cd('docs'):
        runMW(c, 'open ./index.html')
    runMW(c, 'open ./mw4/resource/data/mountwizzard4.pdf')

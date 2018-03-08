#!/usr/bin/python3
# -*- coding: utf-8 -*-

import subprocess
import argparse

parser = argparse.ArgumentParser(prog="verdom")
parser.add_argument("-p", action="store_true", help="Ping um ip")

args = parser.parse_args()
#if args.p:
#    ip = input("Informe o ip/host: ")
#    print(ip)
#    subprocess.run(['ping', '-c4', ip])

def app():
    if args.p:
        ip = input("Informe o ip/host: ")
        search = subprocess.call(['ping', '-c4', ip])
        print(search)


app()

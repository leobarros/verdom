#!/usr/bin/python3
# -*- coding: utf-8 -*-

import subprocess
import argparse

parser = argparse.ArgumentParser(prog="verdom")
parser.add_argument("-p", action="store_true", help="Ping um ip")
parser.add_argument('-d', action="store_true", help="Checar dados de um domínio")

args = parser.parse_args()

def app():
    if args.p:
        ip = input("Informe o ip/host: ")
        subprocess.call(['ping', '-c4', ip])

    if args.d:
        dominio = input("Informe um dominio: ")
        print("\n***MX***")
        subprocess.call(['host', '-t', 'mx', dominio])

        print("\n***Name Server***")
        subprocess.call(['host', '-t', 'NS', dominio])

        print("\n***IPV4***")
        subprocess.call(['host', '-t' 'A', dominio])

        print("\n***IPV6***")
        subprocess.call(['host', '-t', 'AAAA', dominio])

        print("\n***TXT***")
        subprocess.call(['host', '-t', 'TXT', dominio])

        print("\n***SPF***")
        subprocess.call(['host', '-t', 'SPF', dominio])



app()

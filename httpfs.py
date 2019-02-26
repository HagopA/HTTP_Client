# Written by: Hagop Awakian
# Student ID: 27747632
# Lab Assignment #2
# Instructor: Dr. Abdelwahab Elnaka
# For COMP 445 Section W
# Winter 2019
# Date Submitted: Sunday March 3 2019

import argparse
import os
import socket

DEFAULT_PORT = 8080
DEFAULT_DIRECTORY = os.getcwd()

parser = argparse.ArgumentParser(description='httpfs is a simple file server.')
# parser.add_argument('command', type=str, choices=['get', 'post'])
parser.add_argument('-v', help='Prints debugging messages.', action='store_true')
parser.add_argument('-p', help='Specifies the port number that the server will listen and serve at. Default is 8080.',
                    type=int, nargs='?', metavar='PORT')
parser.add_argument('-d', help='Specifies the directory that the server will use to read/write requested files. '
                               'Default is the current directory when launching the application.', type=str, nargs='?',
                    metavar='PATH-TO-DIR')
args = parser.parse_args()

if not args.p:
    args.p = DEFAULT_PORT

if not args.d:
    args.d = DEFAULT_DIRECTORY

files_in_directory = os.listdir(args.d)
print(files_in_directory)

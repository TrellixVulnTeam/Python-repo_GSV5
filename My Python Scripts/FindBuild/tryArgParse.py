import argparse
import glob
import time

parser = argparse.ArgumentParser(description='A versatile script with optional positional argument')

parser.add_argument('product', type=str, nargs='?', default='Enterprise',
		help='the product type, Invincea Enterprise or Dell protected workspace')

parser.add_argument('build_number', type=str, nargs='?', default='latest',
		help='the product build number, default is the latest build when not specified')

parser.add_argument('-c', '--copy', action='store_true', default=None,
		help='copy the build folder to desktop')

parser.add_argument('-l', '--latest', action='store_true', default=None,
		help='check for the latest build via time stamp')

group = parser.add_mutually_exclusive_group()

group.add_argument('-i', '--install', action='store_true', default=None,
		help='install the product build automatically')

group.add_argument('-u', '--upgarde', action='store_true', default=None,
		help='upgrade to the specified product build')

args = parser.parse_args()	#parse the arguments

#src_folder = '\\\\beaver\\Builds\\'
print args.build_number
print args.product

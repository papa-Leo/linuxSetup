from os import system, environ
from os.path import exists

HOME = environ['HOME']

def main():
	system('pip3 install fontTools -qqq')

	if not exists(f'{HOME}/.ossetup'):
		system(f'mkdir {HOME}/.ossetup/ && cd {HOME}/.ossetup && mkdir fonts/ && mkdir assets/icons/ assets/configFiles/ assets/wallpapers/ assets/archives/')

	print('\nPut your prefered monospace font family in the ~/.ossetup/fonts/ directory, then run go.py with sudo.')
	

main()
from os import system, environ
from os.path import exists

HOME = environ['HOME']

def main():
	system('sudo apt install python3-pip -y -qqq')
	system('pip3 install fontTools -qqq')

	if not exists(f'{HOME}/.ossetup'):
		system(f'mkdir {HOME}/.ossetup/ && cd {HOME}/.ossetup && mkdir {HOME}/.ossetup/fonts/ && {HOME}/.ossetup/mkdir {HOME}/.ossetup/assets/icons/ {HOME}/.ossetup/assets/configFiles/ {HOME}/.ossetup/assets/wallpapers/ {HOME}/.ossetup/assets/archives/')

	print('\nPut your prefered monospace font family in the ~/.ossetup/fonts/ directory, then run go.py with sudo.')
	

main()
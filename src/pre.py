from os import system, environ
from os.path import exists

HOME = environ['HOME']

def main():
	print(f'Preparing environment...\n')
	system('sudo apt install python3-pip -y -q')
	system('pip3 install -qq -r requirements.txt')

	if not exists(f'{HOME}/.ossetup'):
		system(f'mkdir {HOME}/.ossetup/ && mkdir {HOME}/.ossetup/fonts/ {HOME}/.ossetup/assets/ {HOME}/.ossetup/assets/icons/ {HOME}/.ossetup/assets/configFiles/ {HOME}/.ossetup/assets/wallpapers/ {HOME}/.ossetup/assets/archives/')

	print('\nYou can now run go.py')
	# print('\nPut your prefered monospace font family in the ~/.ossetup/fonts/ directory, then run go.py with sudo.')
	 

main()
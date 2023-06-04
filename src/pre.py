from os import system
from os.path import exists

def main():
	home = '/home/' + input('What is your home path? /home/')

	if not exists(f'{home}/.ossetup'):
		system(f'mkdir {home}/.ossetup/ && cd {home}/.ossetup && mkdir fonts/')
	elif not exists(f'{home}/.ossetup/fonts/'):
		system(f'cd {home}/.ossetup && mkdir fonts/')
	else:
		system(f'cd {home}/.ossetup')

	print('\nPut your prefered monospace font-family in the ~/.ossetup/fonts/ directory, then run go.py with sudo.')
	

main()
from os import system
from os.path import exists

def main():
	if not exists('/home/papaleo/.ossetup'):
		system('mkdir ~/.ossetup/ && cd ~/.ossetup && mkdir fonts/')
	elif not exists('/home/papaleo/.ossetup/fonts/'):
		system('cd ~/.ossetup && mkdir fonts/')
	else:
		system('cd ~/.ossetup')

	print('\nPut your prefered monospace font-family in the ~/.ossetup/fonts/ directory.')
	print('Run go.py with sudo')
	

main()
from os import system
import fontConfig
home = '~'

def main():
	system('echo WELCOME TO THE LINUX SETUP CLI')
	print('Please ensure you\'ve run the pre.py script before this one')
	system('cd ~/.ossetup')

	home = '/home/' + input('What is your home path? /home/')
	answer = input('Setup default Papa Leo OS? [y/n] ')
	ynMethods(answer, defaultLeoSetup, customSetup)

def defaultLeoSetup():
	print('Leo')

def customSetup():
	ynMethods(input('Is your pre-selected font a NerdFont? [y/n] '), fontConfig.installFont(home), fontConfig.patchFont(home))

# this method takes Y/N user input and executes a given method
def ynMethods(answer, yesMethod, noMethod):
	if answer == 'y' or answer == 'Y':
		yesMethod()
	elif answer == 'n' or answer == 'N':
		noMethod()
	else:
		answer = input('Invalid option, try again: ')
		ynMethods(answer, yesMethod, noMethod)

# this method takes Y/N user input and returns a given value
def ynOptions(answer, yesOption, noOption):
	if answer == 'y' or answer == 'Y':
		return yesOption
	elif answer == 'n' or answer == 'N':
		return noOption
	else:
		answer = input('Invalid option, try again: ')
		return ynOptions(answer, yesOption, noOption)

def ret():
	return

main()
from os import system
import fontConfig, apps, term
home = '~'

def main():
	system('echo WELCOME TO THE LINUX SETUP CLI')
	print('Please ensure you\'ve run pre.py before this one')

	home = '/home/' + input('What is your home path? /home/')
	system('echo "Updating repositories... " && sudo apt update && Done')
	system('echo -n "Installing wget & curl..." && sudo apt install wget > /dev/null 2>&1 && sudo apt install curl > /dev/null 2>&1 && echo Done')
	answer = input('Setup default Papa Leo OS? [y/n] ')
	ynMethods(answer, defaultLeoSetup, customSetup)

def defaultLeoSetup():
	print('Leo')

def customSetup():
	# install nerd fonts
	print()
	ynMethods(input('Is your pre-selected font a NerdFont? [y/n] '), fontConfig.installFont(home), fontConfig.patchFont(home))
	
	# install browsers
	print()
	ynMethods(input('Would you like to choose some browsers to install? [y/n] '), apps.browsers, ret)

	# install apps
	print()
	ynMethods(input('Would you like to choose some apps to install? [y/n] '), apps.apps, ret)

	# configure gnome-terminal
	print()
	if ynOptions(input('Would you like to choose some apps to install? [y/n] '), True, False):
		print('Find the name of your gnome-terminal dconf profile. Use "dconf dump /org/gnome/terminal/legacy/profiles:/:" and press tab. Paste the profile here:')
		term.configureTerminal(input('.../profiles:/:'))

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
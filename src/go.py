import os
from os import system
import fontConfig, apps, term, gnome

# get system information
HOME = os.environ['HOME']
USER = os.environ['USER']

def main():
	# welcome message
	system('echo WELCOME TO THE LINUX SETUP CLI')
	print('Please ensure you\'ve run pre.py before this')

	# install some dependencies
	system('echo "Updating repositories... " && sudo apt -qq update && echo Done')
	system('echo -n "Installing wget & curl..." && sudo apt install wget > /dev/null 2>&1 && sudo apt install curl > /dev/null 2>&1 && echo Done')

	# begin setup
	answer = input('Setup default PalOS? [y/n] ')
	ynMethods(answer, defaultPalOS(), customSetup())

def defaultPalOS():
	print('Papa Leo')

def customSetup():
	# install nerd fonts
	print()
	ynMethods(input('Is your pre-selected font a NerdFont? [y/n] '), fontConfig.installFont(HOME), fontConfig.patchFont(HOME))

	# choose main monospace font
	FONT = fontConfig.chooseDefaultFont(HOME)

	# install zsh
	print()
	ynMethods(input('Would you like to install zsh with oh-my-zsh? [y/n] '), term.installZSH(HOME), ret())

	# configure gnome-terminal
	print()
	term.configureTerminal(HOME, input('Please enter a terminal profile UUID: '), FONT)

	# install CLIs
	print()
	term.installCLIs(HOME)

	# install browsers
	print()
	ynMethods(input('Would you like to choose some browsers to install? [y/n] '), apps.browsers(), ret())

	# install apps
	print()
	ynMethods(input('Would you like to choose some apps to install? [y/n] '), apps.apps(), ret())
	ynMethods(input('Would you like the Spicetify client for Spotify? [y/n] '), apps.installSpicetify(), ret())

	# install and configure gnome-tweaks
	print()
	ynMethods(input('Would you like to install gnome-tweaks? [y/n] '), gnome.tweaks(), ret())

# this method takes Y/N user input and executes a given method
def ynMethods(answer, yesMethod, noMethod):
	if answer == 'y' or answer == 'Y':
		yesMethod()
	elif answer == 'n' or answer == 'N':
		noMethod()
	else:
		answer = input('Invalid option, try again: ')
		ynMethods(answer, yesMethod, noMethod)

# this method takes Y/N user input and ret()urns a given value
def ynOptions(answer, yesOption, noOption):
	if answer == 'y' or answer == 'Y':
		return yesOption
	elif answer == 'n' or answer == 'N':
		return noOption
	else:
		answer = input('Invalid option, try again: ')
		return ynOptions(answer, yesOption, noOption)

# thos method gets user choice within a number range
def getUserChoice(low, hi):
	userChoice = int(input(f'Choose an option [{low}-{hi}]: '))
	if userChoice >= low and userChoice <= hi:
		return userChoice
	else:
		print('Invalid option, please try again.')
		getUserChoice(low, hi)

def ret():
	return

main()
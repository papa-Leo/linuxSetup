from os import system
import fontConfig, apps, term, gnome, gradient_figlet

gradient_figlet.print_with_gradient_figlet('ubuntu setup', 'slant', gradient_figlet.Color('#ff5f6d'), gradient_figlet.Color('#ffc371'))

# get system information
USER = input('Hello! What is your username? ')
HOME = '/home/' + USER

def main():
	# welcome message
	print(f'\nWelcome to the Ubuntu Setup Script, {USER}! Please ensure you\'ve run pre.py before this')

	print(f'\nYour home directory: {HOME}\n')

	# install some dependencies
	# system('echo "Updating repositories... " && sudo apt -q update && echo Done')
	# system('echo -n "Installing wget & curl..." && sudo apt install wget -q -y && sudo apt install curl -q -y && echo Done')

	# begin setup
	answer = input('Setup default PalOS? [y/n] ')
	ynMethods(answer, defaultPalOS, customSetup, [], [])

def defaultPalOS():
	print('Papa Leo')

def customSetup():
	# install nerd fonts
	print()
	ynMethods(input('Is your pre-selected font a NerdFont? [y/n] '), fontConfig.installFont, fontConfig.patchFont, [HOME], [HOME])

	# choose main monospace font
	FONT = fontConfig.chooseDefaultFont(HOME)

	# install zsh
	print()
	ynMethods(input('Would you like to install zsh with oh-my-zsh? [y/n] '), term.installZSH(HOME), ret(), [HOME], [])

	# configure gnome-terminal
	print()
	term.configureTerminal(HOME, input('Please enter a terminal profile UUID: '), FONT)

	# install CLIs
	print()
	term.installCLIs(HOME)

	# install browsers
	print()
	ynMethods(input('Would you like to choose some browsers to install? [y/n] '), apps.browsers(), ret(), [], [])

	# install apps
	print()
	ynMethods(input('Would you like to choose some apps to install? [y/n] '), apps.apps(), ret(), [], [])
	ynMethods(input('Would you like the Spicetify client for Spotify? [y/n] '), apps.installSpicetify(), ret(), [], [])

	# install and configure gnome-tweaks
	print()
	ynMethods(input('Would you like to install gnome-tweaks? [y/n] '), gnome.tweaks(), ret(), [], [])

# this method takes Y/N user input and executes a given method
def ynMethods(answer, yesMethod, noMethod, yesArgs, noArgs):
	while True:
		if answer.lower() in ['y', 'yes']:
			yesMethod(*yesArgs)
			break
		elif answer.lower() in ['n', 'no']:
			noMethod(*noArgs)
			break
		else:
			answer = input('Invalid option, choose yes or no: ')

# this method takes Y/N user input and returns a given value
def ynOptions(answer, yesOption, noOption):
	while True:
		if answer.lower() in ['y', 'yes']:
			return yesOption
		elif answer.lower() in ['n', 'no']:
			return noOption
		else:
			answer = input('Invalid option, choose yes or no: ')

# this method gets user choice within a number range
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
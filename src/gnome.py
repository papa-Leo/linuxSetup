import os
from os import system

def tweaks():
	system('echo -n "Installing gnome-tweaks... "')
	system('sudo apt -qq install gnome-tweaks -y')
	system('echo Done')
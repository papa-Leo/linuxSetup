from os import system

def browsers():
	print('Please select which browser/s you would like to install:')
	print('Brave: b | Chrome: c | Edge: e | Firefox: f')
	b = input('Type character/s of selected browser/s, or blank for none: ')

	system('echo "Installing browser/s... "')
	for char in b:
		match char:
			case 'b':
				system('sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg')
				system('echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list')
				system('sudo apt update && sudo apt install brave-browser -y')
			case 'c':
				system('wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb')
				system('sudo dpkg -i google-chrome-stable_current_amd64.deb')
			case 'e':
				system("curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg && sudo install -o root -g root -m 644 microsoft.gpg /etc/apt/trusted.gpg.d/ && sudo sh -c 'echo \"deb [arch=amd64] https://packages.microsoft.com/repos/edge stable main\" > /etc/apt/sources.list.d/microsoft-edge-dev.list' && sudo rm microsoft.gpg")
				system('sudo apt install microsoft-edge-stable -y')
			case 'f':
				system('sudo apt install firefox -y')
	system('echo "" && echo Browser/s installed!')
			

def apps():
	print('Please select which apps you would like to install:')
	print('Spotify: s | Discord: d | VS Code: c | VLC: v')
	a = input('Type character/s of selected app/s, or blank for none: ')

	system('echo "Installing app/s... "')
	for char in a:
		match char:
			case 's':
				system('sudo apt install spotify-client -y')
			case 'd':
				system('sudo snap install discord')
			case 'c':
				system('sudo apt install code -y')
			case 'v':
				system('sudo apt install vlc -y')
	system('echo "" && echo App/s installed!')
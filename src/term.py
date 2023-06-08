from os import system

def configureTerminal(HOME, profile, FONT):
	dconfPath = f'/org/gnome/terminal/legacy/profiles:/:{profile}/'
	system(f'dconf load {dconfPath} < {HOME}/programming/linuxSetup/assets/configFiles/term.config > /dev/null 2>&1')
	system(f'dconf write {dconfPath}font "\'{FONT} 20\'"')

def installZSH(HOME):
	system('echo -n "Installing zsh... " && sudo apt -qqq install zsh -y && echo Done')
	system('echo -n "Installing oh-my-zsh... " && sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -q -)" && echo Done')
	# config file for zsh
	system(f'cp {HOME}/.ossetup/assets/configFiles/.zshrc {HOME}/')

	# install omz plugins
	system('echo -n "Installing plugins... "')
	system('sudo apt -qqq install fzf thefuck -y && echo Done')

	# install powerlevel10k
	system(f'echo -n "Installing powerlevel10k theme... " && git clone -q --depth=1 https://github.com/romkatv/powerlevel10k.git {HOME}/.oh-my-zsh/themes/powerlevel10k && echo Done')

def installCLIs(HOME):
	system('echo -n "Installing CLIs... "')
	# add repository for speedtest cli
	system('curl -s https://packagecloud.io/install/repositories/ookla/speedtest-cli/script.deb.sh | sudo bash > /dev/null 2>&1')
	# ocs-url
	system(f'sudo apt -qqq install libqt5svg5 qml-module-qtquick-controls && sudo dpkg -i {HOME}/.ossetup/assets/debs/ocs-url_3.1.0-0ubuntu1_amd64.deb > /dev/null 2>&1')
	system('sudo apt -qqq install htop net-tools openssh-server speedtest nodejs npm ocs-url cmatrix cowsay lolcat fortune -y')
	system('pip3 install pywal -qqq')
	system('echo Done')

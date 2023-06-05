from os import system

def configureTerminal(profile, fontName):
    dconfPath = '/org/gnome/terminal/legacy/profiles:/:profile/'
    system('dconf write /background-transparency-percent 30')
    system('dconf write /bold-is-bright true')
    system('dconf write /cursor-shape \'ibeam\'')
    system('dconf write /custom-command \'zsh\'')
    system('dconf write /default-size-columns 72')
    system('dconf write /default-size-rows 24')
    system(f'dconf write /font \'{fontName} 16\'')
    system('dconf write /preserve-working-directory \'always\'')
    system('dconf write /scroll-on-output true')
    system('dconf write /use-custom-command true')
    system('dconf write /use-system-font false')
    system('dconf write /use-theme-colors false')
    system('dconf write /use-theme-transparency false')
    system('dconf write /use-transparent-background true')

def installZSH():
    system('echo -n "Installing zsh... " && sudo apt install zsh -y && echo Done')
    system('echo -n "Installing oh-my-zsh... " && sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)" && echo Done')
	
import os
from os import system

def patchFont(home):
	system('echo Installing fontforge... && sudo apt install python3-fontforge -y > /dev/null 2>&1 && echo Done')
	system(f'cd {home}/.ossetup/ && echo Downloading font-patcher... && wget https://github.com/ryanoasis/nerd-fonts/releases/latest/download/FontPatcher.zip -q && mkdir fontPatcher && unzip -q FontPatcher.zip -d fontPatcher/ && rm -f FontPatcher.zip && echo Done')
	system(f'mkdir {home}/.ossetup/fonts/patched')
	files = os.listdir(f'{home}/.ossetup/fonts/')

	print('Patching font/s; this may take a few minutes...')
	for file in files:
		if file.endswith('otf') or file.endswith('ttf'):
			system(f'python3 {home}/.ossetup/fontPatcher/font-patcher {home}/.ossetup/fonts/"{file}" -s -c -q --fontawesome --fontawesomeextension --fontlogos --octicons --codicons --powersymbols --pomicons --powerline --powerlineextra --material --weather -out {home}/.ossetup/fonts/patched/ > /dev/null 2>&1')
	
	system(f'echo Removing font-patcher && cd {home}/.ossetup/ && rm -rf fontPatcher/ && sudo apt remove python3-fontforge -y > /dev/null 2>&1')
	if not os.path.exists(f'{home}/.local/share/fonts/'):
		system(f'mkdir {home}/.local/share/fonts/')
	system(f'echo Installing patched fonts... && cd {home}/.ossetup/fonts/patched/ && cp ./* {home}/.local/share/fonts/')
	print('Done!')

def installFont(home):
	if not os.path.exists(f'{home}/.local/share/fonts/'):
		system(f'mkdir {home}/.local/share/fonts/')
	system(f'echo Installing fonts... && cd {home}/.ossetup/fonts/ && cp ./* {home}/.local/share/fonts/')

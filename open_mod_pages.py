import re
import sys
import json
# from urllib.parse import quote
import webbrowser

modpack_dir = sys.argv[1]
html_mod_list = modpack_dir + '/modlist.html'
json_file = modpack_dir + '/manifest.json'

modnames = []
with open(html_mod_list) as f:
    for line in f:
        m = re.search(r'<li><a.*>([^\(\[]+).*</a>', line)
        if m:
            modname = m.group(1).strip()
            modname = re.sub(r'[\s-]+', '-', modname).replace("'", '').lower()
            modnames.append(modname)

fileids = []
with open(json_file) as f:
    data = json.load(f)
    for data in data['files']:
        fileids.append(data['fileID'])

assert len(modnames) == len(fileids)

chrome_path = r'open -a /Applications/Google\ Chrome.app %s'

# for modname, fileid in zip(modnames, fileids):
#     url = f'https://www.curseforge.com/minecraft/mc-mods/{modname}/files/{fileid}'
#     webbrowser.get(chrome_path).open(url)

game_version = '1.16.5'
for modname, fileid in zip(modnames, fileids):
    url = f'https://www.curseforge.com/minecraft/mc-mods/{modname}/files/?version={game_version}'
    webbrowser.get(chrome_path).open(url)


# wrong game version
# better leaves 1.17
# FTBlib 1.12

# Tror FTBlib, Fancy menu og Wawla er client side mods. Dem har jeg fjernet fra serveren

# modslug = 'bookshelf'
# fileid = '2965233'
# url = f'https://www.curseforge.com/minecraft/mc-mods/{modslug}/files/{fileid}'

# import webbrowser

# #url = 'http://docs.python.org/'

# # MacOS


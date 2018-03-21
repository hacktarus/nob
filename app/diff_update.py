import os
import glob
import pandas as pd
import re
import shutil
import csv
from datetime import datetime

# on récupère la liste des items de nobuna
colnames =['title-version','title','title_zip','Sales_page_url']
lines = pd.read_csv('..\\csv\\plugin_title.csv', names=colnames)
nobuna = lines.title_zip.tolist()
nobuna.reverse()
nobuna.pop()
nobuna.reverse()
#print(nobuna)

# on récupère la liste des sales page des items de nobuna
colnames =['title-version','title','title_zip','Sales_page_url']
lines = pd.read_csv('..\\csv\\plugin_title.csv', names=colnames)
nobuna_salespage = lines.Sales_page_url.tolist()
nobuna_salespage.reverse()
nobuna_salespage.pop()
nobuna_salespage.reverse()
#print(nobuna_salespage)

# on récupère la liste des items de topgpl
os.chdir('Y:\\PROJETS\\topgpl\\plugins\\nobuna.com\\## ALL ##')
topgpl = glob.glob('*.zip')
#print(topgpl)

# on génère la liste diff avec les items présents chez nobuna et qui ne sont pas sur topgpl
diff = list(set(nobuna) - set(topgpl))
#print(diff)

# on retire les items portant le nom 'Bundle' dedans
regex = re.compile(r'Bundle')
filtered_diff =  [i for i in diff if not regex.search(i)]
print("the following items are not in topgpl.com")
print(filtered_diff)
print("\n")

# on crée une liste old_version a partir de la liste topgpl
#   pour ce faire
#       - on transforme les items diff avec version en item sans version dans une liste diff_sans_version
diff_sans_version_total = []

for i in filtered_diff:
    diff_sans_version = i.split()
    #print(diff_sans_version)
    diff_sans_version.pop()
    #print(diff_sans_version)
    diff_sans_version = ' '.join(diff_sans_version)
    #print(diff_sans_version)
    diff_sans_version_total.append(diff_sans_version) 

#print(diff_sans_version_total)
#       - on crée une liste old_version présent sur topgpl a bouger dans le folder old_version
old_version = [i for e in diff_sans_version_total for i in topgpl if e in i]
#print(old_version)

# on move les anciennes versions dans le folder old_version
print("...moving old items in the folder old_version")
for plug in old_version:
    shutil.move("..\\..\\..\\plugins\\nobuna.com\\## ALL ##\\"+plug, "..\\..\\..\\plugins\\nobuna.com\\## ALL ##\\old_version\\"+plug)
print(old_version)

# On crée un csv avec les titre des items et leur page de download sur nobuna
# on crée un dictionnaire avec les items + les url
dict_item_url = dict(zip(nobuna, nobuna_salespage))

# on en fait un nouveau dico avec seulement les nouveaux item a télécharger
dico_items_to_download = {k: dict_item_url[k] for k in set(filtered_diff) & set(dict_item_url.keys())}

# on récup la date et l'heure
i = datetime.now()
d_h = i.strftime('%Y.%m.%d-%H.%M.%S')

# on en sort un csv
print('csv creation')
with open('..\\..\\..\\py\\nob\\csv\\newItemsToDownload-'+d_h+'.csv','w') as f:
    w = csv.writer(f)
    w.writerows(dico_items_to_download.items())
print('csv created')
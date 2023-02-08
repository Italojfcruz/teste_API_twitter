#from API_consumer import ApiTwitter 
import pandas as pd
import re
#3084950638 -fred
#2936113828 - italo
from unidecode import unidecode

participantes_twitter = ['vulgofop',
'paulafreitasr_',
'cezarblackk',
'larisantosbe',
'eitarickcamargo',
'saa_aline',
'brunornogueira',
'tinacalamba',
'AlineWirley',
'caradesapatojr',
'BrunaGriphaoo',
'domitila_barros',
'fred_b12',
'NicacioFred',
'GabrielSantana',
'keyalvesoficial',
'marvvila',
'mcguime']

regex_names = ['aline',
'bruna|bruna griphao',
'fred',
'domitila',
'sapato|cara de sapato',
'fred nicacio',
'key|key alves',
'Marvvila',
'gabriel santana',
'mc guime|guime',
'paula',
'gabriel',
'cezar',
'gustavo|cowboy',
'larissa|lari',
'ricardo',
'sarah aline|sarah',
'marilia',
'cristian',
'bruno',
'tina',
'amanda']

'''
for i in range(len(participantes1)):
    print(participantes1[i],':',ApiTwitter.quant_follower(participantes1[i]))
'''

dt = pd.read_excel('dados_BBB23.xlsx')

sapato = 0
fred = 0
dt = dt['text']
for menssage in dt:
    for reg in regex_names:
        m = re.search(reg,unidecode(menssage).lower())
        if m:
        
            if m.group(0) == 'sapato':
                sapato+=1
            if m.group(0) == 'fred':
                fred+=1
print('sapato: ', sapato)            
print('fred: ', fred) 
from API_consumer import ApiTwitter 
import pandas as pd


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

'''

for i in range(len(participantes_twitter)):
    print(participantes_twitter[i],':',ApiTwitter.quant_follower(participantes_twitter[i]))
'''

print(ApiTwitter.twitter_quotes(pd.read_excel('dados_BBB23.xlsx')))
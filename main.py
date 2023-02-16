from API_consumer import ApiTwitter,Scrapper 
import pandas as pd

scrapper   =  Scrapper()
apiTwitter =  ApiTwitter()

participantes_twitter = [
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


participantes_insta = [
'paulafreitasr_',
'cezar.black',
'larisantosbe',
'eitarickcamargo',
'saa_aline',
'brunornogueira',
'tinacalamba',
'alinewirley',
'caradesapato',
'brunagriphaoo',
'domitila_barros',
'fred',
'frednicacio',
'gbielsantana',
'keyalves',
'marvvila',
'mcguime',
'mariliamakeupoficial',
'gustavo_benedetii',
'vulgofop',
'ameirelles',
'rickcamargo',
'cristianvanelli']

'''
for i in range(len(participantes_twitter)):
    print(participantes_twitter[i],':',ApiTwitter.quant_follower(participantes_twitter[i]))
'''
#ApiTwitter.twitter_quotes(pd.read_excel('dados_BBB23.xlsx')).to_excel('dados.xlsx')
#print(ApiTwitter.twitter_quotes(pd.read_excel('dados_BBB23.xlsx')))
user = participantes_twitter #['italojcruz','fred_b12']
username = ['fred']

#followers_tw= scrapper.get_follower_twitter(user)
followers= scrapper.get_followers_insta(username)

print('Instagram')
print(followers)
print('------------------------------------------')
'''
print('Twitter')
print(followers_tw)
print('------------------------------------------')
dt  = apiTwitter.get_twitter_recents()
print(apiTwitter.twitter_quotes(dt))
'''


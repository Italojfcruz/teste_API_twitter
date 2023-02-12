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


'''
for i in range(len(participantes_twitter)):
    print(participantes_twitter[i],':',ApiTwitter.quant_follower(participantes_twitter[i]))
'''
#ApiTwitter.twitter_quotes(pd.read_excel('dados_BBB23.xlsx')).to_excel('dados.xlsx')
#print(ApiTwitter.twitter_quotes(pd.read_excel('dados_BBB23.xlsx')))
user = participantes_twitter #['italojcruz','fred_b12']
username = ['fred']
#followers_tw= scrapper.get_follower_twitter(user)
#followers= scrapper.get_followers_insta(username)
#print('Instagram: ',followers)
#print('Twitter: ',followers_tw)

dt  = apiTwitter.get_twitter_recents()
#print(dt)
#print(apiTwitter.twitter_quotes(dt))
import requests
import pandas as pd
import tweepy as tw
from unidecode import unidecode
import re
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

opitions = webdriver.ChromeOptions()
opitions.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=opitions)

#credenciais
bearer_token        ='AAAAAAAAAAAAAAAAAAAAAJVblQEAAAAA8TqsBNhMkEPAcc0CDIGuUFEvhDU%3DP0BFUPVWhp3tf4OshAXQBGywj0J1e5XpTWnB4vS971qExhFNcl'
consumer_key        ='vx7SEtLVOCl2ARgg3CujiwZz0' 
consumer_secret     ='eK5718YwBRXu88aSzeI5C7IwApleQfXk9mzE8TiEZWclIjYLol' 
access_token        ='2936113828-n4E3eLCcjc8zcBEZ08aeYwKdxNYEP7E95ov50UO'
access_token_secret ='40xcsiz3D7sWudoqM3FITovMs4KID5yfBUvWsNLv7KI78'

client = tw.Client(bearer_token,consumer_key, consumer_secret, access_token, access_token_secret)

class ApiTwitter():
    def __init__(self) -> None:
         pass

    def get_twitter_recents():
        url      = 'https://api.twitter.com/2/tweets/search/recent?query=BBB23&max_results=100'
        headers  = {'Authorization':'Bearer '+bearer_token}
        response = requests.get(url,headers=headers)
        response = response.json()
        response = response['data']
        dataset_BBB23 = pd.DataFrame(response)
        print(dataset_BBB23)
        dataset_BBB23.to_excel('dados_BBB23.xlsx')
            
    def tw_get_twitter_recents():
        Client = tw.Client(bearer_token,consumer_key, consumer_secret, access_token, access_token_secret)
        response = Client.search_recent_tweets(query='BBB23',max_results=50)
        response = response.data
        for x in response:
            print(x.text)    

    def quant_follower(user):
        url_twitter   ='https://twitter.com/{user}' 
        driver.get(url_twitter)
        time.sleep(1)
        tags_tw   = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[5]/div[2]/a/span[1]')
        return tags_tw.text
    

    def twitter_quotes(dataframe):
        regex_names = ['aline',
                        'bruna|bruna griphao',
                        'fred',
                        'domitila',
                        'sapato|cara de sapato',
                        'fred nicacio',
                        'key|key alves',
                        'Marvvila',
                        'gabriel santana|mosca',
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
                        'amanda'
                        ]
        
        sapato = 0
        fred   = 0
        nicacio = 0
        aline  = 0
        bruna  = 0
        gabriel = 0
        domitila =0
        key = 0
        marvvila = 0
        guime = 0
        paula=0
        cezar = 0
        gustavo = 0
        larissa = 0
        ricardo = 0
        sarah = 0
        marilia = 0
        cristian = 0
        bruno = 0
        tina  = 0
        amanda = 0

        dataframe = dataframe['text']
        for menssage in dataframe:
            for reg in regex_names:
                match = re.search(reg,unidecode(menssage).lower())
                if match:
                    if match.group(0) == 'sapato':
                        sapato+=1
                    if match.group(0) == 'fred nicacio':
                        nicacio+=1
                    if match.group(0) == 'fred':
                        fred+=1 
                    if match.group(0) == 'bruna' or match.group(0) == 'bruna griphao':
                        bruna+=1
                    if match.group(0) == 'domitila':
                        domitila+=1
                    if match.group(0) == 'key':
                        key+=1
                    if match.group(0) == 'marvilla':
                        marvvila+=1
                    if match.group(0) == 'mc guime' or match.group(0) == 'guime':
                        guime+=1
                    if match.group(0) == 'gabriel santana' or match.group(0) == 'mosca':
                        gabriel+=1    
                    if match.group(0) == 'aline':
                        aline+=1 
                    if match.group(0) == 'paula':
                        paula+=1
                    if match.group(0) == 'cezar':
                        cezar+=1
                    if match.group(0) == 'gustavo' or match.group(0) == 'cowboy':
                        gustavo+=1
                    if match.group(0) == 'larissa':
                        larissa+=1
                    if match.group(0) == 'ricardo':
                        ricardo+=1
                    if match.group(0) == 'sarah':
                        sarah+=1
                    if match.group(0) == 'marilia':
                        marilia+=1
                    if match.group(0) == 'cristian':
                        cristian+=1
                    if match.group(0) == 'bruno':
                        bruno+=1
                    if match.group(0) == 'tina':
                        tina+=1
                    if match.group(0) == 'amanda':
                        amanda+=1
     
        quotes = {
                    'Sapato':sapato,            
                    'Fred':fred, 
                    'Nicacio':nicacio,            
                    'Bruna':bruna,
                    'Domitila':domitila,            
                    'Key':key,
                    'Marvvila':marvvila,            
                    'Mc Guime':guime,
                    'Gabriel':gabriel,
                    'Paula':paula,            
                    'Cezar': cezar, 
                    'Gustavo': gustavo,            
                    'Larissa':larissa,
                    'Ricardo':ricardo,            
                    'Sarah':sarah,
                    'Marilia':marilia,            
                    'Cristian':cristian,
                    'Bruno':bruno,
                    'Tina':tina,
                    'Amanda':amanda
                }
        dataframe = pd.DataFrame({'Names':quotes.keys(),
                                  'Quotes':quotes.values()})
        dataframe = dataframe.sort_values(by='Quotes',ascending=False).reset_index(drop=True)
       
        return dataframe






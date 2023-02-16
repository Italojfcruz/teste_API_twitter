import requests
import pandas as pd
import tweepy as tw
import re
import time
from datetime import datetime,timedelta 
from unidecode                            import unidecode
from selenium                             import webdriver
from selenium.webdriver.support.ui        import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by         import By
from selenium.common.exceptions           import SessionNotCreatedException
from selenium.webdriver.support           import expected_conditions
import random 
import logging
import boto3
from botocore.exceptions import ClientError
import os

class ApiTwitter():
    def __init__(self) -> None:
        self.bearer_token        ='AAAAAAAAAAAAAAAAAAAAAJVblQEAAAAA8TqsBNhMkEPAcc0CDIGuUFEvhDU%3DP0BFUPVWhp3tf4OshAXQBGywj0J1e5XpTWnB4vS971qExhFNcl'
        self.consumer_key        ='vx7SEtLVOCl2ARgg3CujiwZz0' 
        self.consumer_secret     ='eK5718YwBRXu88aSzeI5C7IwApleQfXk9mzE8TiEZWclIjYLol' 
        self.access_token        ='2936113828-n4E3eLCcjc8zcBEZ08aeYwKdxNYEP7E95ov50UO'
        self.access_token_secret ='40xcsiz3D7sWudoqM3FITovMs4KID5yfBUvWsNLv7KI78'
                 
         
    def get_twitter_recents(self):
        token=None
        day_1 = (datetime.now()- timedelta(days=1))
        day_1 = day_1.strftime("%Y-%m-%d %H:%M:%S")

        url      = f'https://api.twitter.com/2/tweets/search/recent?query=BBB23&max_results=100&tweet.fields=created_at'
        headers  = {'Authorization':'Bearer '+ self.bearer_token}
        response = requests.get(url,headers=headers).json() 

        twitters = response['data']
        
        token = response['meta'].get('next_token')
      
        if token:
            for i in range(10):
                if token:
                    response = requests.get(f'{url}&next_token={token}' ,headers=headers).json()
                    twitters.extend(response['data'])
                    token = response['meta'].get('next_token')
                    response = {}
        
        dataset_BBB23 = pd.DataFrame(twitters)
        return dataset_BBB23.drop(columns=['edit_history_tweet_ids'])
  
        dataset_BBB23.to_excel('dados_BBB23.xlsx')
            
    def tw_get_twitter_recents(self):
        self.client = tw.Client(self.bearer_token,self.consumer_key, self.consumer_secret, self.access_token, self.access_token_secret)
        response = self.client.search_recent_tweets(query='BBB23',max_results=50)
        response = response.data
        for x in response:
            print(x.text)    
 
    def twitter_quotes(self,dataframe):
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


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Scrapper:
    def __init__(self, timeout: int = 5):
        self.timeout = timeout
        try:
            options = webdriver.ChromeOptions()
            #options.add_argument('--headless')
            options.add_argument("--disable-infobars")
            self.driver = webdriver.Chrome(executable_path='./chromedriver.exe',options=options)
        except SessionNotCreatedException as ex:
            self.driver = None
            self.show_error(ex.msg)
            exit()
        self.wait = WebDriverWait(self.driver, timeout)

    def get_followers_insta(self, usernames: str) -> int:
        
        for username in usernames: 
            followers = {}
            teste ='https://www.facebook.com/fred08oficial/'
            url = f'https://www.instagram.com/{username}'
            self.driver.get(f'https://www.instagram.com/{username}/')
            time.sleep(1)
            try:
                splash_screen: WebElement = self.wait.until(
                    expected_conditions.presence_of_element_located((By.ID, "splash-screen"))
                )
                self.wait.until(expected_conditions.invisibility_of_element(splash_screen))
                element = self.driver.find_element(By.XPATH, "//div[contains(text(), 'seguidores')]")
                followers_count =  element.find_element(By.CSS_SELECTOR, 'span')
                followers[username] =  int(followers_count.get_attribute('title').replace('.',''))
            except Exception as ex:
                self.show_error(ex)
        dataframe = pd.DataFrame({"username":followers.keys(),"followers":followers.values()})
        return dataframe.sort_values(by='followers',ascending=False).reset_index(drop=True)
   

    def transforma_data(self,data)->int:
        text = data.split(' ') 
        if (len(text)>1):    
            if (text[1]) == 'mil':
                return int(float(text[0].replace(',','.')) * 1000 )
            if (text[1]) == 'mi':
                return int(float(text[0].replace(',','.')) * 1000000 )
        else:
            return int(data.replace('.',''))        
         

    def get_follower_twitter(self,users):
        followers = {}
        for user in users:

            url_twitter   = f'https://twitter.com/{user}' 
            self.driver.get(url_twitter)
            time.sleep(1)
            try:    
                
                teste2= '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[5]/div[2]'
                teste = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[5]/div[2]/a/span[1]/span'
                #tags_tw   = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[5]/div[2]/a/span[1]')
                element = self.driver.find_element(By.XPATH,teste).text
                followers[user] = self.transforma_data(element) 
                  
            except Exception as ex:
                self.show_error(ex)
                #return 0
        dataframe = pd.DataFrame({'username':followers.keys(),'seguidores':followers.values()})
        return dataframe.sort_values(by='seguidores',ascending=False).reset_index(drop=True)


    def show_error(self, error: str):
        print(f'{bcolors.FAIL}{error}{bcolors.ENDC}')





class AmazonAWS:
    def __init__(self) -> None:
        pass

    def upload_file(file_name, bucket, object_name=None):
        """Upload a file to an S3 bucket

        :param file_name: File to upload
        :param bucket: Bucket to upload to
        :param object_name: S3 object name. If not specified then file_name is used
        :return: True if file was uploaded, else False
        """

        # If S3 object_name was not specified, use file_name
        if object_name is None:
            object_name = os.path.basename(file_name)

        # Upload the file
        s3_client = boto3.client('s3')
        try:
            response = s3_client.upload_file(file_name, bucket, object_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True   
            

    
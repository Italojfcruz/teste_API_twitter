import requests
import pandas as pd
import tweepy as tw
from google.cloud import storage
from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()




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
        #dataset_BBB23.to_excel('dados_BBB23.xlsx')
            
    def tw_get_twitter_recents():
        Client = tw.Client(bearer_token,consumer_key, consumer_secret, access_token, access_token_secret)
        response = Client.search_recent_tweets(query='BBB23',max_results=50)
        response = response.data
        for x in response:
            print(x.text)    

    def quant_follower(user):
        url_twitter   ='https://twitter.com/'+ user 
        url_instagram ='https://www.instagram.com/fred/'
        response = requests.get(url_twitter)
        
        html_page = response.text
        
        soup = BeautifulSoup(html_page, 'html.parser')
        

        '''
        elementos intagram
        <span class="_ac2a _ac2b" title="10.476.640"><span>10,4&nbsp;mi</span></span>
        
        <div class="_aacl _aaco _aacu _aacy _aad6 _aadb _aade"><span class="_ac2a _ac2b" title="10.476.640"><span>10,4&nbsp;mi</span></span> seguidores</div>
         
        <button class="_acan _acao _acat _aj1-" type="button"><div class="_aacl _aaco _aacu _aacy _aad6 _aadb _aade"><span class="_ac2a _ac2b" title="10.476.640"><span>10,4&nbsp;mi</span></span> seguidores</div></button>

        '''

        '''
        elementos twitter
        react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div:nth-child(3) > div > div > div > div > div.css-1dbjc4n.r-13awgt0.r-18u37iz.r-1w6e6rj > div:nth-child(2) > a > span.css-901oao.css-16my406.r-1nao33i.r-poiln3.r-1b43r93.r-b88u0q.r-1cwl3u0.r-bcqeeo.r-qvutc0 > span
        
        <span class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0">820,5&nbsp;mil</span>
        
        <span class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0">1.283</span>

        <div class="css-1dbjc4n r-1mf7evn"><a href="/fred_b12/following" dir="ltr" role="link" class="css-4rbku5 css-18t94o4 css-901oao r-1nao33i r-1loqt21 r-1qd0xha r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-qvutc0"><span class="css-901oao css-16my406 r-1nao33i r-poiln3 r-1b43r93 r-b88u0q r-1cwl3u0 r-bcqeeo r-qvutc0"><span class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0">1.283</span></span> <span class="css-901oao css-16my406 r-1bwzh9t r-poiln3 r-1b43r93 r-1cwl3u0 r-bcqeeo r-qvutc0"><span class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0">Seguindo</span></span></a></div>
        <span class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0">FRED </span>
        '''

        #div = soup.find_all("span",{"class":"_acan _acao _acat _aj1-"}) #instagram
        div = soup.find_all("span",{"class":"css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"})#twitter
        
        driver.get(url_twitter)
        time.sleep(5)
        tags_tw   = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[5]/div[2]/a/span[1]')
        
        #driver.get(url_instagram)
        #time.sleep(10)
        #tags_inst = driver.find_element(By.XPATH,'//*[@id="mount_0_0_tF"]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[2]/button/div')

        print("twitter: ",tags_tw.text)
        #print("Instagram: ",tags_inst)
        #file = open('texto.html','a')
        #file.write(div)
        
class Files:
    def __init__(self) -> None:
        pass
    
    def read_file(self,path):
        pass
    def write_file(data):
        file= open('/var/lib/docker/volumes/datas_api/datas.txt','a') 
        file.write(data)
        

class CloudGcp:
    def __init__(self) -> None:
        pass    
    def load_data():
        pass
    
    def upload_blob_from_memory(bucket_name, contents, destination_blob_name):
        # The ID of your GCS bucket
        # bucket_name = "your-bucket-name"

        # The contents to upload to the file
        # contents = "these are my contents"

        # The ID of your GCS object
        # destination_blob_name = "storage-object-name"

        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_string(contents)

        print(
            f"{destination_blob_name} with contents {contents} uploaded to {bucket_name}."
        )
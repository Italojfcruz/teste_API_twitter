import tweepy 

bearer_token ='AAAAAAAAAAAAAAAAAAAAAJVblQEAAAAA8TqsBNhMkEPAcc0CDIGuUFEvhDU%3DP0BFUPVWhp3tf4OshAXQBGywj0J1e5XpTWnB4vS971qExhFNcl'
consumer_key ='vx7SEtLVOCl2ARgg3CujiwZz0' 
consumer_secret='eK5718YwBRXu88aSzeI5C7IwApleQfXk9mzE8TiEZWclIjYLol' 
access_token = '2936113828-n4E3eLCcjc8zcBEZ08aeYwKdxNYEP7E95ov50UO'
access_token_secret = '40xcsiz3D7sWudoqM3FITovMs4KID5yfBUvWsNLv7KI78'

Client = tweepy.Client(bearer_token,consumer_key, consumer_secret, access_token, access_token_secret)
 
response = Client.search_recent_tweets(query='BBB23',max_results=100)
response = response.data

for x in response:
    print(x.text)



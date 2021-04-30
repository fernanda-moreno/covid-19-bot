import sys
import tweepy
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import requests
from lxml import html

def create_tweet():
    response = requests.get('https://www.worldometers.info/coronavirus/usa/florida/')
    doc = html.fromstring(response.content)
    total, deaths, recovered = doc.xpath('//div[@class="maincounter-number"]/span/text()')
    orangeCountyCases = doc.xpath('//*[@id="usa_table_countries_today"]/tbody[1]/tr[5]/td[2]/text()')

    tweet = f'''Florida Coronavirus Latest Updates
            Orange County Total cases: {orangeCountyCases}
            FL Total cases: {total}
            FL Recovered: {recovered}
            FL Deaths: {deaths}
            Source: https://www.worldometers.info/coronavirus/
            #covid19 #coronavirusupdates
            '''

    return tweet

if __name__ == '__main__':
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print('Authentication successful')
    except:
        print('Error while authenticating API')
        sys.exit(1)

tweet = create_tweet()
api.update_status(tweet)

print('Tweet successful!')
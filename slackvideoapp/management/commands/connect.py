from django.core.management.base import BaseCommand
import json
import requests
from websocket import create_connection
import time
import re
from urllib.parse import urlparse,parse_qs
from slackvideoapp.models import Video

#Connect to the Slack rtm api using https://slack.com/api/rtm.connect
def initialize():
  url="https://slack.com/api/rtm.connect" 
  access_token={"token":"Access token here "} #Replace Bot User OAuth Access Token here
  r=requests.post(url,access_token)
  res=json.loads(r.text)
  print(res)
  url1=res['url']
  con = create_connection(url1)
  return con


#Parse Youtube ID from Youtube URL
def get_id(url):
    u_pars = urlparse(url)
    quer_v = parse_qs(u_pars.query).get('v')
    if quer_v:
        return quer_v[0]
    pth = u_pars.path.split('/')
    if pth:
        return pth[-1]


#Add youtube url to database
def add_item(link):
  ytid=get_id(link)
  id_list = Video.objects.order_by('vote')
  ids={ q.yt_id for q in id_list }
  if ytid not in ids:
    row=Video(url=link,yt_id=ytid)
    row.save()
    print("\n Youtube link added to database")
  else:
    print("\nYoutube link not added to database - Link already added!")


#Parse Youtube Url
def parse_yt(con):
  result =  con.recv()
  print(result)
  yt=r"^<((https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+)>$"
  while True:
    result =  con.recv()
    result=json.loads(result)
    if result["type"]=="message" and "hidden" not in result:
      match = re.search(yt, result['text'])
      if match:
        print("match")
        link=match.group(1)
        add_item(link)

    time.sleep(1)
  con.close()


class Command(BaseCommand):
  def handle(self,**options):
    session=initialize() #Connect to RTM API and initialize the websocket connection
    parse_yt(session) #parse youtube Url from incoming events
    


'''
Created on Sep 1, 2016

@author: shihab
'''
import sys, Tkinter
sys.modules['tkinter'] = Tkinter
import urllib
from urllib import FancyURLopener
import json as m_json
import re
import time
import subprocess
from random import randint
from easygui import *
#file  for the playlist
playlist_file = fileopenbox(msg="Provide the Songs list File", title="Song List File", default="~/")
#choices for the audio or video
choices = ["Video","Audio"]
reply = buttonbox("Do you want to download Video or Audio?",choices=choices)
#To choose the output directory
output_path = diropenbox(msg="Output Directory",title="Provide the path for Downloading",default="~/Videos")
#a file to store the song names that are not downloaded
output_temp = open(output_path+'/output_temp.txt','a')
playlist=open(playlist_file,'r')
songs = playlist.readlines()
playlist.close()
song_num = 1
for song in songs:
    query = song
    query = urllib.urlencode ( { 'q' : query } )
    opener = urllib.FancyURLopener()
    response = opener.open( 'Page on Google' + query ).read()
    json = m_json.loads ( response )
    results = json [ 'responseData' ] [ 'results' ]
    song_flag = 0
    for result in results:
        title = result['title']
        url = result['url']
        if re.search(r'www . youtube . com',url):  #it has to be youtube home url. I used spaces between the dots just to avoid it convert into a link
            print ( title + '; ' + url )
            print "DOWNLOADING",title
            decoded_url=urllib.unquote(url).decode('utf8')
            print decoded_url
            if reply=='Audio':
                subprocess.call(['youtube-dl','-o',output_path+'/%(title)s.(ext)s',"--extract-audio","--audio-format","mp3",decoded_url])
                song_flag = 1
            elif reply=='Video':
                subprocess.call(['youtube-dl','-o',output_path+'/%(title)s',decoded_url])
                song_flag = 1
            break;
    if song_flag==1:
        print "Line Number"+str(song_num),song, "DOWNLOADED"
        print "------------------------------------------------------------------------------------"
        song_flag = 0
    else:
        print "Line Number"+str(song_num),song, "NOT DOWNLOADED"
        print "------------------------------------------------------------------------------------"
        output_temp.write(song)
    
    time.sleep(randint(10,15))
    song_num+=1
output_temp.close()


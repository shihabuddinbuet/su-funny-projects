'''
Created on Nov 17, 2016

@author: shihab
'''
import youtube_dl
import argparse

def stat_download(url, format):
    ydl_opts = {'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': format, 'preferredquality': '192',}],}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def read_from_commandLine():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="provide the youtube vide url")
    parser.add_argument("-f", "--format", help="provide the format of video")
    opts = parser.parse_args()
    return (opts.url, opts.format)
    
if __name__ == '__main__':
    (url, format)=read_from_commandLine()
    print url
    print format
    stat_download(url, format)
    pass
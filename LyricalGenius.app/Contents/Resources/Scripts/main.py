#!/usr/bin/env python

import subprocess
import requests
import bs4
from bs4 import BeautifulSoup
import sys
import os


def arg1():
	# os.system(cmd1)
	o = subprocess.Popen([cmd1], stdout=subprocess.PIPE, shell=True)
	return o.stdout.read()

cmd1 = """osascript -e 'tell application "iTunes"
set libCount to count of items in selection
end tell'"""

rawCount = int(arg1().encode('utf-8').strip())
lCount = int(rawCount)+1

for i in range(1,lCount):
	cmd2 = """osascript -e 'tell application "iTunes"
	set songName to get name of item """+str(i)+"""of selection
	end tell'"""

  	cmd3 = """osascript -e 'tell application "iTunes"
  	set artistName to get album artist of item """+ str(i) +"""of selection
  	end tell'"""

	def arg2():
	  	# os.system(cmd1)
		o = subprocess.Popen([cmd2], stdout=subprocess.PIPE, shell=True)
		return o.stdout.read()

	def arg3():
		# os.system(cmd2)
		p = subprocess.Popen([cmd3], stdout=subprocess.PIPE, shell=True)
		return p.stdout.read()

 	song_title=arg2().decode('utf-8').strip()
	artist_name=arg3().decode('utf-8').strip()
	
	# print song_title
	# print artist_name

	base_url = "http://api.genius.com"
	headers = {'Authorization': 'Bearer j3gmGgelWkUoY4I1DkAx7RATodylb5FW_MHLVVD2QiEO1_O9OVCUAIxa6eFvZSoF'}

	def lyrics_from_song_api_path(song_api_path):
		song_url = base_url + song_api_path
		response = requests.get(song_url, headers=headers)
		json = response.json()
		path = json["response"]["song"]["path"]

		#gotta go regular html scraping... come on Genius
		page_url = "http://genius.com" + path
		page = requests.get(page_url)
		html = BeautifulSoup(page.text, "html.parser")

		#remove script tags that they put in the middle of the lyrics
		[h.extract() for h in html('script')]

		#at least Genius is nice and has a tag called 'lyrics'!
		lyrics = html.find("div", class_="lyrics").get_text() #updated css where the lyrics are based in HTML
		return lyrics

	if __name__ == "__main__":
		search_url = base_url + "/search"
		data = {'q': song_title}
		response = requests.get(search_url, params=data, headers=headers)
		json = response.json()
		song_info = None

	for hit in json["response"]["hits"]:
		if hit["result"]["primary_artist"]["name"] == artist_name:
		  song_info = hit
		elif hit["result"]["primary_artist"]["name"] != artist_name:
			song_lyrics = ""

	if song_info:
		song_api_path = song_info["result"]["api_path"]
		song_lyrics = lyrics_from_song_api_path(song_api_path).encode('utf8')

		cmd4 = """osascript -e 'tell application "iTunes"
		set lyrics of item """+str(i)+""" of selection to """+ song_lyrics +"""
		end tell'"""

	def arg4():
		# os.system(cmd4)
		o = subprocess.Popen([cmd4], stdout=subprocess.PIPE, shell=True)
		return o.stdout.read()

	print song_lyrics

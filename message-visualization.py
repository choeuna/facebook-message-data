import json
import re
import matplotlib.pyplot as plt
import pandas as pd 
from wordcloud import WordCloud, STOPWORDS


"""
1. messages exchanged over time
2. word cloud of most common words
3. most common words bar


Functions:
1. messages over time
2. word cloud
3. word bar graph
4. stopwords

Issue - Message content includes sending audio clips, stickers, photos, etc. Need to ensure these are filtered out.
Otherwise you get most common words of Bib, Tak, Becca, etc. 

nonIssue 	- Apostrophe prints incorrectly. An issue with UTF-8 encoding? Same issue with emojis?
		- https://stackoverflow.com/questions/5842115/converting-a-string-which-contains-both-utf-8-encoded-bytestrings-and-codepoints
		- String contains both utf-8 encoded bytestring and codepoints APPARENTLY
		- JSON holds unicode strings
		- YAY FIXED TY STACKOVERFLOW

"""
def fix_hex_string(s):
	# smth smth mojibake smth
	# original data is utf-8 encoded but decoded as latin-1
	# to fix, re-encode as latin-1 and decode again as utf-8
	return re.sub(r'[\xc2-\xf4][\x80-\xbf]+', lambda m: m.group(0).encode('latin1').decode('utf8'), s)

def clean_facebook_messages(data):
	# clean each message
	for message in data['messages']:
		if'content' in message:
			temp = message['content'] 	# is this step necessary? ie. do we need a temp
			message['content'] = fix_hex_string(temp)



file_name = '/Users/rebeccacho/Desktop/Messages/TakAlguire_ncyVNGMZQw/message.json'
f = open(file_name, 'r')
data_store = json.load(f)

clean_facebook_messages(data_store)
# next task is to take care of audio clips, pictures, stickers, gifs, etc.
# typically structured as "__ sent a(n) ___."
#	__ sent a [voice message, picture, sticker, GIF from Giphy, an attachment, 
#				live location, an event link]
# this should be included in clean_fb_msgs



f.close()



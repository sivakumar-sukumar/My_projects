from bdbclientv2 import BDBClient
from itty import *
import urllib2
import json
import bdbclientv2
import re
from PyDictionary import PyDictionary
dictionary=PyDictionary()

'''
from chatterbot import ChatBot
chatbot = ChatBot("Sivakumar")
from chatterbot.trainers import ListTrainer

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "Really!",
    "I'm SRiMATHY",
    "You are very good",
    "That's very nice of you",
    "Thanks for your time",
    "Hope you are doing great"
    "Tell me about yourself",
    "What do you do?",
    "How can i help you",
    "Sorry I cannot answer that now",
    "Can you be very specific",
    "I have knowledge about SR",
    "I am from Cisco",
    "Where are you from",
    "Its good to see you around"
]

#USing List trainer
chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)

#Using Corpus trainer
from chatterbot.trainers import ChatterBotCorpusTrainer

chatterbot = ChatBot("Training Example")
chatterbot.set_trainer(ChatterBotCorpusTrainer)

chatterbot.train(
    "chatterbot.corpus.english"
)

response = chatterbot.get_response("where are you from")
print(response)               
response = chatbot.get_response("getting better")
print(response)
'''

def sendSparkGET(url):
    request = urllib2.Request(url,headers={"Accept" : "application/json","Content-Type":"application/json"})
    request.add_header("Authorization", "Bearer "+bearer)
    contents = urllib2.urlopen(request).read()
    return contents
def sendSparkPOST(url, data):
    request = urllib2.Request(url, json.dumps(data),
                              headers={"Accept" : "application/json","Content-Type":"application/json"})
    request.add_header("Authorization", "Bearer "+bearer)
    contents = urllib2.urlopen(request).read()
    return contents

@post('/')

def index(request):
    result = {}
    webhook = json.loads(request.body)
    print(webhook['data']['id'])
    result = sendSparkGET('https://api.ciscospark.com/v1/messages/{0}'.format(webhook['data']['id']))
    result = json.loads(result)
    msg = None
    msg1 = None
    msg2 = None
    msg3 = None
    meaning = None
    response_flag = False
    user_id = None
    if webhook['data']['personEmail'] != bot_email:
        in_message = result.get('text', '').lower()
        print(in_message)
        in_message = in_message.replace(bot_name,'')
        print(webhook['data']['id'])
        in_message = in_message.replace('srimathy','')
        if "," in in_message:
            sr,user_id = in_message.split(',')
            print(sr + user_id)
        else:
            sr = in_message
        print("in_message: "+in_message)
        #response = chatterbot.get_response(in_message)    
        if 'hi' in in_message or "hello" in in_message or 'Hi' in in_message or "Hello" in in_message:
            html_text = "<p><b>{}</b></p><p><i> {}<i></p><p><i> {}<i></p><p><i> {}<i></p>"
            msg1 = "**Hello! I'm SRiMATHY!**  **Self-improvement Reading Information Made Available To Help You **"+"```Your Personal English Teacher```"
            response_flag = True
            #title = html_text.format("Hello! I'm Dr. SRiMATHY!  SR information Management That Help You ","```Please provide your SR anumber to fetch the information```")
    	if 'Is you okay' in in_message or "is you ok" in in_message or 'Is you k' in in_message or "is u ok" in in_message:
            html_text = "<p><b>{}</b></p><p><i> {}<i></p>"
            msg2 = "The sentence is not correct please use **Are you ok?**"
            response_flag = True
            #title = html_text.format("Hello! I'm Dr. SRiMATHY!  SR information Management That Help You ","```Please provide your SR anumber to fetch the information```")
            #title = html_text.format("Hello! I'm SRiMATHY!  Self-improvement Reading Information Made Available To Help You ","```Contact sivaksiv@cisco.com for more info```")
        if 'score' in in_message:
        	html_text = "<p><b>{}</b></p><p><i> {}<i></p><p><i> {}<i></p><p><i> {}<i></p>"
        	msg3 = html_text.format("Hello! I'm SRiMATHY!  Self-improvement Reading Information Made Available To Help You ","```Your English score: 100/500```","```Your are at position 36 compared to your peers```","To learn about curriculum vist http://xyz.com") 
        	response_flag = True
        if 'learn' in in_message:
            html_text = "<p><b>{}</b></p><p><i> {}<i></p>"
            sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files":'https://www.youtube.com/watch?v=juKd26qkNAw'})
            '''
        if 'emerge' in in_message:
            html_text = "<p><b>{}</b></p><p><i> {}<i></p>"
            meaning = dictionary.meaning(in_message)
            response_flag = True
            trans = dictionary.translateTo(in_message)
        	#sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], 'markdown': '{}'.format(meaning)})
        	
            #sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files":'https://www.youtube.com/watch?v=juKd26qkNAw'})
            '''
            '''
        elif re.findall(r"^68\d{7}", str(in_message)):
            link2script = 'https://scripts.cisco.com/ui/use/SR_Checker?SR_info='+in_message+'&autorun=true'
            bdb_client = bdbclientv2.BDBClient(username="sivaksiv", password="password")
            bdb_client.task_run('Q_manager_test', inputs= {"user": "ajshende","wg":"test"})
            result1 = bdb_client.task_run('SR_Checker', inputs= {"SR_Info": sr,"user_id": user_id})
            reg = re.search(r'<pre>.*<\/pre>',str(result1))
            msg = str(reg.group())
            '''
    	
    	elif re.findall(r"68\d{7}", str(in_message)):
            casenum = re.findall(r"68\d{7}",str(in_message))
            srnum = casenum[0]
            print(srnum)
            link2script = 'https://scripts.cisco.com/ui/use/SR_Checker?SR_info='+str(srnum)+'&autorun=true'
            hyperlink_format = '<a href="{link}">{text}</a>'
            sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], 'markdown': '{}'.format(hyperlink_format.format(link=link2script, text='Click here for full review of '+str(srnum)))})            
        elif response_flag == False:
            print("NANA NANA NANA NANA")
            #sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files": bat_signal})
            #sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], 'markdown': '{}'.format("**OH! OH! I don't think I'm qualified to answer that yet.**")})
            meaning = dictionary.meaning(in_message)
            response_flag = True
            trans = dictionary.translateTo(in_message)
            #sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], 'markdown': '{}'.format("Sorry i cant answer at the moment")})
            '''
        if msg != None:
            hyperlink_format = '<a href="{link}">{text}</a>'
            print(msg)
            output = msg.split('\\n')
            print(output)
            #sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "text": msg})
            sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], 'markdown': '{}'.format("\n".join([str(x) for x in output]))})
            sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], 'markdown': '{}'.format("*For complete review, enter SR number followed by CEC id - e.g.* **6532345,jodepp**")})
            #sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], 'markdown': '{}'.format(hyperlink_format.format(link=link2script, text='Click here for full review'))})
            '''
		
        if msg1 != None:
            print(msg1)
            sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], 'markdown': '{}'.format(msg1)})
        if msg2 != None:
            print(msg2)
            sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], 'markdown': '{}'.format(msg2)})
        if msg3 != None:
            print(msg3)
            sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], 'markdown': '{}'.format(msg3)})
            sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "files":hack1})
    	if meaning != None:
            print(msg1)
            sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], 'markdown': '{}'.format(meaning)})
            sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], 'markdown': '{}'.format(trans)})
        	       
    return "true"

####CHANGE THESE VALUES#####
bot_email = "SRiMATHY@webex.bot"
bot_name = "GoPro"
bearer = "MTE0ZTgyYjgtNzFmOS00MDU3LWE0MTUtZTRjMDE1ZTg5ODQ2NDVlOTFkYjQtM2Zh"
bat_signal = "https://upload.wikimedia.org/wikipedia/en/c/c6/Bat-signal_1989_film.jpg"
hack1 = "https://golpetb.files.wordpress.com/2015/02/il-picture-for-present.jpg"
run_itty(server='wsgiref', host='0.0.0.0', port=8888)

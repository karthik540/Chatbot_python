from pprint import pprint
import json
import apiai
from tkinter import *

CLIENT_ACCESS_TOKEN = '3a79f257e43e497b9d07d18c51e7497d'

def messageFilter(EntryText):
    endText = ''
    for i in range(len(EntryText)-1 , -1 , -1):
        if EntryText[i] != '\n':
            endText = EntryText[0 : i+1]
            break
    for i in range(0 , len(endText) , 1):
        if EntryText[i] != '\n':
            return endText[i:] + "\n"
    return ''

def botResponseReciever(queryMessage):
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    request.query = queryMessage

    response = request.getresponse()

    rawData = str(response.read())
    rawData = rawData.replace(r"\n" , "")       #Remove \n 
    rawData = rawData.replace(r"b'" , "" , 1)   #Remove b'
    rawData = rawData.replace(r"\'" , "")   #Remove \' which causes prob in the bot message
    jsonData = rawData[0:-1]                        #Remove ' in the end

    jsonObj = open("response.json" , "w+")
    jsonObj.write(jsonData)
    jsonObj.close()

    with open('response.json') as f:
        data = json.load(f)
    return data['result']['fulfillment']['speech'] + "\n"

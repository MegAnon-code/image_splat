from textblob import TextBlob
from multiprocessing import Process
import operator
import string
import random
import sys
from google_images_download import google_images_download as gid
from .spriteDisplay import *
punct = string.punctuation
#Pulls image off google and displays
def image_show(image_desc, image_flavour, image_samples, image_format):
    #For displaying gifs.
    sys.stdout = open(os.devnull, "w")
    image_getter = gid.googleimagesdownload()
    #image_getter needs to be fed a dictionary to work properly.
    if image_format == 'gif':
        arguments = {"keywords":image_desc+" "+image_flavour,"limit":image_samples,"output_directory":"contextimage","silent_mode":True, "format":image_format,"type":"animated"}
    else:
        arguments = {"keywords":image_desc+" "+image_flavour,"limit":image_samples,"output_directory":"contextimage","silent_mode":True, "format":image_format}
    image_getter.download(arguments)
    #print("Well, it downloaded.")
    if not os.path.exists("contextimage\\"+image_desc+" "+image_flavour):
        sys.stdout = sys.__stdout__
        return None
    elif len(os.listdir("contextimage\\"+image_desc+" "+image_flavour)) == 0:
        os.rmdir("contextimage\\"+image_desc+" "+ image_flavour)
        sys.stdout = sys.__stdout__
        return None
    #print("And got through checks")
    image_name = str(os.listdir("contextimage\\"+image_desc+" "+image_flavour)[random.randint(0, image_samples - 1)])
    sprite_show('contextimage/' + image_desc+" " + image_flavour, image_name)
    #cleanup our image folder
    #start by going back to the script's working dir
    abspath = os.getcwd()
    os.chdir(abspath)
    for image in os.listdir("contextimage\\"+image_desc+" "+image_flavour):
        os.remove("contextimage\\"+image_desc+" "+ image_flavour+"\\"+image)
    os.rmdir("contextimage\\"+image_desc+" "+image_flavour)
    sys.stdout = sys.__stdout__
    
#Uses some NLP wizardry to get important noun phrases out of a given text to feed image_show
def get_nouns(context_phrase):
    blob = TextBlob(context_phrase)
    #print(str(blob.noun_phrases))
    return blob.noun_phrases
#Checks if punctuation is inside a string.
def check_punct(text):
    for pun in punct:
        if operator.contains(text, pun):
            return True
    return False 
#List of POS tags that we want to keep
good_tags = ['JJ','JJR','JJS','NN','NNS','RB','RBS','VBD','VBG','VB','VBP','VBZ','VBN']
#Concatenates the trigger with its reverse, so as to get TextBlob to detect awkwardly structured noun phrases (terrifying Dragon and Dragon terrifying both detected)
def extend_context(trigger):
    rev = ""
    for word in trigger.split():
        rev = word + " " + rev
    result = trigger + " " + rev
    return result
#Convert text into a form with more noun phrases.
def make_friendly(text):
    nu_text=""
    blob = TextBlob(text)
    for word, dsc in blob.tags:
        if operator.contains(good_tags, dsc):
            nu_text += word + " "
    return nu_text
    
def image_response(trigger, image_flavour, image_samples, image_format):
    friendify = make_friendly(trigger)
    #print(friendify)
    search_list = get_nouns(friendify)
    #print(search_list)
    for search_item in search_list:
        #Stop stupid searches for Wells.
        if len(search_item.split()) == 1:
            continue
        #Stop broken searches for punctuation stuff.
        elif check_punct(search_item) == True:
            continue
        else:
            p = Process(target=image_show, args=(search_item, image_flavour, image_samples, image_format))
            p.start()
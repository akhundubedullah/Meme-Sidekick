import google.generativeai as genai
import os 
from textblob import TextBlob 
import random


print("Hello, Meme Sidekick!")


meme_template = input("Wite a Meme ") 


def generate_surprise_meme():
    template = random.choice(meme_templates)

    # Use AI for a wacky phrase (tailor the prompt for extra absurdity)
    prompt = "Describe a cat wearing a superhero cape and mismatched socks." 
    response = model.generate_content(prompt)
    funny_phrase = response.text 

    meme = template.replace("[text]", funny_phrase)  
    print(meme)     



meme_templates = [
    "Bad Luck Brian: [text]" ,
    "Success Kid: [text] ",
    "One Does Not Simply: [text]" 
    # Hindi Templates
    "Aeyin ye kiya howa? [text]", 
    "Kiya mast joke mara re! [text]",
    "Chup re halkat! [text]",
    # English Templates
    "Nobody: [Silence] / [text]]", 
    "[Common phrase] / Me, taking it literally: [text]" 
    "When you finally [text]",
    "Me as a programmer: [Expectation] / Me as a programmer: [Funny reality]",
    # ... your existing templates
    "When your [noun] does [silly action]: [text]",  # Template for absurdity
    "Me: [normal activity] / My brain: [ridiculous alternative]",
]  


#chosen_template = random.choice(meme_templates)
#final_meme = chosen_template.replace("[text]", sentence)  # Simple insertion 
#print(final_meme)


# Analysis
def add_humorous_response(emotion):
    if emotion == "frustration":
        print("Whoa there! Easy on the keyboard smashing. Let's channel that rage into meme supremacy.")


num_words = len(meme_template.split())  # Count the words
has_exclamation = "!" in meme_template   # Detect exclamation points
print("Number of words:", num_words)
print("Has exclamation:", has_exclamation)


blob = TextBlob(meme_template)
sentiment = blob.sentiment.polarity  # Value between -1 (negative) and 1 (positive)

if sentiment >= 0.5:
    print("Seems like the user is feeling positive!")
elif sentiment <= -0.5:
    print("Seems like the user is feeling negative!")
else:
    print("Seems like the sentiment is neutral")

keywords = {
    "frustration": ["annoyed", "problem", "ugh", "why"],
    "excitement": ["yay", "awesome", "love"],
    "sarcasm": ["seriously", "obviously", "of course"],
}
for emotion, words in keywords.items():
    if any(word in meme_template.lower() for word in words):
     print("Seems like the user is feeling", emotion)
     add_humorous_response(emotion)   
    
genai.configure(api_key="AIzaSyBFthjm8lUCTy42FxhCEq3ytate0O7WTjU") 
model = genai.GenerativeModel('gemini-pro')
funny_prompt = meme_template + ", make it 100x weirder,funnier and sarcastic and two line meme in single reply not like bottom or top not more than 20 words and without bad words"  # Adds a twist 
response = model.generate_content(funny_prompt) 
print(response.text) 


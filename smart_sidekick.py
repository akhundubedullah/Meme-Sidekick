import google.generativeai as genai
import os 
from textblob import TextBlob 
import random




print("Hello, Meme Sidekick!")


meme_template = input("Wite a Meme ") # Get meme template here


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
    "Me as a programmer: [Expectation] / Me as a programmer: [Funny reality]"  
] 

#chosen_template = random.choice(meme_templates)
#final_meme = chosen_template.replace("[text]", sentence)  # Simple insertion 
#print(final_meme)


# Analysis
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

genai.configure(api_key="AIzaSyBFthjm8lUCTy42FxhCEq3ytate0O7WTjU") 
model = genai.GenerativeModel('gemini-pro')
prompt = meme_template  # Use the meme template directly
response = model.generate_content(prompt)
print(response.text)  

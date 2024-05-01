import google.generativeai as genai
import os 
from textblob import TextBlob 
import random

# Configuration (Make sure to add your real API key)
genai.configure(api_key="AIzaSyBFthjm8lUCTy42FxhCEq3ytate0O7WTjU") 
model = genai.GenerativeModel('gemini-pro')

def main():
    print("Hello, Meme Sidekick! Let's make some hilarious memes.")

    while True:  # Keep the meme fun going!
        user_word = input("Enter a single word: ")
        meme_type = choose_meme_type()

        if meme_type == "surprise":
            generate_surprise_meme(user_word)
        elif meme_type == "custom":
            generate_custom_meme(user_word)
        else:
            print("Let's try that again...")  # In case of errors]

        another_meme = input("Want to make another meme? (yes/no): ").lower()
        if another_meme != "yes":
            break 

# Surprise Meme Generator
def generate_surprise_meme(word):
    template = random.choice(meme_templates)
    funny_prompt = f"Tell a joke about {word}."
    meme_text = model.generate_content(funny_prompt).text
    meme = template.replace("[text]", meme_text)
    print(meme) 

# Custom Meme Generator
def generate_custom_meme(word):
    analyze_sentiment(word) 
    funny_prompt = f"{word} but make it 100x funnier, with a dash of sarcasm."
    meme_text = model.generate_content(funny_prompt).text  
    meme = choose_template(meme_text)  
    print(meme)

# Sentiment Analysis (Expanded)
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity  

    if sentiment >= 0.5:
        print("Whoa, someone's feeling positive! 😊")
    elif sentiment <= -0.5:
        print("Hang in there! Let's turn that frown upside down. 😉")
    else:
        print("Okay, keeping it neutral. 😎")

# Choose the Right Template
def choose_template(text):
    # Here you could add logic to select a template based on sentiment!
    return random.choice(meme_templates).replace("[text]", text)

# Meme Templates
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

def choose_meme_type():
    choice = input("Want a 'surprise' meme or a 'custom' one? ").lower()
    if choice in ["surprise", "s"]:
        return "surprise"
    elif choice in ["custom", "c"]:
        return "custom"
    else:
        return None  # Signal an error

if __name__ == "__main__":
    main()

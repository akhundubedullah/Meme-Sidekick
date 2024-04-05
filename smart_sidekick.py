print("Hello, Meme Sidekick!")

import random

sentence = input("Write a funny sentence: ") 


meme_templates = [
    "Bad Luck Brian: [text]" ,
    "Success Kid: [text] ",
    "One Does Not Simply: [text]" 
    # Hindi Templates
    "Aeyin ye kiya howa? [text]", 
    "Kiya mast joke mara re! [text]",
    "Chup re halkat! [text]",
    "Sahi pakde hain! [text]", 
    # English Templates
    "Nobody: [Silence] / [text]]", 
    "[Common phrase] / Me, taking it literally: [text]" 
    "When you finally [text]",
    "Me as a programmer: [Expectation] / Me as a programmer: [Funny reality]"  
] 


chosen_template = random.choice(meme_templates)
final_meme = chosen_template.replace("[text]", sentence)  # Simple insertion 
print(final_meme)
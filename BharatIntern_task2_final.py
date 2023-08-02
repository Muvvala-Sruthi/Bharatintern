#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install jupyter_contrib_nbextensions


# In[89]:


import difflib
def correct_word(word, word_list):
    closest_matches = difflib.get_close_matches(word, word_list)
    if closest_matches:
        return closest_matches[0]  
    else:
        return None
import re
w = []
with open('final.txt', 'r') as f:
    file_name_data = f.read()
    file_name_data = file_name_data.lower()
    w = re.findall('\w+', file_name_data)
word_list = set(w)
word_to_correct = input("enter a word:")
if(word_to_correct in word_list):
    print("Entered word is correct.")
else:
    corrected_word = correct_word(word_to_correct, word_list)
    if corrected_word:
        print("Corrected word could be:",corrected_word)
    else:
        print("No close match found.")


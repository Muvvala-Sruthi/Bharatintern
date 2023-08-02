#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install translate


# In[2]:


from translate import Translator
def translate_text(text,src_language, target_language):
    translator = Translator(to_lang=target_language)
    translated_text = translator.translate(text)
    return translated_text
source_text = input("Enter text to translate:") 
src_language = input('Enter language code of the source text:')
target_language = input('Enter language code  of the target text(to translate into):')      
translated_text = translate_text(source_text,src_language,target_language)
print("Translated text:", translated_text)


# In[ ]:





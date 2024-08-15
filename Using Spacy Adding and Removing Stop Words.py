#python -m venv myenv
#myenv\Scripts\activate
#python -m spacy download en_core_web_sm
import spacy 
import nltk 
from nltk.tokenize import word_tokenize 
nltk.download('punkt_tab')
sp = spacy.load('en_core_web_sm') 
#add the word play to the NLTK stop word collection 
all_stopwords = sp.Defaults.stop_words 
all_stopwords.add("play") 
text = "Yashesh likes to play football, however he is not too fond of tennis." 
text_tokens = word_tokenize(text) 
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords] 
print(tokens_without_sw) 
#remove 'not' from stop word collection 
all_stopwords.remove('not') 
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords] 
print(tokens_without_sw)

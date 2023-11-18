from PyDictionary import PyDictionary
from Body.Listen import Listen
from Body.Speak import Speak


query = Listen()
dict = PyDictionary()
query = query.replace('what', '')
query = query.replace('is', '')
query = query.replace('the', '')
query = query.replace('meaning', '')
query = query.replace('this', '')
query = query.replace('word', '')
query = query.replace('of', '')
word = query
meaning = dict.meaning(str(word))
Speak(meaning)
#convert emoji to text
"""
pip install demoji
import demoji
emoji=input("Enter a Emoji")
demoji.findall(emoji)
"""
import demoji
import unicodedata

list_of_emoji=[]
def check_emoji(char):
    return "So" in unicodedata.category(char)

def find_emojis(sentence):
  k=[]
  for i in sentence:
    if check_emoji(i):
      k.append(i)
  return k
sentence=input("Enter a sentence:")
list_of_emoji= find_emojis(sentence)
s=sentence.split()
d=demoji.findall(sentence)
for i in s:
    if i not in list_of_emoji:
      print(i,end=" ")
    else:
      print(d[i],end=" ")  

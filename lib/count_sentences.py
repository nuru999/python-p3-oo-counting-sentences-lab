#!/usr/bin/env python3

import re
class MyString:
    import re
class MyString:
  def __init__(self, value=""):
      self._value = value
      if type(self._value) != str:
        print("The value must be a string.")
      
  def is_sentence(self):
    return True if self._value.endswith(".") else False
  def is_question(self):
    return True if self._value.endswith("?") else False
  def is_exclamation(self):
    return True if self._value.endswith("!") else False
  def count_sentences(self):
    listy = re.sub(r'[!?]',".",self._value).split(".")
    listy.remove("")
    return len(listy)
string = MyString()
string.value= "1"
# print(string.count_sentences())
print(string.value)
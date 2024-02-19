# import re

class token:
    def __init__(self) -> None:
        pass
    @staticmethod
    def whitespace(sentence: str) -> list:
        arr = []
        word: str = ""
        for ch in sentence:
            if ch!=" " and ch!="\n" and ch!="\t":
                word += ch
            elif word!='':
                arr.append(word)
                word = ""
        arr.append(word)
        return arr
    @staticmethod
    def bigram(sentence: str) -> list:
        arr1st = token.whitespace(sentence)
        if len(arr1st)<2:
            return arr1st
        arr2nd = []
        for i in range( len(arr1st)-1 ):
            arr2nd.append( [arr1st[i], arr1st[i+1]] )
        return arr2nd
    @staticmethod
    def trigram(sentence: str) -> list:
        arr1st = token.whitespace(sentence)
        if len(arr1st)<3:
            return arr1st
        arr2nd = []
        for i in range( len(arr1st)-2 ):
            arr2nd.append( [arr1st[i], arr1st[i+1], arr1st[i+2]] )
        return arr2nd
    @staticmethod
    def regEx(sentence: str) -> list:
        # return re.compile(r'[\w\'\d]+').findall(sentence)
        arr = []
        word: str = ""
        for ch in sentence: # \d  --  A-Z  --  a-z  -- '
            if 47<ord(ch) and ord(ch)<58 or 64<ord(ch) and ord(ch)<91 or 96<ord(ch) and ord(ch)<123 or ch=="'":
                word += ch
            elif word!='':
                arr.append(word)
                word = ""
        arr.append(word)
        return arr

a = str(input("Enter the sentence: "))
print("whitespace: ", token.whitespace(a))
print("bigram: ", token.bigram(a))
print("trigram: ", token.trigram(a))
print("regex: ", token.regEx(a))


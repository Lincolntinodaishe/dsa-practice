class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3 : # length barrier
            return False
        vowels = set('aeiouAEIOU')  #create a set with vowels
        has_vowel =False
        has_consonent =False

        for i in word:
            if i.isalpha():   #if the char is a letter check if it is a vowel then update the boolians
                if i in vowels:
                    has_vowel = True
                else:
                    has_consonent = True
            elif i.isdigit():
                continue
            else:    #If not a digit and a letter return False
                return False
        return has_vowel and has_consonent #return true if both are true


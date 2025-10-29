class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        dict2 ={}
        possible = True  # tracking if my word is possible
        for char in chars:
            dict2[char] = dict2.get(char, 0)+1 # count for chars
        for word in words: # iterate throur each word
            dict1 = {} #new dict for each word
            for char in word:
                dict1[char] = dict1.get(char, 0)+1
            for key, value in dict1.items():
                if dict2.get(key, 0) < value:
                    possible = False
                    break
            if possible:
                res += len(word) # increament len of each word if true
            else:
                possible = True # update possible to default at the end
        return res
                
                
                

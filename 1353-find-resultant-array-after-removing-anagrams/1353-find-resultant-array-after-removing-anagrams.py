class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:

      
        output =[]  #output array
        current =""
        for word in words:
            if  ''.join(sorted(word)) != current:
               current = ''.join(sorted(word))
               output.append(word)
            else:
                continue
        return output
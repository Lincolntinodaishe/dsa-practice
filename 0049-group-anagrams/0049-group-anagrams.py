class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a dictionary that stores lists of the words
        dict1  = defaultdict(list)
        
        for i in strs: # iterate into each and evry word
            count = [0]*26 # for each word i want to find the count of each letter at every position
            for c in i: #for every character in the word
                count[ord(c)-ord('a')] += 1 # cal its specific position by subtractin the ord('a') from each character to get a unique position
            dict1[tuple (count)].append(i) # the key being specific to each word , i want to append the word but lists are not hashable hence i convert them to tuples
        return list (dict1.values()) # I WANT TO RETURN THE LIST OF LISTS THEREFORE I RETURN THE VALUES THEN CONVERT THEM TO LISTS SINCE THEY ARE TUPLES AT THIS POINT
class RandomizedSet:

    def __init__(self):
        # we set a dict and a list so that we can track the index of our value in the dict and are able to pop the val in the list at o(1)
        self.items_dict = {}
        self.items_list = []


    def insert(self, val: int) -> bool:
        # this is straight forward, we append the value to the list hence we know its index gonn be the lenght -1 then add the value in the dict
        # and match it with its index we return true
        if val not in self.items_dict:
            self.items_list.append(val)
            self.items_dict[val] = len(self.items_list)-1
            return True
        return False

        

    def remove(self, val: int) -> bool:
        # if the value is not in the dict we return False
        if val not in self.items_dict:
            return False
        # if it is we want to find an effeieciebt way to remove it.
        # we swap the val with the last number inna de list so that we can pop it from the list and just del it from the hash at o(1)

        last_value = self.items_list[-1]  # last value in the list
        idx = len(self.items_list)-1 # the index of the last value
        self.items_list[idx]= val # assig the val to the last value's position
        self.items_list[self.items_dict[val]] = last_value # assign the last value to the val's position in the list
        self.items_dict[last_value] = self.items_dict[val] # update the dict do that the index of last val is equal to the indexx of val
        self.items_list.pop() # remove the val in the by pop
        del(self.items_dict[val]) # delete val from the dict 
        # since it was available and was removed, wereturn True
        return True

        

    def getRandom(self) -> int:
        return random.choice(self.items_list) # to get a random number in the list we do random.choice, a built in function that works at o(1)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
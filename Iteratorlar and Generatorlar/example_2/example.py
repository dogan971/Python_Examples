class Kareler():
    def __init__(self,max = 0):
        self.max = max
        self.index = 1
    def __iter__(self):
        return self
    def __next__(self):
       
        if(self.index <= self.max):
            sonuc = 2 ** self.index
            self.index += 1
            return sonuc
        else:
            raise StopIteration

kare = Kareler(20)
for i in kare:
    print(i)
 

# failed attempt
# getting better at OOP though, so its ok

class Dict:
       
    def __init__(self):
        print("Initializing Class")
        self.Dict = dict()
        self.sub_Dict = dict()
        
    def add_dict(self, sequence):
        unique_chars = sorted(list(set(sequence)))
        for key in unique_chars:
            self.append_dict(key)
            self.add_sub_dict(key)
            self.link_dict(key)
        length = len(sequence)
        for i in range(0,length-1):
           # a = sequence[i]
           # b = sequence[i+1]
           # self.Dict[a][b] += 1
            
            
    def add_sub_dict(self, key):
            self.sub_Dict[str(key)] = 0
            
    def link_dict(self,key):
        self.Dict[str(key)] = dict(self.sub_Dict)
        
    def print_example(self):
        print(self.Dict['A']['A'])
        
    def print_dict_keys(self):
        for i in self.Dict.keys():
            print(i)
            
    def print_subdict_keys(self):
        for i in self.sub_Dict.keys():
            print(i)
            
    def print_subdict_values(self):
        for i in self.sub_Dict.values():
            print(i)
            
    def print_dict_values(self):
        for i in self.Dict.values():
            print(i)
        
    def append_dict(self, key): 
        self.Dict[str(key)] = dict()
        
session = Dict()
sequence = str(input("Enter sequence: "))
sequence = sequence.upper()
session.add_dict(sequence)
session.print_example()




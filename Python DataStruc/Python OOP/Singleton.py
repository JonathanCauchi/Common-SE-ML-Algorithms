class Participant:
    
    _identifier = 0
    
    def __init__(self):
        self.id = Participant.identifier
        Participant._identifier += 1
        
    def identifier(self):
         print(self.id)
    
class Contractor:
    
    __instance = None
    
    def __init__(self):
        if Contractor.__instance != None:
            raise Exception("Already an instance there")
        else:
            Contractor.__instance = self
        
    @staticmethod
    def get():
        return Contractor.__instance
        
    #def send_request(self, message):
        
if __name__ == "__main__":
    cont1 = Contractor()
    print(cont1)
    print(cont1.get())
class Sort:
    def __init__(self):
        print("Class initialized")
        
    def mergesort(self, array):
        length = len(array)
        if length > 1:
            split = round(length/2)
            a = array[:split]
            b = array[split:]
            self.mergesort(a)
            self.mergesort(b)
            i = j = k = 0
            while i < len(a) and j < len(b):
                if a[i] < b[j]:
                    array[k] = a[i]
                    i += 1
                    k += 1
                else:
                    array[k] = b[j]
                    j += 1
                    k += 1
            
            while i < len(a):
                array[k] = a[i]
                i += 1
                k += 1
                
            while j < len(b):
                array[k] = b[j]
                j += 1
                k += 1
        return array
                
    def print_list(self,array):
        for i in array:
            print(i)
            
if __name__ == "__main__":
    array = [2,5,4,3,7,8,9,1]
    session = Sort()
    session.mergesort(array)
    session.print_list(array)
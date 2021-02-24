alphabet = "abcdefghijklmnopqrstuvwxyz"   

test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the 

def missing_letters(string):
    compare = histogram(string) 
    for key in sorted(compare): 
        if key in alphabet: 
            result = alphabet.replace(key,'') 
            return result # print result
        else:
            return None

for letters in test_miss: 
    if missing_letters(letters) == None:
        print(letters, 'uses all the letters')   
    else:
        print(letters , 'is missing letters', missing_letters(letters))

# output: zzz is missing letters abcdefghijklmnopqrstuvwxy                                                                               
# subdermatoglyphic is missing letters bcdefghijklmnopqrstuvwxyz                                                                 
# the quick brown fox jumps over the lazy dog uses all the letters

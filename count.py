'''
 Exercise 3:
 Given a paragraph of text, 
 1. count the number of times each character occurs in the text, 
   and print out each character and its count (in any order).
 2. do it now in a case-insensitive manner for the alphabets
 3. extension: print in the descending order of the count
'''


def count_char(text):
    dicationary = {}

    for i in text:
        if i in dicationary:
            dicationary[i] += 1   
        else:
            dicationary[i] = 1  
            
    for i in dicationary:
        print(i,dicationary[i])  
    
    

def count_char_insensitive(text):
    dicationary = {}
    text = text.lower()

    for i in text:
        if i in dicationary:
            dicationary[i] += 1   
        else:
            dicationary[i] = 1  
            
    for i in dicationary:
        print(i,dicationary[i])  



# bonus task:
def count_char_ordered(text):
    dicationary = {}
    text = text.lower()

    for i in text:
        if i in dicationary:
            dicationary[i] += 1   
        else:
            dicationary[i] = 1  
            

        
    dicationary.items()  
    result = sorted(dicationary.items(), key = lambda tup:tup[1],reverse = True)

    for i in result:
        print(i[0],i[1])
            
text1 = 'I felt happy because I saw the others were happy and because I knew I should feel happy but I wasn’t really happy' # Robert Bolano
text2 = 'HellO, WorLd!'

# testing exercise 2
count_char(text2)
count_char_insensitive(text2)
print()
count_char_ordered(text2)


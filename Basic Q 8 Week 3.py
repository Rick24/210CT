##Week 3 Task 8

##Write a recursive funcion that removes all vowels from a given string

x = str(input("Input your string"))

def vowel_remove(x):
        vowel = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U") #Define vowels
        if x: #If x exists
                if x[0] in vowel: #Check first letter to be a vowel
                        return(""+vowel_remove(x[1:])) #If it is remove it and recurse with that character removed
                else:
                        return(x[0]+vowel_remove(x[1:])) #If it isn't keep it and recurse with that character removed
        else:
                return("") #If there is no word inputted return empty string

print(vowel_remove(x))

##PSEUDOCODE

#Prompt user for word to remove vowels from (string)

#FUNCTION vowel_remove(string)
#IF string length = 0
        #IF string[0] is a vowel:
                #RETURN("" + FUNCTION vowel_remove(INPUT -1 CHARACTER)
        #ELSE
                #RETURN(INPUT[0] + FUNCTION vowel_remove(INPUT - 1 CHARACTER)
#ELSE
        #RETURN ""
#PRINT(new string)

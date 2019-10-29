def decompress(s):
    characters = []
    numbers = []
    brackets = []
    final_string = ""

    i = 0   
    while i < len (s):

        if s[i] != "]":
            if (s[i].isalpha()): 
                characters.append(s[i])
            
            elif s[i].isdigit():
                j = i
                num = ""

                j = s.index("[", i)
                numbers.append( int (s[i:j]))
                print(numbers)
                i = j-1
              
            
            
            # in this case we need to keep track of open brackets.
            elif s[i] == "[":
                brackets.append(s[i])

            i+=1
        
        

        elif s[i] == "]": # build things
            if len(brackets) > 1 :
                temp = ("".join(characters) * numbers.pop())
                characters = []
                characters.append(temp)
                brackets.pop()


            elif len(brackets) == 1:
                final_string += ("".join(characters) * numbers.pop())
                characters = []
            i+=1

                
        
    
    print(final_string)

decompress('3[a]')
decompress('3[abc]4[ab]c')
decompress('4[3[a]b]')

decompress('12[ab]')
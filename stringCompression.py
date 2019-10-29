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
                numbers.append(int (s[i:j]))
                i = j-1

            # in this case we need to keep track of open brackets.
            elif s[i] == "[":
                brackets.append(s[i])

        # running into a closing bracket
        elif s[i] == "]": 

            # if we have seen more than opening bracket, 
            # build the final string iteratively
            if len(brackets) > 1 : 
                temp = ("".join(characters) * numbers.pop())
                characters = []
                characters.append(temp)
                brackets.pop()
            
            # only one more opening bracket, final string
            elif len(brackets) == 1:
                final_string += ("".join(characters) * numbers.pop())
                characters = []
        i+=1
  
    return final_string

print(decompress('3[a]'))
print(decompress('3[abc]4[ab]c'))
print(decompress('4[3[a]b]'))
print(decompress('12[ab]'))
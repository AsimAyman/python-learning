#---------------------------
#-----Function Recursion----
#---------------------------
# To understand Recursion,first you have to understand Recursion.
#---------------------------
# Test Word [WWWoooorrldd]

world = 'WWWoooorrldd'
#  print(world[1:]) #WWo0oorrldd

def cleanWord(world):
    if len(world)==1:
        return world

    if world[0] == world[1]:
       return cleanWord(world[1:])
    
    return world[0] + cleanWord(world[1:])


    

print(cleanWord(world))
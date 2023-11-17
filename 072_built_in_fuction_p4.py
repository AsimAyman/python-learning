# --------------------------------
# ----Built in function => map----
# --------------------------------
# map take A functoin + iterator
# map called map because it map the function on every element
# the function can be pre-defined function or lambda function
#---------------------------------

# use map with predefined function

def formatText(text):
    return f"-{text.strip().capitalize()}-"


my_text = {'assem','Ahmed','sayed'}

my_text_formated = map(formatText,my_text)

for name in my_text_formated:    
    print(name)

for name in map(formatText,my_text):  
    print(name)

my_text_formated = list(map(formatText,my_text))    


# use map with lambda function
my_text = {'assem','Ahmed','sayed'}

my_text_formated = map(lambda t  : f"-{t.strip().capitalize()}-"  ,my_text)
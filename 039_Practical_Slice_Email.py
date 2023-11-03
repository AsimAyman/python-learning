#--------------------------------
#------Practical Slice Email-----
#--------------------------------

email = 'Osama@elzero.org'
print(email[0]) #O
print(email[0:5]) #Osama
print(email[:email.index('@')]) #Osama

theName = input('what is your name? ').strip()
theEmail = input('what is your email? ').strip()
userName = theEmail[:theEmail.index('@')]
websit = theEmail[theEmail.index('@')+1:theEmail.index('.')]
domain = theEmail[theEmail.index('.')+1:]
print(f'Hello {theName} your email is {theEmail}')
print(f'your user name is {userName}')
print(f"your websit is {websit}")
print(f"your domain is {domain}")
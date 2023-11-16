# ------------------------------------------------
# ----File handling => Write and append in file---
# ------------------------------------------------

# myFile = open('file.txt', 'w') # it will create the file
# myFile.write('Hello from python file with love \n')
# myFile.write('Second line') #
# myFile.write('therd part') #evry time it will remove the current txt and write the new write
# myFile.write('assem school\n'  * 1000)


# myFile.writelines(['hello\n','there\n','i\n','am\n','assem\n'])


# append
myFile = open('file.txt', 'a')
myFile.write('new line')  # will not remove the prevese txt

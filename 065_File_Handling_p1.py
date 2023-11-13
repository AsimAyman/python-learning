#--------------------------
#---Files Handling part 1--
#--------------------------
# "a" append open file for appending values, create file if not exists
# "r" read [default value] open file for read and give error if file is not exists
# "w" write open file for writing, create file if not exists
# "x" create create file, give error if file exists
#--------------------------
# import os
# print(f"=> {os.getcwd()}")
# print(os.path.dirname(os.path.abspath(__file__))) #065_File_Handling.p1.py
# print(os.path.abspath(__file__))

# #change current working directory 
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

file = open(r"myfile.txt",)  #read by default r means raw string
#---------------------------------------
#--- Modules install exteranl packages--
#---------------------------------------
# module vs package
# package is a group of modules
# exteranl package donwloaded from the interent
# you can install packages with python package manager PIP
# PIP install the package and its dependencies
# modules list "https://pymotw.com/3/py-modindex.html"
# packages exteranal and modules dirctory "https://pypi.org/"

# pip install packageName, packageName
# pip install package pip --upgrade

import termcolor , pyfiglet

print(dir(pyfiglet))
print(pyfiglet.figlet_format('Elzero'))
print(termcolor.colored(pyfiglet.figlet_format('Elzero'),color= 'yellow'))

help(termcolor.colored)
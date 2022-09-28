# make sure you have two additional files
# 1: config.py : This needs to have a variable with a string thats your API KEY
# 2: a .gitignore MUST exist on the same level. This literally just a file, with config.py named in it. Make sure you save this change!

from config import token
token = token

print(token)
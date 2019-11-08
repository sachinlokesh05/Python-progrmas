#importing the json module
import json

#it's an module,it is used to get the data directly from the server using request
from requests import *

#

#pesting this url in the get method of request,we can the information from api using link
data_requests=requests.get("https://www.quandl.com/api/v3/datasets/CHRIS/EUREX_FMCN1.json?api_key=nUFS3aepZ3WQdzAFfdec")


#


# #this is going the read the data in text format or string format
data_text=requests.text


#


# #putting data into the json file
data=json.loads(data_text)


#


# #and printing the data in "<dict>"
print(data)


# #reading the sample json file and loading it into data(<dict>)
data=json.load(open("data.json"))


#


# #printing the loaded data into data object
print(data)

#

# #printing the object type

print(type(data))

#

# #writitng the data into the json file use json.dumps
data_serialized=json.dumps(data)

#

# #printing the type of object, the data_serialized is str
print(type(data_serialized))

#

# #printing the updated json file
print(data_serialized)


#load the data into the specific json file
#indent keyword is make json file more readable format and more visible
data_serilazition=json.dump(data,open("data.json","w"),indent=4)

# separators keyword is use to change the json file syntax,In separators there two argv,
# first one for key-value pair separators and second one is for item separators
data_serilazition=json.dump(data,open("data.json","w"),separators=(";","-"))


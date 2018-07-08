
#def packer(**kwargs):
#  
#  print(kwargs)
#  
#packer(name="Felix", num=42, spanish_inquisition=None)  
#
##Run: {'spanish_inquisition': None, 'num': 42, 'name': 'Felix'} 


#def packer(name= None, **kwargs):
#  
#  print(kwargs)
#  
#packer(name="Felix", num=42, spanish_inquisition=None)  
#
##Run: {'spanish_inquisition': None, 'num': 42}  



#def packer(name= None, **kwargs):
#  
#  print(kwargs)
#  
#def unpacker(first_name = None, last_name = None):
#  if first_name and last_name:
#    print("Hi {} {}!".format(first_name,last_name))
#  else: 
#    print("Hi no name!")
#  
#packer(name="Felix", num=42, spanish_inquisition=None)  
#unpacker(**{"last_name": "Sapalaran", "first_name": "Felix"})
#
##Run: {'spanish_inquisition': None, 'num': 42}                                                      
##Hi Felix Sapalaran!  





def packer(name= None, **kwargs):
  
  print(kwargs)
  
def unpacker(first_name = None, last_name = None):
  if first_name and last_name:
    print("Hi {} {}!".format(first_name,last_name))
  else: 
    print("Hi no name!")
  
packer(name="Felix", num=42, spanish_inquisition=None)  
unpacker(**{"last_name": "Sapalaran", "first_name": "Felix"})

#So to explore this multiple return values thing, let's use this course dictionary.

#Let's create a variable and assign it with dictionary.
course_minutes = {"Python Basics": 232, "Django Basics": 237, "Flask Basics": 189, "Java Basics": 133}

#Now do you remember how the items method on a dictionary gives back a tuple of key value pairs? Let's use that and tuple unpacking to print out some of the info about our courses.

for course, minutes in course_minutes.items():
  print("{} is {} minutes long".format(course, minutes))
  
  
#Run: {'num': 42, 'spanish_inquisition': None}                                      
#Hi Felix Sapalaran!                                                           
#Python Basics is 232 minutes long                                             
#Django Basics is 237 minutes long                                             
#Java Basics is 133 minutes long                                               
#Flask Basics is 189 minutes long   


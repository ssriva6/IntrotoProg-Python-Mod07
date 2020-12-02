
# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: In this script i will show pickling and error handling
#
# ChangeLog (Who,When,What):
# Shruthi Srivatsan, 11.25.2020, Created script to complete assignment 7

#Pickling Demo---------------------#
#Pickling Example:
#Data--------------------------------#
#Pickling is straightfoward- instead of writing characters to a file, you will write a pickled object to a file
# Step 1: To use pickle - import pickle
import pickle
# Step 2: Dictionary:
dogs_dict = {"ozzy":3, "Golden": 8,"Husky":4,"Doodle":12,"Cockerspaniel":2}
# Step 3: File name, Open File and Write in Binary Code
filename= "Dogs"
outfile = open(filename,'wb')
readfile = open(filename,'rb')
# Step 4: Pickling and Unpickling
pickled_obj = pickle.dumps(dogs_dict) #pickles the data
unpickled_obj = pickle.loads(pickled_obj) #unpickles the data

#Step 5: Once file is open, you can pickle.dump
pickle.dump(dogs_dict,outfile)
outfile.close()

lstTable= pickle.load(readfile)
readfile.close()
input("Press Enter to Exit")


# This is to show a simple pickling script.
# This would allow you to find a new file named dogs in the same directory as your Python script.













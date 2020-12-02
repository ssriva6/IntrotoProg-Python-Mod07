# Assignment 7

## Examples of Pickling and Error Handling on Python
### Introduction: 
For this assignment I was asked to come up with my own example of pickling and error handling. For this assignment, I read through the textbook, watched the class videos and looked through examples online. First I will go through the pickling example and then I will go through the error handling example.

#### Pickling:
Pickling is very straightforward. Instead of writing the characters to the file I will write a pickled object to the file of my choice. Step 1 would be to make sure that the “pickle” is imported in order for python to process the script correctly. Step 2 would be to have a dictionary. For my dictionary I had types of dogs. The list consisted of 5 dogs with input values. Then once that is done step 3 would be to define a file name, write code to open the file and write “wb” to indicate that it is a binary code that you are writing into the file. The next line is with “rb” that reads the file in binary code. Then you want to write the pickle and unpickle code so that the pickled information can be unpickled for the user to use the strings. Once I wrote this code, I finished this code with a pickle.dum(dogs_dict, outfile) which basically will create that new file in your folder for you, same folder where your python script is saved- in this case it would be assignment 7 folder. Then the last line of code will load the pickled file. All of this is captured in the screenshot image below (Figure1). 


![Code for Pickling](https://github.com/ssriva6/IntrotoProg-Python-Mod07/blob/main/Picture1.png "Code for Pickling") 
#### Figure 1. Code for pickling on Pycharm

When you run this in Pycharm you should see just the file location displayed in the first line and then it will prompt you to a message that says process finished (Figure 2).

![Running pickling](https://github.com/ssriva6/IntrotoProg-Python-Mod07/blob/main/Picture2.png "Running pickling")
#### Figure 2: Running Pickling in Pycharm


![Running Pickling in Terminal](https://github.com/ssriva6/IntrotoProg-Python-Mod07/blob/main/Picture3.png "Running Pickling in Terminal")
 #### Figure 3: Running Pickling in Terminal


![Stored File](https://github.com/ssriva6/IntrotoProg-Python-Mod07/blob/main/Picture4.png "Stored File")
#### Figure 4: Stored Text File




#### Error Handling in Python
For this error handling example I chose to use a math problem to show how the try, except and else statements work together. Error handling is basically when a exception occurs when normal flow of the program instructions are interrupted. I started off with a print statement that displays to the user that we are going to be calculating the quotient of two numbers. That is followed by an try statement where it asks the user to enter an input for the first number. If the user enters a different character, the except function will come in and print “Enter numbers only”. If the user enters a number then it will proceed to asking the user for another input for the second number. This is done by inserting an “else” right after the except and print. If the user again fails to input a number, the except value error will kick in and let the user know that only numbers can be entered. Following that, if the user does enter a number correctly then the program will proceed to the else clause that will “try” num1/num2 to give you a quotient. I also added an except after the try: num1/num2 because I wanted to show the Zerodivisionerror exception. If the denominator is 0, then it will print” Re-Enter second number: can’t be zero”. If the denominator is not zero, then it will proceed with the last “else” statement of displaying the quotient. All of this code is captured in the screenshot image below (Figure 5). The output in Pycharm is shown in Figure 6 and the code run in Terminal is shown in Figure 7.


![Error Handling Code](https://github.com/ssriva6/IntrotoProg-Python-Mod07/blob/main/Picture5.png "Error Handling Code")
#### Figure 5: Code for Error Handling in Pycharm


![Running the Code](https://github.com/ssriva6/IntrotoProg-Python-Mod07/blob/main/Picture6.png "Running the code")
#### Figure 6: Running the code in Pycharm


![Running Error Handling on Terminal](https://github.com/ssriva6/IntrotoProg-Python-Mod07/blob/main/Picture7.png "Running Error Handling")
#### Figure 7: Running Error Handling on Terminal 


### Summary: 
In this assignment I was able to write about two simple examples of pickling and error handling in python. I was able to use the internet sources, readings and videos to draft my own code for these two examples. This can be found on my Github as well. Here is the link to my upload: https://github.com/ssriva6/IntrotoProg-Python-Mod07


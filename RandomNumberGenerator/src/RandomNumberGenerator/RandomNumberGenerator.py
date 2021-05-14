'''
Created on May 11, 2021

Simple GUI using Tkinter for a random number generator. User inputs the desired range for a number
to be generated (in integer form) and clicks "generate" to obtain output. Negative numbers are allowed.

@author: Eric Li
'''

from random import randint
import Tkinter
import tkMessageBox

# Main window of the GUI with name and size.
mainWindow = Tkinter.Tk()
mainWindow.title("Random Number Generator")
mainWindow.geometry("400x400")

# Top frame of GUI where upper and lower bound will be displayed.
boundsFrame = Tkinter.Frame(mainWindow)
boundsFrame.pack(pady = 20, side = Tkinter.TOP)

# Label and text box entry for lower bound.
lowerBoundFrame = Tkinter.Frame(boundsFrame)
lowerBoundFrame.pack(side = Tkinter.LEFT)
lowerBoundLabel = Tkinter.Label(lowerBoundFrame, text = "Lower Bound: ")
lowerBoundLabel.pack(side = Tkinter.LEFT)
lowerBoundInput = Tkinter.Entry(lowerBoundFrame, bd = 3, relief = Tkinter.GROOVE, width = 10)
lowerBoundInput.pack(side = Tkinter.RIGHT)

# Label and text box entry for upper bound.
upperBoundFrame = Tkinter.Frame(boundsFrame)
upperBoundFrame.pack(side = Tkinter.RIGHT)
upperBoundLabel = Tkinter.Label(upperBoundFrame, text = "Upper Bound: ")
upperBoundLabel.pack(side = Tkinter.LEFT)
upperBoundInput = Tkinter.Entry(upperBoundFrame, bd = 3, relief = Tkinter.GROOVE, width = 10)
upperBoundInput.pack(side = Tkinter.RIGHT)

# Function used to generate a random number.
def generateNumber():
    # Gets the two inputs from the Entry boxes.
    lowerNum = lowerBoundInput.get()
    upperNum = upperBoundInput.get()
    
    # If the first character of the lower bound is '-' representing a negative.
    if lowerNum[0] == '-':
        # Removes the first character.
        lowerNum = lowerNum[1:]
        
        # If the first character of the upper bound is '-' representing a negative
        # Both the lower bound and upper bound will be negative.
        if upperNum[0] == '-':
            # Removes the first character.
            upperNum = upperNum[1:]
            
            # Checks if both the lower bound and upper bound are digits after the negative sign has
            # been removed from both.
            if lowerNum.isdigit() and upperNum.isdigit():
                
                # Checks to see if the absolute value of the lower bound is greater than the absolute
                # value of the upper bound. If so, will generate a random number with the given bounds.
                if int(lowerNum) > int(upperNum):
                    generatedNum.config(text = str(randint(int(lowerNum) * -1, int(upperNum) * -1)))
                
                # If the absolute value of the lower bound is less than the absolute value of the upper
                # bound when both values are negative, will display pop-up message with error.
                else:
                    tkMessageBox.showerror("Error", "Lower bound cannot be greater than the upper bound.")
           
            # If either the lower bound or upper bound is not a digit after the negative sign has been
            # removed, will display pop-up message with error.
            else:
                tkMessageBox.showerror("Error", "Please input integers for bounds.")
        
        # If the lower bound is negative but upper bound is positive.
        else:
            # If both the lower bound and upper bound are digits after the negative signs are
            # removed, will generate random number with given bounds.
            if lowerNum.isdigit() and upperNum.isdigit():
                generatedNum.config(text = str(randint(int(lowerNum) * -1, int(upperNum))))
            
            # If either the lower bound or upper bound is not a digit after the negative sign has been
            # removed, will display pop-up message with error.
            else:
                tkMessageBox.showerror("Error", "Please input integers for bounds.")
    
    # If the upper bound is negative.
    elif upperNum[0] == '-':
        upperNum = upperNum[1:]
        
        # If the lower bound is positive and upper bound is negative, will display pop-up message with error.
        if lowerNum.isdigit() and upperNum.isdigit():
            tkMessageBox.showerror("Error", "Lower bound cannot be greater than the upper bound.")
        
        # Displays pop-up message with error if bounds are not digits.
        else:
            tkMessageBox.showerror("Error", "Please input integers for bounds.")
    
    # Displays pop-up message with error if either the lower bound or upper bound is not a digit.
    elif not lowerNum.isdigit() or not upperNum.isdigit():
        tkMessageBox.showerror("Error", "Please input integers for bounds.")
    
    # Displays pop-up message with error if the lower bound is greater than the upper bound.
    elif int(lowerNum) > int(upperNum):
        tkMessageBox.showerror("Error", "Lower bound cannot be greater than the upper bound.")
    
    # Generates random number with correct bounds if all other errors have been checked.
    else:
        generatedNum.config(text = str(randint(int(lowerNum), int(upperNum))))
        

# Button used to generate a number with the generateNumber function after it is clicked.
generateButton = Tkinter.Button(mainWindow, text = "Generate", command = generateNumber)
generateButton.pack(side = Tkinter.TOP)

# Label that displays "Generated Number:"
# Actual generated number will go below this label.
numGeneratedLabel = Tkinter.Label(mainWindow, text = "Generated Number:")
numGeneratedLabel.pack(pady = 20, side = Tkinter.TOP)

# Label to display the generated number.
generatedNum = Tkinter.Label(mainWindow, text = "")
generatedNum.pack(side = Tkinter.TOP)

# Function used to reset the GUI
def clearAllInput():
    lowerBoundInput.delete(0, 'end')
    upperBoundInput.delete(0, 'end')
    generatedNum.config(text = "")

# Button to clear all input - lower bound, upper bound, and recent generated number, if applicable.
clearAllButton = Tkinter.Button(mainWindow, text = "Clear All", command = clearAllInput)
clearAllButton.pack(pady = 10, side = Tkinter.BOTTOM)

# Execute GUI.
mainWindow.mainloop()


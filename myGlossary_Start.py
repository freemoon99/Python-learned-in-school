# myGlossary_Final.py
# Glossary program using dictionary data type

from tkinter import *

# key input function:
def click():
    entered_text = entry.get()  #collect text from text entry box
    output.delete(0.0, END) #clear text box
    try:
        definition = my_glossary[entered_text]
    except:
        definition = "There is no entry for this word."
    output.insert(END, definition)

##### main:
window = Tk()
window.title("My Coding Club Glossary")

# generate label
Label (window, text="Enter the world you want defining:").grid(row=0, column=0, sticky=W)

# generate text entry widget
entry = Entry(window, width=20, bg="light green")
entry.grid(row=1, column=0, sticky=W)

# add submit button
Button(window, text="SUBMIT", width=5, command=click).grid(row=2, column=0, sticky=W)

# generate another label
Label (window, text="\nDefinition").grid(row=3, column=0, sticky=W)


# generate text box
output = Text(window, width=75, height=6, wrap=WORD, background="light green")
output.grid(row=4, column=0, columnspan=2, sticky=W)

# glossary:
my_glossary = {
    'Algorithm': 'A step-by-step description of the job of computer',
    'Arguments': 'A piece of information required by the function that can perform the operation. Usually a character or number is used and is used with my_function (argument). ',
    'Binary number': 'number in binary notation',
    'Bug': 'A piece of code that provides a reason why a program fails to work properly or does not work at all',
    'Casting': 'The process of converting from one data type to another. For example, if the number is in character format from time to time, and you need to convert it to a number format, use the following conversion: int ("3") ',
    'Comment': 'This is text written to a computer program that is read by humans and is ignored by the computer during program execution. In Python, all comments begin with a hash sign (#). ',
    'Comparison operator': 'Sometimes calls a logical operator to compare data in a program. This operator includes the ==,> operator. ',
    'Constant': 'Unchanged number. It is good practice to name a constant name in upper case. Example: SPEED_OF_LIGHT ',
    'Container': 'Container data types are data types that store multiple data types together and can contain multiple containers. Container data types are used in tuples, lists, and dictionaries. ',
    'Data type': 'Other types of information stored on your computer are, for example, real numbers, integers, strings, tuples, lists and dictionaries.',
    'Debugging': 'Finding program bugs',
    'Default': 'Starting value for argument or variable',
    'Dictionary': 'You can store data in the form of a different key-value pair with an unaligned container datatype.',
    'Equals operator': 'Equals sign is used to include a value in a variable when coding. For example, n = 2 means to put a value of 2 in variable n. ',
    'Escape': 'In Python, any character that is meaningful is escaped when it is needed for a regular string, so the computer is recognized as a regular string.',
    'Run': 'Execute some code',
    'Mist': 'Numeric datatype with decimal values with decimal point',
    'Frame': '"tkinter" is a type of widget that is used to configure the layout of a complex user interface with group widgets that contain other widgets. ',
    'for loop': 'One kind of useful loop that uses container data types and iterates',
    'Function': 'reusable code snippet',
    'Global variable': 'Variables available anywhere in the program',
    'GUI': 'Graphical user interface means. Buttons and entry widgets, windows is an example of a graphical user interface. ',
    'Hacking': 'It means to rip some of the already created programs to make them behave differently.',
    'IDE': 'means "Integrated Development Environment", IDLE is one of them. It is a text editor with useful features for programmers. ',
    'IDLE': '"Integrated development environment", which comes with Python 3 installation. ',
    'Index': 'A string, tuple, or string of numbers to refer to a value in a list. Each entry in the container data type is indexed, with 0 indicating the first item and 1 indicating the next item. Index values �뗢�땇re incremented sequentially. ',
    'Infinite loop': 'means a piece of code that runs forever, and generally this is not a good situation.',
    'Integer': 'Can not have a decimal value as a numeric datatype, it must be an integer',
    'Interactive mode': 'IDLE (Python IDE - integrated development environment) to go outside the code to test without saving.',
    'Key': 'This is the value corresponding to the index of a string, tuple or list in the dictionary, defined by the programmer, and can be a string, a number, a real number, or a tuple. key: corresponds to key in pair ',
    'List': 'Any type of value can be added or deleted as an element and is an aligned container type. Similar to tuples, index values start at 0. ',
    'Local variables':' Variables defined within a function are only available inside the function ',
    'Logical operator': 'See comparison operator',
    'Loops':' Code snippet that repeats until a certain condition is met ',
    'Arithmetic operator': 'This operator is provided as a mathematical function to perform functions on some numeric data types. Yes. Multiplication or addition ',
    'Method': 'The name of the function calling the function',
    'Module': 'Python file containing functions available in other programs',
    'Modulo': 'The mathematical operator used to return the remainder in division calculations. For example, if you run 22% 7, 1 is returned. ',
    'Operator': 'A symbol that performs a simple function that is used to do things such as multiply or compare two numbers. See also the equals operator. ',
    'Aligned container': 'refers to a datatype whose values within the container are aligned. Aligned containers have tuples or lists. In the dictionary, this is an unaligned datatype. ',
    'Output': 'Send data from a program to a screen or printer or other readable program for easier management', 
    'Parameter': 'Another name for the argument used in the function',
    'Refactoring': 'The process of changing the structure of your code to reduce the number of iterations. ',
    'Return': '1. This is the value created after the function has finished executing and is a Python reserved word. \ N2. The enter key on the keyboard that represents the end of line.',
    'Script mode': 'Use IDLE to help you write code to save to a file',
    'Slicing': 'The process of extracting a portion of a string or container variable. Also called a slice of an array. ',
    'Sentence': 'Used in this book to mean a piece of code. Strictly speaking, it is a piece of code that represents a command or action. ',
    'String': 'Text type stored in variable',
    'Grammar error': 'Grammar error occurs when the program\'s code can not be recognized after running the program. For example, when you are missing a closing parenthesis in your code. ',
    'tkinter': 'Python programs provide useful methods for importing packages of classes and creating windows and image drawings and animations.',
    'Tuple': 'Sorted data type index starts at 0. The value inside the tuple can not be changed. ',
    'Value': 'Anything that can be stored in a variable, such as an element of a container type',
    'Variable': 'The name used to refer to the value stored in the computer memory, which can be used to refer to the data more loosely.',
    'while loop': 'The type of loop loop that repeats while the comparison statement returns "True"',
    'Widgets': 'GUI elements that point to buttons or text entry boxes'
    }

##### execute main loop
window.mainloop()

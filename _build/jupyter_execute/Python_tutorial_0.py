#!/usr/bin/env python
# coding: utf-8

# # Basic introduction of python

# ## Setting the environment for Python
# * [Anaconda](https://www.anaconda.com/products/individual) : Include essential packages for basic scientific computation. It is easy to install it just follow the instruction.
# * Not required, but easy to use for beginners.

# ## Why numerical approach? 
# 
# ### Need to confirm the mechanism of your idea 
#   - An idea for the novel physics
#   - Numerical experiments driven by scientific ideas
#   - Numerical experiments driven theoretical ideas
# 
# ### Need to connect with real experiments 
#   - To strenthen the abstract idea and connect with real world
#   - Get additional information that is difficult to access in experiments and make prediction that is accessible for experiments
# 
# ### Numerics for many body physics is non-trivial! 
#   - The problem itself is a intelletral challenging and interesting discrete mathmetical problems. 
#   - Hardware limitation force one to think in a smart way
#   
# ### Generate data to convey what you mean
#   - Statistics
#   - Plots
# 
# ## My point of view of numerical approaches
# 
# ### Level of numerical loading
# 
# * Light: Mathematica, Python, matlab (For quick checking and benchmark. Once the simple concept passes, use the medium or heavy numerical approach)
# * Heavy: C/C++, Fortran
# 
# 
# ## Why Python? 
# 
# ### Simple, well-structured, general-purpose language
#   - Readability great for quality control and collaboration
#   - Code how you think: many books now use python as pseudocode
#   
# ### High-level 
#   - Rapid development
#   - Do complicated things in few lines
# 
# ### Interactive 
#   - Rapid development and exploration
#   - No need to compile, run, debug, revise, compile
#   - Data collection, generation, analysis and publication plotting in one place
# 
# ### Speed
#   - Usually plenty fast -- will discuss more
#   - Your development time is more important than CPU time
#   - Not as fast as C, C++, Fortran but these can be easily woven in where necessary
# 
# ### Vibrant community
#   - Great online documentation / help available
#   - Open source
#   
# ### Rich scientific computing libraries
#   - Don't reinvent the wheel. Only reinvent important wheels!
#     
# ### Accessible for everyone. No need to pay money
# 
# 
# 
# 
# 
# ## Scientific Python Key Components
# 
# The core pieces of the scientific Python platform are:
# 
# **[Python](http://www.python.org)**, the language interpreter 
#   - Many standard data types, libraries, etc
#   - Python 3.7 is the current version; use this
#   - Python 2.7 (released 2010) is still maintained but will die in 2020
# 
# **[Jupyter](http://www.jupyter.org)**: notebook based (in browser) interface
#   - Builds on **[IPython](http://www.ipython.org)**, the interactive Python shell
#   - Interactive manipulation of plots
#   - Easy to use basic parallelization
#   - Lots of useful extra bells and whistles for Python
#   
# **[Numpy](http://www.numpy.org)**, powerful numerical array objects, and routines to manipulate them. 
#   - Work horse for scientific computing
#   - Basic linear algebra (np.linalg)
#   - Random numbers (np.random)
#   
# **[Scipy](http://www.scipy.org)**, high-level data processing routines. 
#   - Signal processing (scipy.signal)
#   - Optimization (scipy.optimize)
#   - Special functions (scipy.special)
#   - Sparse matrices and linear algebra
# 
# **[Matplotlib](http://www.matplotlib.org)**, plotting and visualization
#   - 2-D and basic 3-D interactive visualization
#   - “Publication-ready” plots
#   - LaTeX labels/annotations automagically
# 
# **[Pandas](https://pandas.pydata.org)**, data analysis/management
#   - data structures for relational data manipulation
#   - useful in observational/numerical analysis
#   - Won't discuss here
# 
# **[Mayavi](http://code.enthought.com/projects/mayavi/)**, 3-D visualization
#   - For more sophisticated 3-D needs (won't discuss)
# 
# ## Jupyter Workflow
# 
# ### Two primary workflows:
# 
# 1. Work in a Jupyter/IPython notebook. Write code in cells, analyze, plot, etc. Everything stored in **.ipynb** file.
# 2. Write code in **.py** files using a text editor and run those within the IPython notebook or from the shell.
# 
# We still stick to the first. 
# 
# While you are using a notebook, there is a **kernel** running which actually executes your commands and stores your variables, etc. If you quit/restart the kernel, all variables will be forgotten and you will need to re-execute the commands that set them up. This can be useful if you want to reset things. The input and output that is visible in the notebook is saved in the notebook file.
# 
# *Note:* .py files are called **scripts** if they consist primarily of a sequence of commands to be run and **modules** if they consist primarily of function definitions for import into other scripts/notebooks. 
# 
# ### Notebook Usage
# 
# Two modes: editing and command mode.
# 
# Press escape to go to command mode.
# Press return to go into editing mode on selected cell.
# 
# In command mode:
# 1. Press h for a list of keyboard commands.
# 2. Press a or b to create a new cell above or below the current.
# 3. Press m or y to convert the current cell to markdown or code.
# 4. Press shift-enter to execute.
# 5. Press d d to delete the current cell. (Careful!)
# 
# In editing mode:
# 1. Press tab for autocomplete
# 2. Press shift-tab for help on current object
# 3. Shift-enter to execute current cell
# 
# Two types of cells:
# 1. Markdown for notes (like this)
# 2. Code for things to execute
# 
# 
# 
# **Exercise**
# 
# Try editing this markdown block to make it more interesting. For example, type in some equations $e^{i\pi}+1=0$.
# 
# 

# **Exercise**
# 
# Execute the next block and then create a new block, type x. and press tab and shift-tab.

# In[1]:


x = 10


# **Exercise**
# 
# Run this stuff.

# In[2]:


print('Hello, world!')


# In[3]:


"Hello, world!"


# In[4]:


2.5 * 3


# In[5]:


3**3


# In[6]:


3 + 3


# In[7]:


"ab" + "cd"


# In[8]:


"Hello" == 'Hello'


# ## Variables and Objects
# 
# Everything in memory in Python is an object. Every object has a type such as int (for integer), str (for strings) or ndarray (for numpy arrays). Variables can reference objects of any type and that type can change.
# 
# The equals sign in programming does not mean 'is equal to' as in math. It means **'assign the object on the right to the variable on the left'**.
# 

# In[9]:


a = 3


# In[10]:


a


# In[11]:


type(a)


# In[12]:


a+a


# In[13]:


2+a


# In[14]:


import numpy as np


# In[15]:


a = np.array([1,2])


# In[16]:


a


# In[17]:


type(a)


# In[18]:


# All objects have properties, accessible with a .
a.shape


# In[19]:


a+a


# In[20]:


2+a


# In[21]:


a = "Hello, world!"


# In[22]:


a


# In[23]:


type(a)


# In[24]:


a+a


# In[25]:


2+a


# ### Overloading 
# 
# Operators and functions will try to execute no matter what type of objects are passed to them, but they may do different things depending on the type. + adds numbers and concatenates strings.

# ### Variables as References
# 
# All variables are **references** to the objects they contain. Assignment does not make copies of objects.

# In[26]:


a = np.array([1,2])
a


# In[27]:


b = a
b


# In[28]:


b[0] = 0
b


# In[29]:


a


# ## Types of Objects
# 
# ### Basic Types
# 
# 1. Numeric, Immutable
#   1. Integer: -1, 0, 1, 2, ...
#   2. Float: 1.2, 1e8
#   3. Complex: 1j, 1. + 2.j
#   4. Boolean: True, False
# 2. Strings, "hi"
# 3. Tuples, (2,7, "hi")
#   - Ordered collection of other objects, represented by parentheses
#   - can't change after creation (*immutable*)
# 3. Lists, [0,1,2,"hi", 4]
#   - Ordered collection of other objects, represented by square brackets
#   - can add/remove/change elements after creation (*mutable*)
# 4. Dictionaries, {'hi': 3, 4: 7, 'key': 'value'}
# 5. Functions, def func()
# 
# ### Common Scientific Types 
# 
# 6. NumPy arrays, array([1,2,3])
#   - Like lists but all entries have same type
# 7. Sparse arrays, scipy.sparse
# 8. Pandas DataFrames, high level 'table' a bit like an excel spreadsheet

# ## Basic Types: Numeric
# 
# There are 4 numeric types: 
# - int: positive or negative integer
# - float: a 'floating point' number is a real number like 3.1415 with a finite precision
# - complex: has real and imaginary part, each of which is a float
# - bool: two 'Boolean' values, True or False
# 

# In[30]:


a = 4
type(a)


# In[31]:


c = 4.
type(c)


# In[32]:


a = 1.5 + 0.1j
type(a)


# In[33]:


a.real


# In[34]:


a.imag


# In[35]:


flag = (3>4)
flag


# In[36]:


type(flag)


# In[37]:


type(True)


# In[38]:


# Type conversion
float(1)


# ### Careful with integer division!
# 
# In Python 3, dividing integers promotes to a float. Use // for integer division.

# In[39]:


3/2


# In[40]:


3/2.


# ***Force integer division:***

# In[41]:


3//2


# ## Basic Types: Strings
# 
# Strings are **immutable** sequences of characters. This means you can't change a character in the middle of a string, you have to create a new string. 
# 
# Literal strings can be written with single or double-quotes. Multi-line strings with triple quotes. 'Raw' strings are useful for embedding LaTeX because they treat backslashes differently.

# In[42]:


'Hello' == "Hello"


# In[43]:


a = """This is a multiline string.
Nifty, huh?"""


# In[44]:


a


# In[45]:


print("\nu")


# In[46]:


print(r"\nu")


# In[47]:


a = 3.1415


# In[48]:


# Simple formatting (type convert to string)
"Blah " + str(a)


# In[49]:


# Old style string formatting (ala sprintf in C)
"Blah %1.2f, %s" % (a, "hi")


# In[50]:


# New style string formatting 
"Blah {:1.2f}, {}".format(a, "hi")


# ## Basic Types: Lists
# 
# Python lists store **ordered** collections of arbitrary objects. They are efficient maps **from index to values**. Lists are represented by square brackets [ ]. 
# 
# Lists are **mutable**: their contents can be changed after they are created.
# 
# It takes time O(1) to:
# 1. Lookup an entry at given index.
# 2. Change an item at a given index.
# 3. Append or remove (pop) from the end of the list. 
# 
# It takes time O(N) to:
# 1. Find items by value if you don't know where they are.
# 2. Remove items from near the beginning of the list.
# 
# You can also grab arbitrary **slices** from a list efficiently.
# 
# Lists are 0-indexed. This means that the first item in the list is at position 0 and the
# last item is at position N-1 where N is the length of the list.

# In[51]:


days_of_the_week = ["Sunday","Monday","Tuesday",
                    "Wednesday","Thursday","Friday"]


# In[52]:


days_of_the_week[0]


# In[53]:


# The slice from 2 to 5 (inclusive bottom, exclusive top)
days_of_the_week[2:5]


# In[54]:


days_of_the_week[-1]


# In[55]:


# every other day
days_of_the_week[0:-1:2]


# In[56]:


# every other day (shorter)
days_of_the_week[::2]


# In[57]:


# Oops!
days_of_the_week.append("Saturday")


# In[58]:


days_of_the_week[-1]


# In[59]:


days_of_the_week[5] = "Casual Friday"


# In[60]:


days_of_the_week


# In[61]:


# Get the length of the list
len(days_of_the_week)


# In[62]:


# Sort the list in place
days_of_the_week.sort()


# In[63]:


days_of_the_week


# **Remember tab completion** Every thing in Python (even the number 10) is an object. Objects can have methods which can be accessed by the notation a.method(). Typing a.<TAB> allows you to see what methods an object a supports. Try it now with days_of_the_week:
# 

# In[64]:


days_of_the_week.


# **Each item is arbitrary**: You can have lists of lists or lists of different types of objects.

# In[65]:


aList = ["zero", 1, "two", 3., 4.+0j]
aList


# In[66]:


listOfLists = [[1,2], [3,4], [5,6,7], 'Hi']


# In[67]:


listOfLists[2][1]


# ## Basic Types: Dictionaries
# 
# A dictionary is an efficient map **from keys to values**. They are represented by curly brackets {}. 
# 
# Dictionaries are **mutable** but all **keys must be immutable**. IE. keys can be strings, numbers, or tuples thereof but not lists or other dictionaries. Values can be anything.
# 
# It is unordered but takes time O(1) to:
# 1. Lookup a value from a key
# 2. Add a key, value pair
# 3. Remove a key, value pair
# 
# It takes time O(N) to find an entry with a particular value.
# 
# You can iterate through all the entries efficiently O(N).

# In[68]:


tel = {'emmanuelle': 5752, 'sebastian': 5578}
tel['francis'] = 5915


# In[69]:


tel


# In[70]:


tel['sebastian']


# In[71]:


tel.keys()


# In[72]:


tel.values()


# In[73]:


len(tel)


# In[74]:


'francis' in tel


# In[75]:


del tel['francis']


# In[76]:


tel


# ## Basic Types: Tuples
# 
# A tuple is an **ordered** collection of objects. They are represented by round parantheses ().
# 
# Tuples are almost like lists but they are **immutable**. This means that they cannot be changed once they are created. 

# In[77]:


t = (1,2,3,'Hi')
t


# In[78]:


# IMMUTABLE !
t[0] = 2


# The empty tuple and length 1 tuples have special notation since parentheses can also represent grouping.

# In[79]:


emptyTuple = ()
emptyTuple


# In[80]:


lengthOne = ('hi',)
lengthOne


# In[81]:


notLengthOne = ('hi')
notLengthOne


# In[82]:


notLengthOne[0]


# ## Control Flow
# 
# The flow of a program is the order in which the computer executes the statements in the code. Typically, this is in order from top to bottom. However, there are many cases where we want to change the flow in some way. For example, we might want to divide two numbers but only if the divisor is not zero. Or we might want to iterate: repeat a block of code many times for each value in some list. The commands which allow these are called control flow commands.
# 
# **WARNING**: Python cares about **white space**! You must **INDENT CORRECTLY** because that's how Python knows when a block of code ends. 
# 
# Typically, people indent with 4 spaces per block but 2 spaces or tabs are okay. They must be consistent in any block.

# ### If/elif/else

# In[83]:


if 2>3:
    print("Yep")
    print("It is")

elif 3>4:
    print("Not this one either.")
    
else:
    print("Not")
    print("At all")


# ### For Loops ###
# 
# For loops *iterate* through elements in a collection. This can be a list, tuple, dictionary, array or any other such collection. 
# 
# These are the most *Pythonic* way to think about iterations.

# In[84]:


for i in range(5):
    j = i**3
    print("The cube of " + str(i) + " is " + str(j))


# In[85]:


for day in days_of_the_week:
    print("Today is " + day)


# In[86]:


for key in tel:
    print(key + "'s telephone number is " + str(tel[key]))


# **Enumerate** to get index and value of iteration element

# In[87]:


words = ('your', 'face', 'is', 'beautiful')

for (i, word) in enumerate(words):
    print(i, word)


# ### While Loops
# 
# Repeats a block of code while a condition holds true.

# In[88]:


x = 5

while x > 0:
    print("Bark " + str(x))
    x -= 1


# ## Functions
# 
# Any code that you call multiple times with different values should be wrapped up in a function. For example:

# In[89]:


def square(x):
    """Return the square of x."""
    return x*x


# In[90]:


get_ipython().run_line_magic('pinfo', 'square')


# In[91]:


square(9)


# In[92]:


def printAndSquare(x):
    """Print the square of x and return it."""
    y = x**2
    print(y)
    return y


# In[93]:


get_ipython().run_line_magic('pinfo', 'printAndSquare')


# In[94]:


printAndSquare(8)


# ### Functions are Objects ###
# 
# Functions are just like any object in Python:

# In[95]:


type(square)


# Make another variable refer to the same function:

# In[96]:


a = square


# In[97]:


a(5)


# A function being passed to another function.

# In[98]:


def test():
    print("In Test!")
    return

def callIt(fun):
    print("In callIt!")
    fun()
    return


# In[99]:


callIt(test)


# In[ ]:





from rich.console import Console
from rich.theme import Theme
from rich.markdown import Markdown
from rich.prompt import Prompt

from week1.method1 import method1
from week1.method2 import method2
from week1.method3 import method3
from week1.gamma import gammaTransection

from week2.RGB import rgbToBgr
from week2.RGB2 import rgb2
from week2.logaritmic import logTransformation

from week3.resize import resize
from week3.negative import getNegative

from week4.readableText import readableText
from week4.GaussianNoise import addNoise

from week5.convertBit import GrayScaleToBit

from week6.filter import addFilter

from week7.paperAndSalt import paperAndSalt



custom_theme = Theme({"success":"bold green", "error":"bold red","warning":"bold yellow",})
console = Console(theme=custom_theme)

#Main menu markdown
markdown = """

# Image Processing

First week exercise : 1 \n
Second week exercise : 2\n
Third week exercise : 3\n
Fourth week exercise : 4\n
Fifth week exercise : 5\n
Sixth week exercise : 6\n
Seventh week exercise : 7\n

"""

# 1st week exercise markdown
markdown2 = """

# First week exercises

Method 1 : 1 \n
Method 2 : 2 \n
Method 3 : 3 \n
Gamma Transformation 4 : 4 \n 
"""

# 2nd week exercise markdown
markdown3 = """

# Second week exercise

Convert BGR and RGB  : 1 \n
RGB color Blue, Green, Red colors : 2 \n
Logaritmic Transformation : 3 \n
\n
"""

# 3rd week exercise markdown
markdown4 = """

# Third week exercise

Resize an image  : 1 \n
Get negative an image  : 2 \n
\n
"""

# 4th week exercise markdown
markdown5 = """

# Fourth week exercise

Add gaussian noise on an image  : 1 \n
Readable text  : 2 \n
\n
"""

# 5th week exercise markdown
markdown6 = """

# Fifth week exercise

Convert an image to 8, 16 and, 16 bits  : 1 \n

\n
"""

# 6th week exercise markdown
markdown7 = """

# Sixth week exercise

Add filters on an image  : 1 \n

\n
"""

# 7th week exercise markdown
markdown8 = """

# Seventh week exercise

Paper and salt noise example and histogram   : 1 \n
\n
"""






def main():
    md = Markdown(markdown)
    console.print(md)
    #weekSelection = input("Haftayı seç aga: ")
    Prompt.illegal_choice_message = "Wrong choice!"
    weekSelection = Prompt.ask("Choose the week",choices=["1", "2", "3", "4", "5", "6", "7"])
    switch(weekSelection)


#Week switch
def switch(choise):
    if choise == "1":
        md2 = Markdown(markdown2)
        console.print(md2)
        Prompt.illegal_choice_message = "Wrong exercise choice!"
        workSelection = Prompt.ask("Choose the exercise",choices=["1", "2", "3","4"])
        switch2(workSelection) 

    elif choise == "2":
        md3 = Markdown(markdown3)
        console.print(md3)
        Prompt.illegal_choice_message = "Wrong exercise choice!"
        workSelection = Prompt.ask("Choose the exercise",choices=["1", "2","3"])
        switch3(workSelection) 

    elif choise == "3":
        md4 = Markdown(markdown4)
        console.print(md4)
        Prompt.illegal_choice_message = "Wrong exercise choice!"
        workSelection = Prompt.ask("Choose the exercise",choices=["1","2"])
        switch4(workSelection)

    elif choise == "4":
        md5 = Markdown(markdown5)
        console.print(md5)
        Prompt.illegal_choice_message = "Wrong exercise choice!"
        workSelection = Prompt.ask("Choose the exercise",choices=["1","2"])
        switch5(workSelection)

    elif choise == "5":
        md6 = Markdown(markdown6)
        console.print(md6)
        Prompt.illegal_choice_message = "Wrong exercise choice!"
        workSelection = Prompt.ask("Choose the exercise",choices=["1"])
        switch6(workSelection)
        
    elif choise == "6":
        md7 = Markdown(markdown7)
        console.print(md7)
        Prompt.illegal_choice_message = "Wrong exercise choice!"
        workSelection = Prompt.ask("Choose the exercise",choices=["1"])
        switch7(workSelection)

    elif choise == "7":
        md8 = Markdown(markdown8)
        console.print(md8)
        Prompt.illegal_choice_message = "Wrong exercise choice!"
        workSelection = Prompt.ask("Choose the exercise",choices=["1"])
        switch8(workSelection)

    else:
        console.print("There is nothing here!",style="error")

#first week exercise switch
def switch2(choise):
    if choise == "1":
        method1()
    elif choise == "2":
        method2()
    elif choise == "3":
        method3()
    elif choise == "4":
        gammaTransection()
    else:
        console.print("There is nothing here!",style="error")

#second week exercise switch
def switch3(choise):
    if choise == "1":
        rgbToBgr()
    elif choise == "2":
        rgb2()
    elif choise == "3":
        logTransformation()
    else:
        console.print("There is nothing here!",style="error")

#third week exercise switch
def switch4(choise):
    if choise == "1":
        resize()
    elif choise == "2":
        getNegative()
    # elif choise == "3":
    #     method3()
    else:
        console.print("There is nothing here!",style="error")

#fourth week exercise switch
def switch5(choise):
    if choise == "1":
        addNoise()
    elif choise == "2":
        readableText()
    # elif choise == "3":
    #     method3()
    else:
        console.print("There is nothing here!",style="error")

#fifth week exercise switch
def switch6(choise):
    if choise == "1":
        print("5.hafta")
        GrayScaleToBit()
    else:
        console.print("There is nothing here!",style="error")

#sixth week exercise switch
def switch7(choise):
    if choise == "1":
        addFilter()
    else:
        console.print("There is nothing here!",style="error")

#seventh week exercise switch
def switch8(choise):
    if choise == "1":
        paperAndSalt()
    # elif choise == "2":
    #     method2()
    # elif choise == "3":
    #     method3()
    else:
        console.print("There is nothing here!",style="error")

main()
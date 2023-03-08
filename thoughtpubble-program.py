### Running Question/Thought List

### Save as MD file.
### Save as separate files wiht dates
### database of questions, stored in list

### Parameters of topics / subjects, macros

# Query
### What's the questions/thoughts for today?
###### Date/Time/Mood/
###### Topic/Subject

### Print the prompt
### "...Is there another thought for today?"
# Query

### .......
### Print the prompts(s)

import os, time

dataThoughtBubble = []

def program_RTL_FileCreate():

    if os.path.exists("" + str(time.get_clock_info)): ### of the same date
        open("", "a")
    else:
        open("", "w")
    

def program_RTL_DecoIntro():
    print()

def program_RTL_DecoThinkSim():
    ### Decorator, running thought
    for x in range(0, 5):             
        print("."+ "\n")

def program_RTL_Inquiry(self, thought, date, time, topic, subject):
    inputThought = input("What questions/thoughts are on your mind, Greater?")
    date, time = int(input("Enter the timestamp? ")).split() ### Split the question, using one line.
    topic = input("What is the topic of said question?")
    subject = input("What is the subject of said question")

def main():

    questLoop = "Yes"

    while questLoop == "Yes" or questLoop == "yes" or questLoop == "y":
        program_RTL_Inquiry()

        questLoop = input("...Is there another thought for today?")

main()
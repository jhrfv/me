"""
Commenting skills:

NOTE: this file runs just fine, this is for you to learn to use the debugger!

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# I think this will print "what" from the some_words list by calling the print function
some_words = ["what", "does", "this", "line", "do", "?"]
print(some_words[0]) # it printed "what"

#it will print the words from some_words list
for word in some_words:
    print(word)
#it printed "what", "does", "this", "line", "do", "?"

#it will print the words from some_words list
for x in some_words:
    print(x)
#it printed "what", "does", "this", "line", "do", "?"

# it will print the words "what", "does", "this", "line"
print(some_words)

if len(some_words) > 3:
    print("some_words contains more than 3 words")
#it printed the whole list???


# it will print "system, node, release, version, machine, and processor"
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())


usefulFunction()

mylist = []
mylist.append("now, from this point down I have ran just the print(x) so you will see all the lines in the list not just those specifically defined for printing")
mylist.append('my list')
mylist.append('of course')
mylist.append("is awesome")
mylist.append("")
mylist.append("This is an interesting concept")
mylist.append("and I have enjoyed expanding on this concept")
mylist.append("")
mylist.append("another thing to note is that you can define 'mylist' with numbers, and you can print the specific list you defined with that number, but if the list doesn't exist, you will receive an error")
mylist.append("also I want to give credit where it's due, I am learning these from learnpython.org and am doing my best to expand on the concepts")
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3
print(mylist[3]) # prints 4
print(mylist[4]) # prints 5

# prints out any of the lines
for x in mylist:
    print(x)
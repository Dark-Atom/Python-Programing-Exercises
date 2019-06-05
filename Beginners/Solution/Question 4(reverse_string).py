# with help of for loop
def reverse_string(string):
    for i in reversed(string):
        yield i

#one liner in python
def oneliner_reverse_string(string):
    return string[::-1]

if __name__=="__main__":
    print(oneliner_reverse_string("HELLO"))
    print("".join(list(reverse_string("HELLO"))))

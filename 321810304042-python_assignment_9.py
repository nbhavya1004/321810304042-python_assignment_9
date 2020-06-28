#     1...    Write a pyhton program to read an entire text file.

# METHOD_1 :

file= open("myfile.txt","w") 
L = ["Mango\n","Apple\n","Banana \n"]  
file.write("Fruits\n") 
file.writelines(L) 
file.close() 
file = open("myfile.txt","r")  
print("Output of Read function is ")
print (file.read())

# METHOD_2 :

def read(a):
        txt = open(a)
        print(txt.read())
a=input("enter the file name:")
read(a)





#     2...     Write a python program to read first n lines of a file.

def readfirst(a, n):
        from itertools import islice
        with open(a) as f:
                for l in islice(f,n):
                        print(l,end ='')
a=input("enter the file name:")
readfirst(a,2)





#     3...     Write a python program to append text to a file and display the text.

# METHOD_1 :

file=open('myfile2.txt','w')
L2=["Hi\n","Hello\n","Gitam\n"]
file.writelines(L2)
file.close()
file=open('myfile2.txt','r')
print('Before appending the text:')
print(file.read())
file=open('myfile2.txt','a')
file.write('Good morning')
file.close()
file=open('myfile2.txt','r')
print('After appending the text:')
print(file.read())

# METHOD_2 :

def read(a):
        from itertools import islice
        with open(a,"w") as file:
                file.write("Python Exercises\n")
                file.write("Java Exercises")
        txt = open(a)
        print(txt.read())
read('alekhya.txt')





#     4...     Write a python program to read last n lines of a file.

def LastNLines(f,n):
    with open(f) as file:
        print('Last',n,"lines from file:",f)
        for line in (file.readlines() [-n:]):
            print(line, end='')
name=input("enter the file name:" )
n= int(input("no of last lines to read:"))
try:
    LastNLines(name,n)
except:
    print("file error....")





#     5...     Write a python program to read a file line by line store it into a variable.

def read(a):
        with open (a) as file:
                cse=file.readlines()
                print(cse)
a=input("enter the file name:")
read(a)





#     6...     Write a python program to read a file line by line and store it into a list.

def read(a):
        with open(a) as file:     
                list = file.readlines()
                print(list)
a=input("enter the file name:")
read(a)







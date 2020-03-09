try:
    f = open("simple.txt", "r")
    f.write("Test write to simple text!")
except:
    print("could not find file or read data!")
finally:
    print("I always work no matter what")
 

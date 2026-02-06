try:
    f = open("example.txt", "w")
    f.write("Hello, world!")
except IOError:
    print("Error: Could not write to file!")
finally:
    f.close()
    print("File closed successfully.")
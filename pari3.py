try:
    num = int("abc")  
    print("Number:", num)
except ValueError:
    print("Error: Invalid integer conversion!")
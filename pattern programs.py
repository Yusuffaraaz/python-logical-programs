# 10.PATTERN PRINTING

# 1.PRINTING SQUARE PATTERN

"""for i in range(5):
    for j in range(5) :
        print("*" , end = "  ")
    print()"""    

# 2.PRINTING TRIANGLE PATTERN

for i in range(5):
    for j in range(i+1) :
        print(j , end = "  ")
    print()

# 3.PRINTING REVERSE TRIANGLE PATTERN

"""for i in range(5):
    for j in range(i , 5) :
        print("*" , end = "  ")
    print()"""
    
# 4.PRINTING RIGHT SIDED TRIANGLE PATTERN

"""for i in range(5):
    for j in range(i , 5):
        print(" " , end = "")
    for j in range(i+1):
        print("*" , end = "")
    print()"""

# 5.PRINTING REVERESE RIGHT SIDED TRIANGLE PATTERN

"""for i in range(5):
    for j in range(i+1):
        print(" " , end = "")
    for j in range(i , 5):
        print("*" , end = "")
    print()"""

# 6.PRINTING HILL PATTERN

"""for i in range(5):
    for j in range(i , 5):
        print("" , end = " ")
    for j in range(i):
        print("*" , end = "")
    for j in range(i+1):
        print("*" , end = "")
    print()"""

# 7.PRINTING REVERSE HILL PATTERN

"""for i in range(5):
    for j in range(i+1):
        print("" , end = " ")
    for j in range(i , 5-1):
        print("*" , end = "")
    for j in range(i , 5):
        print("*" , end = "")
    print()"""    

# 8. DIAMOND PATTERN

"""for i in range(4):
    for j in range(i , 5):
        print("" , end = " ")
    for j in range(i):
        print("*" , end = "")
    for j in range(i+1):
        print("*" , end = "")
    print()

for i in range(5):
    for j in range(i+1):
        print("" , end = " ")
    for j in range(i , 5-1):
        print("*" , end = "")
    for j in range(i , 5):
        print("*" , end = "")
    print()"""

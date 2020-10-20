counter = 0b0000
j = 0

if((counter & (1 << j)) > 0):
    print("True")
else:
    print("False")

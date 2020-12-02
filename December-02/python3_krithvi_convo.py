# Letters for each number in Keypad
keypad = [['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
num = range(2,9)

# Function to return character combinations list
def combo(keys):
    # Extract the two digits for array iteration
    tens = (keys // 10)
    ones = (keys % 10)
    if(tens not in num or ones not in num):
        print("Invalid input. Enter two digits from (2-9) only")
        return
    else:
        tens -=2
        ones -=2

    # Iterative loop to append the character combinations
    c = []
    i = 0
    j = 0
    for i in range(0,len(keypad[tens])):
        for j in range(0,len(keypad[ones])):
            c.append(str(keypad[tens][i]) + str(keypad[ones][j]))
    return c

# Driver Code
keys = input("Input: ")
print "Output: " + str(combo(keys))
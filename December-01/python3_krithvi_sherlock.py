# Function to check if sum of the left half and right half of the square of a number is equal to the number
def sqequal(n):
    # Digits of square in an int array
    a = map(int, str(n*n))
    l = len(a) 
  
    left = 0
    right = 0
    for i in range(l):       
        # Extract left half 
        if (i < l // 2): 
            left *= 10
            left += a[i]
  
        # Extract right half 
        else: 
            right *= 10
            right += a[i];

    # Add left half and right half
    sqsum = left + right

    return 1 if sqsum==n else 0

# Function to check if number is a multiple of 3
def mul3(n):
    return 1 if (n%3==0) else 0

# Return 'Safe' or not by implementing the function calls
def status_check(n):
    if(mul3(n) == 1 and sqequal(n) == 1):
        return 'Safe'
    else:
        return 'Not Safe'

# Driver Code        
room = input("Room: ")
print 'Status: '  + status_check(room)
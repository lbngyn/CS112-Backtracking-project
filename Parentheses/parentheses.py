def Try(id, point, currentString):  

    global maxLength
    global ans 
    if point == 0: 
        if maxLength == len(currentString): 
            ans = min(ans, currentString)

        if maxLength < len(currentString): 
            maxLength = len(currentString)
            ans = currentString

    if point < 0 or id >= len(S): return

    
    newPoint = 0 
    if S[id] == '(': newPoint = point + 1
    else: newPoint = point - 1 

    Try(id+1, newPoint, currentString + S[id]) 
    Try(id+1, point, currentString)  

    return

# Read input from a file
with open('input10.txt', 'r') as f:
    S = f.readline().strip()
    
ans = '' 
maxLength = 0 

# Call the function to compute and store the result
Try(0,0,'')

# Write output to a file
with open('output10.txt', 'w') as f:
    f.write(str(len(ans)) + '\n')
    f.write(ans + '\n')
# Q04a
numberList = [5,9,13,63,65,79,86,100]
start = 0
middle = 0 
end = len (numberList) - 1
found = False
count = 0
item = int(input('Enter integer number:'))
while start <= end and found == False:
    middle = (start + end) // 2
    if numberList [middle] == item:
        found = True
    else:
        if item < numberList [middle]:
            end= middle -1
        else:
            start = middle + 1
    count = count + 1

if found == True:
    print(item, 'was found in the list')
else:
     print(item,'not found in the list')
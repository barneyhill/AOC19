start = 193651
end = 649729
current = start
valid = 0
while current != end:
    last_digit = 0
    repeated = False
    for i in range(0, len(str(current))):
        if str(last_digit) == str(current)[i]:
            repeated = True
            try:
                if str(last_digit) == str(current)[i-2]:
                    repeated = False
            except:
                continue
            try:
                if str(last_digit) == str(current)[i+1]:
                    repeated = False
            except:
                continue
        if last_digit <= int(str(current)[i]):
            if (i == len(str(current)) - 1) and repeated:
                valid +=1
        else:
            break
        last_digit = int(str(current)[i])
    current += 1
print(valid)
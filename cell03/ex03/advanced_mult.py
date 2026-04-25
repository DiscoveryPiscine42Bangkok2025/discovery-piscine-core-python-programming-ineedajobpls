
f=1

while f<=10 :
    l = 1
    t = print(str ('Table de '+ str(f) ), end =': ')
    while l <= 10:
        print(str (f * l )+ '\t', end = ' ')
        l+=1

    print()
    f += 1
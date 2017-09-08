import random

n = 200
while n:
    tic = ""
    i = 4
    while i:
        tic = tic + "".join(random.sample("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789", 4)) + "-"
        i = i - 1
    tic = tic.rstrip("-")    
    print(tic)
    n = n -1

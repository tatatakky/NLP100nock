with open("hightemp.txt") as f:
    for line in f:
        print(line.replace('tr',' '),end = '')
# cat hightemp.txt | sed

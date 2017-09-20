## mbox-short.txt

fhandler = open("mbox-short.txt")
emails = dict()
for line in fhandler:
    line.rstrip()
    if line.startswith("From" ) == 0:
        line = line.split(" ")
        email = line[1]
        if email not in emails:
            emails[email] = 1
        else:
            emails[email] +=1


email = ""
count = 0

for key in emails:
    if emails[key] > count:
        count = emails[key]
email = key

print (email , str(count))
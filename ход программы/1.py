mac = ["XXXX:XXXX:XXXX"]
result = []
for line in mac:

    words = line.split(':')
    line2 = words[0] + '.' + words[1] + '.' + words[2]
    result.append(line2)

print (result)
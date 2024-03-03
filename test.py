f = open('text.txt', 'r')
for char in f.read():
    print(char, end='')

f.close()
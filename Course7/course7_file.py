f_write = open('workfile', 'a')

f_write.write('x line\n')
f_write.close()

f_read = open('workfile')
s = f_read.read()
print(s)
f_read.close()

s = s.split('\n')
for line in s:
    print(line)

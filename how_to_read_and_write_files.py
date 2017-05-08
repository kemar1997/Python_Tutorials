fw = open('sample.txt', 'w')
fw.write("Writing some stuff in a new text file.\n")
fw.write('I like bacon\n')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()

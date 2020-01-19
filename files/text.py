from text_file import Text

txt = Text(r'../spreadsheets/iris.csv')
# print(next(txt))

print(txt.read_last_two_lines())
for line in txt:
    print(line)
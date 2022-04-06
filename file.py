


with open('file/demo.txt', 'r+', encoding='utf8') as f:
    str = f.read()
    print (str)
f.close()

# with open('file/demo.txt', 'w+', encoding='utf8') as f:
#     text = '你好'
#     f.write(text)
# f.close()
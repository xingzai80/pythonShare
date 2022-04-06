# //单张图片转文字
import pytesseract
from PIL import Image

img = Image.open(r'file/baidu.png')
text = pytesseract.image_to_string(img,lang='chi_sim')
with open('file/demo01.txt', 'w', encoding='utf8') as f:
    f.write(text)
    f.close()
print(text)
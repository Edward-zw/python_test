import os
from PIL import Image

#创建新的图片存放目录
os.mkdir(r"C:\Users\60381\Desktop\new_pics")
#获取图片地址列表
def get_paths(path):
    paths = os.listdir(path)
    return paths

#改变图片尺寸并保存到新文件夹
def change_size(path):
    im = Image.open(os.path.join(r"C:\pictures", path))
    (x, y) = im.size
    new_width = 1136
    new_height = int(y * 1136 / x)
    new_im = im.resize((new_width, new_height))
    new_im.save(os.path.join(r"C:\Users\60381\Desktop\new_pics", path))

path = r"C:\pictures"
paths = get_paths(path)
for path in paths:
    change_size(path)

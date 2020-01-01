from PIL import Image, ImageFilter

# 打开一个jpg图像，注意是当前路径
im = Image.open(r'D:\6、python\PythonABC\chapter fourteen\70j.jpg')
# 应用模糊滤镜
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')

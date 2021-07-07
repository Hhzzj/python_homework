# 0000.将你的QQ头像（或者微博头像）右上角加上红色的数字，类似于微信未读消息数量那种提示效果。

from PIL import Image, ImageDraw, ImageFont
import random


def add_num_to_pic(picture, num, color='red'):
    canvas = ImageDraw.Draw(picture)  # 创建一个在原头像图片上进行绘图的对象
    width, height = picture.size  # 获取图片尺寸

    font_size = min(width, height) // 4  # 根据图片大小尺寸设置字体大小
    num_font = ImageFont.truetype("arial.ttf", font_size)  # 设置显示字体格式以及大小

    if width < height:
        pos = (width-font_size-10, 0)
    else:
        pos = (height-font_size-10, 0)

    canvas.text(pos, num, font=num_font, fill=color)  # 在右上角添加红色数字
    return picture


if __name__ == '__main__':
    head_picture = Image.open("picture.jpg")  # 打开头像图片 close
    num = str(random.randint(0, 100))  # 随机一个要显示的红色数字的数值大小
    add_num_to_pic(head_picture, num)
    head_picture.save("picture1.jpg")  # 保存图片
    head_picture.close()

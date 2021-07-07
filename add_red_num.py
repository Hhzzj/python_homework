# 0000.将你的QQ头像（或者微博头像）右上角加上红色的数字，类似于微信未读消息数量那种提示效果。
# 图片路径：C:\\Users\\Ocean\\Desktop\\picture.jpg

from PIL import Image, ImageDraw, ImageFont
import random


def add_red_num(head_picture, num):
    draw = ImageDraw.Draw(head_picture)  # 创建一个在原头像图片上进行绘图的对象
    width, height = head_picture.size  # 获取图片尺寸
    font_size = min(width, height) // 4  # 根据图片大小尺寸设置字体大小
    my_font = ImageFont.truetype(
        "C:\\WINDOWS\\Fonts\\arial.ttf", font_size)  # 设置显示字体格式以及大小
    draw.text((width-font_size-10, 0), num, font=my_font,
              fill='red')  # 在右上角添加红色数字
    head_picture.save("C:\\Users\\Ocean\\Desktop\\picture1.jpg")  # 保存图片

    return 0


picture_path = input("请输入你的头像图片路径:")
head_picture = Image.open(picture_path)  # 打开头像图片
num = str(random.randint(0, 100))  # 随机一个要显示的红色数字的数值大小
add_red_num(head_picture, num)

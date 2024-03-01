#!/usr/bin/python
# -*- coding: utf-8 -*-
# jxb3019
# feature: 图像亮度函数
import os

from PIL import Image, ImageEnhance


def enhance_brightness(input_path, output_path, brightness_factor):
    # 获取选择的输入路径和输出路径
    print('打印参数信息！！！\n')
    print('输入路径：', input_path)
    print('输出路径：', output_path)
    print('亮度参数：', brightness_factor)
    if not os.path.exists(output_path):
        output_path = os.path.join(input_path, 'res')
        print('未输入输出路径，新建输出路径：', output_path)
        if not os.path.exists(output_path):
            os.mkdir(output_path)
    for f in os.listdir(input_path):
        if f.endswith('jpg') or f.endswith('png') or f.endswith('bmp'):
            print('输入图像---', f)
            filename = os.path.join(input_path, f)
            # 打开图像
            image = Image.open(filename)
            # 创建亮度增强器
            enhancer = ImageEnhance.Brightness(image)
            # 增加亮度（增益因子大于1增加亮度，小于1降低亮度）
            brightened_image = enhancer.enhance(brightness_factor)
            # 保存结果
            res = os.path.join(output_path, f)
            print('输出图像+++', res)
            brightened_image.save(res)
    print('success')
    print('亮度处理完成')


if __name__ == '__main__':
    enhance_brightness(r"D:\work_record\1031",'',1.5)
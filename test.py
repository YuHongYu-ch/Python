# -*- coding:utf-8 -*-
from imutils import contours
import cv2
import math

image = cv2.imread('1.jpg')  # 读入图片
cv2.namedWindow("yuantu", 0)
cv2.imshow("yuantu", image)  # 显示原图片

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 二值化操作
cv2.namedWindow("erzhihua", 0)
cv2.imshow("erzhihua", gray)

gauss = cv2.GaussianBlur(gray, (7, 7), 0)  # 高斯滤波
cv2.namedWindow("guss", 0)
cv2.imshow("guss", gauss)

retval, result = cv2.threshold(gauss, 128, 255, cv2.THRESH_BINARY)  # 阈值分割
cv2.namedWindow("yuzhi", 0)
cv2.imshow("yuzhi", result)

edged = cv2.Canny(result, 50, 100)  # canny算子边缘检测
cv2.namedWindow("canny", 0)
cv2.imshow("canny", edged)


pengzhang = cv2.dilate(edged, None, iterations=1)  # 膨胀操作
cv2.namedWindow("pengzhang", 0)
cv2.imshow("pengzhang", pengzhang)

fushi = cv2.erode(pengzhang, None, iterations=1)  # 腐蚀操作
cv2.namedWindow("fushi", 0)
cv2.imshow("fushi", fushi)

cnts = cv2.findContours(fushi.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)  # 找出图像的边缘轮廓点坐标放到cnts里
# 返回两个值  第一个是原图 第二个是列表存放点的坐标 第三个是轮廓的关系

cnt = cnts[1]  # 初始化循环排序轮廓

# 给轮廓排序  从左到右
(cnt, _) = contours.sort_contours(cnt)

i = 1
pixelsPerMetric = None  # 定义比例尺--物体像素的宽度/物体实际宽度
# print("比例尺(物体像素的宽度/物体实际宽度)为： %.03f" % pixelsPerMetric)

for c in cnt:  # 进入循环

    if cv2.contourArea(c) < 100:  # 如果轮廓面积小于100忽略
        continue

    orig = image.copy()  # 把原图像数据拷贝到orig变量中

    box = cv2.fitEllipse(c)  # 得到最佳拟合椭圆

    x = box[0][0]  # 中心点的X坐标
    y = box[0][1]  # 中心点的Y坐标
    a = box[1][0]  # 计算机测量的像素点短轴长度
    b = box[1][1]  # 计算机测量的像素点长轴长度

    # 测试#############################################
    # print(box[0])  # box[0] 中心点的坐标
    # print(box[0][0])  # box[0][0]-中心点x坐标，box[0][1]-中心点y坐标
    # print(box[1])  # box[1][0]-短轴 box[1][1]-长轴
    # print(box[2])  # box[2]旋转角
    # 测试#############################################

    cv2.ellipse(orig, box, (0, 255, 0), 2)  # 画出拟合椭圆

    # print("计算机测量的长轴像素长度为： %.03f" % b)
    if pixelsPerMetric is None:
        sja = input("请输入物体物体实际长轴长度：")
        sja = float(sja)
        pixelsPerMetric = b / sja
        print("比例尺(物体像素的宽度/物体实际宽度)为： %.03f" % pixelsPerMetric)

    # pixelsPerMetric = b / 8.0  # 定义比例尺--物体像素的宽度/物体实际宽度
    # print("比例尺(物体像素的宽度/物体实际宽度)为： %.03f" % pixelsPerMetric)

    dima = a / pixelsPerMetric  # 实际的物体短轴长度
    dimb = b / pixelsPerMetric  # 实际的物体长轴长度

    # 把标识在图片上打印出来
    # 打印短轴
    cv2.putText(orig, "a:{:.1f}cm".format(dima),
                (int(x + 35), int(y - 30)), cv2.FONT_HERSHEY_SIMPLEX,
                0.65, (255, 255, 255), 2)

    cv2.putText(orig, "b:{:.1f}cm".format(dimb),
                (int(x + 35), int(y - 10)), cv2.FONT_HERSHEY_SIMPLEX,
                0.65, (255, 255, 255), 2)

    area = math.pi * dima * dimb
    cv2.putText(orig, "{:.1f}cm*2".format(area),
                (int(x + 10), int(y + 30)), cv2.FONT_HERSHEY_SIMPLEX,
                0.65, (255, 255, 255), 2)  # 在图像上显示面积

    cv2.putText(orig, "{:d}'".format(i),
                (int(x - 65), int(y - 10)), cv2.FONT_HERSHEY_SIMPLEX,
                0.65, (255, 255, 255), 2)

    cv2.namedWindow("IMG", 0)
    cv2.imshow("IMG", orig)

    cv2.waitKey(500)
    i = i + 1


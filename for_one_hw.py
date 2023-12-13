import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import xlwt
import pandas as pd
import math
from scipy import interpolate
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


root = tk.Tk()
root.title("My GUI")  # 设置窗口标题

# 手动输入
def manual():
    win4 = tk.Tk()
    text4_1 = tk.Label(win4,text="Please key in a set of numbers and delimited by space >")
    text4_1.pack()
    x_entry = tk.Entry(win4,width=40)
    x_entry.pack()
    y_entry = tk.Entry(win4, width=40)
    y_entry.pack()# 分别输入x，y值
    b4 = tk.Radiobutton(win4, text="Entry", command=mode)
    b4.pack()

    x_input_str = x_entry.get()
    x_input_arr = [float(i) for i in x_input_str.split()]
    x = np.array([])
    x = np.append(x, x_input_arr)
    y_input_str = y_entry.get()
    y_input_arr = [float(j) for j in y_input_str.split()]
    y = np.array([])
    y = np.append(y, y_input_arr)# 将x，y转为数组
    win4.mainloop()
    return 
    #输出两个值组成的列表，在后面代码中会拆开（还没写完）



# 导入表格
def import_form():
    win5 = tk.Tk()
    text5_1 = tk.Label(win5, text="Please enter your file location >")
    text5_1.pack()
    form_entry = tk.Entry(win5, width=40)
    form_entry.pack()# 输入表格地址

    text5_2 = tk.Label(win5, text="Please enter the row positions of x and y in the table respectively >")
    text5_2.pack()
    xl_entry = tk.Entry(win5, width=20)
    xl_entry.pack()
    yl_entry = tk.Entry(win5, width=20)
    yl_entry.pack()# 输入表格中变量所在行数


    file_location = form_entry.get()
    data = xlrd.open_workbook(file_location)
    data.sheet_names()
    print("sheets:" + str(data.sheet_names()))
    x_line = xl_entry.get()
    y_line = yl_entry.get()
    x = table.row_values(int(x_line))
    y = table.row_values(int(y_line))#分别提取表中x，y数据为数组，

    b5 = tk.Radiobutton(win5, text="Entry", command=mode)
    b5.pack()
    win5.mainloop()
    return

# 散点图
def scatterplot():
    plt.figure(figsize=(8,4))
    plt.scatter(x,
            y,
            c='red')
    plt.legend()
    plt.show()
    return
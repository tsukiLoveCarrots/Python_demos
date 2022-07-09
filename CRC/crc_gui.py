from tkinter import *
from tkinter import messagebox
from crc import CRC
import warnings

warnings.filterwarnings("ignore")

crc = CRC()
root = Tk()
root.geometry('1200x371')
root.title("CRC校验编码器")


def check_poly(poly):
    if poly[0] != '1' or poly[-1] != '1':
        messagebox.showwarning(title='输入多项式错误', message='首位和末位必须为1！')
        return False

    for i in poly:
        if len(i) == 0:
            messagebox.showwarning(title='输入多项式错误', message='输入多项式不能存在空值！')
            return False
        elif i != '0' and i != '1':
            messagebox.showwarning(title='输入多项式错误', message='多项式只能输入0和1！')
            return False
    return True


def check_data(data):
    if len(data) == 0:
        messagebox.showwarning(title='输入多项式错误', message='请输入数据！')
        return False
    for i in data:
        if i != '0' and i != '1':
            messagebox.showwarning(title="输入数据错误！", message="数据只能输入0和1！")
            return False
    return True


def author():
    messagebox.showinfo(title='author', message=' 班级 : 自卓1901\n 姓名 : 孙鸿宇 \n 学号 : U201914606')


def CRC_4():
    def callback_crc4():
        d1 = v1.get()  # d1: str
        d2 = v2.get()
        d3 = v3.get()
        d4 = v4.get()
        d5 = v5.get()
        crc4_poly = [d1, d2, d3, d4, d5]
        data = v_data.get()

        if check_data(data) and check_poly(crc4_poly):
            crc4_poly = list(map(int, crc4_poly))
            data = list(map(int, data))
            result = crc.CRC_code(data, crc4_poly)
            v_res.set(result)

    crc_4 = Toplevel(root)
    crc_4.title("CRC-4")
    crc_4.geometry("420x260")

    Label(crc_4, text='输入生成多项式和数据', font=('宋体', 14)).place(x=120, y=10)

    v1 = StringVar()
    Entry(crc_4, borderwidth=3, width=2, font=("Arial", 14), justify='center', textvariable=v1).place(x=20, y=65)
    Label(crc_4, text='x^4 +', font=("Arial", 14)).place(x=50, y=64)

    v2 = StringVar()
    Entry(crc_4, borderwidth=3, width=2, font=("Arial", 14), justify='center', textvariable=v2).place(x=100, y=65)
    Label(crc_4, text='x^3 +', font=("Arial", 14)).place(x=130, y=64)

    v3 = StringVar()
    Entry(crc_4, borderwidth=3, width=2, font=("Arial", 14), justify='center', textvariable=v3).place(x=180, y=65)
    Label(crc_4, text='x^2 +', font=("Arial", 14)).place(x=210, y=64)

    v4 = StringVar()
    Entry(crc_4, borderwidth=3, width=2, font=("Arial", 14), justify='center', textvariable=v4).place(x=260, y=65)
    Label(crc_4, text='x^1 +', font=("Arial", 14)).place(x=290, y=64)

    v5 = StringVar()
    Entry(crc_4, borderwidth=3, width=2, font=("Arial", 14), justify='center', textvariable=v5).place(x=340, y=65)
    Label(crc_4, text='x^0', font=("Arial", 14)).place(x=370, y=64)

    v_data = StringVar()
    Entry(crc_4, borderwidth=3, width=30, font=("Arial", 12), textvariable=v_data).place(x=105, y=125)
    Label(crc_4, text='输入数据', font=("宋体", 13)).place(x=20, y=125)

    v_res = StringVar()
    Entry(crc_4, borderwidth=3, width=30, font=("Arial", 12), textvariable=v_res).place(x=130, y=170)
    Label(crc_4, text='CRC校验结果', font=("宋体", 13)).place(x=20, y=170)

    Button(crc_4, text='开始计算', font=("宋体", 16), command=callback_crc4).place(x=150, y=210)


def CRC_5():
    def callback_crc5():
        d1 = v1.get()  # d1: str
        d2 = v2.get()
        d3 = v3.get()
        d4 = v4.get()
        d5 = v5.get()
        d6 = v6.get()
        crc5_poly = [d1, d2, d3, d4, d5, d6]
        data = v_data.get()

        if check_data(data) and check_poly(crc5_poly):
            crc5_poly = list(map(int, crc5_poly))
            data = list(map(int, data))
            result = crc.CRC_code(data, crc5_poly)
            v_res.set(result)

    crc_5 = Toplevel(root)
    crc_5.title("CRC-5")
    crc_5.geometry("500x260")
    Label(crc_5, text='输入生成多项式和数据', font=('宋体', 14)).place(x=180, y=10)

    v1 = StringVar()
    Entry(crc_5, borderwidth=3, width=2, font=("Arial", 12), justify='center', textvariable=v1).place(x=20, y=65)
    Label(crc_5, text='x^5 +', font=("Arial", 12)).place(x=50, y=64)

    v2 = StringVar()
    Entry(crc_5, borderwidth=3, width=2, font=("Arial", 12), justify='center', textvariable=v2).place(x=100, y=65)
    Label(crc_5, text='x^4 +', font=("Arial", 12)).place(x=130, y=64)

    v3 = StringVar()
    Entry(crc_5, borderwidth=3, width=2, font=("Arial", 12), justify='center', textvariable=v3).place(x=180, y=65)
    Label(crc_5, text='x^3 +', font=("Arial", 12)).place(x=210, y=64)

    v4 = StringVar()
    Entry(crc_5, borderwidth=3, width=2, font=("Arial", 12), justify='center', textvariable=v4).place(x=260, y=65)
    Label(crc_5, text='x^2 +', font=("Arial", 12)).place(x=290, y=64)

    v5 = StringVar()
    Entry(crc_5, borderwidth=3, width=2, font=("Arial", 12), justify='center', textvariable=v5).place(x=340, y=65)
    Label(crc_5, text='x^1 + ', font=("Arial", 12)).place(x=370, y=64)

    v6 = StringVar()
    Entry(crc_5, borderwidth=3, width=2, font=("Arial", 12), justify='center', textvariable=v6).place(x=420, y=65)
    Label(crc_5, text='x^0', font=("Arial", 12)).place(x=450, y=64)

    v_data = StringVar()
    Entry(crc_5, borderwidth=3, width=40, font=("Arial", 12), textvariable=v_data).place(x=105, y=125)
    Label(crc_5, text='输入数据', font=("宋体", 13)).place(x=20, y=125)

    v_res = StringVar()
    Entry(crc_5, borderwidth=3, width=40, font=("Arial", 12), textvariable=v_res).place(x=130, y=170)
    Label(crc_5, text='CRC校验结果', font=("宋体", 13)).place(x=20, y=170)

    Button(crc_5, text='开始计算', font=("宋体", 16), command=callback_crc5).place(x=200, y=210)


def CRC_16():
    def callback_crc16():
        d1 = v1.get()  # d1: str
        d2 = v2.get()
        d3 = v3.get()
        d4 = v4.get()
        d5 = v5.get()
        d6 = v6.get()
        d7 = v7.get()
        d8 = v8.get()
        d9 = v9.get()
        d10 = v10.get()
        d11 = v11.get()
        d12 = v12.get()
        d13 = v13.get()
        d14 = v14.get()
        d15 = v15.get()
        d16 = v16.get()
        d17 = v17.get()
        crc16_poly = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17]
        data = v_data.get()

        if check_data(data) and check_poly(crc16_poly):
            crc16_poly = list(map(int, crc16_poly))
            data = list(map(int, data))
            result = crc.CRC_code(data, crc16_poly)
            v_res.set(result)

    crc_16 = Toplevel(root)
    crc_16.title("CRC-16")
    crc_16.geometry("750x300")

    Label(crc_16, text='输入生成多项式和数据', font=('宋体', 16)).place(x=270, y=10)

    v1 = StringVar()
    Entry(crc_16, borderwidth=3, width=2, font=("Arial", 12), justify='center', textvariable=v1).place(x=20, y=65)
    Label(crc_16, text='x^16 +', font=("Arial", 12)).place(x=50, y=64)

    v2 = StringVar()
    Entry(crc_16, borderwidth=3, width=2, font=("Arial", 12), justify='center', textvariable=v2).place(x=100, y=65)
    Label(crc_16, text='x^15 +', font=("Arial", 12)).place(x=130, y=64)

    v3 = StringVar()
    Entry(crc_16, borderwidth=3, width=2, font=("Arial", 12), justify='center', textvariable=v3).place(x=180, y=65)
    Label(crc_16, text='x^14 +', font=("Arial", 12)).place(x=210, y=64)

    v4 = StringVar()
    Entry(crc_16, borderwidth=3, width=2, font=("Arial", 12), justify='center', textvariable=v4).place(x=260, y=65)
    Label(crc_16, text='x^13 +', font=("Arial", 12)).place(x=290, y=64)

    v5 = StringVar()
    Entry(crc_16, borderwidth=3, width=2, font=("Arial", 12), justify='center', textvariable=v5).place(x=340, y=65)
    Label(crc_16, text='x^12 + ', font=("Arial", 12)).place(x=370, y=64)

    v6 = StringVar()
    Entry(crc_16, borderwidth=3, width=2, font=("Arial", 12), justify='center', textvariable=v6).place(x=420, y=65)
    Label(crc_16, text='x^11 + ', font=("Arial", 12)).place(x=450, y=64)

    v7 = StringVar()
    Entry(crc_16, borderwidth=3, width=2, font=("Arial", 12), justify='center', textvariable=v7).place(x=500, y=65)
    Label(crc_16, text='x^10 +', font=("Arial", 12)).place(x=530, y=64)

    v8 = StringVar()
    Entry(crc_16, borderwidth=3, width=2, font=("Arial", 12), justify='center', textvariable=v8).place(x=580, y=65)
    Label(crc_16, text='x^9 +', font=("Arial", 12)).place(x=610, y=64)

    v9 = StringVar()
    Entry(crc_16, borderwidth=3, width=2, font=("Arial", 12), justify='center', textvariable=v9).place(x=660, y=65)
    Label(crc_16, text='x^8 +', font=("Arial", 12)).place(x=690, y=64)

    v10 = StringVar()
    Entry(crc_16, borderwidth=3, width=2, font=("Arial", 12), justify='center', textvariable=v10).place(x=20, y=125)
    Label(crc_16, text='x^7 +', font=("Arial", 12)).place(x=50, y=124)

    v11 = StringVar()
    Entry(crc_16, borderwidth=3, width=2, font=("Arial", 12), justify='center', textvariable=v11).place(x=100, y=125)
    Label(crc_16, text='x^6 +', font=("Arial", 12)).place(x=130, y=124)

    v12 = StringVar()
    Entry(crc_16, borderwidth=3, width=2, font=("Arial", 12), justify='center', textvariable=v12).place(x=180, y=125)
    Label(crc_16, text='x^5 +', font=("Arial", 12)).place(x=210, y=124)

    v13 = StringVar()
    Entry(crc_16, borderwidth=3, width=2, font=("Arial", 12), justify='center', textvariable=v13).place(x=260, y=125)
    Label(crc_16, text='x^4 + ', font=("Arial", 12)).place(x=290, y=124)

    v14 = StringVar()
    Entry(crc_16, borderwidth=3, width=2, font=("Arial", 12), justify='center', textvariable=v14).place(x=340, y=125)
    Label(crc_16, text='x^3 + ', font=("Arial", 12)).place(x=370, y=124)

    v15 = StringVar()
    Entry(crc_16, borderwidth=3, width=2, font=("Arial", 12), justify='center', textvariable=v15).place(x=420, y=125)
    Label(crc_16, text='x^2 +', font=("Arial", 12)).place(x=450, y=124)

    v16 = StringVar()
    Entry(crc_16, borderwidth=3, width=2, font=("Arial", 12), justify='center', textvariable=v16).place(x=500, y=125)
    Label(crc_16, text='x^1 +', font=("Arial", 12)).place(x=530, y=124)

    v17 = StringVar()
    Entry(crc_16, borderwidth=3, width=2, font=("Arial", 12), justify='center', textvariable=v17).place(x=580, y=125)
    Label(crc_16, text='x^0', font=("Arial", 12)).place(x=610, y=124)

    v_data = StringVar()
    Entry(crc_16, borderwidth=3, width=60, font=("Arial", 12), textvariable=v_data).place(x=130, y=175)
    Label(crc_16, text='输入数据：', font=("宋体", 14)).place(x=20, y=175)

    v_res = StringVar()
    Entry(crc_16, borderwidth=3, width=60, font=("Arial", 12), textvariable=v_res).place(x=130, y=220)
    Label(crc_16, text='CRC校验结果：', font=("宋体", 14)).place(x=20, y=220)

    Button(crc_16, text='开始计算', font=("宋体", 16), command=callback_crc16).place(x=300, y=250)


def about_crc():
    info = Toplevel(root)
    info.title("CRC-16")
    info.geometry("430x150")
    Label(info, text="CRC校验简介", font=("黑体", 12)).place(x=150, y=0)
    Label(info, text=
    "1.CRC编码属于检错编码技术的一种。收发双方约定相同的生成多项式G(x)\n"
    "其最高, 最低项系数必须为1,并采用该生成多项式进行编码运算.\n\n"
    "2.编码过程. 确定生成多项式的最高幂数值,在待发送的比特数据后附加\n"
    "生成多项式最高幂次数相同数量的比特0, 采用附加后的数据对生成多项式\n"
    "进行二进制除法,得到的余数(不足补0)添加到原数据后即为CRC编码的结果").place(x=10, y=20)


def crc_check():
    s = v_input_data.get()
    x = v_poly.get()
    if check_data(s) and check_poly(x):
        s = [int(i) for i in s]
        x = [int(j) for j in x]
        # print(s, x)
        if crc.binary_division(s, x) == 0 or sum(crc.binary_division(s, x)) == 0:
            v_check.set('正确')
        else:
            v_check.set('错误')

Label(root, text='please pick a mode.', font=("Arial", 18)).place(x=200, y=20)
bn_config = Button(root, text='about CRC', font=('Arial', 22), command=about_crc).place(x=345, y=200)
bn_crc4 = Button(root, text='CRC-4', font=('Arial', 24), command=CRC_4).place(x=100, y=80)
bn_crc5 = Button(root, text='CRC-5', font=('Arial', 24), command=CRC_5).place(x=100, y=200)
bn_crc16 = Button(root, text='CRC-16', font=('Arial', 24), command=CRC_16).place(x=345, y=80)
bn_author = Button(root, text='author', font=('Arial', 14), command=author).place(x=480, y=15)



Label(root, text='检验', font=("Arial", 23)).place(x=850, y=20)
Label(root, text='输入', font=("Arial", 18)).place(x=650, y=80)
Label(root, text='输入生成多项式', font=("Arial", 16)).place(x=560, y=123)

v_input_data = StringVar()
Entry(root, borderwidth=3, width=45, font=("Arial", 12), textvariable=v_input_data).place(x=725, y=85)

v_poly = StringVar()
Entry(root, borderwidth=3, width=45, font=("Arial", 12), textvariable=v_poly).place(x=725, y=125)

Button(root, text="开始校验", font=("Arial", 20), command=crc_check).place(x=820, y=175)
Label(root, text='鉴定为', font=("Arial", 18)).place(x=650, y=250)
v_check = StringVar()
Entry(root, borderwidth=7, width=10, font=("Arial", 12), textvariable=v_check).place(x=745, y=250)

root.mainloop()

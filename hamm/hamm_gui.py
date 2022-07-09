from hamm import hamming
from tkinter import *
from tkinter import messagebox
import warnings
import copy

warnings.filterwarnings("ignore")


def check_input(code):
    if len(code) == 0:
        messagebox.showwarning(title='输入数据错误!', message='输入数据不能为0')
        return False

    for i in code:
        if i != '1' and i != '0':
            messagebox.showwarning(title='输入数据错误!', message='请输入正确的二进制数')
            return False
    return True


ham = hamming()
root = Tk()
root.geometry('400x530')
root.title("海明码编码实验")


def callback_calc():
    code = v1.get()
    if check_input(code):
        ham_code = ham.code(code)
        assert isinstance(ham_code, object), 'unknown error'
        v2.set(ham_code)


def callback_test():
    code = v3.get()
    copy.deepcopy(code)
    if not ham.check(code):
        wrong_pos = ham.check(code)
        v5.set(wrong_pos)
        correct_code = ham.list_str_transform(code, switch='str2list')
        correct_code[wrong_pos-1] = 0 if correct_code[wrong_pos-1] == 1 else 1
        v4.set(correct_code)
    else:
        v4.set("correct")


Label(root, text='海明码生成', font=("Arial", 19)).place(x=140, y=15)
Label(root, text='海明码译码', font=("Arial", 19)).place(x=140, y=240)
Label(root, text='输入', font=("Arial", 18)).place(x=25, y=60)
Label(root, text='输出', font=("Arial", 18)).place(x=25, y=130)
Button(root, text='开始计算', font=("Arial", 18), command=callback_calc).place(x=150, y=175)
Label(root, text='输入', font=("Arial", 18)).place(x=25, y=300)
Button(root, text='开始校验', font=("Arial", 18), command=callback_test).place(x=150, y=350)
Label(root, text='第', font=("Arial", 18)).place(x=50, y=420)
Label(root, text='位错, 正确编码应为', font=("Arial", 18)).place(x=100, y=420)


v1 = StringVar()
Entry(root, borderwidth=3, width=30, font=("Arial", 12), textvariable=v1).place(x=90, y=65)

v2 = StringVar()
Entry(root, borderwidth=3, width=30, font=("Arial", 12), textvariable=v2).place(x=90, y=135)

v3 = StringVar()
Entry(root, borderwidth=3, width=30, font=("Arial", 12), textvariable=v3).place(x=90, y=305)

v4 = StringVar()
Entry(root, borderwidth=3, width=30, font=("Arial", 12), textvariable=v4).place(x=60, y=460)

v5 = StringVar()
Entry(root, borderwidth=3, width=2, font=("Arial", 12), textvariable=v5).place(x=77, y=423)


root.mainloop()
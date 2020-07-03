from tkinter import *

def add(a,b):
    return a + b

def substrct(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

def mod(a,b):
    return a % b

def lcm(a,b):
    L = a if a > b else b
    while L <= a*b:
        if L%a == 0 and L%b == 0:
            return L
        L += 1

def hcf(a,b):
    H = a if a < b else b
    while H >= 1:
        if a%H == 0 and b%H == 0:
            return H
        H -= 1

def extract_from_text(text):
    l = []
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l

def calculate():
    text = textin.get()
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l = extract_from_text(text)
                r = operations[word.upper()](l[0] , l[1])
                list.delete(0,END)
                list.insert(END,r)
            except:
                list.delete(0,END)
                list.insert(END,'something went wrong, please enter again.')
            finally:
                break
        elif word.upper() not in operations.keys():
            list.delete(0,END)
            list.insert(END,'something went wrong, please enter again.')

operations = {'ADD':add , 'ADDITION':add , 'SUM':add , 'PLUS':add ,
                'SUB':substrct , 'DIFFERENCE':substrct , 'MINUS':substrct , 'SUBSTRACT':substrct ,
                'LCM':lcm , 'HCF':hcf , 'PRODUCT':mul , 'MULTIPLICATION':mul , 'MULTIPLY':mul ,
                'DIVISION':div , 'DIV':div , 'DIVIDE':div , 'MOD':mod , 'REMANDER':mod , 'MODULUS':mod}        

win = Tk()
win.geometry('500x300')
win.title('Smart Calculator with Python')
win.configure(bg='Black')

l1 = Label(win , text='Smart Calculator by Brilliant Ace')
l1.place(x=150 , y=10)
l2 = Label(win , text='I Want To Calculate Something!')
l2.place(x=151 , y=40)
l3 = Label(win , text='Calculate Something, Please')
l3.place(x=155 , y=130)

textin = StringVar()
e1 = Entry(win , width=30 , textvariable = textin)
e1.place(x=140 , y=160)

b1 = Button(win , text='CALCULATE' , command=calculate)
b1.place(x=200 , y=200)

list = Listbox(win , width=20 , height=3)
list.place(x=173 , y=230)

win.mainloop()
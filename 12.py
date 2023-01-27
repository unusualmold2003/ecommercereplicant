from tkinter import messagebox as mb
import tkinter as tk

window = tk.Tk()
window.geometry('600x600')
window.title('Amazon Shopping')
window.configure(bg='white')

global cart_items_price
#cart_bill = list(sum(e_cart_items_price)+sum(f_cart_items_price)+sum(g_cart_items_price))

def order_placed():
    global w1,window
    global cart_items_price
    mb.showinfo("THANK YOU","YOUR ORDER HAS BEEN PLACED\nTHANK YOU FOR SHOPPING WITH US")
    w1.destroy()
    window.deiconify()

e_items = {'Mobile':50000,'AirPods':20000,'Charger':1000}
e_list = []
e_list_cost = []
for key,value in e_items.items():
        e_list.append(key)
        e_list_cost.append(value)
f_items = {'Table':1000,'Chair':700,'Desk':2000}
f_list = []
f_list_cost = []
for key,value in f_items.items():
        f_list.append(key)
        f_list_cost.append(value)
g_items = {'Milk':20,'Potato':50,'Tomato':50}
g_list = []
g_list_cost = []
for key,value in g_items.items():
        g_list.append(key)
        g_list_cost.append(value)

def goback():
    global window,e_window,f_window,g_window
    w1.destroy()
    e_window.destroy()
    f_window.destroy()
    g_window.destroy()
    window.deiconify()

cart_items_price = []

def buynow(a):
    global cart_items_price
    #e_cart_items = []
    #cart_items_price = []
    cart_items_price.append(a)
    mb.showinfo("ATTENTION", "ITEM ADDED TO CART")

def coupon():
    global e1,dis,total,gst,w1,l_h5
    a=e1.get()
    apply= True
    if(apply==True):
        if a=='':
            dis=0
            mb.showerror("!!!", "INVALID COUPON")
        elif a == sum(cart_items_price):
            dis = sum(cart_items_price)
            mb.showinfo("Congrats!","You have received a 100% discount")
        else:
            dis=300
            mb.showinfo("!!!","A DISCOUNT OF Rs. 300 HAS BEEN APPLIED")
            apply=False
        total = sum(cart_items_price) + gst - dis
        l_h5 = tk.Label(w1, text=f"TOTAL: ₹{total}", font=("Arial", 15), bg='black', fg='orange')
        l_h5.place(x=70, y=290)

def bill():
    global w1, e1, dis, window,gst,l_h5
    global cart_items_price
    window.withdraw()
    w1 = tk.Toplevel()
    w1.geometry('600x600')
    w1.title('BILL')
    print(cart_items_price)
    gst=sum(cart_items_price)*0.18
    total = sum(cart_items_price) + gst
    l_h1 = tk.Label(w1, text="Bill", font=("Arial", 25), bg='black', fg='orange')
    l_h1.place(x=180, y=50)
    l_hp = tk.Label(w1, text=f"Final Price: ₹{sum(cart_items_price)}", font=("Arial", 15), bg='black', fg='orange')
    l_hp.place(x=70, y=120)
    l_h2 = tk.Label(w1, text=f"GST: Rs.{gst}", font=("Arial", 15), bg='black', fg='orange')
    l_h2.place(x=70, y=170)
    l_h3 = tk.Label(w1, text="Coupon (if any):", font=("Arial", 15), bg='black', fg='orange')
    l_h3.place(x=70, y=220)
    e1 = tk.Entry(w1)
    e1.place(x=170, y=225)
    b=tk.Button(w1, text='Apply', bg='black', fg='orange', command=coupon)
    b.place(x=300,y=220)
    l_h5 = tk.Label(w1, text=f"Total: ₹{total}", font=("Arial", 15), bg='black', fg='orange')
    l_h5.place(x=70, y=290)
    b1 = tk.Button(w1, text='Place Order', bg='black', fg='orange', command=order_placed)
    b1.place(x=260, y=330)
    b2 = tk.Button(w1, text='Go Back', bg='black', fg='orange', command=goback)
    b2.place(x=260, y=360)

def electronics():
        global e_b2,e_b3,e_b4,e_window
        e_window = tk.Toplevel()
        e_window.title("Electronics")
        e_window.geometry('600x600')
        e_window.configure(bg='white')

        e_l1 = tk.Label(e_window,text='Electronics',font=('Times New Roman', 30))
        e_l1.place(x=130, y=10)

        e_l2 = tk.Label(e_window,text="{}:{}".format(e_list[0],e_list_cost[0]),font=('Times New Roman', 30))
        e_l2.place(x=70, y=70)
        e_b2 = tk.Button(e_window,text='Buy Now',command= lambda: buynow(e_items['Mobile']),font=('Times New Roman', 15))
        e_b2.place(x=320, y=75)
        e_l3 = tk.Label(e_window, text="{}:{}".format(e_list[1],e_list_cost[1]),font=('Times New Roman', 30))
        e_l3.place(x=70, y=120)
        e_b3 = tk.Button(e_window, text='Buy Now',command= lambda: buynow(e_items['AirPods']),font=('Times New Roman', 15))
        e_b3.place(x=320, y=125)
        e_l4 = tk.Label(e_window, text="{}:{}".format(e_list[2],e_list_cost[2]),font=('Times New Roman', 30))
        e_l4.place(x=70, y=170)
        e_b4 = tk.Button(e_window, text='Buy Now',command= lambda: buynow(e_items['Charger']),font=('Times New Roman', 15))
        e_b4.place(x=320, y=175)
        e_window.mainloop()

def furniture():
    global f_window
    f_window = tk.Toplevel()
    f_window.title("Furniture")
    f_window.geometry('600x600')
    f_window.configure(bg='white')

    f_l1 = tk.Label(f_window, text='Furniture',font=('Times New Roman', 30))
    f_l1.place(x=130, y=10)

    f_l2 = tk.Label(f_window, text="{}:{}".format(f_list[0], f_list_cost[0]),font=('Times New Roman', 30))
    f_l2.place(x=70, y=70)
    f_b2 = tk.Button(f_window, text='Buy Now',command= lambda: buynow(f_items["Table"]),font=('Times New Roman', 15))
    f_b2.place(x=320, y=75)
    f_l3 = tk.Label(f_window, text="{}:{}".format(f_list[1], f_list_cost[1]),font=('Times New Roman', 30))
    f_l3.place(x=70, y=120)
    f_b3 = tk.Button(f_window, text='Buy Now',command= lambda: buynow(f_items["Chair"]),font=('Times New Roman', 15))
    f_b3.place(x=320, y=125)
    f_l4 = tk.Label(f_window, text="{}:{}".format(f_list[2], f_list_cost[2]),font=('Times New Roman', 30))
    f_l4.place(x=70, y=170)
    f_b4 = tk.Button(f_window, text='Buy Now',command= lambda: buynow(f_items["Desk"]),font=('Times New Roman', 15))
    f_b4.place(x=320, y=175)
    f_window.mainloop()

def grocery():
    global g_window
    g_window = tk.Toplevel()
    g_window.title("Grocery")
    g_window.geometry('600x600')
    g_window.configure(bg='white')

    g_l1 = tk.Label(g_window, text='Grocery',font=('Times New Roman', 30))
    g_l1.place(x=130, y=10)

    g_l2 = tk.Label(g_window, text="{}:{}".format(g_list[0], g_list_cost[0]),font=('Times New Roman', 30))
    g_l2.place(x=70, y=70)
    g_b2 = tk.Button(g_window, text='Buy Now',command= lambda: buynow(g_items["Milk"]),font=('Times New Roman', 15))
    g_b2.place(x=320, y=75)
    g_l3 = tk.Label(g_window, text="{}:{}".format(g_list[1], g_list_cost[1]),font=('Times New Roman', 30))
    g_l3.place(x=70, y=120)
    g_b3 = tk.Button(g_window, text='Buy Now',command= lambda: buynow(g_items["Potato"]),font=('Times New Roman', 15))
    g_b3.place(x=320, y=125)
    g_l4 = tk.Label(g_window, text="{}:{}".format(g_list[2], g_list_cost[2]),font=('Times New Roman', 30))
    g_l4.place(x=70, y=170)
    g_b4 = tk.Button(g_window, text='Buy Now',command= lambda: buynow(g_items["Tomato"]),font=('Times New Roman', 15))
    g_b4.place(x=320, y=175)
    g_window.mainloop()

a1 = "Welcome to Amazon.in\nIndia's most trusted website for Online shopping"
l1 = tk.Label(window, text=a1, bg='white', fg='black', font=('Times New Roman', 30))
l1.place(x=200, y=10)

l2 = tk.Label(window,text = 'Electronics', bg='white', fg='black', font=('Times New Roman', 25))
l2.place(x=200,y=100)
b2 = tk.Button(window, text='Shop Now', bg='white', fg='black', font=('Times New Roman', 12),command=electronics)
b2.place(x=400, y=110)

l3 = tk.Label(window, text='Furniture', bg='white', fg='black', font=('Times New Roman', 25))
l3.place(x=240, y=200)
b3 = tk.Button(window, text='Shop Now', bg='white', fg='black', font=('Times New Roman', 12),command=furniture)
b3.place(x=400, y=210)

l4 = tk.Label(window, text='Grocery', bg='white', fg='black', font=('Times New Roman', 25))
l4.place(x=240, y=300)
b4 = tk.Button(window, text='Shop Now', bg='white', fg='black', font=('Times New Roman', 12),command=grocery)
b4.place(x=400, y=310)

b5 = tk.Button(window, text='Cart', bg='white', fg='black', font=('Times New Roman', 12),command=bill)
b5.place(x=400,y=500)

def quit():
    if mb.askyesno("Quit","Do you wanna Quit"):
        window.destroy()

b6=tk.Button(window,text='Quit',command=quit)
b6.place(x=530,y=410)


window.mainloop()
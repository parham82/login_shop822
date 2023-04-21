# ----------------------- PARHAM KHOSSRAVI ------------------------

import tkinter
import sqlite3
import datetime


x=sqlite3.Connection("shop82.db")
print("connect to database!!")

#------------- create users-----------------
# query='''create table user82
# (id integer primary key,
# user char(30) not null,
# psw char(30) not null,
# addr char(40) not null)'''

# x.execute(query)
# x.close()


#------------------- insert into----------------
# query='''insert into user82(user,psw,addr)
# values('admin','123456789','rasht')'''

# x.execute(query)
# x.commit()
#------------------- create table product -------
# query='''CREATE TABLE products82
# ( ID INTEGER PRIMARY KEY,
# name CHAR(20) NOT NULL,
# price int NOT NULL,
# qnt int NOT NULL,
# comment TEXT,
# time char(20) not null)'''

# x.execute(query)
# x.close()

#-------- insert into products table -------------------
# query='''INSERT INTO products82 (name,price,qnt,time)
#       VALUES ('phone',2500,15,"?") '''

# x.execute(query)
# x.commit()
# x.close()

def delete():
    txt_user.delete(0,"end")
    txt_psw.delete(0,"end")

#------------------ login-------------------------
def login():
    user=txt_user.get()
    psw=txt_psw.get()
    if user=="admin":
        btn_admin_plan.configure(state="active",command=admin_plan)
    if len(user)==0 or len(psw)==0:
        lbl_msg.configure(text="please fill inputs",fg="red")
        return
    query='''select * from user82 where user=? and psw=?'''
    result=x.execute(query,(user,psw))
    rows=result.fetchall()
    if len(rows)==0:
        lbl_msg.configure(text="username or password are wrong",fg="red")
        return
    else:
        lbl_msg.configure(text="welcome to your acount",fg="green")
        delete()
        btn_login.configure(state="disabled")
        btn_logout.configure(state="active")
        btn_shop.configure(state="active")
        # btn_admin_plan.configure(state="disabled")
#--------------------- logout---------------------------
def logout():
    btn_login.configure(state="active")
    btn_logout.configure(state="disabled")
    btn_shop.configure(state="disabled")
    btn_admin_plan.configure("disabled")
    lbl_msg.configure(text="you are logged out",fg="green")
#--------------------- submit----------------------------
def fainal_submit():
    user=txt_user1.get()
    psw=txt_psw1.get()
    addr=txt_addr1.get()
    if len(user)==0 or len(psw)==0 or len(addr)==0:
        lbl_msg1.configure(text="please fill inputs",fg="red")
        return
    if len(psw)<8:
        lbl_msg.configure(text="password lenght wrong",fg="red")
        return
    query='''select * from user82 where user=? '''
    result=x.execute(query,(user,))
    rows=result.fetchall()
    if len(rows)!=0:
        lbl_msg1.configure(text="Username already exist",fg="red")
        return
    else:
        query='''insert into user82(user,psw,addr)
        values(?,?,?)'''
        x.execute(query,(user,psw,addr))
        x.commit()
        lbl_msg1.configure(text="submit done",fg="green")
        txt_user1.delete(0,"end")
        txt_psw1.delete(0,"end")
        txt_addr1.delete(0,"end")
def submit():
    global txt_addr1,txt_psw1,txt_user1,lbl_msg1
    win_submit=tkinter.Toplevel(win)
    win_submit.title("project")
    win_submit.geometry("200x200")

    lbl_user1=tkinter.Label(win_submit,text="Username: ")
    lbl_user1.pack()

    txt_user1=tkinter.Entry(win_submit,width=30)
    txt_user1.pack()

    lbl_psw1=tkinter.Label(win_submit,text="Password: ")
    lbl_psw1.pack()

    txt_psw1=tkinter.Entry(win_submit,width=30)
    txt_psw1.pack()

    lbl_addr1=tkinter.Label(win_submit,text="Addres")
    lbl_addr1.pack()

    txt_addr1=tkinter.Entry(win_submit,width=30)
    txt_addr1.pack()

    lbl_msg1=tkinter.Label(win_submit,text="")
    lbl_msg1.pack()

    btn_login=tkinter.Button(win_submit,text="submit now!",fg="brown",command=fainal_submit)
    btn_login.pack()

    win_submit.mainloop()
#------------------- shop------------------------
def shop():
    win_shop=tkinter.Toplevel(win)
    win_shop.title("shop")
    win_shop.geometry("400x400")

    lstbox=tkinter.Listbox(win_shop,width=40)
    lstbox.pack()

    query='''SELECT user FROM products'''
    result=x.execute(query)
    rows=result.fetchall()
    for product in rows:
        mystr=f"id: {product[0]}  name: {product[1]}  price: {product[2]}  qnt: {product[3]} "
        lstbox.insert(0, mystr)




    win_shop.mainloop()
#---------------------- read user --------------------------
def lst_user():
    query='''select * from user82 '''
    result=x.execute(query)
    rows=result.fetchall()
    for items in rows:
        lstbox2.insert(0,items)
#--------------------- list products ------------------------
def lst_products():
    win_lst_product=tkinter.Toplevel(win)
    win_lst_product.title("product")
    win_lst_product.geometry("400x400")

    lbl_pro=tkinter.Label(win_lst_product,text="report product",bg="green")
    lbl_pro.pack()

    PBox=tkinter.Listbox(win_lst_product,width=40)
    PBox.pack()
    
    query='''select name from products82'''
    result=x.execute(query)
    rows=result.fetchall()
    for pname in rows:
        PBox.insert(0,pname)

    win_lst_product.mainloop()
#------------------------ finish product --------------------
def lst_finish():
    win_lst_finish=tkinter.Toplevel(win)
    win_lst_finish.title("product")
    win_lst_finish.geometry("400x400")

    lbl_finish=tkinter.Label(win_lst_finish,text="report product",bg="gray")
    lbl_finish.pack()

    PBox=tkinter.Listbox(win_lst_finish,width=40)
    PBox.pack()
    
    query='''select * from products82 where qnt=0'''
    result=x.execute(query)
    rows=result.fetchall()
    for finish in rows:
        PBox.insert(0,finish)

    win_lst_finish.mainloop()
#---------------------- high shop -----------------------------------
def lst_hshop():
    win_lst_hshop=tkinter.Toplevel(win)
    win_lst_hshop.title("product")
    win_lst_hshop.geometry("400x400")

    lbl_h=tkinter.Label(win_lst_hshop,text="report product",bg="brown")
    lbl_h.pack()

    hBox=tkinter.Listbox(win_lst_hshop,width=40)
    hBox.pack()
    
    query='''select * from products82 where price!=0'''
    result=x.execute(query)
    rows=result.fetchall()
    for high in rows:
        st=f"high shope: {high[0]} "
        hBox.insert(0,st)

    win_lst_hshop.mainloop()
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ time @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def time():
    win_time=tkinter.Toplevel(win)
    win_time.title("Products bought in specific dates: " )
    win_time.geometry("400x400")
    
    
    query = '''SELECT * FROM products82 WHERE time= ? '''
    result=x.execute(query,(time,))
    rows=result.fetchall()
    
    timebox=tkinter.Listbox(win_time,width=40)
    timebox.pack()
    
    for product in rows :
         timebox.insert(0,product)
         
         
         
    win_time.mainloop()
    
    
def time2():
    Time=datetime.date.today()
    query=''' update product82 set time=?'''
    x.execute(query,(Time,))
    x.commit()
    
#----------------------- admin paln -------------------------
def admin_plan():
    global btn_user2,lstbox2
    win_admin=tkinter.Toplevel(win)
    win_admin.title("admin paln")
    win_admin.geometry("400x400")

    lbl_ad=tkinter.Label(win_admin,text="report user",bg="red")
    lbl_ad.pack()

    lstbox2=tkinter.Listbox(win_admin,width=40)
    lstbox2.pack()


    btn_user2=tkinter.Button(win_admin,text="list user",command=lst_user)
    btn_user2.pack()

    btn_prouduct2=tkinter.Button(win_admin,text="list prouduct",command=lst_products)
    btn_prouduct2.pack()


    btn_finish=tkinter.Button(win_admin,text="list finish",command=lst_finish)
    btn_finish.pack()


    btn_high=tkinter.Button(win_admin,text="list high shop",command=lst_hshop)
    btn_high.pack()

    btn_time=tkinter.Button(win_admin,text="time",command=time)
    btn_time.pack()


    win_admin.mainloop()

#----------------------- main------------------------------------
win=tkinter.Tk()
win.title("project")
win.geometry("400x400")

lbl_user=tkinter.Label(win,text="Username: ")
lbl_user.pack()

txt_user=tkinter.Entry(win,width=30)
txt_user.pack()

lbl_psw=tkinter.Label(win,text="Password: ")
lbl_psw.pack()

txt_psw=tkinter.Entry(win,width=30)
txt_psw.pack()

lbl_msg=tkinter.Label(win,text="")
lbl_msg.pack()

btn_login=tkinter.Button(win,text="login",fg="blue",command=login)
btn_login.pack()

btn_logout=tkinter.Button(text="logout",state="disabled",command=logout)
btn_logout.pack()

btn_submit=tkinter.Button(win,text="submit",fg="blue",command=submit)
btn_submit.pack()

btn_shop=tkinter.Button(win,text="shop",state="disabled",command=shop)
btn_shop.pack()

btn_admin_plan=tkinter.Button(win,text="admin plan",state="disabled",command=admin_plan)
btn_admin_plan.pack()


win.mainloop()
    
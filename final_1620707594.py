

from tkinter import*
import sqlite3
from tkinter import messagebox
from tkinter import ttk


def mainwindow() :
    global menubar,emptyMenu
    root = Tk()
    
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.title("หน้าเริ่มต้น")
    root.option_add("*font","supermarket 18 ")
    
    root.resizable(False,False)
    
    menubar = Menu(root)
    emptyMenu = Menu(root)
    
    menubar.add_command(label="ร้านค้า",command=shoppage)
    menubar.add_command(label="โปรไฟล์",command=showprofile)
    menubar.add_command(label="ออกจากระบบ", command=logoutclick)
    menubar.add_command(label="ออกจากโปรแกรม", command=root.quit) 
    
    return root

def rootwidget(root) :
    global loot
    loot = Frame(root, bg='lightpink')
    loot.place(x=0,y=0,width=w,height=h)
    loot.rowconfigure((0,1,2,3),weight=1)
    loot.columnconfigure((0,1,2,3),weight=1)
    Label(loot, text="""ยินดีต้อนรับสู่โปรแกรมสำหรับการสั่งซื้อสินค้า""", bg='lightpink', font='supermarket 32').grid(row=1,column=1,columnspan=2,sticky="news")
    Button(loot, text='get started', font="supermarket 24",command=loginlayout,width=20).grid(row=2, column=1, columnspan=2)



#เชื่อต่อกับDB
def createconnection() :
    global conn,cursor
    conn = sqlite3.connect('db/finalproject.db')
    cursor = conn.cursor()
    
# สร้างloginlayaut
def loginlayout() :
    global userentry,pwdentry,loginframe
    
    loginframe = Frame(loot,bg='#709fb0')
    loginframe.rowconfigure((0,1,2,3,4), weight=1)
    loginframe.columnconfigure((0,1,2), weight=1)
    root.title("หน้าล็อกอินเข้าสู่ระบบ")
    
    Label(loginframe, image=img_logo,bg='#709fb0').grid(row=0,column=0,columnspan=3)
    Label(loginframe, text='เข้าสู่ระบบ', fg='white', bg='#709fb0').grid(row=1, column=0,columnspan=3)
    Label(loginframe, text="Username :",fg="white",bg='#709fb0').grid(row=2,column=0,sticky=E)
    Label(loginframe, text="รหัสผ่าน :",fg="white",bg='#709fb0').grid(row=3,column=0,sticky=E)
    
    userentry = Entry(loginframe, width=20)
    userentry.grid(row=2, column=1, columnspan=2, sticky=W, padx=50)
    
    pwdentry = Entry(loginframe, width=20, show="*")
    pwdentry.grid(row=3, column=1, columnspan=2, sticky=W, padx=50)
    
    Button(loginframe, text="กลับ", width=10, height=1, command=loginframe.destroy).grid(row=4, column=0)
    Button(loginframe, text="สมัครบัญชีผู้ใช้", width=15, height=1, command=regiswindow).grid(row=4, column=1, sticky=E)    
    Button(loginframe, text="ล็อกอิน", width=10, height=1, bg="lightgreen", command=loginclick).grid(row=4, column=2, sticky=W, padx=20) 
    
    loginframe.grid(row=1,column=1,columnspan=2,rowspan=2,sticky='news')

def regiswindow() :
    global fullname,lastname,newuser,newpwd,cfpwd,identry,newid
    global regisframe
    loginframe.destroy()
    
    root.title("หน้าการสมัครบัญชี")
    loot.config(bg='lightblue')    
    regisframe = Frame(loot,bg='#8ac4d0')
    regisframe.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11),weight=1)
    regisframe.columnconfigure((0,1),weight=1)
    
    Label(regisframe,text="สร้างบัญชีผู้ใช้",font="supermarket 26",fg='#e4fbff',bg='#1687a7').grid(row=0,column=0,columnspan=2,sticky='news',pady=10)
    
    sql = 'SELECT * FROM user'
    cursor.execute(sql)
    id = cursor.fetchall()
    for i,data in enumerate(id) :
        print(data[0])
    newid = data[0] + 1
    
    Label(regisframe,text='ชื่อจริง : ',bg='#8ac4d0',fg='#f6f5f5').grid(row=2,column=0,sticky='e',padx=10)
    fullname = Entry(regisframe,width=20,bg='#d3e0ea')
    fullname.grid(row=2,column=1,sticky='w',padx=10)
    
    Label(regisframe,text='นามสกุล : ',bg='#8ac4d0',fg='#f6f5f5').grid(row=3,column=0,sticky='e',padx=10)
    lastname = Entry(regisframe,width=20,bg='#d3e0ea')
    lastname.grid(row=3,column=1,sticky='w',padx=10)
    

    Label(regisframe, text="เพศ :", bg='#8ac4d0', fg='#f6f5f5').grid(row=6,column=0, sticky="e",padx=18)
    Radiobutton(regisframe, text="ชาย", bg='#8ac4d0', variable=genderinfo,value="ชาย").grid(row=6, column=1,sticky="w",padx=5)
    Radiobutton(regisframe, text="หญิง", bg='#8ac4d0', variable=genderinfo,value="หญิง").grid(row=7, column=1,sticky="w",padx=5)
    Radiobutton(regisframe, text="อื่นๆ", bg='#8ac4d0', variable=genderinfo,value="อื่นๆ").grid(row=8, column=1,sticky="w",padx=5)
    genderinfo.set(" ")
    
    Label(regisframe,text="อายุ : ",bg='#8ac4d0',fg='#f6f5f5').grid(row=9,column=0,sticky='e',padx=10)
    Spinbox(regisframe, width=10, from_=1,to=100, bg='#d3e0ea', textvariable=year).grid(row=9,column=1, sticky='w',padx=10)
    
    Label(regisframe,text="Username : ",bg='#8ac4d0',fg='#f6f5f5').grid(row=10,column=0,sticky='e',padx=10)
    newuser = Entry(regisframe,width=20,bg='#d3e0ea')
    newuser.grid(row=10,column=1,sticky='w',padx=10)
    
    
    Label(regisframe,text="รหัสผ่าน : ",bg='#8ac4d0',fg='#f6f5f5').grid(row=11,column=0,sticky='e',padx=10)
    newpwd = Entry(regisframe,width=20,bg='#d3e0ea',show='*')
    newpwd.grid(row=11,column=1,sticky='w',padx=10)
    
    Label(regisframe,text="ยืนยันรหัสผ่าน : ",bg='#8ac4d0',fg='#f6f5f5').grid(row=12,column=0,sticky='e',padx=10)
    cfpwd = Entry(regisframe,width=20,bg='#d3e0ea',show='*')
    cfpwd.grid(row=12,column=1,sticky='w',padx=10)
    
    #Add Cancel button
    regisaction = Button(regisframe,text="ยืนยันการสมัคร",bg="blue",fg="white",command=registration)
    regisaction.grid(row=13,column=1,ipady=5,ipadx=5,pady=5,sticky='e')
    Button(regisframe,text="ยกเลิก",command=exitRegistClick).grid(row=13,column=0,ipady=5,ipadx=5,padx=10,sticky='w')
    regisframe.grid(row=1,column=1,columnspan=2,rowspan=2,sticky='news')
    
def loginclick() :
    global user
    user = userentry.get() 
    
    if user == "" :
        messagebox.showwarning("แอดมิน:","กรุณาใส่ username")
        userentry.focus_force()
    elif pwdentry.get() == "" :
        messagebox.showwarning("แอดมิน:","กรุณาใส่ password")
        pwdentry.focus_force()
    else :
        sql = "SELECT * FROM user WHERE username = ? and password = ?"
        cursor.execute(sql, [user, pwdentry.get()])
        result = cursor.fetchall() #fetch data from sql
        if result :
            messagebox.showinfo("แอดมิน:","ล็อกอินเสร็จสิ้น")
            showprofile()
            loginframe.destroy()   
        else :
            #no result
            messagebox.showwarning("แอดมิน:","Username หรือ Password ไม่ถูกต้อง")
            userentry.select_range(0,END)
            userentry.focus_force()

def showprofile() :
    global profile_frm
    
    root.title("หน้าโปรไฟล์")
    root.config(menu=menubar)
    
    profile_frm = Frame(loot, bg='#C0F58B')
    profile_frm.rowconfigure((0,1,2,3,4,5,6), weight=1)
    profile_frm.columnconfigure((0,1), weight=1)
    profile_frm.place(x=0,y=0,width=w,height=h)
    
    sql_user = "SELECT * FROM user WHERE username = ?"
    cursor.execute(sql_user, [user])
    result_user = cursor.fetchone() # fetch data from sql
    
    name = result_user[3]+" "+result_user[4] #create variable for use later
    root.title("ยินดีต้อนรับ : %s "%(name))
    
    if result_user :
        print(result_user)
        if result_user[6] == "ชาย" :
            Label(profile_frm, image=img_m, bg='#C0F58B').grid(row=0, column=0, columnspan=2, pady=5)
        elif result_user[6] == "หญิง":
            Label(profile_frm, image=img_f, bg='#C0F58B').grid(row=0, column=0, columnspan=2, pady=5)
        else :
            Label(profile_frm, image=img_birb, bg='#C0F58B').grid(row=0, column=0, columnspan=2, pady=5)
        
        Label(profile_frm, text="ID ผู้ใช้ :", bg='#C0F58B').grid(row=1, column=0, sticky=E)
        Label(profile_frm, text= result_user[0], bg='#C0F58B').grid(row=1, column=1, sticky=W)      
        
        if user == "admin" :
            Button(profile_frm, text="แก้ไขข้อมูลลูกค้า").grid(row=6, column=1, columnspan=2, padx=10, pady=10, ipadx=10, ipady=10, sticky="e")
        else :
            Button(profile_frm, text="แก้ไขข้อมูล").grid(row=6, column=1, columnspan=2, padx=10, pady=10, ipadx=10, ipady=10, sticky="e")
        
        Label(profile_frm, text="ชื่อ :", bg='#C0F58B').grid(row=2, column=0, sticky=E)
        Label(profile_frm, text= name, bg='#C0F58B').grid(row=2, column=1, sticky=W)
        
        Label(profile_frm, text="แต้มคงเหลือ :", bg='#C0F58B').grid(row=3, column=0, sticky=E)
        Label(profile_frm, text=result_user[7], bg='#C0F58B').grid(row=3, column=1, sticky=W)
        
        Label(profile_frm, text="อายุ :", bg='#C0F58B').grid(row=4, column=0, sticky=E)
        Label(profile_frm, text= result_user[5], bg='#C0F58B').grid(row=4, column=1, sticky=W)
        
        Label(profile_frm, text="เพศ :", bg='#C0F58B').grid(row=5, column=0, sticky=E)
        Label(profile_frm, text= result_user[6], bg='#C0F58B').grid(row=5, column=1, sticky=W)
          
def registration() :
    if fullname.get() == '' :
        messagebox.showwarning("แอดมิน:","กรุณาใส่ ชื่อจริง")
        fullname.focus_force()
    elif lastname.get() == '' :
        messagebox.showwarning("แอดมิน:","กรุณาใส่ นามสกุล")
        lastname.focus_force()
    elif genderinfo.get() == ' ' :
        messagebox.showwarning("แอดมิน:","กรุณาเลือก เพศ")
    elif newuser.get() == '' :
        messagebox.showwarning("แอดมิน:","กรุณาใส่ username")
        newuser.focus_force()
    #check blank other field
    else :
        sql_chk = "SELECT * FROM user WHERE username=?"
        cursor.execute(sql_chk, [newuser.get()])
        chk_user = cursor.fetchall()
        if chk_user :
            messagebox.showwarning("แอดมิน","ขออภัย username นี้มีผู้ใช้แล้ว\nกรุณาลองอีกครั้ง")
            newuser.select_range(0, END)
            newuser.focus_force()
        
        sql_chk = "SELECT * FROM user WHERE password=?"
        cursor.execute(sql_chk, [newpwd.get()])
        chk_pass = cursor.fetchall()
        if chk_pass :
            messagebox.showwarning("แอดมิน","ขออภัยรหัสผ่านนี้มีผู้ใช้แล้ว\nกรุณาลองอีกครั้ง")
            newpwd.select_range(0, END)
            newpwd.focus_force()
        else :
            if newpwd.get() == cfpwd.get() :
                point = 0
                sql_ins = "INSERT INTO  user VALUES(?,?,?,?,?,?,?,?)"
                cursor.execute(sql_ins,[newid,newuser.get(),newpwd.get(),fullname.get(),lastname.get(),year.get(),genderinfo.get(),point])   
                    
                conn.commit()
                retrivedata()
                    
                messagebox.showinfo("แอดมิน:","สมัครบัญชีเสร็จสิ้น\nกรุณาล็อกอิน")
                    
                newuser.delete(0, END)
                newpwd.delete(0, END)
                cfpwd.delete(0, END)
                fullname.delete(0, END)
                lastname.delete(0, END)
                genderinfo.set(" ")
                year.set(1)
                    
                exitRegistClick()         
            else :
                messagebox.showwarning("แอดมิน:","รหัสผ่านไม่ตรงกัน\nกรุณาลองอีกครั้ง")

def shoppage() :

    global shopframe
    root.title("หน้าร้านค้า")
    
    shopframe = Frame(loot,bg='skyblue')
    shopframe.place(x=0,y=0,width=w,height=h)
    shopframe.rowconfigure((0,1,2,3,4,5,6), weight=1)
    shopframe.columnconfigure((0,1,2,3), weight=1)
    
    sql = 'SELECT * FROM product'
    cursor.execute(sql)
    result = cursor.fetchall()        
    
    for i,data in enumerate(result) :
        
        if data[0] == 'C001' :
            Label(shopframe,image=img_shirt1,bg='lightpink').grid(row=i,column=0,sticky='news',pady=5)
        elif data[0] == 'C002' :
            Label(shopframe,image=img_shirt2,bg='lightpink').grid(row=i,column=0,sticky='news',pady=5)
        elif data[0] == 'C003' :
            Label(shopframe,image=img_shoe,bg='lightpink').grid(row=i,column=0,sticky='news',pady=5)
        elif data[0] == 'C004' :
            Label(shopframe,image=img_shirt3,bg='lightpink').grid(row=i,column=0,sticky='news',pady=5)
        elif data[0] == 'C005' :
            Label(shopframe,image=img_mask,bg='lightpink').grid(row=i,column=0,sticky='news',pady=5)

        Label(shopframe,text=data[1],bg='lightpink').grid(row=i,column=1,sticky='news',pady=5)
        Label(shopframe,text=str(data[2])+" "+"บาท",bg='lightpink').grid(row=i,column=2,sticky='news',pady=5)
        
        Checkbutton(shopframe,bg='lightpink',variable=chkspy[i]).grid(row=i,column=3,sticky='news',pady=5)
        
        Button(shopframe,text="สั่งสินค้า",width=13,command=buypage).grid(row=i+1,column=1,columnspan=2)
        
        if user == "admin" :
            Button(shopframe,text="ดูตารางสินค้า",width=13,command=detailshop).grid(row=i+1,column=0)

def detailshop() :
    global bgframe,mytree,detailframe,p_id,p_name,price,quantity
    
    root.title("หน้าตารางสินค้า")
    
    bgframe = Frame(loot, bg='red')
    bgframe.place(x=0,y=0,width=w,height=h)
    bgframe.columnconfigure((0,1), weight=1)                                     
    bgframe.rowconfigure((0,1), weight=1)
    
    treeframe = Frame(bgframe,bg='yellow')
    treeframe.rowconfigure((0,1,2), weight=1)
    treeframe.columnconfigure((0,1), weight=1)
    treeframe.grid(column=0,row=0,rowspan=2,sticky='news')
    
    Label(treeframe, text="ตารางสินค้า",bg='yellow').grid(row=0,column=0,columnspan=2)
    
    mytree = ttk.Treeview(treeframe, columns=("id","product name", "price","quantity"), height=2)
    
    #create headings
    mytree.heading('#0', text='') #default
    mytree.heading('product name', text="Product Name", anchor=CENTER)
    mytree.heading('price', text="Price", anchor=CENTER)
    mytree.heading('id', text="ID", anchor=CENTER)
    mytree.heading('quantity', text="Quantity", anchor=CENTER) 
    
    #format columns
    mytree.column("#0", width=0, minwidth=0)
    mytree.column('quantity', anchor=W, width=150)
    mytree.column('id', anchor=W, width=150)
    mytree.column('product name', anchor=W, width=150)
    mytree.column('price', anchor=W, width=150)
    
    mytree.grid(row=1, column=0,columnspan=2, sticky='news')
    
    mytree.bind('<Double-1>', treeviewclick) # Double click event
    
    fetch_tree()

    Button(treeframe,text="แก้ไขข้อมูลสินค้า",width=13).grid(row=2,column=0)
    Button(treeframe,text="เพิ่มสินค้า",width=13).grid(row=2,column=1)
          
    detailframe = LabelFrame(bgframe, bg='orange',text='รายละเอียดสินค้า',font='supermarket 10')
    detailframe.rowconfigure((0,1,2,3,4,5,6,7), weight=1)
    detailframe.columnconfigure((0,1), weight=1)
    detailframe.grid(column=1,row=0,rowspan=2,sticky='news')
    
    Label(detailframe, text='ID สินค้า :',bg='orange').grid(row=2,column=0,sticky=E)
    p_id = Entry(detailframe,width=20)
    p_id.grid(row=2,column=1,sticky=W)
    
    Label(detailframe, text='ชื่อสินค้า :',bg='orange').grid(row=3,column=0,sticky=E)
    p_name = Entry(detailframe,width=20)
    p_name.grid(row=3,column=1,sticky=W)
    
    Label(detailframe, text='ราคาสินค้า:',bg='orange').grid(row=4,column=0,sticky=E)
    price = Entry(detailframe,width=20)
    price.grid(row=4,column=1,sticky=W)
        
    Label(detailframe, text='สินค้าคงเหลือ :',bg='orange').grid(row=5,column=0,sticky=E)
    quantity = Entry(detailframe,width=20)
    quantity.grid(row=5,column=1,sticky=W)
    
def retrivedata() :
    sql = "select * from user"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Total row = ",len(result))
    for i,data in enumerate(result) :
        print("Row#",i+1,data)

def exitRegistClick() :
    regisframe.destroy()
    loot.config(bg="lightpink")
    loginlayout()


# ออกจากระบบ
    
def logoutclick() :
    root.config(menu=emptyMenu)
    loot.destroy()
    rootwidget(root)
    loginlayout()
               
def fetch_tree():
    mytree.delete(*mytree.get_children())
    sql = 'SELECT * FROM product'
    cursor.execute(sql)
    result = cursor.fetchall()
    if result :
        for i,data in enumerate(result) :
            mytree.insert('','end', values=(data[0],data[1],data[2],data[3]))
        
def treeviewclick(event):
    prod = mytree.item(mytree.focus(), 'values')
    
    p_id.delete(0,END)
    p_name.delete(0,END)
    price.delete(0,END)
    
    p_id.insert(0, prod[0])
    p_name.insert(0, prod[1])
    price.insert(0, prod[2])
    
    quantity.delete(0,END)
    quantity.insert(0, prod[3])
    
def buypage() :
    global buyframe,spinspy,totalentry,amtentry
    sum = 0
    for i in range(prodamt) :
        sum = sum + int(chkspy[i].get()) 
            #chkspy[i].set(0)
    
    if sum == 0 :
        messagebox.showinfo("แอดมิน","กรุณาเลือกสินค้า")            
    else :
        root.config(menu=emptyMenu)
        root.title("หน้าดำเนินการชำระเงิน")
        buyframe = Frame(loot, bg='lightblue')
        buyframe.place(x=0,y=0,width=w,height=h)
        buyframe.rowconfigure((0,1,2,3,4,5,6,7), weight=1)
        buyframe.columnconfigure((0,1,2,3), weight=1)
        
        sql = "SELECT * FROM product"
        cursor.execute(sql)
        result = cursor.fetchall()
        
        Label(buyframe, text="ชื่อสินค้า",bg='lightblue',font='supermarket 18').grid(row=0,column=0,sticky=W,padx=15)
        Label(buyframe, text="ราคาสินค้า",bg='lightblue',font='supermarket 18').grid(row=0,column=2,sticky=W,padx=15)
        Label(buyframe, text="จำนวนสินค้า",bg='lightblue',font='supermarket 18').grid(row=0,column=3,sticky=W,padx=15)
        j = 0
        
        for i,data in enumerate(result) :
            if chkspy[i].get() :
                Label(buyframe, text=data[1],bg='lightblue',font='supermarket 14').grid(row=j+1,column=0,sticky=W,padx=15)
                Label(buyframe, text=str(data[2])+" "+"บาท",bg='lightblue',font='supermarket 14').grid(row=j+1,column=2,sticky=W,padx=15)
                Spinbox(buyframe,width=10,from_=1,to=999,textvariable=amtlist[i]).grid(row=j+1,column=3,padx=15)
                #chkspy[i].set(0)
                j = j + 1
        totalentry = Entry(buyframe)
        totalentry.grid(row=j+1,column=2)
        
        amtentry = Entry(buyframe)
        amtentry.grid(row=j+1,column=3)
             
        Button(buyframe, text='กลับ',width=10,command=buyexit).grid(row=i+3,column=0) 
        Button(buyframe, text='ตรวจสอบยอดสุทธิ',width=18,command=totalchk).grid(row=j+1,column=0)
        Button(buyframe, text='ยืนยันการชำาระ',width=14,command=buy).grid(row=i+3,column=1,columnspan=2)


# ทำราคา

def totalchk() :
    total = 0
    amt = 0
    sql = "SELECT * FROM product"
    cursor.execute(sql)
    result = cursor.fetchall()
    
    for i,data in enumerate(result) :
        if chkspy[i].get() :
            amt = amt + amtlist[i].get()
            total = total + (data[2]*amtlist[i].get())
            
    print("amt",amt)        
    print("total",total)
    
    totalentry.delete(0, END)
    amtentry.delete(0, END)
    
    totalentry.insert(0, total)
    amtentry.insert(0, amt)
            
#  ซื้อ   
def buy() :
    if totalentry.get() == "" :
        messagebox.showwarning("แอดมิน:","กรุณาตรวจสอบยอดสุทธิ")
    else :
        messagebox.showinfo("แอดมิน:","ดำเนินการชำระเงินเสร็จสิ้น\nขอบคุณที่ใช้บริการ")
        for i in range(prodamt) :
            chkspy[i].set(0)
        buyexit()
    
def buyexit() :
    buyframe.destroy()
    root.config(menu=menubar)   
def sql() :
    global prodamt
    sql = "SELECT * FROM product"
    cursor.execute(sql)
    result = cursor.fetchall()
    prodamt = len(result)
    
w = 1000
h = 700

createconnection()
root = mainwindow()

sql()
amtlist = [IntVar() for i in range(prodamt)]
chkspy = [IntVar() for i in range(prodamt)] 
year = StringVar()
genderinfo = StringVar()

img_logo = PhotoImage(file="img/login.png").subsample(5,5)
img_m = PhotoImage(file="img/profile.png").subsample(2,2)
img_f = PhotoImage(file="img/profile_f.png").subsample(6,6)
img_birb = PhotoImage(file="img/birb.png").subsample(6,6)

# สินค้า
img_shirt1 = PhotoImage(file='img/shirt001.png').subsample(8,8)
img_shirt2 = PhotoImage(file='img/shirt002.png').subsample(8,8)
img_shirt3 = PhotoImage(file='img/shirt003.png').subsample(8,8)
img_mask = PhotoImage(file="img/mask.png").subsample(8,8)
img_shoe = PhotoImage(file="img/shoe.png").subsample(8,8)

rootwidget(root)

root.mainloop()
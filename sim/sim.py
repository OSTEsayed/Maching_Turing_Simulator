import tkinter as tk
from tkinter.constants import END, Y
from tkinter import filedialog as fd
import time
mat=[]
pon=0
def start():
    def disp(s,p,r,xw,x):
        z="".join([str(item) for item in s])
        e.delete(0,END)
        e.insert(0,z)
        e.select_range(p,p+1)
        e.update()
        for tag in etat.tag_names():
            etat.tag_delete(tag)
        etat.see("{}.0".format(r))
        etat.tag_add("start", "{}.0".format(r),"{}.20".format(r))
        etat.tag_configure("start", background="#0080FF", foreground="black")
        tap.config(text="Etape:{}".format(x))
        cer.config(text="Etat Curent:{}".format(xw))
        
        time.sleep(0.3)
    def Accpt(s):
        z="".join([str(item) for item in s])
        e.delete(0,END)
        e.insert(0,z)
        
        result= tk.Label(frame2,text="   Resultat :", font=("Courrier", 20),fg="Black",bg="#38FFAE")
        result.grid(row=0,column=6,columnspan=5)
        result_ak= tk.Label(frame2,text="   Accepte ", font=("Courrier", 30),fg="blue",bg="#38FFAE")
        result_ak.grid(row=1,column=6,columnspan=5)
        sim.mainloop()
    def refuse():
        result= tk.Label(frame2,text="   Resultat :", font=("Courrier", 20),fg="Black",bg="#38FFAE")
        result.grid(row=0,column=6,columnspan=5)
        result_ak= tk.Label(frame2,text="   Refuse ", font=("Courrier", 30),fg="red",bg="#38FFAE")
        result_ak.grid(row=1,column=6,columnspan=5)
        sim.mainloop()
    def simuler():
        for i in range(len(mat)):
            if mat[i][2]=="_":
                mat[i][2]=" "
            if mat[i][1]=="_":
                mat[i][1]=" "
                
        c=[]
        s=e.get()
        ni="          "
        for j in ni:c.append(j)
        for i in s:c.append(i)
        for j in ni:c.append(j)
        b=0
        p=10
        ref=0
        etape=0
        etat="q0"
        tster=0
        
        while tster==0: 
            if c[p]==";" and ref==2:
                            p=p-1
                            while c[p]!=";":
                                p=p-1
                            p=p-1
            elif c[p]==";" and ref==1:
                            p=p+1
                            while c[p]!=";":
                                p=p+1
                            p=p+1
            ref=0
            b=1
            for i in range(len(mat)):
                if mat[i][1]=="*" and etat==mat[i][0]:
                    etat=mat[i][4]
                    if mat[i][2]!="*":
                        c[p]=mat[i][2]
                    etape=etape+1
                    disp(c,p,i+1,mat[i][0],etape)    
                    if mat[i][3]=="r":
                        p=p+1
                        ref=1
                    if mat[i][3]=="l":
                        p=p-1
                        ref=2
                    if etat=="stop":
                        Accpt(c)
                        b=0
                        tster=1
                    else :
                        b=0
                        break
                elif c[p]==mat[i][1] and etat==mat[i][0] :
                    if mat[i][2]!="*":
                        c[p]=mat[i][2]
                    etape=etape+1
                    disp(c,p,i+1,mat[i][0],etape)    

                    etat=mat[i][4]
                    if mat[i][3]=="r":
                        p=p+1
                        ref=1
                    if mat[i][3]=="l":
                        p=p-1
                        ref=2
                    if etat=="stop":
                        Accpt(c)
                        b=0
                        tster=1
                    else :
                        b=0
                        break
            if b==1:
                    refuse()
                    tster=1
    
    def auto1():
        etat.delete('1.0', END)
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='C:/Users/admin/Desktop/sayed/codes/python/sim',
            filetypes=filetypes)

        global mat
        mat = []
        a  = open(filename, "r")
        b  = open(filename, "r")
        f2= b.read() 
        if a.mode == 'r':
            f1=a.readlines()
            for i in f1:
                x=i.split()
                mat.append(x)
        etat.insert(END,f2) 
    def save():
        global mat
        mat = []
        path = fd.asksaveasfile(filetypes = (("Text files", "*.txt"), ("All files", "*.*"))).name
        f=open(path, 'w')
        f.write(etat.get('1.0', tk.END))
        x=etat.get('1.0', tk.END)
        mat=[s.split(' ') for s in x.split('\n')]
        mat.pop(len(mat)-1)
        print(mat)
        
    frame1.destroy()
    frame2=tk.Frame(sim,background="#38FFAE")
    e= tk.Entry(sim,border=5,font=("Courrier",20),justify="center")
    e.place(width=600,height=50)
    lab= tk.Label(frame2,text="Entre Votre Module :", font=("Courrier", 20),fg="Black",bg="#38FFAE")
    lab.grid(row=0,column=0,columnspan=5)
    cer= tk.Label(sim,text="Etat Curent:", font=("Courrier", 15),fg="Black",bg="#38FFAE")
    cer.place(x=10,y=70)
    tap= tk.Label(sim,text="Etape:", font=("Courrier", 15),fg="Black",bg="#38FFAE")
    tap.place(x=420,y=70)

    etat= tk.Text(frame2, width=40, height=12, font=16,)
    etat.grid(row=1,column=0,columnspan=5)

    simule=tk.Button(sim,text="Simuler",font=("Courrier",20),bg="black",fg="white",command=simuler)
    simule.place(x=200,y=500,width=200,height=60)
    frame2.place(x=120,y=100)
    Auto1=tk.Button(frame2,text="Open File",font=("Courrier",20),bg="red",fg="white",command=auto1,width=7,height=1)
    Auto1.grid(row=2,column=0)
    save1=tk.Button(frame2,text="save File",font=("Courrier",20),bg="white",fg="red",command=save,width=7,height=1)
    save1.grid(row=2,column=3)


    frame2.place(x=10,y=150)
    simule=tk.Button(sim,text="Simuler",font=("Courrier",20),bg="black",fg="white",command=simuler)
    sim.mainloop()
sim = tk.Tk()
sim.title("Simulateur")
sim.geometry("600x600+300+100")
sim.config(background="#38FFAE")
sim.iconbitmap("2172814.ico")
sim.maxsize(600,600)
sim.minsize(600,600)
frame1=tk.Frame(sim,background="#38FFAE")
play=tk.Button(frame1,text="Start Simulation",font=("Courrier",20),bg="black",fg="white",command=start)
width= 600   
height =500  
image = tk.PhotoImage(file="2172814.png")
canvas= tk.Canvas(frame1,width=width,height=height,bg='#38FFAE',bd=0,highlightthickness=0)               
canvas.create_image(width/2,height/2, image=image)


frame1.place(x=0,y=0)
canvas.pack()
play.pack(expand=Y)
sim.mainloop()
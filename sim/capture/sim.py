import tkinter as tk
from tkinter.constants import END, Y
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

mat=[]
pon=0
def start():
    
    def addetat():
        global mat
        et=etat.get()
        val=valeur.get()
        val_c=valeur_c.get()
        d=direct.get()
        net=etat_s.get()
        etate=[et,val,val_c,d,net]
        if d !='l' and d !='r' and d !='*':
            res=tk.Tk() 
            res.title("Ereur!!")
            res.geometry("600x150+200+150")
            res.config(background="black")
            r1 =tk.Label(res, text="the direction must be (r) or (l) or (*)\n ajoute etat refuse!", font=("Courrier", 20),fg="white",bg="black")
            r1.pack()

            res.mainloop()
        else:
            #res=tk.Tk() 
            #res.title("success")
            #res.geometry("600x150+200+150")
            #res.config(background="black")
            #r1 =tk.Label(res, text="L'ajoutation de etate effectue avec success", font=("Courrier", 20),fg="white",bg="Black")
            #r1.pack() 

            mat.append(etate)    
            etat.delete(0,END)
            valeur.delete(0,END)
            valeur_c.delete(0,END)
            direct.delete(0,END)
            etat_s.delete(0,END)

            #res.mainloop()
    def voire():
        s=""
        for i in mat:
            s=s+"<"+i[0]+"><"+i[1]+"><"+i[2]+"><"+i[3]+"><"+i[4]+">\n"
        res1=tk.Tk() 
        res1.title("Module")
        res1.geometry("700x400+200+150")
        res1.config(background="black")
        r1 =tk.Label(res1, text=s, font=("Courrier", 20),fg="white",bg="Black")
        r1.pack()
        res1.mainloop()
    def Accpt(s):
        z="".join([str(item) for item in s])
        e.delete(0,END)
        e.insert(0,z)
        result= tk.Label(frame2,text="-----Resultat------", font=("Courrier", 30),fg="Black",bg="#38FFAE")
        result.grid(row=3,column=0,columnspan=5)
        result_ak= tk.Label(frame2,text="Accepte ", font=("Courrier", 30),fg="Black",bg="#38FFAE")
        result_ak.grid(row=4,column=0,columnspan=5)
        sim.mainloop()
    def refuse():
        result= tk.Label(frame2,text="-----Resultat------", font=("Courrier", 30),fg="Black",bg="#38FFAE")
        result.grid(row=3,column=0,columnspan=5)
        result_ak= tk.Label(frame2,text=" Refuse ", font=("Courrier", 30),fg="Black",bg="#38FFAE")
        result_ak.grid(row=4,column=0,columnspan=5)
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
        p=12
        ref=0
        etater=[]
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
            for i in range(len(mat)):
                if etat==mat[i][0]:
                    b=b+1
                    etater.append(mat[i])
            for i in range(b):
                if etater[i][1]=="*":
                    etat=etater[i][4]
                    if etater[i][2]!="*":
                        c[p]=etater[i][2]
                    if etater[i][3]=="r":
                        p=p+1
                        ref=1
                    if etater[i][3]=="l":
                        p=p-1
                        ref=2
                    if etat=="stop":
                        Accpt(c)
                        b=0
                        tster=1
                    else :
                        etater.clear()
                        b=0
                        break
                elif c[p]==etater[i][1]:
                    if etater[i][2]!="*":
                        c[p]=etater[i][2]
                    etat=etater[i][4]
                    if etater[i][3]=="r":
                        p=p+1
                        ref=1
                    if etater[i][3]=="l":
                        p=p-1
                        ref=2
                    if etat=="stop":
                        Accpt(c)
                        b=0
                        tster=1
                    else :
                        etater.clear()
                        b=0
                        break
                elif i==(b-1):
                    refuse()
                    tster=1
    def rest():
        global mat
        mat = []
    def auto1():
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        showinfo(
            title='Selected File',
            message=filename
        )
        global mat
        mat = []
        a  = open(filename, "r")
        if a.mode == 'r':
            f1=a.readlines()
            for i in f1:
                x=i.split()
                mat.append(x) 
   















    frame1.destroy()
    frame2=tk.Frame(sim,background="#38FFAE")
    e= tk.Entry(sim,border=5,font=("Courrier",20))
    e.place(width=600,height=50)
    lab= tk.Label(frame2,text="Entre Votre Module :", font=("Courrier", 30),fg="Black",bg="#38FFAE")
    lab.grid(row=0,column=0,columnspan=5)

    etat= tk.Entry(frame2,border=5,font=("Courrier",15),width=5)
    etat.grid(row=1,column=0)
    valeur= tk.Entry(frame2,border=5,font=("Courrier",15),width=1)
    valeur.grid(row=1,column=1)
    valeur_c= tk.Entry(frame2,border=5,font=("Courrier",15),width=1)
    valeur_c.grid(row=1,column=2)
    direct= tk.Entry(frame2,border=5,font=("Courrier",15),width=1)
    direct.grid(row=1,column=3)
    etat_s= tk.Entry(frame2,border=5,font=("Courrier",15),width=5)
    etat_s.grid(row=1,column=4)
    add=tk.Button(frame2,text="Add etat",font=("Courrier",20),bg="black",fg="white",command=addetat)
    add.grid(row=2,column=0,columnspan=2)
    Voir=tk.Button(frame2,text="votre module",font=("Courrier",20),bg="black",fg="white",command=voire)
    Voir.grid(row=2,column=3,columnspan=2)
    notef=tk.Button(sim,text="Important notice!",font=("Courrier",20),bg="black",fg="white",command=notfic)
    notef.place(x=400,y=560,width=200,height=40)
    simule=tk.Button(sim,text="Simuler",font=("Courrier",20),bg="black",fg="white",command=simuler)
    simule.place(x=200,y=500,width=200,height=60)
    frame2.place(x=120,y=100)
    Auto1=tk.Button(sim,text="Open File",font=("Courrier",20),bg="red",fg="white",command=auto1)
    Auto1.place(x=10,y=400,width=200,height=60)

    frame2.place(x=120,y=100)
    rest=tk.Button(sim,text="Reset Module",font=("Courrier",20),bg="black",fg="white",command=rest)
    rest.place(x=0,y=560,width=200,height=40)
    simule=tk.Button(sim,text="Simuler",font=("Courrier",20),bg="black",fg="white",command=simuler)
    sim.mainloop()
def notfic():
    notif=tk.Tk() 
    notif.title("Simulateur")
    notif.geometry("800x300+200+150")
    notif.config(background="#38FFAE")
    fr= tk.Frame(notif,background="#38FFAE")
    r1 =tk.Label(fr, text="1-le nom de etat intial (q0)", font=("Courrier", 30),fg="Black",bg="#38FFAE")
    r2 =tk.Label(fr, text="2-le nom de etat final (stop)", font=("Courrier", 30),fg="Black",bg="#38FFAE")
    r3 =tk.Label(fr, text="3-la valeur (*) represente (tout le character)", font=("Courrier", 30),fg="Black",bg="#38FFAE")
    r4 =tk.Label(fr, text="4-pour ne change pas la valeur entre(*)", font=("Courrier", 30),fg="Black",bg="#38FFAE")
    r5 =tk.Label(fr, text="5-le direction sont [r][l][*]", font=("Courrier", 30),fg="Black",bg="#38FFAE")
    fr.pack()
    r1.pack()
    r2.pack()
    r3.pack()
    r4.pack()
    r5.pack()
    notif.mainloop()
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
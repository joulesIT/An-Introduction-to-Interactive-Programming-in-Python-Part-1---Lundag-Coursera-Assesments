import tkinter as tk, random

W,H,PAD,BALL=600,400,10,8
root=tk.Tk()
root.title("Pong")
c=tk.Canvas(root,width=W,height=H,bg="#141414")
c.pack()

s1=s2=0
p1=p2=H//2
v1=v2=0
bx=by=vx=vy=0
ph=40

def new_ball(d=1):
    global bx,by,vx,vy
    bx,by=W/2,H/2
    vx=random.randint(3,5)*d
    vy=random.choice([-1,1])*random.randint(2,4)

def new_game():
    global s1,s2
    s1=s2=0
    new_ball()

def update():
    global bx,by,vx,vy,p1,p2,s1,s2
    p1=max(ph,min(H-ph,p1+v1))
    p2=max(ph,min(H-ph,p2+v2))
    bx+=vx; by+=vy

    if by<=BALL or by>=H-BALL: vy*=-1
    if bx<=PAD*2+BALL:
        if p1-ph<=by<=p1+ph: vx=abs(vx)*1.1
        else: s2+=1; new_ball(-1)
    if bx>=W-PAD*2-BALL:
        if p2-ph<=by<=p2+ph: vx=-abs(vx)*1.1
        else: s1+=1; new_ball(1)

    c.delete("all")
    c.create_line(W//2,0,W//2,H,fill="#333")
    c.create_rectangle(0,p1-ph,PAD,p1+ph,fill="white",outline="")
    c.create_rectangle(W-PAD,p2-ph,W,p2+ph,fill="white",outline="")
    c.create_oval(bx-BALL,by-BALL,bx+BALL,by+BALL,fill="white",outline="")
    c.create_text(W//4,30,text=str(s1),fill="white",font=("Arial",32,"bold"))
    c.create_text(3*W//4,30,text=str(s2),fill="white",font=("Arial",32,"bold"))
    c.create_text(W//2,H-12,text="W/S  |  Arrows  |  R=Restart",fill="#555",font=("Arial",11))
    root.after(16,update)

root.bind("<KeyPress-w>",lambda e: set_v1(-5))
root.bind("<KeyRelease-w>",lambda e: set_v1(0))
root.bind("<KeyPress-s>",lambda e: set_v1(5))
root.bind("<KeyRelease-s>",lambda e: set_v1(0))
root.bind("<KeyPress-Up>",lambda e: set_v2(-5))
root.bind("<KeyRelease-Up>",lambda e: set_v2(0))
root.bind("<KeyPress-Down>",lambda e: set_v2(5))
root.bind("<KeyRelease-Down>",lambda e: set_v2(0))
root.bind("<KeyPress-r>",lambda e: new_game())

def set_v1(v): global v1; v1=v
def set_v2(v): global v2; v2=v

btn=tk.Button(root,text="Restart",command=new_game,bg="#333",fg="white",relief="flat",padx=10)
btn.pack(pady=4)

new_game()
update()
root.mainloop()

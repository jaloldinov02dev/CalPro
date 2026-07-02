import tkinter as tk

def click(v):
    if v=='=':
        try:
            e.set(str(eval(e.get())))
        except:
            e.set('Error')
    elif v=='C':
        e.set('')
    else:
        e.set(e.get()+v)

r=tk.Tk();r.title('Python Calculator')
e=tk.StringVar()
tk.Entry(r,textvariable=e,font=('Arial',18),justify='right').grid(row=0,column=0,columnspan=4)
buttons=['7','8','9','/','4','5','6','*','1','2','3','-','C','0','=','+']
for i,b in enumerate(buttons):
    tk.Button(r,text=b,width=5,height=2,command=lambda x=b:click(x)).grid(row=1+i//4,column=i%4)
r.mainloop()

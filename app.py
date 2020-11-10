from tkinter import *
import tkinter.messagebox
from tkinter.ttk import Notebook,Progressbar,Combobox
from pyfiglet import *


class Make:
    def __init__(self,root):
        self.root=root
        self.root.title("Ascii Arts")
        self.root.geometry("600x500")
        self.root.iconbitmap('logo316.ico')
        self.root.resizable(0,0)



        query=StringVar()
        fonts=StringVar()


        def create():
            if query.get()!="":
                if fonts.get()!="Select Font":
                    texttopaste.delete('1.0','end')
                    art=figlet_format(text=query.get(),font=fonts.get())
                    texttopaste.insert('end',art)
                else:
                    tkinter.messagebox.showerror('Error','Please Select Fonts')
            else:
                tkinter.messagebox.showerror("Error","Please Enter Query")




        def clear():
            query.set("")
            fonts.set("Select Font")
            texttopaste.delete('1.0','end')



        def on_enter1(e):
            but_create['background']="black"
            but_create['foreground']="cyan"  
        def on_leave1(e):
            but_create['background']="SystemButtonFace"
            but_create['foreground']="SystemButtonText"

            

        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"  
        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"


        mainframe=Frame(self.root,width=600,height=500,bd=3,relief="ridge")
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=594,height=210,bd=3,relief="ridge",bg="#852825")
        firstframe.place(x=0,y=0)


        secondframe=Frame(mainframe,width=594,height=284,bd=3,relief="ridge")
        secondframe.place(x=0,y=210)


#====================firstframe=================================================#
        
        lab_ent=Label(firstframe,text="Please Enter Query",font=('times new roman',12),bg="#852825",fg="white")
        lab_ent.place(x=20,y=20)

        ent=Entry(firstframe,width=45,font=('times new roman',14),relief="ridge",bd=3,textvariable=query)
        ent.place(x=150,y=20)


        list_fonts=['standard',"bulbhead","digital","bubble","dotmatrix","alligator","letters","isometric1","doh","banner3-D","alphabet","5lineoblique","3x5","3-d","slant"]
        list_fonts_combo=Combobox(firstframe,values=list_fonts,font=('arial',16),width=22,state="readonly",textvariable=fonts)
        list_fonts_combo.set("Select Font")
        list_fonts_combo.place(x=152,y=60)

        but_create=Button(firstframe,text="Create",width=17,font=('times new roman',12),cursor="hand2",command=create)
        but_create.place(x=70,y=130)
        but_create.bind("<Enter>",on_enter1)
        but_create.bind("<Leave>",on_leave1)

        but_clear=Button(firstframe,text="Clear",width=17,font=('times new roman',12),cursor="hand2",command=clear)
        but_clear.place(x=340,y=130)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)




        

#====================secondframe=================================================#

        scol1=Scrollbar(secondframe,orient="vertical")
        scol1.place(relx=1, rely=0, relheight=1, anchor='ne')
        
        texttopaste=Text(secondframe,height=17,width=70,yscrollcommand=scol1.set,relief="sunken",bd=3,bg="black",fg="white")      
        texttopaste.place(x=1,y=1)
        scol1.config(command=texttopaste.yview)


       




if __name__ == "__main__":
    root=Tk()
    Make(root)
    root.mainloop()
from tkinter import *

def main():
    root=Tk()

    head=Frame(root,borderwidth=10)
    
    label1=Label(head,text="SourcePath")
    label1.pack(side=LEFT,)



    
    SourcePath=StringVar()
    sp_text=Entry(head,width=40,textvariable=SourcePath)
    SourcePath.set('SourcePath')
    sp_text.pack(side=LEFT,)

    label2=Label(head,text="SourceFile")
    label2.pack(side=LEFT,)

    SourceFile=StringVar()
    sf_text=Entry(head,width=20,textvariable=SourceFile)
    SourceFile.set('SourceFile')
    sf_text.pack(side=LEFT)
    Botton_Load=Button(head,text='Load')
    Botton_Load.pack(side=LEFT)
    head.pack(side=TOP,expand=YES,anchor=NW,fill=X)
    
    text_fr=Frame(root,borderwidth=10)
    text=Text(text_fr,height=50)
    text.pack(side=TOP,fill=Y)
    text_fr.pack(expand=YES)

    tail=Frame(root,borderwidth=10)
    label3=Label(tail,text="TargetFile")
    label3.pack(side=LEFT,expand=YES,fill=X)
    TargetFile=StringVar()
    tf_text=Entry(tail,width=20,textvariable=TargetFile)
    TargetFile.set('TargetFile')
    tf_text.pack(side=LEFT,expand=YES,fill=X)
    Botton_Save=Button(tail,text='Save')
    Botton_Save.pack(side=LEFT)

    tail.pack(side=TOP)
    
    root.mainloop()

main()

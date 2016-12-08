from tkinter import *

def main():
    root=Tk()


    x1=Text(width=100,height=40)
    x1.pack(side=LEFT,padx=10,pady=10)

    
    x2=Text(root,width=100,height=40)
    scroll=Scrollbar(x2,command=x2.yview)
    color_tag=['']*1000
    for i in range(11,100):
        color_tag[i]='#0000'+repr(i);
        x2.tag_configure('color'+repr(i),foreground=color_tag[i])
    x2.tag_bind('bite','<1>',
                lambda e,t=x2:t.insert(END,"I'll bite your legs off!\n"))
    for i in range(11,100):
        x2.insert(END,'aaaaa\n','color'+repr(i))

    button=Button(x2,text='123123')
    x2.window_create(END,window=button)

    x2.insert(END,'I dare you to click on this\n', 'bite')
    
    x2.pack(side=LEFT,padx=10,pady=10)
  #  scroll.pack(side=RIGHT,fill=Y)




    toolbar=Frame(root)
    
    b=Button(toolbar,text="Accept",width=6)
    b.pack(side=LEFT,padx=20,pady=20)

    toolbar.pack(side=TOP,fill=X)
   
    root.mainloop()
    
main()

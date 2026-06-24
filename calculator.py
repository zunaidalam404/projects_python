import tkinter as tk
root=tk.Tk()
root.title("HELLO I AM CALCULATOR")
root.geometry=("500x500")
entry1=tk.Entry(root,width=100)
entry1.pack()

entry2=tk.Entry(root,width=100)
entry2.pack()

enter_symbols=tk.Entry(root,width=50)
enter_symbols.pack()

result_label=tk.Label(root, text="result will show here")
result_label.pack()

def calculator():
    try:
        users_1=float(entry1.get())
        symbols=enter_symbols.get()
        users_2=float(entry2.get())

        if symbols=="+":
            result= users_1+users_2
        
        elif symbols=="*":
           result=users_1*users_2
        
        elif symbols=="/":
            result= users_1/users_2
        
        elif symbols=="-":
            result= users_1-users_2
        else:
           result="invalid input"
       
        result_label.config(text=f"Result is {result}")
    except ValueError:
        result_label.config(text="invalid input")
btn=tk.Button(root, text="calculate", command=calculator)
btn.pack()
root.mainloop()
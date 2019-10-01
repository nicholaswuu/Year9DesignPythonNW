import tkinter as tk

print("Start Program")
root = tk.Tk() #Builds main window


#Step 1: Construct the widget
btn1=tk.Button(root, width = 10, height = 5)
#Step 2: Configure the widget
btn1.config(text = "I am a button")
#Step 3: Place the widget - pack(), grid()
btn1.pack()

output = tk.Text(root, width=100, height=30)
output.config()
output.pack();

root.mainloop()

print("END PROGRAM")
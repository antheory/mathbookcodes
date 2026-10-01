# プログラム2-7（入力ウインドウの操作）
def button_click():
    try:
        c_over_m = float(input_valone.get())
        omega_0 = float(input_valtwo.get())
    except ValueError:
        messagebox.showerror(
            "Input error", "Please enter valid numbers."
        )
        return
    mymain(c_over_m, omega_0)
    myplotgraph(c_over_m, omega_0)
def button_quit():
    root.destroy()
    plt.close("all")
button1 = tk.Button(root, text="ENTER", command=button_click)
button1.place(x=10, y=80)
button2 = tk.Button(root, text="Quit", command=button_quit)
button2.place(x=100, y=80)
root.mainloop()

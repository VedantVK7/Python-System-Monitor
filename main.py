import time
import psutil
import tkinter as tk


class SystemMonitor:
    def __init__(self) -> None:
        # window initialization
        root = tk.Tk()
        root.title('CPU Monitor')
        root.resizable(False,False)
        root.geometry('720x480')

        # Frames
        btn_frame = tk.Frame(root,bg='red',width=240,height=480)
        btn_frame.grid(row=0, column=0, padx=10, pady=10)

        stat_frame = tk.Frame(root,bg='lightblue',width=500,height=455)
        stat_frame.grid(row=0, column=1, padx=10, pady=10)

        # Basic buttons in btn_frame
        cpu_btn = tk.Button(btn_frame,text="Show CPU Information", command=self.show_cpu_info)
        cpu_btn.pack(anchor='w',pady=(40,10),padx=10)

        ram_btn = tk.Button(btn_frame,text="Show RAM Information", command=self.show_cpu_info)
        ram_btn.pack(anchor='w',pady=(40,10),padx=10)

        disk_btn = tk.Button(btn_frame,text="Show Disk Information", command=self.show_cpu_info)
        disk_btn.pack(anchor='w',pady=(40,10),padx=10)

        root.mainloop()


    def show_cpu_info(e):
        pass
    
    def show_ram_info(e):
        pass

    def show_disk_info(e):
        pass    

obj = SystemMonitor()




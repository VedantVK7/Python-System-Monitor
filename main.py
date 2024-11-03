import time
import psutil
import tkinter as tk
import threading
from tkinter import ttk



class SystemMonitor:
    def __init__(self) -> None:

        def show_cpu_info():

            def cpu_stat(): 
                while True:
                    freq = psutil.cpu_freq()[0]
                    freq = round(freq, 2)
                    freq_count.config(text=f'{freq} MHz')   

                    cpu_usage = psutil.cpu_percent()
                    cpu_usage_progress["value"] = cpu_usage
                    cpu_usage_label.config(text=f'CPU Usage : {cpu_usage}%')

                    stat_frame.update_idletasks()
                    print(cpu_usage)

                    time.sleep(1)
                
            for widget in stat_frame.winfo_children():
                widget.destroy() # Remove all elements

            core_label = tk.Label(stat_frame,text='Physical CPU count : ')
            core_count = tk.Label(stat_frame,text=f'{psutil.cpu_count(logical=False)}')

            core_log_label = tk.Label(stat_frame,text='Logical CPU count : ')
            core_log_count = tk.Label(stat_frame,text=f'{psutil.cpu_count(logical=True)}')

            core_label.grid(row=0,column=0,padx=10,pady=10)
            core_count.grid(row=0,column=1,padx=10,pady=10)
            core_log_label.grid(row=1,column=0,padx=10,pady=10)
            core_log_count.grid(row=1,column=1,padx=10,pady=10)   

            freq_label = tk.Label(stat_frame,text='CPU Frequency : ')
            freq_count = tk.Label(stat_frame,text=f'{psutil.cpu_freq()[0]} MHz')

            freq_label.grid(row=2,column=0,padx=10,pady=10)
            freq_count.grid(row=2,column=1,padx=10,pady=10)       

            cpu_usage_progress = ttk.Progressbar(stat_frame, orient="horizontal", length=200, mode="determinate")
            cpu_usage_progress["maximum"] = 100
            cpu_usage_progress.grid(row=3,pady=(20,3),padx=10,columnspan=2)

            cpu_usage_label = tk.Label(stat_frame,text=f'CPU Usage : ')
            cpu_usage_label.grid(row=4,padx=10,columnspan=2)

            thread = threading.Thread(target=cpu_stat)     
            thread.start()       

        
        def show_ram_info():
            for widget in stat_frame.winfo_children():
                widget.destroy() # Remove all elements


        def show_disk_info():
            for widget in stat_frame.winfo_children():
                widget.destroy() # Remove all elements


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
        cpu_btn = tk.Button(btn_frame,text="Show CPU Information", command=show_cpu_info)
        cpu_btn.pack(anchor='w',pady=(40,10),padx=10)

        ram_btn = tk.Button(btn_frame,text="Show RAM Information", command=show_ram_info)
        ram_btn.pack(anchor='w',pady=(40,10),padx=10)

        disk_btn = tk.Button(btn_frame,text="Show Disk Information", command=show_disk_info)
        disk_btn.pack(anchor='w',pady=(40,10),padx=10)

        root.mainloop()


obj = SystemMonitor()




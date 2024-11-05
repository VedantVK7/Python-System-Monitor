import time
import psutil
import tkinter as tk
from tkinter import ttk
import threading

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

                    time.sleep(1)
                
            for widget in stat_frame.winfo_children():
                widget.destroy() # Remove all elements


            cpu_count = psutil.cpu_count(logical=False)
            log_cpu_count = psutil.cpu_count(logical=True)
            core_label = tk.Label(stat_frame,text='Physical CPU count : ')
            core_count = tk.Label(stat_frame,text=cpu_count)

            core_log_label = tk.Label(stat_frame,text='Logical CPU count : ')
            core_log_count = tk.Label(stat_frame,text=log_cpu_count)

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
            def ram_stat(): 
                while True:
                    vm = psutil.virtual_memory()
                    avail = vm.available / 1000000
                    avail = round(avail,2) 
                    used = vm.used / 1000000
                    used = round(used,2)
                    usage = vm.percent

                    ram_usage_progress['value']=usage
                    mem_used_count.config(text=f'{used} MegaBytes')
                    mem_avail_count.config(text=f'{avail} MegaBytes')
                    ram_usage_label.config(text=f'RAM Usage : {usage}%')

                    time.sleep(1)
                
            for widget in stat_frame.winfo_children():
                widget.destroy() # Remove all elements

            total_mem = psutil.virtual_memory().total / 1000000
            total_mem = round(total_mem,2)     

            mem_label = tk.Label(stat_frame,text='Total Memory : ')
            mem_count = tk.Label(stat_frame,text=f'{total_mem} MegaBytes')

            mem_label.grid(row=0,column=0,padx=10,pady=10)
            mem_count.grid(row=0,column=1,padx=10,pady=10)      

            mem_avail_label = tk.Label(stat_frame,text='Available Memory : ')
            mem_avail_count = tk.Label(stat_frame,text=f'0 MegaBytes')

            mem_avail_label.grid(row=1,column=0,padx=10,pady=10)
            mem_avail_count.grid(row=1,column=1,padx=10,pady=10)   

            mem_used_label = tk.Label(stat_frame,text='Used Memory : ')
            mem_used_count = tk.Label(stat_frame,text=f'0 MegaBytes')

            mem_used_label.grid(row=2,column=0,padx=10,pady=10)
            mem_used_count.grid(row=2,column=1,padx=10,pady=10)   

            ram_usage_progress = ttk.Progressbar(stat_frame, orient="horizontal", length=200, mode="determinate")
            ram_usage_progress["maximum"] = 100
            ram_usage_progress.grid(row=3,pady=(20,3),padx=10,columnspan=2)

            ram_usage_label = tk.Label(stat_frame,text=f'RAM Usage : ')
            ram_usage_label.grid(row=4,padx=10,columnspan=2)

            thread = threading.Thread(target=ram_stat)     
            thread.start()

        def show_nw_info():
            def nw_stat(): 
                while True:
                    net_io = psutil.net_io_counters()

                    bt_sent_count.config(text=f'Bytes Sent : {net_io.bytes_sent}')
                    bt_rec_count.config(text=f'Bytes Received : {net_io.bytes_recv}')
                    pct_sent_count.config(text=f'Packets Sent : {net_io.packets_sent}')
                    pct_rec_count.config(text=f'Packets Received : {net_io.packets_recv}')

                    time.sleep(1)
                
            for widget in stat_frame.winfo_children():
                widget.destroy() # Remove all elements

            bt_sent_lbl = tk.Label(stat_frame,text='Bytes sent : ')
            bt_sent_count = tk.Label(stat_frame)

            bt_sent_lbl.grid(row=0,column=0,padx=10,pady=10)
            bt_sent_count.grid(row=0,column=1,padx=10,pady=10)      

            bt_rec_lbl = tk.Label(stat_frame,text='Bytes Received : ')
            bt_rec_count = tk.Label(stat_frame)

            bt_rec_lbl.grid(row=1,column=0,padx=10,pady=10)
            bt_rec_count.grid(row=1,column=1,padx=10,pady=10)   

            pct_sent_lbl = tk.Label(stat_frame,text='Packets Sent : ')
            pct_sent_count = tk.Label(stat_frame)

            pct_sent_lbl.grid(row=2,column=0,padx=10,pady=10)
            pct_sent_count.grid(row=2,column=1,padx=10,pady=10)   

            pct_rec_lbl = tk.Label(stat_frame,text='Packets Received : ')
            pct_rec_count = tk.Label(stat_frame)

            pct_rec_lbl.grid(row=3,column=0,padx=10,pady=10)
            pct_rec_count.grid(row=3,column=1,padx=10,pady=10)   


            thread = threading.Thread(target=nw_stat)     
            thread.start()


        # window initialization
        root = tk.Tk()
        root.title('CPU Monitor')
        root.resizable(False,False)
        root.geometry('600x300')

        # Frames
        btn_frame = tk.Frame(root)
        btn_frame.grid(row=0, column=0, padx=10, pady=10)

        stat_frame = tk.Frame(root)
        stat_frame.grid(row=0, column=1, padx=10, pady=10)


        # Basic buttons in btn_frame
        cpu_btn = tk.Button(btn_frame,text="Show CPU Information", command=show_cpu_info)
        cpu_btn.pack(pady=(40,10),padx=10)

        ram_btn = tk.Button(btn_frame,text="Show RAM Information", command=show_ram_info)
        ram_btn.pack(pady=(40,10),padx=10)

        nw_btn = tk.Button(btn_frame,text="Show Network Information", command=show_nw_info)
        nw_btn.pack(pady=(40,10),padx=10)

        root.mainloop()


obj = SystemMonitor()




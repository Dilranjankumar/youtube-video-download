import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from pytube import YouTube

def download_video():
    link = link_entry.get()
    if link:
        try:
            yt = YouTube(link)
            ys = yt.streams.get_highest_resolution()
            download_path = filedialog.askdirectory()
            if download_path:
                ys.download(download_path)
                messagebox.showinfo("Success", "Download completed!")
            else:
                messagebox.showwarning("Warning", "Download directory not selected.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        messagebox.showwarning("Warning", "Please enter a valid YouTube link.")

root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("400x200")
root.resizable(False, False)

main_frame = ttk.Frame(root, padding=(20, 10))
main_frame.grid(row=0, column=0, sticky="nsew")

link_label = ttk.Label(main_frame, text="Enter YouTube Link:")
link_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

link_entry = ttk.Entry(main_frame, width=50)
link_entry.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

download_button = ttk.Button(main_frame, text="Download", command=download_video)
download_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

# Add some styling
style = ttk.Style()
style.configure("TButton", foreground="blue")  # Change button color
style.configure("TLabel", foreground="black", background="lightgray")  # Change label color

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
main_frame.columnconfigure(0, weight=1)

root.mainloop()

import tkinter as tk
import subprocess

def get_ipv4_config():
    ipconfig_output = subprocess.check_output(['ipconfig']).decode('utf-8')
    ipv4_config = ""
    is_ipv4_section = False

    for line in ipconfig_output.splitlines():
        if "IPv4 Address" in line:
            is_ipv4_section = True
            ipv4_config += line# + "\n"
        #elif "Subnet Mask" in line or "Default Gateway" in line:
            #ipv4_config += line + "\n"
            ipv4_config = ipv4_config.replace(" ","")
            ipv4_config = ipv4_config.replace(":"," ")
            ipv4_config = ipv4_config.replace("IPv4","IP ")
            ipv4_config = ipv4_config.replace("Address","Address ")
        elif is_ipv4_section and not line.strip():
            break
    return ipv4_config

def display_ipv4_config(ipv4_config):
    window = tk.Tk()
    window.title("THIS PC "+ipv4_config)

    font = ("Tahoma", 50)  # Define your desired font and size
    text_color = "magenta"       # Define the desired text color (can be any valid color name or hexadecimal value)

    text_widget = tk.Text(window, font=font, fg=text_color)
    text_widget.insert(tk.END, ipv4_config)
    text_widget.pack()
    # Calculate the width and height of the text widget contents
    text_widget.update_idletasks()
    width = text_widget.winfo_reqwidth()
    height = text_widget.winfo_reqheight()

    text_widget.tag_configure("center", justify="center")
    text_widget.tag_add("center", "1.0", "end")

    # Set the window size to fit the text widget contents
    window.geometry(f"{1100}x{90}")

    window.mainloop()

ipv4_config = get_ipv4_config()
display_ipv4_config(ipv4_config)
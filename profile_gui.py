import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

# Global dictionary to store profiles
profiles = {}

# Load profiles from file if it exists
def load_profiles():
    global profiles
    if os.path.exists("profiles.json"):
        with open("profiles.json", "r") as f:
            profiles = json.load(f)

# Save profiles to file
def save_profiles():
    with open("profiles.json", "w") as f:
        json.dump(profiles, f, indent=4)

# Add a profile
def add_profile():
    id = entry_id.get().strip()
    name = entry_name.get().strip()
    sec = entry_sec.get().strip()
    phno = entry_phno.get().strip()

    if not (id and name and sec and phno):
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    profiles[id] = {"name": name, "sec": sec, "phno": phno}
    save_profiles()
    messagebox.showinfo("Success", f"Profile for {name} added.")
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_sec.delete(0, tk.END)
    entry_phno.delete(0, tk.END)

# View all profiles
def view_profiles():
    if not profiles:
        messagebox.showinfo("Profiles", "No profiles found.")
        return

    view_win = tk.Toplevel(root)
    view_win.title("Saved Profiles")
    text = tk.Text(view_win, width=60, height=20)
    text.pack()

    for id, data in profiles.items():
        text.insert(tk.END, f"ID: {id}, Name: {data['name']}, Sec: {data['sec']}, Phno: {data['phno']}\n")

# Remove a profile
def remove_profile():
    id = simpledialog.askstring("Remove", "Enter student ID to remove:")
    if id and id in profiles:
        del profiles[id]
        save_profiles()
        messagebox.showinfo("Removed", f"Profile ID {id} removed.")
    else:
        messagebox.showerror("Error", "ID not found.")

# GUI Setup
root = tk.Tk()
root.title("Student Profile Manager")

tk.Label(root, text="Student ID").grid(row=0, column=0, sticky="w")
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1)

tk.Label(root, text="Name").grid(row=1, column=0, sticky="w")
entry_name = tk.Entry(root)
entry_name.grid(row=1, column=1)

tk.Label(root, text="Section").grid(row=2, column=0, sticky="w")
entry_sec = tk.Entry(root)
entry_sec.grid(row=2, column=1)

tk.Label(root, text="Phone No.").grid(row=3, column=0, sticky="w")
entry_phno = tk.Entry(root)
entry_phno.grid(row=3, column=1)

tk.Button(root, text="Add Profile", command=add_profile).grid(row=4, column=1, pady=5)
tk.Button(root, text="View Profiles", command=view_profiles).grid(row=5, column=1)
tk.Button(root, text="Remove Profile", command=remove_profile).grid(row=6, column=1)

load_profiles()
root.mainloop()

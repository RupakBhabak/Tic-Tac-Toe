import tkinter as tk

from game_pvc import render_game_pvc
from game_pvp import render_game_pvp

def exit_window(root):
    root.destroy()

root = tk.Tk()
root.title("Main Menu")  # Setting the title of the menu

# --- Setting Window Geometry ---
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 600
X = int((root.winfo_screenwidth() - WINDOW_WIDTH) / 2)
Y = int((root.winfo_screenheight() - WINDOW_HEIGHT) / 2)
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{X}+{Y}")
root.configure(bg="white")
icon = tk.PhotoImage(file="icon.png")
root.iconphoto(True, icon)

# --- Create a frame and center it ---
menu_frame = tk.Frame(root, bg="white")
menu_frame.place(relx=0.5, rely=0.5, anchor="center")  # Center in window

# --- Branding Label ---
branding = tk.Label(menu_frame, text="TIC TAC TOE", font=('Arial', 30, 'bold'), bg="white")
branding.pack(pady=(0, 30))  # Extra space below

# --- Buttons ---
button_1 = tk.Button(menu_frame, text="2 PLAYER", font=('Arial', 20), command=lambda: render_game_pvp(root))
button_1.pack(pady=10)

button_2 = tk.Button(menu_frame, text="VS COM", font=('Arial', 20), command=lambda: render_game_pvc(root))
button_2.pack(pady=10)

button_3 = tk.Button(menu_frame, text="EXIT", font=('Arial', 20), command=lambda: exit_window(root))
button_3.pack(pady=10)

# --- Credit Label ---
credit = tk.Label(menu_frame, text="\n\n\nby Rupak Bhabak\n\n(C) 2025", font=('Arial', 16), bg="white")
credit.pack(pady=10)

root.mainloop()

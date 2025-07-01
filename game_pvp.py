import tkinter as tk
from ai import check_for_win
from random import choice

#Global Variables
board_data = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
boxes = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
player_1_symbol = ""
player_2_symbol = ""
player_1_turn = True

def show_popup(text, game, root):
    popup = tk.Toplevel(game)
    popup.title("Result")
    popup.geometry("300x200")
    popup.grab_set()

    popup.update_idletasks()
    x = (popup.winfo_screenwidth() - popup.winfo_width()) // 2
    y = (popup.winfo_screenheight() - popup.winfo_height()) // 2
    popup.geometry(f"+{x}+{y}")

    label = tk.Label(popup, text=f"{text}")
    label.pack(pady=10)

    def close_all():
        popup.destroy()
        game.destroy()
        root.deiconify() 

    close_button = tk.Button(popup, text="OK", command=close_all)
    close_button.pack(pady=5)

def show_result(key, game, root):
    if key == 1:
        show_popup("Player 1 has won this game!", game, root)
    elif key == 2:
        show_popup("Player 2 has won this game!", game, root)
    else:
        show_popup("Game has tied!", game, root)

def check_for_draw(board_data):
    for i in range(len(board_data)):
        if board_data[i] == 0:
            return False
    return True

def set_winning_ui(board_data, box_data, key):
    WIN_MATCHES = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    for i in range(len(WIN_MATCHES)):
        current_case = WIN_MATCHES[i]
        if key == 1:
            if (board_data[current_case[0]-1] == 1 and board_data[current_case[1]-1] == 1 and board_data[current_case[2]-1] == 1):
                for pos in current_case:
                    row = (pos - 1) // 3
                    col = (pos - 1) % 3
                    box_data[row][col].config(bg="green", fg="white")
                    box_data[row][col].update()

        else:
            if (board_data[current_case[0]-1] == -1 and board_data[current_case[1]-1] == -1 and board_data[current_case[2]-1] == -1):
                for pos in current_case:
                    row = (pos - 1) // 3
                    col = (pos - 1) % 3
                    box_data[row][col].config(bg="green", fg="white")
                    box_data[row][col].update()

def on_click_box(row, col, info, game, root):
    global board_data, player_1_symbol, player_2_symbol, boxes, player_1_turn
    modified_board_data = []

    if (boxes[row][col]['text'] == ""):
        if player_1_turn:
            boxes[row][col]['text'] = player_1_symbol
            boxes[row][col].config(fg="blue")
            board_data[row][col] = 1
            boxes[row][col].update()

            for i in range(3):
                for j in range(3):
                    modified_board_data.append(board_data[i][j])

            if check_for_win(modified_board_data):
                set_winning_ui(modified_board_data, boxes, 1)
                show_result(1, game, root)
                return
            if check_for_draw(modified_board_data):
                show_result(3, game, root)
                return
            
            info.config(text=f"Player 2's turn ({player_2_symbol})")
            info.update()

            player_1_turn = False
        else:
            boxes[row][col]['text'] = player_2_symbol
            boxes[row][col].config(fg="red")
            board_data[row][col] = -1
            boxes[row][col].update()

            for i in range(3):
                for j in range(3):
                    modified_board_data.append(board_data[i][j])

            if check_for_win(modified_board_data, "c"):
                set_winning_ui(modified_board_data, boxes, 2)
                show_result(2, game, root)
                return
            if check_for_draw(modified_board_data):
                show_result(3, game, root)
                return
            
            info.config(text=f"Player 1's turn ({player_1_symbol})")
            info.update()

            player_1_turn = True

def back_to_menu(game, root):
    game.destroy()
    root.deiconify()

def render_game_pvp(root):
    global boxes, player_1_symbol, player_2_symbol, board_data, player_1_turn

    board_data = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]
    boxes = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    player_1_turn = True
    
    root.withdraw()
    game = tk.Toplevel()
    game.title("Player vs Player")

    player_1_symbol = choice(["X", "O"])
    if player_1_symbol == "X":
        player_2_symbol = "O"
    else:
        player_2_symbol = "X"

    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 600
    X = int((root.winfo_screenwidth() - WINDOW_WIDTH) / 2)
    Y = int((root.winfo_screenheight() - WINDOW_HEIGHT) / 2)
    game.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{X}+{Y}")

    game_frame = tk.Frame(game)
    game_frame.columnconfigure(0, weight=1)
    game_frame.columnconfigure(1, weight=1)
    game_frame.columnconfigure(2, weight=1)

    game_frame.rowconfigure(0, weight=1)
    game_frame.rowconfigure(1, weight=1)
    game_frame.rowconfigure(2, weight=1)
    game_frame.rowconfigure(3, weight=1)
    game_frame.rowconfigure(4, weight=1)

    info = tk.Label(game_frame, text=f"Player 1's turn ({player_1_symbol})", font=('Arial', 15))
    info.grid(row=0, column=0, columnspan=3)

    try:
        for i in range(1, 4):
            for j in range(3):
                boxes[i-1][j] = tk.Button(game_frame, text="", font=('Arial', 40, 'bold'), command=lambda row=i-1, col=j: on_click_box(row, col, info, game, root))
                boxes[i-1][j].grid(row=i, column=j, sticky="nsew")
    except:
        pass

    back = tk.Button(game_frame, text="BACK", font=('Arial', 20), command=lambda g=game, r=root: back_to_menu(g, r))
    back.grid(row=4, column=0, columnspan=3)

    game_frame.pack(fill='both', expand=True)

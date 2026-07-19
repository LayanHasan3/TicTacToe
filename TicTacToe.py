import tkinter as tk

# Game logic

def check_winner(board):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],  # rows
        [0,3,6],[1,4,7],[2,5,8],  # cols
        [0,4,8],[2,4,6]           # diagonals
    ]
    for combo in wins:
        a, b, c = combo
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]  # returns 'X' or 'O'
    return None

def is_draw(board):
    return all(cell != '' for cell in board) and not check_winner(board)


# Minimax 

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    
    #base cases
    if winner == 'O': return 10 - depth  # AI wins
    if winner == 'X': return depth - 10 # Human wins
    if is_draw(board): return 0
    
    if is_maximizing: # AI's Turn
        best = -1000
        for i in range(9):
            if board[i] == '':
                board[i] = 'O'
                score = minimax(board, depth+1, False)
                board[i] = ''
                best = max(best, score)
        return best
    
    else:  # Human's Turn
        best = 1000
        for i in range(9):
           if board[i] == '':
                board[i] = 'X'
                score = minimax(board, depth+1, True)
                board[i] = ''
                best = min(best, score)
        return best 


def best_move(board):
    best_score = -1000
    move = -1
    for i in range(9):
        if board[i] == '':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ''
            if score > best_score:
                best_score = score
                move = i
    return move
    
    

# Tkinter GUI
class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe — Minimax AI")
        self.root.resizable(False, False)
        self.board = ['' for _ in range(9)]
        self.buttons = []
        self.game_over = False
        self._build_ui()
 
    def _build_ui(self):
        # Title
        tk.Label(self.root, text="Tic-Tac-Toe", font=("Arial", 18, "bold"),
                 pady=8).grid(row=0, column=0, columnspan=3)
 
        # Status label
        self.status = tk.Label(self.root, text="Your turn (X)",
                               font=("Arial", 13), pady=6, fg="darkblue")
        self.status.grid(row=1, column=0, columnspan=3)
 
        # 3x3 grid of buttons
        for i in range(9):
            btn = tk.Button(
                self.root, text='', font=("Arial", 32, "bold"),
                width=4, height=2, relief="groove",
                command=lambda idx=i: self.human_move(idx)
            )
            btn.grid(row=i//3 + 2, column=i%3, padx=4, pady=4)
            self.buttons.append(btn)
 
        # Restart button
        tk.Button(self.root, text="Restart", font=("Arial", 12),
                  command=self.restart, bg="#f0f0f0").grid(
                  row=5, column=0, columnspan=3, pady=10, ipadx=10)
 
    def human_move(self, idx):
        if self.board[idx] != '' or self.game_over:
            return  # ignore invalid clicks
 
        self.board[idx] = 'X'
        self.buttons[idx].config(text='X', fg='blue')
 
        if self._check_end():
            return
 
        self.status.config(text="AI is thinking...")
        self.root.after(300, self.ai_move)  # small delay feels natural
 
    def ai_move(self):
        move = best_move(self.board)
        self.board[move] = 'O'
        self.buttons[move].config(text='O', fg='red')
 
        if self._check_end():
            return
 
        self.status.config(text="Your turn (X)")
 
    def _check_end(self):
        winner = check_winner(self.board)
        if winner:
            msg = "You win!" if winner == 'X' else "AI wins!"
            self.status.config(text=msg, fg="green" if winner == 'X' else "red")
            self._highlight_winner()
            self.game_over = True
            return True
        if is_draw(self.board):
            self.status.config(text="It's a draw!", fg="darkorange")
            self.game_over = True
            return True
        return False
 
    def _highlight_winner(self):
        wins = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]
        for combo in wins:
            a, b, c = combo
            if self.board[a] and self.board[a] == self.board[b] == self.board[c]:
                for idx in combo:
                    self.buttons[idx].config(bg='lightgreen')
 
    def restart(self):
        self.board = ['' for _ in range(9)]
        self.game_over = False
        self.status.config(text="Your turn (X)", fg="darkblue")
        for btn in self.buttons:
            btn.config(text='', bg='SystemButtonFace')   






if __name__ =="__main__":    
   root = tk.Tk()   #it creates the main application window
   app = TicTacToe(root)
   root.mainloop() # it starts the event loop and keeps window responses
import tkinter as tk
import sqlite3
from tkinter import messagebox, Toplevel

class Formation:
    def __init__(self,name, side):
        self.name = name
        self.side = side
        self.qb_position = ()
        self.center_position = ()
        self.Player_x_position = ()
        self.Player_y_position = ()
        self.Player_z_position = ()
          
class Play:
    def __init__(self, name, side):
        self.name = name
        self.side = side
        self.Throw_forward = ()
        self.qb_move = ""
        self.center_move = ""
        self.x_move = ""
        self.y_move = ""
        self.z_move = ""
        self.throw_back = ()
        self.qb_player_id = 0
        self.center_Player_id = 0
        self.x_player_id = 0
        self.y_player_id = 0
        self.z_player_id = 0


class Player:
    def __init__(self, name, positions, status="En forme"):
        self.name = name
        self.positions = positions
        self.status = status

    def __str__(self):
        return f"{self.name} ({', '.join(self.positions)}): {self.status}"

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def __str__(self):
        return f"Équipe {self.name}:\n" + "\n".join(str(player) for player in self.players)

class TeamManagementWindow:
    def __init__(self, parent, conn):
        self.parent = parent
        self.conn = conn
        self.window = Toplevel(parent)
        self.window.title("Gestion des Équipes et Joueurs")

        self.team_name = tk.StringVar()
        tk.Entry(self.window, textvariable=self.team_name).pack()
        tk.Button(self.window, text="Ajouter Équipe", command=self.add_team).pack()

        self.team_var = tk.StringVar()
        self.team_dropdown = tk.OptionMenu(self.window, self.team_var, "")
        self.team_dropdown.pack()
        tk.Button(self.window, text="Charger Équipe", command=self.update_team_dropdown).pack()

        self.player_name = tk.StringVar()
        self.player_positions = tk.StringVar()
        self.player_status = tk.StringVar(value="En forme")

        tk.Entry(self.window, textvariable=self.player_name).pack()
        tk.Entry(self.window, textvariable=self.player_positions).pack()
        tk.OptionMenu(self.window, self.player_status, "En forme", "Fatigué", "Blessé", "Absent").pack()
        tk.Button(self.window, text="Ajouter Joueur", command=self.add_player).pack()

        self.update_team_dropdown()

    def update_team_dropdown(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT name FROM teams')
        teams = cursor.fetchall()
        self.team_dropdown['menu'].delete(0, 'end')
        for team in teams:
            self.team_dropdown['menu'].add_command(label=team[0], command=tk._setit(self.team_var, team[0]))

    def add_team(self):
        team_name = self.team_name.get()
        if team_name:
            cursor = self.conn.cursor()
            cursor.execute('INSERT INTO teams (name) VALUES (?)', (team_name,))
            self.conn.commit()
            self.team_name.set("")
            self.update_team_dropdown()
            messagebox.showinfo("Info", f"Équipe {team_name} ajoutée avec succès.")

    def add_player(self):
        team_name = self.team_var.get()
        if not team_name:
            messagebox.showerror("Erreur", "Veuillez sélectionner une équipe.")
            return

        player_name = self.player_name.get()
        positions = self.player_positions.get()
        status = self.player_status.get()

        if player_name and positions:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO players (name, positions, status, team_id)
                VALUES (?, ?, ?, (SELECT id FROM teams WHERE name = ?))
            ''', (player_name, positions, status, team_name))
            self.conn.commit()
            self.player_name.set("")
            self.player_positions.set("")
            messagebox.showinfo("Info", f"Joueur {player_name} ajouté avec succès à l'équipe {team_name}.")

class PlaybookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flag Football Playbook")

        self.conn = sqlite3.connect('flag_football.db')
        self.create_tables()

        self.current_team = None

        # Canvas for playbook
        self.canvas = tk.Canvas(root, width=350, height=450, bg='green')
        self.canvas.pack()

        self.draw_field()

        # Team selection
        self.team_var = tk.StringVar()
        self.team_dropdown = tk.OptionMenu(root, self.team_var, "")
        self.team_dropdown.pack()
        tk.Button(root, text="Charger Équipe", command=self.load_team).pack()

        # Display players
        self.players_text = tk.Text(root, height=10, width=50)
        self.players_text.pack()

        # Playbook interface
        self.route_type = tk.StringVar(value="Slant")
        tk.OptionMenu(root, self.route_type, "Fly/Go", "Post", "Corner", "Out", "In/Dig", "Curl", "Comeback", "Flat", "Slant").pack()

        self.qb_position = tk.StringVar(value="Under Center")
        tk.OptionMenu(root, self.qb_position, "Under Center", "Shotgun").pack()

        tk.Button(root, text="Place Quarterback", command=self.place_quarterback).pack(side=tk.LEFT)
        tk.Button(root, text="Place Center", command=self.place_center).pack(side=tk.RIGHT)

        tk.Button(root, text="Gérer les Équipes", command=self.open_team_management).pack()

        self.canvas.bind("<Button-1>", self.add_route)

        self.update_team_dropdown()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS teams (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                positions TEXT NOT NULL,
                status TEXT NOT NULL,
                team_id INTEGER,
                FOREIGN KEY (team_id) REFERENCES teams (id)
            )
        ''')
        self.conn.commit()

    def draw_field(self):
        self.canvas.create_rectangle(50, 50, 300, 400, outline='white')
        self.canvas.create_rectangle(50, 300, 300, 400, fill='blue', outline='white')

    def update_team_dropdown(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT name FROM teams')
        teams = cursor.fetchall()
        self.team_dropdown['menu'].delete(0, 'end')
        for team in teams:
            self.team_dropdown['menu'].add_command(label=team[0], command=tk._setit(self.team_var, team[0]))

    def load_team(self):
        team_name = self.team_var.get()
        if team_name:
            cursor = self.conn.cursor()
            cursor.execute('SELECT name, positions, status FROM players WHERE team_id = (SELECT id FROM teams WHERE name = ?)', (team_name,))
            players = cursor.fetchall()
            self.players_text.delete(1.0, tk.END)
            for player in players:
                self.players_text.insert(tk.END, f"{player[0]} ({player[1]}): {player[2]}\n")

    def open_team_management(self):
        TeamManagementWindow(self.root, self.conn)
        self.update_team_dropdown()

    def place_quarterback(self):
        if self.qb_position.get() == "Under Center":
            self.canvas.create_oval(300-5, 250-5, 300+5, 250+5, fill='purple', tags="quarterback")
        else:  # Shotgun
            self.canvas.create_oval(300-5, 270-5, 300+5, 270+5, fill='purple', tags="quarterback")

    def place_center(self):
        self.canvas.create_oval(300-5, 230-5, 300+5, 230+5, fill='orange', tags="center")

    def add_route(self, event):
        route_type = self.route_type.get()
        x, y = event.x, event.y

        colors = {
            "Fly/Go": "yellow",
            "Post": "red",
            "Corner": "blue",
            "Out": "green",
            "In/Dig": "cyan",
            "Curl": "magenta",
            "Comeback": "orange",
            "Flat": "pink",
            "Slant": "brown"
        }

        if route_type == "Fly/Go":
            self.canvas.create_line(x, y, x, y-100, fill=colors[route_type], arrow=tk.LAST)
        elif route_type == "Post":
            self.canvas.create_line(x, y, x, y-50, x+50, y-100, fill=colors[route_type], arrow=tk.LAST)
        elif route_type == "Corner":
            self.canvas.create_line(x, y, x+50, y, x+50, y-50, fill=colors[route_type], arrow=tk.LAST)
        elif route_type == "Out":
            self.canvas.create_line(x, y, x+50, y-50, fill=colors[route_type], arrow=tk.LAST)
        elif route_type == "In/Dig":
            self.canvas.create_line(x, y, x+50, y+50, fill=colors[route_type], arrow=tk.LAST)
        elif route_type == "Curl":
            self.canvas.create_line(x, y, x+50, y, x+50, y+30, fill=colors[route_type], arrow=tk.LAST)
        elif route_type == "Comeback":
            self.canvas.create_line(x, y, x+50, y, x+50, y+50, fill=colors[route_type], arrow=tk.LAST)
        elif route_type == "Flat":
            self.canvas.create_line(x, y, x+100, y, fill=colors[route_type], arrow=tk.LAST)
        elif route_type == "Slant":
            if x < 300 :
                self.canvas.create_line(x, y, x, y-30, x+50, y-50, fill=colors[route_type], arrow=tk.LAST)
            else :
                self.canvas.create_line(x, y, x, y-30, x-50, y-50, fill=colors[route_type], arrow=tk.LAST)

    def __del__(self):
        self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = PlaybookApp(root)
    root.mainloop()

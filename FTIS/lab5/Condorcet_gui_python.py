"""
Condorcet GUI tool (Python + Tkinter) for Minsk housing reconstruction problem

- Alternatives are now named explicitly for the Minsk case:
    A1 = "Money compensation for residents"
    A2 = "Temporary hostel housing"
    A3 = "Resettlement to better conditions in other districts"
- Users can specify number of experts and input rankings.
- Computes Condorcet winner or Copeland scores.
- Displays pairwise comparison matrix and heatmap.

Requirements:
- Python 3.8+
- matplotlib (for heatmap). Install: pip install matplotlib
"""

import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

ALT_NAMES = [
    "Money compensation for residents",
    "Temporary hostel housing",
    "Resettlement to better conditions in other districts"
]

class CondorcetApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Condorcet Decision Helper - Minsk Housing")
        self.geometry("980x700")
        self.default_experts = 3
        self.default_alts = len(ALT_NAMES)
        self.create_widgets()

    def create_widgets(self):
        control_frame = ttk.Frame(self)
        control_frame.pack(side=tk.TOP, fill=tk.X, padx=8, pady=6)

        ttk.Label(control_frame, text="Experts:").pack(side=tk.LEFT)
        self.experts_var = tk.IntVar(value=self.default_experts)
        experts_spin = ttk.Spinbox(control_frame, from_=1, to=10, textvariable=self.experts_var, width=4, command=self.rebuild_table)
        experts_spin.pack(side=tk.LEFT, padx=4)

        build_btn = ttk.Button(control_frame, text="Rebuild table", command=self.rebuild_table)
        build_btn.pack(side=tk.LEFT, padx=8)

        sample_btn = ttk.Button(control_frame, text="Fill sample data", command=self.fill_sample)
        sample_btn.pack(side=tk.LEFT, padx=4)

        compute_btn = ttk.Button(control_frame, text="Compute Condorcet", command=self.compute_condorcet)
        compute_btn.pack(side=tk.LEFT, padx=8)

        reset_btn = ttk.Button(control_frame, text="Reset ranks", command=self.reset_ranks)
        reset_btn.pack(side=tk.LEFT, padx=4)

        table_frame = ttk.LabelFrame(self, text="Expert rankings (1 = best)")
        table_frame.pack(side=tk.TOP, fill=tk.X, padx=8, pady=6)

        self.table_canvas = tk.Canvas(table_frame)
        self.table_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.table_inner = ttk.Frame(self.table_canvas)
        self.table_canvas.create_window((0,0), window=self.table_inner, anchor='nw')
        self.table_inner.bind('<Configure>', lambda e: self.table_canvas.configure(scrollregion=self.table_canvas.bbox('all')))

        self.entries = []

        results_frame = ttk.Frame(self)
        results_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=8, pady=6)

        left = ttk.Frame(results_frame)
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.result_label = ttk.Label(left, text="Press 'Compute Condorcet' to evaluate", justify=tk.LEFT)
        self.result_label.pack(anchor='nw', pady=4)

        self.matrix_tree = ttk.Treeview(left, columns=[f"c{i}" for i in range(10)], show='headings', height=8)
        self.matrix_tree.pack(fill=tk.BOTH, expand=True, pady=6)

        right = ttk.Frame(results_frame)
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.fig = Figure(figsize=(4,3), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_title('Pairwise wins heatmap')
        self.canvas_fig = FigureCanvasTkAgg(self.fig, master=right)
        self.canvas_fig.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.rebuild_table()

    def rebuild_table(self):
        for child in self.table_inner.winfo_children():
            child.destroy()
        self.entries.clear()

        m = self.experts_var.get()
        n = self.default_alts

        ttk.Label(self.table_inner, text="Expert\\Alt").grid(row=0, column=0, padx=4, pady=4)
        for j in range(n):
            ttk.Label(self.table_inner, text=ALT_NAMES[j]).grid(row=0, column=j+1, padx=4, pady=4)

        for i in range(m):
            ttk.Label(self.table_inner, text=f"E{i+1}").grid(row=i+1, column=0, padx=4, pady=4)
            row_entries = []
            for j in range(n):
                e = ttk.Entry(self.table_inner, width=5)
                e.grid(row=i+1, column=j+1, padx=4, pady=4)
                row_entries.append(e)
            self.entries.append(row_entries)

        cols = [f"c{i}" for i in range(n)]
        if hasattr(self, 'matrix_tree') and self.matrix_tree is not None:
            self.matrix_tree.config(columns=cols)
            for j in range(n):
                self.matrix_tree.heading(f"c{j}", text=f"A{j+1}")
                self.matrix_tree.column(f"c{j}", width=120, anchor='center')

    def fill_sample(self):
        m = self.experts_var.get()
        n = self.default_alts
        sample_ranks = [
            [1,2,3],  # E1
            [2,1,3],  # E2
            [3,1,2]   # E3
        ]
        for i in range(m):
            for j in range(n):
                try:
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(0, str(sample_ranks[i][j]))
                except IndexError:
                    pass

    def reset_ranks(self):
        for row in self.entries:
            for e in row:
                e.delete(0, tk.END)

    def read_rankings(self):
        m = self.experts_var.get()
        n = self.default_alts
        ranks = np.full((m,n), np.nan)
        for i in range(m):
            for j in range(n):
                val = self.entries[i][j].get().strip()
                if val == '':
                    ranks[i,j] = np.nan
                else:
                    try:
                        ranks[i,j] = int(val)
                    except ValueError:
                        raise ValueError(f"Invalid rank at expert {i+1}, alt {j+1}: '{val}'")
        return ranks

    def compute_condorcet(self):
        try:
            ranks = self.read_rankings()
        except ValueError as e:
            messagebox.showerror("Input error", str(e))
            return

        m, n = ranks.shape
        for i in range(m):
            row = ranks[i]
            if np.isnan(row).any():
                messagebox.showwarning("Incomplete data", f"Expert {i+1} has empty fields.")
                return
            if set(row.astype(int).tolist()) != set(range(1, n+1)):
                messagebox.showwarning("Invalid ranking", f"Expert {i+1} must rank alternatives 1..{n} once each.")
                return

        W = np.zeros((n,n), dtype=int)
        for a in range(n):
            for b in range(n):
                if a==b: continue
                W[a,b] = np.sum(ranks[:,a] < ranks[:,b])

        condorcet_winner = None
        for a in range(n):
            if all(W[a,b] > m/2 for b in range(n) if b!=a):
                condorcet_winner = a
                break

        txt_lines = []
        if condorcet_winner is not None:
            txt_lines.append(f"Condorcet winner: {ALT_NAMES[condorcet_winner]}")
        else:
            wins = np.zeros(n, dtype=int)
            losses = np.zeros(n, dtype=int)
            for a in range(n):
                for b in range(n):
                    if a==b: continue
                    if W[a,b] > W[b,a]: wins[a] += 1
                    elif W[a,b] < W[b,a]: losses[a] += 1
            copeland = wins - losses
            ranking = sorted([(copeland[i], i) for i in range(n)], key=lambda x: -x[0])
            txt_lines.append("No Condorcet winner. Copeland ranking:")
            for score, idx in ranking:
                txt_lines.append(f"{ALT_NAMES[idx]}: score={score}")

        self.result_label.config(text='\n'.join(txt_lines))

        self.matrix_tree.delete(*self.matrix_tree.get_children())
        for a in range(n):
            self.matrix_tree.insert('', 'end', values=[str(W[a,b]) if a!=b else '-' for b in range(n)])

        self.ax.clear()
        hm = W.astype(float)
        for i in range(n): hm[i,i] = np.nan
        im = self.ax.imshow(hm, interpolation='nearest')
        self.ax.set_xticks(range(n))
        self.ax.set_yticks(range(n))
        self.ax.set_xticklabels([f"A{i+1}" for i in range(n)])
        self.ax.set_yticklabels([f"A{i+1}" for i in range(n)])
        self.ax.set_title('Pairwise counts')
        for i in range(n):
            for j in range(n):
                if i==j: continue
                self.ax.text(j,i,str(W[i,j]),ha='center',va='center')
        self.fig.colorbar(im, ax=self.ax)
        self.canvas_fig.draw()

if __name__ == '__main__':
    app = CondorcetApp()
    app.mainloop()
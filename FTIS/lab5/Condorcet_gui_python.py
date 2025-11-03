"""
Condorcet GUI tool (Python + Tkinter)

- Lets you specify number of experts and alternatives (defaults: 3 experts, 3 alternatives).
- Each expert enters a ranking (1 = best, 2 = second, ...) for each alternative.
- Computes pairwise comparison matrix, identifies Condorcet winner if exists.
- If no Condorcet winner, shows Copeland scores (number of pairwise wins minus losses) and ranks alternatives by Copeland.
- Displays pairwise results in a table and a heatmap.

Requirements:
- Python 3.8+
- matplotlib (for heatmap). Install: pip install matplotlib

Save this file and run: python Condorcet_gui_python.py
"""

import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class CondorcetApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Condorcet Decision Helper")
        self.geometry("980x680")
        self.default_experts = 3
        self.default_alts = 3
        self.create_widgets()

    def create_widgets(self):
        control_frame = ttk.Frame(self)
        control_frame.pack(side=tk.TOP, fill=tk.X, padx=8, pady=6)

        ttk.Label(control_frame, text="Experts:").pack(side=tk.LEFT)
        self.experts_var = tk.IntVar(value=self.default_experts)
        experts_spin = ttk.Spinbox(control_frame, from_=1, to=10, textvariable=self.experts_var, width=4, command=self.rebuild_table)
        experts_spin.pack(side=tk.LEFT, padx=4)

        ttk.Label(control_frame, text="Alternatives:").pack(side=tk.LEFT, padx=(10,0))
        self.alts_var = tk.IntVar(value=self.default_alts)
        alts_spin = ttk.Spinbox(control_frame, from_=2, to=10, textvariable=self.alts_var, width=4, command=self.rebuild_table)
        alts_spin.pack(side=tk.LEFT, padx=4)

        build_btn = ttk.Button(control_frame, text="Rebuild table", command=self.rebuild_table)
        build_btn.pack(side=tk.LEFT, padx=8)

        sample_btn = ttk.Button(control_frame, text="Fill sample data", command=self.fill_sample)
        sample_btn.pack(side=tk.LEFT, padx=4)

        compute_btn = ttk.Button(control_frame, text="Compute Condorcet", command=self.compute_condorcet)
        compute_btn.pack(side=tk.LEFT, padx=8)

        reset_btn = ttk.Button(control_frame, text="Reset ranks", command=self.reset_ranks)
        reset_btn.pack(side=tk.LEFT, padx=4)

        # Frame for table of ranks
        table_frame = ttk.LabelFrame(self, text="Expert rankings (1 = best)")
        table_frame.pack(side=tk.TOP, fill=tk.X, padx=8, pady=6)

        self.table_canvas = tk.Canvas(table_frame)
        self.table_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.table_inner = ttk.Frame(self.table_canvas)
        self.table_canvas.create_window((0,0), window=self.table_inner, anchor='nw')
        self.table_inner.bind('<Configure>', lambda e: self.table_canvas.configure(scrollregion=self.table_canvas.bbox('all')))

        self.entries = []  # entries[expert][alt]

        # Results / matrix
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

        # теперь таблица уже создана — можно вызывать
        self.rebuild_table()

    def rebuild_table(self):
        # clear
        for child in self.table_inner.winfo_children():
            child.destroy()
        self.entries.clear()

        m = self.experts_var.get()
        n = self.alts_var.get()

        ttk.Label(self.table_inner, text="Expert\\Alt").grid(row=0, column=0, padx=4, pady=4)
        for j in range(n):
            ttk.Label(self.table_inner, text=f"A{j+1}").grid(row=0, column=j+1, padx=4, pady=4)

        for i in range(m):
            ttk.Label(self.table_inner, text=f"E{i+1}").grid(row=i+1, column=0, padx=4, pady=4)
            row_entries = []
            for j in range(n):
                e = ttk.Entry(self.table_inner, width=5)
                e.grid(row=i+1, column=j+1, padx=4, pady=4)
                row_entries.append(e)
            self.entries.append(row_entries)

        # adjust matrix tree headings (если matrix_tree ещё не создана — пропускаем)
        cols = [f"c{i}" for i in range(n)]
        if hasattr(self, 'matrix_tree') and self.matrix_tree is not None:
            self.matrix_tree.config(columns=cols)
            for j in range(n):
                self.matrix_tree.heading(f"c{j}", text=f"A{j+1}")
                self.matrix_tree.column(f"c{j}", width=60, anchor='center')

    def fill_sample(self):
        # Sample rankings for 3 experts and 3 alternatives
        m = self.experts_var.get()
        n = self.alts_var.get()
        # create a simple pattern: expert i prefers alternative i+1 first (cyclic)
        for i in range(m):
            ranks = list(range(1, n+1))
            # cyclic shift
            shift = i % n
            ranks = ranks[shift:] + ranks[:shift]
            for j in range(n):
                try:
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(0, str(ranks[j]))
                except IndexError:
                    pass

    def reset_ranks(self):
        for row in self.entries:
            for e in row:
                e.delete(0, tk.END)

    def read_rankings(self):
        m = self.experts_var.get()
        n = self.alts_var.get()
        ranks = np.full((m,n), np.nan)
        for i in range(m):
            for j in range(n):
                val = self.entries[i][j].get().strip()
                if val == '':
                    ranks[i,j] = np.nan
                else:
                    try:
                        r = int(val)
                        ranks[i,j] = r
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
                messagebox.showwarning("Incomplete data", f"Expert {i+1} has empty fields. Fill all ranks or use sample.")
                return
            ints = row.astype(int)
            if set(ints.tolist()) != set(range(1, n+1)):
                messagebox.showwarning("Invalid ranking", f"Expert {i+1} must rank alternatives with numbers 1..{n}, each exactly once.")
                return

        W = np.zeros((n,n), dtype=int)
        for a in range(n):
            for b in range(n):
                if a == b: continue
                count = 0
                for e in range(m):
                    if ranks[e,a] < ranks[e,b]:
                        count += 1
                W[a,b] = count

        txt_lines = []
        txt_lines.append(f"Experts: {m}, Alternatives: {n}")
        txt_lines.append("Pairwise counts (how many experts prefer row alt over column alt):")

        condorcet_winner = None
        for a in range(n):
            wins_all = True
            for b in range(n):
                if a == b: continue
                if W[a,b] <= m/2:
                    wins_all = False
                    break
            if wins_all:
                condorcet_winner = a
                break

        if condorcet_winner is not None:
            txt_lines.append(f"Condorcet winner: A{condorcet_winner+1}")
        else:
            txt_lines.append("No Condorcet winner (cycle or tie). Computing Copeland scores...")
            wins = np.zeros(n, dtype=int)
            losses = np.zeros(n, dtype=int)
            ties = np.zeros(n, dtype=int)
            for a in range(n):
                for b in range(n):
                    if a == b: continue
                    if W[a,b] > W[b,a]:
                        wins[a] += 1
                    elif W[a,b] < W[b,a]:
                        losses[a] += 1
                    else:
                        ties[a] += 1
            copeland = wins - losses
            ranking = sorted([(copeland[i], wins[i], ties[i], i) for i in range(n)], key=lambda x: (-x[0], -x[1]))
            txt_lines.append("Copeland scores (wins-losses), higher is better:")
            for score, w, t, idx in ranking:
                txt_lines.append(f"A{idx+1}: score={score}, wins={w}, ties={t}")

        self.result_label.config(text='\n'.join(txt_lines))

        self.matrix_tree.delete(*self.matrix_tree.get_children())
        for a in range(n):
            rowvals = [str(W[a,b]) if a!=b else '-' for b in range(n)]
            self.matrix_tree.insert('', 'end', values=rowvals)

        self.ax.clear()
        hm = W.astype(float)
        for i in range(n):
            hm[i,i] = np.nan
        im = self.ax.imshow(hm, interpolation='nearest')
        self.ax.set_xticks(range(n))
        self.ax.set_yticks(range(n))
        self.ax.set_xticklabels([f"A{i+1}" for i in range(n)])
        self.ax.set_yticklabels([f"A{i+1}" for i in range(n)])
        self.ax.set_title('Pairwise counts (row beats column)')
        for i in range(n):
            for j in range(n):
                if i==j: continue
                self.ax.text(j, i, str(W[i,j]), ha='center', va='center')
        self.fig.colorbar(im, ax=self.ax)
        self.canvas_fig.draw()

if __name__ == '__main__':
    app = CondorcetApp()
    app.mainloop()

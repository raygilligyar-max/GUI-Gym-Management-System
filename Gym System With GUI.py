import tkinter as tk
from tkinter import messagebox

class GymManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Gym Management System")
        self.root.geometry("650x600")
        self.root.config(bg="#0f172a")

        self.members = []

        # ===== TITLE =====
        tk.Label(root, text="Gym Management System",
                 font=("Arial", 18, "bold"),
                 bg="#0f172a", fg="white").pack(pady=10)

        # ===== FORM FRAME =====
        form = tk.Frame(root, bg="#0f172a")
        form.pack()

        self.entries = {}

        fields = [
            "Name", "ID", "Phone",
            "Membership Type", "Duration (months)", "Fee"
        ]

        for i, field in enumerate(fields):
            tk.Label(form, text=field, bg="#0f172a", fg="white").grid(row=i, column=0, pady=5, sticky="w")

            entry = tk.Entry(form, width=30)
            entry.grid(row=i, column=1, pady=5)
            self.entries[field] = entry

        # ===== BUTTONS =====
        btn_frame = tk.Frame(root, bg="#0f172a")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Add Member",
                  command=self.add_member,
                  bg="#16a34a", fg="white", width=15).grid(row=0, column=0, padx=10)

        tk.Button(btn_frame, text="Clear Fields",
                  command=self.clear_fields,
                  bg="#dc2626", fg="white", width=15).grid(row=0, column=1, padx=10)

        # ===== DISPLAY =====
        self.display = tk.Text(root, width=75, height=15)
        self.display.pack(pady=10)

    # ===== ADD MEMBER =====
    def add_member(self):
        name = self.entries["Name"].get()
        member_id = self.entries["ID"].get()
        phone = self.entries["Phone"].get()
        membership = self.entries["Membership Type"].get()
        duration = self.entries["Duration (months)"].get()
        fee = self.entries["Fee"].get()

        # Validation
        if not all([name, member_id, phone, membership, duration, fee]):
            messagebox.showerror("Error", "All fields are required!")
            return

        if not duration.isdigit() or not fee.isdigit():
            messagebox.showerror("Error", "Duration and Fee must be numbers!")
            return

        # Store data
        member = {
            "name": name,
            "id": member_id,
            "phone": phone,
            "membership_type": membership,
            "duration": duration,
            "fee": fee
        }

        self.members.append(member)

        self.update_display()
        self.clear_fields()

    # ===== UPDATE DISPLAY =====
    def update_display(self):
        self.display.delete(1.0, tk.END)

        for i, m in enumerate(self.members, start=1):
            self.display.insert(tk.END, f"Member {i}\n")
            self.display.insert(tk.END, f"Name: {m['name']}\n")
            self.display.insert(tk.END, f"ID: {m['id']}\n")
            self.display.insert(tk.END, f"Phone: {m['phone']}\n")
            self.display.insert(tk.END, f"Membership: {m['membership_type']}\n")
            self.display.insert(tk.END, f"Duration: {m['duration']} months\n")
            self.display.insert(tk.END, f"Fee: {m['fee']}\n")
            self.display.insert(tk.END, "-" * 50 + "\n")

    # ===== CLEAR =====
    def clear_fields(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)


# ===== RUN =====
root = tk.Tk()
app = GymManagement(root)
root.mainloop()
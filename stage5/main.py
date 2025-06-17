import tkinter as tk
from tkinter import ttk, messagebox
from database import DatabaseManager
from config import APP_CONFIG
import sys

class LoginWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Login - " + APP_CONFIG['title'])
        self.root.geometry("400x300")
        self.root.configure(bg=APP_CONFIG['bg_color'])
        self.root.resizable(False, False)
        
        # Center the window
        self.center_window()
        
        self.db_manager = DatabaseManager()
        self.setup_ui()
    
    def center_window(self):
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (400 // 2)
        y = (self.root.winfo_screenheight() // 2) - (300 // 2)
        self.root.geometry(f"400x300+{x}+{y}")
    
    def setup_ui(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg=APP_CONFIG['bg_color'])
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Title
        title_label = tk.Label(
            main_frame, 
            text="Maternity Ward\nManagement System",
            font=('Arial', 18, 'bold'),
            bg=APP_CONFIG['bg_color'],
            fg=APP_CONFIG['primary_color']
        )
        title_label.pack(pady=(0, 30))
        
        # Login form
        form_frame = tk.Frame(main_frame, bg=APP_CONFIG['bg_color'])
        form_frame.pack(expand=True)
        
        # Username
        tk.Label(form_frame, text="Username:", font=('Arial', 12), bg=APP_CONFIG['bg_color']).pack(anchor='w')
        self.username_entry = tk.Entry(form_frame, font=('Arial', 12), width=25)
        self.username_entry.pack(pady=(5, 15))
        self.username_entry.insert(0, "Lielv")  # Default username
        
        # Password
        tk.Label(form_frame, text="Password:", font=('Arial', 12), bg=APP_CONFIG['bg_color']).pack(anchor='w')
        self.password_entry = tk.Entry(form_frame, font=('Arial', 12), width=25, show="*")
        self.password_entry.pack(pady=(5, 25))
        self.password_entry.insert(0, "lielvadee3055")  # Default password
        
        # Login button
        login_btn = tk.Button(
            form_frame,
            text="Login",
            font=('Arial', 12, 'bold'),
            bg=APP_CONFIG['primary_color'],
            fg='white',
            width=20,
            height=2,
            command=self.login
        )
        login_btn.pack()
        
        # Bind Enter key to login
        self.root.bind('<Return>', lambda event: self.login())
        
        # Focus on username entry
        self.username_entry.focus()
    
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password")
            return
        
        # Try to connect to database
        if self.db_manager.connect():
            messagebox.showinfo("Success", "Login successful!")
            self.root.destroy()
            # Launch main application
            app = MainApplication(self.db_manager)
            app.run()
        else:
            messagebox.showerror("Error", "Invalid credentials or database connection failed")
    
    def run(self):
        self.root.mainloop()

class MainApplication:
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self.root = tk.Tk()
        self.root.title(APP_CONFIG['title'])
        self.root.geometry(APP_CONFIG['geometry'])
        self.root.configure(bg=APP_CONFIG['bg_color'])
        
        self.setup_ui()
        
        # Handle window close
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def setup_ui(self):
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create tabs
        self.create_maternity_tab()
        self.create_baby_tab()
        self.create_birth_record_tab()
        self.create_queries_tab()
        self.create_procedures_tab()
    
    def create_maternity_tab(self):
        # Maternity management tab
        maternity_frame = ttk.Frame(self.notebook)
        self.notebook.add(maternity_frame, text="Maternity Management")
        
        # Create MaternityManager
        self.maternity_manager = MaternityManager(maternity_frame, self.db_manager)
    
    def create_baby_tab(self):
        # Baby management tab
        baby_frame = ttk.Frame(self.notebook)
        self.notebook.add(baby_frame, text="Baby Management")
        
        # Create BabyManager
        self.baby_manager = BabyManager(baby_frame, self.db_manager)
    
    def create_birth_record_tab(self):
        # Birth record management tab
        birth_frame = ttk.Frame(self.notebook)
        self.notebook.add(birth_frame, text="Birth Records")
        
        # Create BirthRecordManager
        self.birth_manager = BirthRecordManager(birth_frame, self.db_manager)
    
    def create_queries_tab(self):
        # Queries tab
        queries_frame = ttk.Frame(self.notebook)
        self.notebook.add(queries_frame, text="Reports & Queries")
        
        # Create QueriesManager
        self.queries_manager = QueriesManager(queries_frame, self.db_manager)
    
    def create_procedures_tab(self):
        # Procedures tab
        procedures_frame = ttk.Frame(self.notebook)
        self.notebook.add(procedures_frame, text="Procedures & Functions")
        
        # Create ProceduresManager
        self.procedures_manager = ProceduresManager(procedures_frame, self.db_manager)
    
    def on_closing(self):
        self.db_manager.disconnect()
        self.root.destroy()
        sys.exit()
    
    def run(self):
        self.root.mainloop()

class MaternityManager:
    def __init__(self, parent, db_manager):
        self.parent = parent
        self.db_manager = db_manager
        self.setup_ui()
        self.refresh_data()
    
    def setup_ui(self):
        # Main container
        main_frame = tk.Frame(self.parent, bg=APP_CONFIG['bg_color'])
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Title
        title_label = tk.Label(
            main_frame,
            text="Maternity Management",
            font=('Arial', 16, 'bold'),
            bg=APP_CONFIG['bg_color'],
            fg=APP_CONFIG['primary_color']
        )
        title_label.pack(pady=(0, 20))
        
        # Form frame
        form_frame = tk.LabelFrame(main_frame, text="Maternity Information", font=('Arial', 12, 'bold'))
        form_frame.pack(fill='x', pady=(0, 20))
        
        # Form fields
        fields_frame = tk.Frame(form_frame)
        fields_frame.pack(padx=10, pady=10)
        
        # ID (for updates/deletes)
        tk.Label(fields_frame, text="ID:", font=('Arial', 10)).grid(row=0, column=0, sticky='w', padx=(0, 10))
        self.id_entry = tk.Entry(fields_frame, font=('Arial', 10), width=15)
        self.id_entry.grid(row=0, column=1, padx=(0, 20))
        
        # Name
        tk.Label(fields_frame, text="Name:", font=('Arial', 10)).grid(row=0, column=2, sticky='w', padx=(0, 10))
        self.name_entry = tk.Entry(fields_frame, font=('Arial', 10), width=20)
        self.name_entry.grid(row=0, column=3, padx=(0, 20))
        
        # Age
        tk.Label(fields_frame, text="Age:", font=('Arial', 10)).grid(row=1, column=0, sticky='w', padx=(0, 10), pady=(10, 0))
        self.age_entry = tk.Entry(fields_frame, font=('Arial', 10), width=15)
        self.age_entry.grid(row=1, column=1, padx=(0, 20), pady=(10, 0))
        
        # Phone
        tk.Label(fields_frame, text="Phone:", font=('Arial', 10)).grid(row=1, column=2, sticky='w', padx=(0, 10), pady=(10, 0))
        self.phone_entry = tk.Entry(fields_frame, font=('Arial', 10), width=20)
        self.phone_entry.grid(row=1, column=3, padx=(0, 20), pady=(10, 0))
        
        # Room
        tk.Label(fields_frame, text="Room ID:", font=('Arial', 10)).grid(row=2, column=0, sticky='w', padx=(0, 10), pady=(10, 0))
        self.room_entry = tk.Entry(fields_frame, font=('Arial', 10), width=15)
        self.room_entry.grid(row=2, column=1, padx=(0, 20), pady=(10, 0))
        
        # Buttons frame
        buttons_frame = tk.Frame(form_frame)
        buttons_frame.pack(pady=10)
        
        # CRUD buttons
        tk.Button(buttons_frame, text="Add", bg=APP_CONFIG['success_color'], fg='white', 
                 font=('Arial', 10, 'bold'), command=self.add_maternity).pack(side='left', padx=5)
        tk.Button(buttons_frame, text="Update", bg=APP_CONFIG['warning_color'], fg='white', 
                 font=('Arial', 10, 'bold'), command=self.update_maternity).pack(side='left', padx=5)
        tk.Button(buttons_frame, text="Delete", bg=APP_CONFIG['error_color'], fg='white', 
                 font=('Arial', 10, 'bold'), command=self.delete_maternity).pack(side='left', padx=5)
        tk.Button(buttons_frame, text="Clear", bg=APP_CONFIG['secondary_color'], fg='white', 
                 font=('Arial', 10, 'bold'), command=self.clear_fields).pack(side='left', padx=5)
        tk.Button(buttons_frame, text="Refresh", bg=APP_CONFIG['primary_color'], fg='white', 
                 font=('Arial', 10, 'bold'), command=self.refresh_data).pack(side='left', padx=5)
        
        # Data display frame
        data_frame = tk.LabelFrame(main_frame, text="Maternity Records", font=('Arial', 12, 'bold'))
        data_frame.pack(fill='both', expand=True)
        
        # Treeview for data display
        columns = ('ID', 'Name', 'Age', 'Phone', 'Room ID', 'Floor', 'Availability')
        self.tree = ttk.Treeview(data_frame, columns=columns, show='headings', height=15)
        
        # Define headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)
        
        # Scrollbars
        v_scrollbar = ttk.Scrollbar(data_frame, orient='vertical', command=self.tree.yview)
        h_scrollbar = ttk.Scrollbar(data_frame, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        # Pack treeview and scrollbars
        self.tree.pack(side='left', fill='both', expand=True, padx=(10, 0), pady=10)
        v_scrollbar.pack(side='right', fill='y', pady=10)
        h_scrollbar.pack(side='bottom', fill='x', padx=10)
        
        # Bind double-click to populate fields
        self.tree.bind('<Double-1>', self.on_item_select)
    
    def add_maternity(self):
        name = self.name_entry.get().strip()
        age = self.age_entry.get().strip()
        phone = self.phone_entry.get().strip()
        room_id = self.room_entry.get().strip()
        
        if not all([name, age, phone, room_id]):
            messagebox.showerror("Error", "Please fill all fields")
            return
        
        try:
            age = float(age)
            room_id = int(room_id)
        except ValueError:
            messagebox.showerror("Error", "Age must be a number and Room ID must be an integer")
            return
        
        if self.db_manager.insert_maternity(name, age, phone, room_id):
            messagebox.showinfo("Success", "Maternity record added successfully")
            self.clear_fields()
            self.refresh_data()
    
    def update_maternity(self):
        id_m = self.id_entry.get().strip()
        name = self.name_entry.get().strip()
        age = self.age_entry.get().strip()
        phone = self.phone_entry.get().strip()
        room_id = self.room_entry.get().strip()
        
        if not all([id_m, name, age, phone, room_id]):
            messagebox.showerror("Error", "Please fill all fields including ID")
            return
        
        try:
            id_m = int(id_m)
            age = float(age)
            room_id = int(room_id)
        except ValueError:
            messagebox.showerror("Error", "ID, Age, and Room ID must be numbers")
            return
        
        if self.db_manager.update_maternity(id_m, name, age, phone, room_id):
            messagebox.showinfo("Success", "Maternity record updated successfully")
            self.clear_fields()
            self.refresh_data()
    
    def delete_maternity(self):
        id_m = self.id_entry.get().strip()
        
        if not id_m:
            messagebox.showerror("Error", "Please enter ID to delete")
            return
        
        try:
            id_m = int(id_m)
        except ValueError:
            messagebox.showerror("Error", "ID must be a number")
            return
        
        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete maternity record {id_m}?"):
            if self.db_manager.delete_maternity(id_m):
                messagebox.showinfo("Success", "Maternity record deleted successfully")
                self.clear_fields()
                self.refresh_data()
    
    def clear_fields(self):
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.room_entry.delete(0, tk.END)
    
    def refresh_data(self):
        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Fetch and display new data
        data = self.db_manager.get_all_maternity()
        if data:
            for row in data:
                self.tree.insert('', 'end', values=row)
    
    def on_item_select(self, event):
        selection = self.tree.selection()
        if selection:
            item = self.tree.item(selection[0])
            values = item['values']
            
            self.id_entry.delete(0, tk.END)
            self.id_entry.insert(0, values[0])
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, values[1])
            self.age_entry.delete(0, tk.END)
            self.age_entry.insert(0, values[2])
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, values[3])
            self.room_entry.delete(0, tk.END)
            self.room_entry.insert(0, values[4] if values[4] else '')

class BabyManager:
    def __init__(self, parent, db_manager):
        self.parent = parent
        self.db_manager = db_manager
        self.setup_ui()
        self.refresh_data()
    
    def setup_ui(self):
        # Main container
        main_frame = tk.Frame(self.parent, bg=APP_CONFIG['bg_color'])
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Title
        title_label = tk.Label(
            main_frame,
            text="Baby Management",
            font=('Arial', 16, 'bold'),
            bg=APP_CONFIG['bg_color'],
            fg=APP_CONFIG['primary_color']
        )
        title_label.pack(pady=(0, 20))
        
        # Form frame
        form_frame = tk.LabelFrame(main_frame, text="Baby Information", font=('Arial', 12, 'bold'))
        form_frame.pack(fill='x', pady=(0, 20))
        
        # Form fields
        fields_frame = tk.Frame(form_frame)
        fields_frame.pack(padx=10, pady=10)
        
        # ID
        tk.Label(fields_frame, text="ID:", font=('Arial', 10)).grid(row=0, column=0, sticky='w', padx=(0, 10))
        self.id_entry = tk.Entry(fields_frame, font=('Arial', 10), width=15)
        self.id_entry.grid(row=0, column=1, padx=(0, 20))
        
        # Weight
        tk.Label(fields_frame, text="Weight (kg):", font=('Arial', 10)).grid(row=0, column=2, sticky='w', padx=(0, 10))
        self.weight_entry = tk.Entry(fields_frame, font=('Arial', 10), width=15)
        self.weight_entry.grid(row=0, column=3, padx=(0, 20))
        
        # Gender
        tk.Label(fields_frame, text="Gender:", font=('Arial', 10)).grid(row=1, column=0, sticky='w', padx=(0, 10), pady=(10, 0))
        self.gender_var = tk.StringVar()
        gender_combo = ttk.Combobox(fields_frame, textvariable=self.gender_var, values=['M', 'F'], width=12)
        gender_combo.grid(row=1, column=1, padx=(0, 20), pady=(10, 0))
        
        # Buttons frame
        buttons_frame = tk.Frame(form_frame)
        buttons_frame.pack(pady=10)
        
        # CRUD buttons
        tk.Button(buttons_frame, text="Add", bg=APP_CONFIG['success_color'], fg='white', 
                 font=('Arial', 10, 'bold'), command=self.add_baby).pack(side='left', padx=5)
        tk.Button(buttons_frame, text="Update", bg=APP_CONFIG['warning_color'], fg='white', 
                 font=('Arial', 10, 'bold'), command=self.update_baby).pack(side='left', padx=5)
        tk.Button(buttons_frame, text="Delete", bg=APP_CONFIG['error_color'], fg='white', 
                 font=('Arial', 10, 'bold'), command=self.delete_baby).pack(side='left', padx=5)
        tk.Button(buttons_frame, text="Clear", bg=APP_CONFIG['secondary_color'], fg='white', 
                 font=('Arial', 10, 'bold'), command=self.clear_fields).pack(side='left', padx=5)
        tk.Button(buttons_frame, text="Refresh", bg=APP_CONFIG['primary_color'], fg='white', 
                 font=('Arial', 10, 'bold'), command=self.refresh_data).pack(side='left', padx=5)
        
        # Data display frame
        data_frame = tk.LabelFrame(main_frame, text="Baby Records", font=('Arial', 12, 'bold'))
        data_frame.pack(fill='both', expand=True)
        
        # Treeview for data display
        columns = ('ID', 'Weight (kg)', 'Gender')
        self.tree = ttk.Treeview(data_frame, columns=columns, show='headings', height=15)
        
        # Define headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)
        
        # Scrollbars
        v_scrollbar = ttk.Scrollbar(data_frame, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=v_scrollbar.set)
        
        # Pack treeview and scrollbars
        self.tree.pack(side='left', fill='both', expand=True, padx=(10, 0), pady=10)
        v_scrollbar.pack(side='right', fill='y', pady=10)
        
        # Bind double-click to populate fields
        self.tree.bind('<Double-1>', self.on_item_select)
    
    def add_baby(self):
        weight = self.weight_entry.get().strip()
        gender = self.gender_var.get().strip()
        
        if not all([weight, gender]):
            messagebox.showerror("Error", "Please fill all fields")
            return
        
        try:
            weight = float(weight)
        except ValueError:
            messagebox.showerror("Error", "Weight must be a number")
            return
        
        if self.db_manager.insert_baby(weight, gender):
            messagebox.showinfo("Success", "Baby record added successfully")
            self.clear_fields()
            self.refresh_data()
    
    def update_baby(self):
        id_b = self.id_entry.get().strip()
        weight = self.weight_entry.get().strip()
        gender = self.gender_var.get().strip()
        
        if not all([id_b, weight, gender]):
            messagebox.showerror("Error", "Please fill all fields including ID")
            return
        
        try:
            id_b = int(id_b)
            weight = float(weight)
        except ValueError:
            messagebox.showerror("Error", "ID must be an integer and Weight must be a number")
            return
        
        if self.db_manager.update_baby(id_b, weight, gender):
            messagebox.showinfo("Success", "Baby record updated successfully")
            self.clear_fields()
            self.refresh_data()
    
    def delete_baby(self):
        id_b = self.id_entry.get().strip()
        
        if not id_b:
            messagebox.showerror("Error", "Please enter ID to delete")
            return
        
        try:
            id_b = int(id_b)
        except ValueError:
            messagebox.showerror("Error", "ID must be a number")
            return
        
        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete baby record {id_b}?"):
            if self.db_manager.delete_baby(id_b):
                messagebox.showinfo("Success", "Baby record deleted successfully")
                self.clear_fields()
                self.refresh_data()
    
    def clear_fields(self):
        self.id_entry.delete(0, tk.END)
        self.weight_entry.delete(0, tk.END)
        self.gender_var.set('')
    
    def refresh_data(self):
        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Fetch and display new data
        data = self.db_manager.get_all_babies()
        if data:
            for row in data:
                self.tree.insert('', 'end', values=row)
    
    def on_item_select(self, event):
        selection = self.tree.selection()
        if selection:
            item = self.tree.item(selection[0])
            values = item['values']
            
            self.id_entry.delete(0, tk.END)
            self.id_entry.insert(0, values[0])
            self.weight_entry.delete(0, tk.END)
            self.weight_entry.insert(0, values[1])
            self.gender_var.set(values[2])

class BirthRecordManager:
    def __init__(self, parent, db_manager):
        self.parent = parent
        self.db_manager = db_manager
        self.setup_ui()
        self.refresh_data()
    
    def setup_ui(self):
        # Main container
        main_frame = tk.Frame(self.parent, bg=APP_CONFIG['bg_color'])
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Title
        title_label = tk.Label(
            main_frame,
            text="Birth Record Management",
            font=('Arial', 16, 'bold'),
            bg=APP_CONFIG['bg_color'],
            fg=APP_CONFIG['primary_color']
        )
        title_label.pack(pady=(0, 20))
        
        # Form frame
        form_frame = tk.LabelFrame(main_frame, text="Birth Record Information", font=('Arial', 12, 'bold'))
        form_frame.pack(fill='x', pady=(0, 20))
        
        # Form fields
        fields_frame = tk.Frame(form_frame)
        fields_frame.pack(padx=10, pady=10)
        
        # Row 1
        tk.Label(fields_frame, text="Record ID:", font=('Arial', 10)).grid(row=0, column=0, sticky='w', padx=(0, 10))
        self.id_entry = tk.Entry(fields_frame, font=('Arial', 10), width=15)
        self.id_entry.grid(row=0, column=1, padx=(0, 20))
        
        tk.Label(fields_frame, text="Delivery Type:", font=('Arial', 10)).grid(row=0, column=2, sticky='w', padx=(0, 10))
        self.delivery_var = tk.StringVar()
        delivery_combo = ttk.Combobox(fields_frame, textvariable=self.delivery_var, 
                                    values=['C-Section', 'Vaginal'], width=12)
        delivery_combo.grid(row=0, column=3, padx=(0, 20))
        
        # Row 2
        tk.Label(fields_frame, text="Birth Date:", font=('Arial', 10)).grid(row=1, column=0, sticky='w', padx=(0, 10), pady=(10, 0))
        self.birth_date_entry = tk.Entry(fields_frame, font=('Arial', 10), width=15)
        self.birth_date_entry.grid(row=1, column=1, padx=(0, 20), pady=(10, 0))
        tk.Label(fields_frame, text="(YYYY-MM-DD)", font=('Arial', 8), fg='gray').grid(row=2, column=1, sticky='w')
        
        tk.Label(fields_frame, text="Discharge Date:", font=('Arial', 10)).grid(row=1, column=2, sticky='w', padx=(0, 10), pady=(10, 0))
        self.discharge_date_entry = tk.Entry(fields_frame, font=('Arial', 10), width=15)
        self.discharge_date_entry.grid(row=1, column=3, padx=(0, 20), pady=(10, 0))
        tk.Label(fields_frame, text="(YYYY-MM-DD)", font=('Arial', 8), fg='gray').grid(row=2, column=3, sticky='w')
        
        # Row 3
        tk.Label(fields_frame, text="Mother ID:", font=('Arial', 10)).grid(row=3, column=0, sticky='w', padx=(0, 10), pady=(10, 0))
        self.mother_id_entry = tk.Entry(fields_frame, font=('Arial', 10), width=15)
        self.mother_id_entry.grid(row=3, column=1, padx=(0, 20), pady=(10, 0))
        
        tk.Label(fields_frame, text="Baby ID:", font=('Arial', 10)).grid(row=3, column=2, sticky='w', padx=(0, 10), pady=(10, 0))
        self.baby_id_entry = tk.Entry(fields_frame, font=('Arial', 10), width=15)
        self.baby_id_entry.grid(row=3, column=3, padx=(0, 20), pady=(10, 0))
        
        # Buttons frame
        buttons_frame = tk.Frame(form_frame)
        buttons_frame.pack(pady=10)
        
        # CRUD buttons
        tk.Button(buttons_frame, text="Add", bg=APP_CONFIG['success_color'], fg='white', 
                 font=('Arial', 10, 'bold'), command=self.add_birth_record).pack(side='left', padx=5)
        tk.Button(buttons_frame, text="Update", bg=APP_CONFIG['warning_color'], fg='white', 
                 font=('Arial', 10, 'bold'), command=self.update_birth_record).pack(side='left', padx=5)
        tk.Button(buttons_frame, text="Delete", bg=APP_CONFIG['error_color'], fg='white', 
                 font=('Arial', 10, 'bold'), command=self.delete_birth_record).pack(side='left', padx=5)
        tk.Button(buttons_frame, text="Clear", bg=APP_CONFIG['secondary_color'], fg='white', 
                 font=('Arial', 10, 'bold'), command=self.clear_fields).pack(side='left', padx=5)
        tk.Button(buttons_frame, text="Refresh", bg=APP_CONFIG['primary_color'], fg='white', 
                 font=('Arial', 10, 'bold'), command=self.refresh_data).pack(side='left', padx=5)
        
        # Data display frame
        data_frame = tk.LabelFrame(main_frame, text="Birth Records", font=('Arial', 12, 'bold'))
        data_frame.pack(fill='both', expand=True)
        
        # Treeview for data display
        columns = ('Record ID', 'Delivery Type', 'Birth Date', 'Discharge Date', 'Mother Name', 'Baby Gender', 'Baby Weight')
        self.tree = ttk.Treeview(data_frame, columns=columns, show='headings', height=12)
        
        # Define headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)
        
        # Scrollbars
        v_scrollbar = ttk.Scrollbar(data_frame, orient='vertical', command=self.tree.yview)
        h_scrollbar = ttk.Scrollbar(data_frame, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        # Pack treeview and scrollbars
        self.tree.pack(side='left', fill='both', expand=True, padx=(10, 0), pady=10)
        v_scrollbar.pack(side='right', fill='y', pady=10)
        h_scrollbar.pack(side='bottom', fill='x', padx=10)
        
        # Bind double-click to populate fields
        self.tree.bind('<Double-1>', self.on_item_select)
    
    def add_birth_record(self):
        delivery_type = self.delivery_var.get().strip()
        birth_date = self.birth_date_entry.get().strip()
        discharge_date = self.discharge_date_entry.get().strip()
        mother_id = self.mother_id_entry.get().strip()
        baby_id = self.baby_id_entry.get().strip()
        
        if not all([delivery_type, birth_date, discharge_date, mother_id, baby_id]):
            messagebox.showerror("Error", "Please fill all fields")
            return
        
        try:
            mother_id = int(mother_id)
            baby_id = int(baby_id)
        except ValueError:
            messagebox.showerror("Error", "Mother ID and Baby ID must be integers")
            return
        
        if self.db_manager.insert_birth_record(delivery_type, birth_date, discharge_date, mother_id, baby_id):
            messagebox.showinfo("Success", "Birth record added successfully")
            self.clear_fields()
            self.refresh_data()
    
    def update_birth_record(self):
        id_br = self.id_entry.get().strip()
        delivery_type = self.delivery_var.get().strip()
        birth_date = self.birth_date_entry.get().strip()
        discharge_date = self.discharge_date_entry.get().strip()
        mother_id = self.mother_id_entry.get().strip()
        baby_id = self.baby_id_entry.get().strip()
        
        if not all([id_br, delivery_type, birth_date, discharge_date, mother_id, baby_id]):
            messagebox.showerror("Error", "Please fill all fields including Record ID")
            return
        
        try:
            id_br = int(id_br)
            mother_id = int(mother_id)
            baby_id = int(baby_id)
        except ValueError:
            messagebox.showerror("Error", "IDs must be integers")
            return
        
        if self.db_manager.update_birth_record(id_br, delivery_type, birth_date, discharge_date, mother_id, baby_id):
            messagebox.showinfo("Success", "Birth record updated successfully")
            self.clear_fields()
            self.refresh_data()
    
    def delete_birth_record(self):
        id_br = self.id_entry.get().strip()
        
        if not id_br:
            messagebox.showerror("Error", "Please enter Record ID to delete")
            return
        
        try:
            id_br = int(id_br)
        except ValueError:
            messagebox.showerror("Error", "Record ID must be a number")
            return
        
        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete birth record {id_br}?"):
            if self.db_manager.delete_birth_record(id_br):
                messagebox.showinfo("Success", "Birth record deleted successfully")
                self.clear_fields()
                self.refresh_data()
    
    def clear_fields(self):
        self.id_entry.delete(0, tk.END)
        self.delivery_var.set('')
        self.birth_date_entry.delete(0, tk.END)
        self.discharge_date_entry.delete(0, tk.END)
        self.mother_id_entry.delete(0, tk.END)
        self.baby_id_entry.delete(0, tk.END)
    
    def refresh_data(self):
        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Fetch and display new data
        data = self.db_manager.get_all_birth_records()
        if data:
            for row in data:
                self.tree.insert('', 'end', values=row)
    
    def on_item_select(self, event):
        selection = self.tree.selection()
        if selection:
            item = self.tree.item(selection[0])
            values = item['values']
            
            self.id_entry.delete(0, tk.END)
            self.id_entry.insert(0, values[0])
            self.delivery_var.set(values[1])
            self.birth_date_entry.delete(0, tk.END)
            self.birth_date_entry.insert(0, values[2])
            self.discharge_date_entry.delete(0, tk.END)
            self.discharge_date_entry.insert(0, values[3])

class QueriesManager:
    def __init__(self, parent, db_manager):
        self.parent = parent
        self.db_manager = db_manager
        self.setup_ui()
    
    def setup_ui(self):
        # Main container
        main_frame = tk.Frame(self.parent, bg=APP_CONFIG['bg_color'])
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Title
        title_label = tk.Label(
            main_frame,
            text="Reports & Queries",
            font=('Arial', 16, 'bold'),
            bg=APP_CONFIG['bg_color'],
            fg=APP_CONFIG['primary_color']
        )
        title_label.pack(pady=(0, 20))
        
        # Queries frame
        queries_frame = tk.LabelFrame(main_frame, text="Available Queries", font=('Arial', 12, 'bold'))
        queries_frame.pack(fill='x', pady=(0, 20))
        
        # Query buttons
        buttons_frame = tk.Frame(queries_frame)
        buttons_frame.pack(pady=10)
        
        tk.Button(buttons_frame, text="Night Shift Nurses Report", 
                 bg=APP_CONFIG['primary_color'], fg='white', font=('Arial', 11, 'bold'),
                 command=self.run_night_shift_query, width=25).pack(side='left', padx=10)
        
        tk.Button(buttons_frame, text="Birth Weight Analysis", 
                 bg=APP_CONFIG['secondary_color'], fg='white', font=('Arial', 11, 'bold'),
                 command=self.run_weight_analysis_query, width=25).pack(side='left', padx=10)
        
        # Results frame
        results_frame = tk.LabelFrame(main_frame, text="Query Results", font=('Arial', 12, 'bold'))
        results_frame.pack(fill='both', expand=True)
        
        # Treeview for results
        self.results_tree = ttk.Treeview(results_frame, show='headings', height=15)
        
        # Scrollbars
        v_scrollbar = ttk.Scrollbar(results_frame, orient='vertical', command=self.results_tree.yview)
        h_scrollbar = ttk.Scrollbar(results_frame, orient='horizontal', command=self.results_tree.xview)
        self.results_tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        # Pack treeview and scrollbars
        self.results_tree.pack(side='left', fill='both', expand=True, padx=(10, 0), pady=10)
        v_scrollbar.pack(side='right', fill='y', pady=10)
        h_scrollbar.pack(side='bottom', fill='x', padx=10)
    
    def run_night_shift_query(self):
        data = self.db_manager.query_night_shift_nurses()
        if data is not None:
            self.display_results(data, ['Room ID', 'Mother Name', 'Nurse Name', 'Shift Hours'])
        else:
            messagebox.showerror("Error", "Failed to execute query")
    
    def run_weight_analysis_query(self):
        data = self.db_manager.query_birth_weight_analysis()
        if data is not None:
            self.display_results(data, ['Delivery Type', 'Total Births', 'Average Baby Weight'])
        else:
            messagebox.showerror("Error", "Failed to execute query")
    
    def display_results(self, data, columns):
        # Clear existing data
        for item in self.results_tree.get_children():
            self.results_tree.delete(item)
        
        # Configure columns
        self.results_tree['columns'] = columns
        for col in columns:
            self.results_tree.heading(col, text=col)
            self.results_tree.column(col, width=150)
        
        # Insert data
        if data:
            for row in data:
                self.results_tree.insert('', 'end', values=row)
            messagebox.showinfo("Success", f"Query executed successfully. {len(data)} records found.")
        else:
            messagebox.showinfo("Info", "No records found for this query.")

class ProceduresManager:
    def __init__(self, parent, db_manager):
        self.parent = parent
        self.db_manager = db_manager
        self.setup_ui()
    
    def setup_ui(self):
        # Main container
        main_frame = tk.Frame(self.parent, bg=APP_CONFIG['bg_color'])
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Title
        title_label = tk.Label(
            main_frame,
            text="Procedures & Functions",
            font=('Arial', 16, 'bold'),
            bg=APP_CONFIG['bg_color'],
            fg=APP_CONFIG['primary_color']
        )
        title_label.pack(pady=(0, 20))
        
        # Procedures frame
        procedures_frame = tk.LabelFrame(main_frame, text="Available Procedures & Functions", font=('Arial', 12, 'bold'))
        procedures_frame.pack(fill='x', pady=(0, 20))
        
        # Program 1 section
        program1_frame = tk.Frame(procedures_frame)
        program1_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Label(program1_frame, text="Program 1: Assign C-Section Mothers to Rooms", 
                font=('Arial', 12, 'bold')).pack(anchor='w')
        tk.Label(program1_frame, text="Automatically assigns mothers who had C-sections to available rooms on floors 4 or 5", 
                font=('Arial', 10), fg='gray').pack(anchor='w', pady=(0, 10))
        
        tk.Button(program1_frame, text="Run Room Assignment Program", 
                 bg=APP_CONFIG['success_color'], fg='white', font=('Arial', 11, 'bold'),
                 command=self.run_room_assignment_program, width=30).pack(anchor='w')
        
        # Separator
        tk.Frame(procedures_frame, height=2, bg='gray').pack(fill='x', padx=10, pady=10)
        
        # Program 2 section
        program2_frame = tk.Frame(procedures_frame)
        program2_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Label(program2_frame, text="Program 2: Department Summary", 
                font=('Arial', 12, 'bold')).pack(anchor='w')
        tk.Label(program2_frame, text="Randomly selects a department and returns relevant summary information", 
                font=('Arial', 10), fg='gray').pack(anchor='w', pady=(0, 10))
        
        tk.Button(program2_frame, text="Run Department Summary Program", 
                 bg=APP_CONFIG['warning_color'], fg='white', font=('Arial', 11, 'bold'),
                 command=self.run_department_summary_program, width=30).pack(anchor='w')
        
        # Results frame
        results_frame = tk.LabelFrame(main_frame, text="Execution Results", font=('Arial', 12, 'bold'))
        results_frame.pack(fill='both', expand=True)
        
        # Text widget for results
        self.results_text = tk.Text(results_frame, font=('Courier', 10), wrap=tk.WORD)
        results_scrollbar = ttk.Scrollbar(results_frame, orient='vertical', command=self.results_text.yview)
        self.results_text.configure(yscrollcommand=results_scrollbar.set)
        
        # Pack text widget and scrollbar
        self.results_text.pack(side='left', fill='both', expand=True, padx=(10, 0), pady=10)
        results_scrollbar.pack(side='right', fill='y', pady=10)
    
    def run_room_assignment_program(self):
        try:
            # Execute the room assignment function
            result = self.db_manager.execute_function("SELECT assign_rooms_and_return() AS refcur")
            
            if result:
                self.results_text.delete(1.0, tk.END)
                self.results_text.insert(tk.END, "Room Assignment Program Executed Successfully!\n\n")
                self.results_text.insert(tk.END, "Program assigns C-section mothers to available rooms on floors 4 or 5.\n")
                self.results_text.insert(tk.END, "Check the Maternity Management tab to see updated room assignments.\n\n")
                self.results_text.insert(tk.END, f"Execution completed at: {result}\n")
                messagebox.showinfo("Success", "Room assignment program executed successfully!")
            else:
                messagebox.showerror("Error", "Failed to execute room assignment program")
        except Exception as e:
            messagebox.showerror("Error", f"Error executing program: {str(e)}")
    
    def run_department_summary_program(self):
        try:
            # Execute the department summary function
            result = self.db_manager.execute_function("SELECT get_department_summary() AS refcur")
            
            if result:
                self.results_text.delete(1.0, tk.END)
                self.results_text.insert(tk.END, "Department Summary Program Executed Successfully!\n\n")
                self.results_text.insert(tk.END, "Program randomly selects a department and provides summary information.\n")
                self.results_text.insert(tk.END, "If maternity department (ID=7) is selected, it updates staff information\n")
                self.results_text.insert(tk.END, "and returns birth statistics. Otherwise, it returns cancer patient data.\n\n")
                self.results_text.insert(tk.END, f"Execution completed at: {result}\n")
                messagebox.showinfo("Success", "Department summary program executed successfully!")
            else:
                messagebox.showerror("Error", "Failed to execute department summary program")
        except Exception as e:
            messagebox.showerror("Error", f"Error executing program: {str(e)}")

if __name__ == "__main__":
    # Start with login window
    login = LoginWindow()
    login.run()
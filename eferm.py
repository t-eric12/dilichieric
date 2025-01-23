import tkinter as tk
from tkinter import ttk, messagebox
import os
import json
#ndaruhukira aha

class EFarming(tk.Tk):
    def __init__(self, root):
        self.root = root
        self.root.title("E-Farming Management System")
        self.root.geometry("900x600")
        root.configure(bg="green")

       
        # Farmers and Buyers Data Files
        self.farmers_file = "farmers_data.json"
        self.buyers_file = "buyers_data.json"
        self.orders_file="orders_data.json"
        self.products_file="products.json"
        self.products=[]
        for file in [self.farmers_file, self.buyers_file,self.orders_file,self.products_file]:
            if not os.path.exists(file):
                with open(file, "w") as f:
                    json.dump([], f)
        self.load_products()    

        # Title Header
        title = tk.Label(
            self.root,
            text="E-Farmer Management System",
            font=("Helvetica", 24, "bold"),
            bg="blue",
            fg="white",
        )
        title.pack(side=tk.TOP, fill=tk.X)

        # Navigation Frame (Sidebar)
        self.nav_frame = tk.Frame(self.root, bg="cyan", relief=tk.RIDGE, bd=2)
        self.nav_frame.place(x=10, y=70, width=200, height=520)

        # Content Frame
        self.content_frame = tk.Frame(self.root, bg="white", relief=tk.RIDGE, bd=2)
        self.content_frame.place(x=220, y=70, width=670, height=520)

        # Navigation Buttons
        nav_buttons = [
            ("Home", self.show_home),
            ("Farmer Management", self.show_farmer_management),
            ("Buyer Management", self.show_buyer_management),
            ("Product Management", self.show_product_management),
            ("Order Management", self.show_order_management),
            ("Admin Panel", self.show_admin_panel),
            ("Exit", self.exit_app),
        ]
        for i, (text, command) in enumerate(nav_buttons):
            btn = tk.Button(
                self.nav_frame,
                text=text,
                command=command,
                font=("Helvetica", 12),
                bg="skyblue",
                relief=tk.GROOVE,
            )
            btn.pack(pady=10, fill=tk.X)

        # Display Welcome Screen by Default
       # self.show_home()
        self.show_home()

    def load_products(self):
        """Load products from the products file."""
        try:
            with open(self.products_file, "r") as file:
                self.products = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.products = []


    def clear_content_frame(self):
        """Clear all widgets in the content frame."""
        for widget in self.content_frame.winfo_children():
            widget.destroy()

   
    
        
    def show_home(self):
        """Display the Home Page with product list and search bar."""
        self.clear_content_frame()

        # Search Bar
        search_frame = tk.Frame(self.content_frame, bg="lightblue")
        search_frame.pack(fill=tk.X, pady=10)

        search_label = tk.Label(search_frame, text="Search Product:", font=("Helvetica", 12), bg="lightblue")
        search_label.pack(side=tk.LEFT, padx=10)
        self.search_entry = tk.Entry(search_frame, font=("Helvetica", 12), width=30)
        self.search_entry.pack(side=tk.LEFT, padx=10)
        search_button = tk.Button(search_frame, text="Search", font=("Helvetica", 12), command=self.filter_products)
        search_button.pack(side=tk.LEFT, padx=10)

        # Product List
        product_list_frame = tk.Frame(self.content_frame, bg="yellow")
        product_list_frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(product_list_frame, text="Product List", font=("Helvetica", 16), bg="orange").pack(pady=10)
        self.product_canvas = tk.Canvas(product_list_frame, bg="gray")
        self.product_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(product_list_frame, orient=tk.VERTICAL, command=self.product_canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.product_canvas.configure(yscrollcommand=scrollbar.set)

        self.product_frame = tk.Frame(self.product_canvas, bg="blue")
        self.product_canvas.create_window((0, 0), window=self.product_frame, anchor="nw")
        self.product_frame.bind("<Configure>", lambda e: self.product_canvas.configure(scrollregion=self.product_canvas.bbox("all")))

        self.display_products(self.products)

    def display_products(self, products):
        """Display products in the product list."""
        for widget in self.product_frame.winfo_children():
            widget.destroy()

        for product in products:
            frame = tk.Frame(self.product_frame, bg="cyan", relief=tk.RIDGE, bd=2)
            frame.pack(fill=tk.X, pady=5, padx=10)

            info_frame = tk.Frame(frame, bg="green")
            info_frame.pack(side=tk.LEFT, padx=10)

            tk.Label(info_frame, text=f"Name: {product.get('name', 'N/A')}", font=("Helvetica", 12), bg="cyan").pack(anchor="w")
            tk.Label(info_frame, text=f"Price per unit: frw{product.get('price', 'N/A')}", font=("Helvetica", 12), bg="cyan").pack(anchor="w")

    def filter_products(self):
        """Filter products based on search input."""
        query = self.search_entry.get().lower()
        filtered_products = [product for product in self.products if query in product.get("name", "").lower()]
        self.display_products(filtered_products)

    def show_farmer_management(self):
        """Farmer Management Section."""
        self.clear_content_frame()
        tk.Label(self.content_frame, text="Farmer Management", font=("Helvetica", 16)).pack(pady=10)

        actions = [
            ("Register Farmer", self.register_farmer),
            ("Login Farmer", self.login_farmer),
        ]
        for action_text, action_cmd in actions:
            tk.Button(self.content_frame, text=action_text, command=action_cmd,bg="yellow").pack(pady=5)

    def show_buyer_management(self):
        """Buyer Management Section."""
        self.clear_content_frame()
        tk.Label(self.content_frame, text="Buyer Management", font=("Helvetica", 16)).pack(pady=10)

        actions = [
            ("Register Buyer", self.register_buyer),
            ("Login Buyer", self.login_buyer),
        ]
        for action_text, action_cmd in actions:
            tk.Button(self.content_frame, text=action_text, command=action_cmd,bg="yellow").pack(pady=5)
    def show_product_management(self):
        """Product Management Section."""
        self.clear_content_frame()
        tk.Label(self.content_frame, text="Product Management", font=("Helvetica", 16),bg="green").pack(pady=10)

        actions = [
            ("Add Product", self.add_product),
           
        ]
        for action_text, action_cmd in actions:
            tk.Button(self.content_frame, text=action_text, command=action_cmd,bg="darkblue").pack(pady=5)
    def show_order_management(self):
        """Order Management Section."""
        self.clear_content_frame()
        tk.Label(self.content_frame, text="Order Management", font=("Helvetica", 16),bg="green").pack(pady=10)

        actions = [
            ("Place Order", lambda: self.show_message("Place Order")),
            ("Track Order", lambda: self.show_message("Track Order")),
            ("View Pending Orders",self.view_pending_orders),
        ]
        for action_text, action_cmd in actions:
            tk.Button(self.content_frame, text=action_text, command=action_cmd,bg="skyblue").pack(pady=5)
    

    def view_pending_orders(self, buyer_name):
        """View pending orders by buyer."""
        self.clear_content_frame()
        tk.Label(self.content_frame, text="Pending Orders", font=("Helvetica", 16)).pack(pady=10)

        try:
            with open(self.orders_file, "r") as file:
                orders = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            orders = []

        buyer_orders = [order for order in orders if order.get("buyer") == buyer_name]

        if not buyer_orders:
            tk.Label(self.content_frame, text="No pending orders.", font=("Helvetica", 12)).pack(pady=10)
        else:
            for order in buyer_orders:
                tk.Label(
                    self.content_frame,
                    text=f"Product: {order['product']}, Quantity: {order['quantity']}, Status: {order['status']}",
                    font=("Helvetica", 12),
                    bg="cyan"
                ).pack(pady=5)

    def show_admin_panel(self):
        """Admin Panel Section."""
        self.clear_content_frame()
        tk.Label(self.content_frame, text="Admin Panel", font=("Helvetica", 16),bg="green").pack(pady=10)

        
        actions = [
            ("Generate Product Report", self.generate_product_report),
            ("Generate Buyer Report", self.generate_buyer_report),
            ("Generate Order Report", self.generate_order_report),
        ]
        for action_text, action_cmd in actions:
            tk.Button(self.content_frame, text=action_text, command=action_cmd,bg="orange").pack(pady=5)
    def generate_product_report(self):
       
           # Placeholder code for report generation
        messagebox.showinfo("Report", "products report feature not implemented yet.")
    def generate_buyer_report(self):
        """Generate an Excel report for buyers."""
        # Placeholder code for report generation
        messagebox.showinfo("Report", "Buyer report feature not implemented yet.")

    def generate_order_report(self):
      
           # Placeholder code for report generation
        messagebox.showinfo("Report", "order report feature not implemented yet.")


    def exit_app(self):
        """Exit the application."""
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.quit()

    
    def add_product(self):
        """Add a new product."""
        super().__init__()
        self.title("Product Management")
        self.geometry("600x400")
        self.configure(bg="green")
        self.products = []
        self.load_products()
    

        # TreeView for displaying products
        self.tree = ttk.Treeview(self, columns=("name", "price", "quantity", "total_price"), show="headings")
        self.tree.heading("name", text="Product Name")
        self.tree.heading("price", text="Price per Unit")
        self.tree.heading("quantity", text="Quantity")
        self.tree.heading("total_price", text="Total Price")
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

        # Buttons
        button_frame = tk.Frame(self)
        button_frame.pack(pady=5)

        tk.Button(button_frame, text="Add Product", command=self.add_product_window, bg="yellow",width=15).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Edit Product", command=self.edit_product_window, bg="yellow",width=15).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Delete Product", command=self.delete_product,bg="yellow", width=15).grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="Search Product", command=self.search_product_window, bg="yellow",width=15).grid(row=0, column=3, padx=5)

        self.refresh_tree()

    def load_products(self):
        """Load products from a JSON file."""
        if os.path.exists("products.json"):
            with open("products.json", "r") as file:
                self.products = json.load(file)

    def save_products(self):
        """Save products to a JSON file."""
        with open("products.json", "w") as file:
            json.dump(self.products, file)

    def refresh_tree(self):
        """Refresh the TreeView with the latest product list."""
        for item in self.tree.get_children():
            self.tree.delete(item)
        for product in self.products:
            #self.tree.insert("", "end", values=(product["name"], product["price"], product["quantity"], product["total_price"]))
    
        # Use .get() to safely access keys with default values
         name = product.get("name", "Unknown")
         price = product.get("price", "0")
         quantity = product.get("quantity", "0")
         total_price = product.get("total_price", "0")
         self.tree.insert("", "end", values=(name, price, quantity, total_price))

    def add_product_window(self):
        """Open a new window to add product details."""
        self.product_form_window("Add Product", self.save_product)

    def save_product(self, window, name_entry, price_entry, quantity_entry):
        """Save the new product to the product list."""
        name, price, quantity = self.get_product_details(name_entry, price_entry, quantity_entry)
        if name is None:
            return

        total_price = price * quantity
        self.products.append({
            "name": name,
            "price": price,
            "quantity": quantity,
            "total_price": total_price
        })
        self.save_products()
        self.refresh_tree()
        window.destroy()
        messagebox.showinfo("Success", f"Product added successfully!\nTotal Price: ${total_price:.2f}")

    def edit_product_window(self):
        """Open a new window to edit selected product details."""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No product selected!")
            return

        product_index = self.tree.index(selected_item[0])
        product = self.products[product_index]

        self.product_form_window("Edit Product", self.save_edited_product, product, product_index)

    def save_edited_product(self, window, name_entry, price_entry, quantity_entry, product_index):
        """Save the edited product details."""
        name, price, quantity = self.get_product_details(name_entry, price_entry, quantity_entry)
        if name is None:
            return

        total_price = price * quantity
        self.products[product_index] = {
            "name": name,
            "price": price,
            "quantity": quantity,
            "total_price": total_price
        }
        self.save_products()
        self.refresh_tree()
        window.destroy()
        messagebox.showinfo("Success", "Product edited successfully!")

    def delete_product(self):
        """Delete the selected product."""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No product selected!")
            return

        product_index = self.tree.index(selected_item[0])
        del self.products[product_index]
        self.save_products()
        self.refresh_tree()
        messagebox.showinfo("Success", "Product deleted successfully!")

    def search_product_window(self):
        """Open a new window to search for products by name."""
        search_window = tk.Toplevel(self)
        search_window.title("Search Product")
        search_window.geometry("300x150")

        tk.Label(search_window, text="Enter Product Name").pack(pady=5)
        search_entry = tk.Entry(search_window)
        search_entry.pack(pady=5)

        tk.Button(search_window, text="Search", command=lambda: self.search_product(search_window, search_entry)).pack(pady=10)

    def search_product(self, window, search_entry):
        """Search for a product and display results."""
        search_term = search_entry.get().strip().lower()
        results = [product for product in self.products if search_term in product["name"].lower()]

        if not results:
            messagebox.showinfo("No Results", "No products found!")
        else:
            result_window = tk.Toplevel(self)
            result_window.title("Search Results")
            result_window.geometry("400x300")

            tree = ttk.Treeview(result_window, columns=("name", "price", "quantity", "total_price"), show="headings")
            tree.heading("name", text="Product Name")
            tree.heading("price", text="Price per Unit")
            tree.heading("quantity", text="Quantity")
            tree.heading("total_price", text="Total Price")
            tree.pack(pady=10, fill=tk.BOTH, expand=True)

            for product in results:
                tree.insert("", "end", values=(product["name"], product["price"], product["quantity"], product["total_price"]))

        window.destroy()

    def product_form_window(self, title, save_command, product=None, product_index=None):
        """Create a form window for adding or editing a product."""
        form_window = tk.Toplevel(self)
        form_window.title(title)
        form_window.geometry("300x250")

        tk.Label(form_window, text="Product Name").grid(row=0, column=0, pady=5, padx=5)
        tk.Label(form_window, text="Price per Unit in frw").grid(row=1, column=0, pady=5, padx=5)
        tk.Label(form_window, text="Quantity in kg").grid(row=2, column=0, pady=5, padx=5)

        name_entry = tk.Entry(form_window)
        name_entry.grid(row=0, column=1, pady=5, padx=5)
        price_entry = tk.Entry(form_window)
        price_entry.grid(row=1, column=1, pady=5, padx=5)
        quantity_entry = tk.Entry(form_window)
        quantity_entry.grid(row=2, column=1, pady=5, padx=5)

        if product:
            name_entry.insert(0, product["name"])
            price_entry.insert(0, product["price"])
            quantity_entry.insert(0, product["quantity"])

        tk.Button(form_window, text="Save", command=lambda: save_command(form_window, name_entry, price_entry, quantity_entry)).grid(row=3, column=0, columnspan=2, pady=10)

    def get_product_details(self, name_entry, price_entry, quantity_entry):
        """Get product details from the form entries."""
        name = name_entry.get().strip()
        try:
            price = float(price_entry.get().strip())
            quantity = int(quantity_entry.get().strip())
        except ValueError:
            messagebox.showerror("Error", "Price must be a number and Quantity must be an integer!")
            return None, None, None

        if not name:
            messagebox.showerror("Error", "Product Name cannot be empty!")
            return None, None, None

        return name, price, quantity

    def show_product_details(self, product):
        """Display product details."""
        self.clear_content_frame()
        tk.Label(self.content_frame, text="Product Details", font=("Helvetica", 16)).pack(pady=10)

        for key, value in product.items():
            tk.Label(
                self.content_frame, text=f"{key.capitalize()}: {value}", font=("Helvetica", 12)
            ).pack(anchor="w", pady=5)

        tk.Button(self.content_frame, text="Back", command=self.show_product_management,bg="darkgreen").pack(pady=10)
    def register_farmer(self):
        """farmer registration """
        self.clear_content_frame()
        tk.Label(self.content_frame, text="Register farmer", font=("Helvetica", 16)).pack(pady=10)

        fields = ["Name", "Phone", "Email","place", "Username", "Password"]
        self.registration_data = {}
        for field in fields:
            tk.Label(self.content_frame, text=field, font=("Helvetica", 12)).pack()
            entry = tk.Entry(self.content_frame, font=("Helvetica", 12), show="*" if field == "Password" else None)
            entry.pack(pady=5)
            self.registration_data[field] = entry

        tk.Button(self.content_frame, text="Submit", command=self.save_farmer,bg="yellow").pack(pady=10)

    def save_farmer(self):
        """Save farmer data to file."""
        farmer_data = {field: entry.get() for field, entry in self.registration_data.items()}
        with open(self.farmers_file, "r+") as file:
            farmers = json.load(file)
            farmers.append(farmer_data)
            file.seek(0)
            json.dump(farmers, file)
        messagebox.showinfo("Success", "farmer registered successfully!")
        self.show_farmer_management()

    def login_farmer(self):
        """farmer block Login."""
        self.clear_content_frame()
        tk.Label(self.content_frame, text="Login farmer", font=("Helvetica", 16)).pack(pady=10)

        self.login_data = {}
        for field in ["Username", "Password"]:
            tk.Label(self.content_frame, text=field, font=("Helvetica", 12)).pack()
            entry = tk.Entry(self.content_frame, font=("Helvetica", 12), show="*" if field == "Password" else None)
            entry.pack(pady=5)
            self.login_data[field] = entry

        tk.Button(self.content_frame, text="Login", command=self.authenticate_farmer,bg="yellow").pack(pady=10)

    def authenticate_farmer(self):
        """Authenticate farmer login."""
        username = self.login_data["Username"].get()
        password = self.login_data["Password"].get()
        with open(self.farmers_file, "r") as file:
            farmers = json.load(file)
            for farmer in farmers:
                if farmer["Username"] == username and farmer["Password"] == password:
                    messagebox.showinfo("Success", "Login successful!")
                    self.add_product()
                    return
        messagebox.showerror("Error", "Invalid username or password!")

    def register_buyer(self):
        """Buyer Registration."""
        self.clear_content_frame()
        tk.Label(self.content_frame, text="Register Buyer", font=("Helvetica", 16)).pack(pady=10)

        fields = ["Name", "Phone", "Email","place", "Username", "Password"]
        self.registration_data = {}
        for field in fields:
            tk.Label(self.content_frame, text=field, font=("Helvetica", 12)).pack()
            entry = tk.Entry(self.content_frame, font=("Helvetica", 12), show="*" if field == "Password" else None)
            entry.pack(pady=5)
            self.registration_data[field] = entry

        tk.Button(self.content_frame, text="Submit", command=self.save_buyer,bg="yellow").pack(pady=10)

    def save_buyer(self):
        """Save buyer data to file."""
        buyer_data = {field: entry.get() for field, entry in self.registration_data.items()}
        with open(self.buyers_file, "r+") as file:
            buyers = json.load(file)
            buyers.append(buyer_data)
            file.seek(0)
            json.dump(buyers, file)
        messagebox.showinfo("Success", "Buyer registered successfully!")
        self.show_buyer_management()

    def login_buyer(self):
        """Buyer Login."""
        self.clear_content_frame()
        tk.Label(self.content_frame, text="Login Buyer", font=("Helvetica", 16)).pack(pady=10)

        self.login_data = {}
        for field in ["Username", "Password"]:
            tk.Label(self.content_frame, text=field, font=("Helvetica", 12)).pack()
            entry = tk.Entry(self.content_frame, font=("Helvetica", 12), show="*" if field == "Password" else None)
            entry.pack(pady=5)
            self.login_data[field] = entry

        tk.Button(self.content_frame, text="Login", command=self.authenticate_buyer).pack(pady=10)

    def authenticate_buyer(self):
        """Authenticate buyer login."""
        username = self.login_data["Username"].get()
        password = self.login_data["Password"].get()
        with open(self.buyers_file, "r") as file:
            buyers = json.load(file)
            for buyer in buyers:
                if buyer["Username"] == username and buyer["Password"] == password:
                    messagebox.showinfo("Success", "Login successful!")
                    self.order_product(buyer["Name"])
                    return
        messagebox.showerror("Error", "Invalid username or password!")

     # Main content frame
        self.content_frame = tk.Frame(self.root,bg="red")
        self.content_frame.pack(fill=tk.BOTH, expand=True)

    def clear_content_frame(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def order_product(self, buyer_name):
        self.clear_content_frame()
        tk.Label(self.content_frame, text="Order Product", font=("Helvetica", 16)).pack(pady=10)

        # Create a frame to hold the canvas and scrollbar
        scroll_frame = tk.Frame(self.content_frame,bg="orange")
        scroll_frame.pack(fill=tk.BOTH, expand=True)

        # Create a canvas for scrolling
        canvas = tk.Canvas(scroll_frame,bg="green")
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add a vertical scrollbar to the canvas
        scrollbar = tk.Scrollbar(scroll_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the canvas to work with the scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Create a frame inside the canvas to hold the product list
        product_list_frame = tk.Frame(canvas,bg="orange")
        canvas.create_window((0, 0), window=product_list_frame, anchor="nw")

        try:
            with open(self.products_file, "r") as file:
                products = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            messagebox.showerror("Error", "Unable to load products.")
            return

        # Populate the product list frame
        for product in products:
            frame = tk.Frame(product_list_frame, bg="blue", relief=tk.RIDGE, bd=2)
            frame.pack(fill=tk.X, pady=5, padx=10)

            tk.Label(frame, text=f"Name: {product['name']}", font=("Helvetica", 12), bg="blue", fg="white").pack(anchor="w")
            tk.Label(frame, text=f"Price: ${product['price']}", font=("Helvetica", 12), bg="blue", fg="white").pack(anchor="w")

            order_button = tk.Button(
                frame, text="Order", command=lambda p=product: self.place_order(buyer_name, p), bg="green", fg="white"
            )
            order_button.pack(anchor="e")

    def place_order(self, buyer_name, product):
        order = {
            "buyer": buyer_name,
            "product": product["name"],
            "quantity": 1,  # For simplicity, set quantity to 1
            "status": "Pending"
        }
        try:
            with open(self.orders_file, "r+") as file:
                try:
                    orders = json.load(file)
                except json.JSONDecodeError:
                    orders = []
                orders.append(order)
                file.seek(0)
                json.dump(orders, file)
        except FileNotFoundError:
            with open(self.orders_file, "w") as file:
                json.dump([order], file)

        messagebox.showinfo(
            "Order Placed",
            f"{buyer_name} has successfully ordered {product['name']} for ${product['price']}!"
        )



    def exit_app(self):
        """Exit the application."""
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.quit()
    


# Main Execution
if __name__ == "__main__":
    root = tk.Tk()
    app = EFarming(root)
    #app.order_product("eric tuyi")
    root.mainloop()
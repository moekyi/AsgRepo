import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

    # Create the main application window
root = tk.Tk()
root.title("Travel System ")
    #root.geometry("800x300")
    # Create a Treeview widget
tree = ttk.Treeview(root, columns=("Zone", "Station"), show="headings")
tree.heading("Zone", text="Zone")
tree.heading("Station", text="Station")
tree.column('Station', width=600)

    # Add sample data
tree.insert("", "end", values=("1", "Yaen, Jaund, Tallan, Rede, Ninia, Bylyn, Frestin, Lomil, Soth"))
tree.insert("", "end", values=("2", "Agralle, Docia, Stonyam, Obelyn, talith, Garion, Sylas, Riclya, Quthief,Wicyt, Riladia, Oloadus"))
tree.insert("", "end", values=("3", "Zord, Perinad, Keivia,Erean, Brunad, Marend, Ryall, Pryn, Edenif, Holmer, Vertwall, Runil, Elyot, Adohad"))
    #tree.pack(pady=10,padx=10)
tree.grid(row=0, columnspan=3, padx=10, pady=10, sticky="nsew")
    # Create a LabelFrame to contain the system
sys_frame = ttk.LabelFrame(root, text="System Operations", padding="10")
    #sys_frame.pack(side='left',padx=20, pady=20)
sys_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
    # Create a LabelFrame for Voucher Operations
voucher_frame = ttk.LabelFrame(root, text="Generate Voucher", padding="10")
    #voucher_frame.pack(side='center',padx=20, pady=20)
voucher_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

    # Define button callback functions
def add_item():
        # messagebox.showinfo("Add", "Add button clicked")
    add_window = tk.Toplevel(root)  # Create a new popup window
    add_window.title("Add New Zone and Station")
    add_window.geometry("300x200")

    # Labels and Entry Fields
    tk.Label(add_window, text="Zone:").grid(row=0, column=0, padx=10, pady=5)
    entry_zone = tk.Entry(add_window, width=20)
    entry_zone.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(add_window, text="Station").grid(row=1, column=0, padx=10, pady=5)
    entry_station = tk.Entry(add_window, width=20)
    entry_station.grid(row=1, column=1, padx=10, pady=5)

        
    def add_newitem():
        zone = entry_zone.get()
        station = entry_station.get()
     
    # Check if both fields are filled
        if not zone or not station:
            result_label.config(text="All fields must be filled!.", foreground="red")
            return
        
    # Iterate through existing items to check for duplicates
        for item in tree.get_children():
            item_values = tree.item(item, 'values')
            if  item_values[0] == zone or item_values[1] == station:
                messagebox.showerror("Error", "This zone is already exists!")
                return   

    # Insert the new item
        tree.insert("", "end", values=(zone, station))
        add_window.destroy()  # Close the popup window after adding
    
    # Creating a result label to display messages
    result_label = ttk.Label(add_window, text="", foreground="black")
    result_label.grid(row=2, columnspan=2, pady=10)
    
    # Add button inside popup window
    btn_submit = tk.Button(add_window, text="Add", command=add_newitem)
    btn_submit.grid(row=3, columnspan=2, pady=10, padx=10)
    
    def clear_action():
        entry_zone.delete(0, tk.END)  # Clear zone entry
        entry_station.delete(0, tk.END)  # Clear station entry
        result_label.config(text="", foreground="black")  # Clear result message
    
 
        # reset  button inside popup window
    btn_cancel = tk.Button(add_window, text="Reset", command=clear_action)
    btn_cancel.grid(row=3, column=1, pady=10, padx=10)



def edit_item():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select an item to edit!")
        return
    # Get selected item data
    item = selected_item[0]
    values = tree.item(item, "values")
    # Create an edit popup window
    edit_window = tk.Toplevel(root)  # Create a new popup window
    edit_window.title("Add New Zone and Station")
    edit_window.geometry("300x200")

    # Labels and Entry Fields
    tk.Label(edit_window, text="Zone:").grid(row=0, column=0, padx=10, pady=5)
    entry_zone = tk.Entry(edit_window, width=20)
    entry_zone.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(edit_window, text="Station").grid(row=1, column=0, padx=10, pady=5)
    entry_station = tk.Entry(edit_window, width=20)
    entry_station.grid(row=1, column=1, padx=10, pady=5)  
    def edit_newitem():
         pass
    # Add button inside edit-popup window
    def cancel_newitem():
       pass 
    
    btn_edit = tk.Button(edit_window, text="Save", command=edit_newitem)
    btn_edit.grid(row=2, column=0, pady=10, padx=10)
    btn_cancel = tk.Button(edit_window, text="Cancel", command=cancel_newitem)
    btn_edit.grid(row=2, column=1, pady=10, padx=10)


def delete_item():
        messagebox.showinfo("Delete", "Delete button clicked")
    # Define the voucher button callback function
def voucher_operation():
    root.destroy()
    import Gen_voucher
    Gen_voucher.generate_voucher()
    
    # Create buttons and add them to the LabelFrame
add_button = ttk.Button(sys_frame, text="Add", command=add_item)
edit_button = ttk.Button(sys_frame, text="Edit", command=edit_item)
delete_button = ttk.Button(sys_frame, text="Delete", command=delete_item)


    # Pack buttons into the LabelFrame
    # add_button.pack(side="left", padx=5, pady=5)
    # edit_button.pack(side="left", padx=5, pady=5)
    # delete_button.pack(side="left", padx=5, pady=5)
add_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
edit_button.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
delete_button.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
    # Create the Voucher button and add it to the Voucher Operations LabelFrame
voucher_button = ttk.Button(voucher_frame, text="Voucher", command=voucher_operation)
    #voucher_button.pack(side="left",padx=5, pady=5)
voucher_button.grid(row=1, column=3, padx=10, pady=10, sticky="nsew")
root.mainloop()
    # return

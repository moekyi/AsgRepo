import tkinter as tk
from tkinter import messagebox
import datetime

# Stations Data
stations = {
    1: ["Central Zone", "Yaen, Jaund, Tallan, Rede, Ninia, Bylyn, Frestin, Lomil, Soth"],
    2: ["Midtown Zone", "Agralle, Docia, Stonyam, Obelyn, talith, Garion, Sylas, Riclya, Quthief,Wicyt, Riladia, Oloadus"],
    3: ["Downtown Zone", "Zord, Perinad, Keivia,Erean, Brunad, Marend, Ryall, Pryn, Edenif, Holmer, Vertwall, Runil, Elyot, Adohad"],
}

# Fare Constants (in cents)
FARES = {
    "Adult": 2105,    # 21.05 EUR
    "Child": 1410,    # 14.10 EUR
    "Senior": 1025,   # 10.25 EUR
    "Student": 1750,  # 17.50 EUR
}
# Create main application window
app = tk.Tk()
app.title("Travel System")
#app.configure()
app.geometry("400x350")

# Variables
start_zone_var = tk.StringVar()
dest_zone_var = tk.StringVar()
adults_var = tk.StringVar(value="0")
children_var = tk.StringVar(value="0")
seniors_var = tk.StringVar(value="0")
students_var = tk.StringVar(value="0")

# Set default selection for zones
start_zone_var.set(list(stations.keys())[0])  # Select first station by default
dest_zone_var.set(list(stations.keys())[0])   # Select first station by default

def generate_voucher():
    try:
        start_zone = int(start_zone_var.get())
        dest_zone = int(dest_zone_var.get())

        if start_zone not in stations or dest_zone not in stations:
            messagebox.showerror("Error", "Invalid zone selection.")
            return

        num_travellers = {
            "Adult": int(adults_var.get()),
            "Child": int(children_var.get()),
            "Senior": int(seniors_var.get()),
            "Student": int(students_var.get()),
        }

        zones_travelled = abs(dest_zone - start_zone) + 1
        total_travellers = sum(num_travellers.values())
        total_fares = 0  
        for category in num_travellers:  
            total_fares += num_travellers[category] * FARES[category] 

        
        voucher_text = f"Travel Voucher\n===============\n"
        voucher_text += f"Date and Time     : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        voucher_text += f"Boarding Zone     : {start_zone} ({stations[start_zone][0]})\n"
        voucher_text += f"Destination Zone  : {dest_zone} ({stations[dest_zone][0]})\n\n"
        #voucher_text += f"Zones Travelled   : {zones_travelled}\n\n"

        voucher_text += "Traveller Details:\n"
        for category, count in num_travellers.items():
            fare =  FARES[category] / 100  # Convert cents to Euros
            fare_1 = count * fare
            voucher_text += f"{category}s   : {count} (Fare: €{fare:.2f}) : €{fare_1:.2f}\n"
           
        voucher_text += "\nSummary:\n"
        voucher_text += f"Zones Travelled    : {zones_travelled}\n"
        voucher_text += f"Total Travellers   : {total_travellers}\n"
        voucher_text += f"Total Fare         : €{(total_fares *zones_travelled) / 100:.2f}\n"  # Convert cents to Euros
        voucher_text += "\n \n Thank You... See you again!"
        show_voucher_window(voucher_text)

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numbers only.")

def show_voucher_window(voucher_text):
    result_window = tk.Toplevel()
    result_window.title("Travel Voucher")
    #result_window.configure(bg=BG_COLOR)

    tk.Label(result_window, text=voucher_text, justify="left",  font=("Courier", 10)).grid(row=0, column=0, padx=10, pady=10)
    tk.Button(result_window, text="Close", command=result_window.destroy).grid(row=1, column=0, padx=10, pady=10)
    
def reset_voucher():
    start_zone_var.set(list(stations.keys())[0])  # Reset to default boarding zone
    dest_zone_var.set(list(stations.keys())[0])   # Reset to default destination zone
    adults_var.set("0")       # Reset to 0
    children_var.set("0")     # Reset to 0
    seniors_var.set("0")      # Reset to 0
    students_var.set("0")     # Reset to 0

# UI Elements using Grid Layout
tk.Label(app, text="Boarding Zone:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
tk.OptionMenu(app, start_zone_var, *stations.keys()).grid(row=0, column=1, padx=10, pady=5)

tk.Label(app, text="Destination Zone:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
tk.OptionMenu(app, dest_zone_var, *stations.keys()).grid(row=1, column=1, padx=10, pady=5)

tk.Label(app, text="Number of Adults:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
tk.Entry(app, textvariable=adults_var).grid(row=2, column=1, padx=10, pady=5)

tk.Label(app, text="Number of Children:").grid(row=3, column=0, sticky="w", padx=10, pady=5)
tk.Entry(app, textvariable=children_var).grid(row=3, column=1, padx=10, pady=5)

tk.Label(app, text="Number of Seniors:").grid(row=4, column=0, sticky="w", padx=10, pady=5)
tk.Entry(app, textvariable=seniors_var).grid(row=4, column=1, padx=10, pady=5)

tk.Label(app, text="Number of Students:").grid(row=5, column=0, sticky="w", padx=10, pady=5)
tk.Entry(app, textvariable=students_var).grid(row=5, column=1, padx=10, pady=5)

tk.Button(app, text="Generate Voucher", command=generate_voucher).grid(row=6, column=0,  pady=10)
tk.Button(app, text="Reset",  font=("Arial", 10), command=reset_voucher).grid(row=6, column=1,  pady=10)
def close_voucher():
    app.quit()  # Stop the Tkinter event loop
    app.destroy()  # Destroy the window and free resources
    exit()
tk.Button(app, text="Close",  font=("Arial", 10), command=close_voucher).grid(row=6, column=2,  pady=10)

app.mainloop()

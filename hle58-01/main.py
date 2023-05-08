
# TODO 1 => Cancel button must reset all states to 0
# TODO 4 => Use or remove entirely the buy button and transition
# TODO 6 => Improve design in tkinter
# TODO 7 => Create a README documentation for usage and exmplanation what P,T do and represent
# TODO 8 => Complete the modeling for IceTea and Lemonade
# TODO 9 => Add overvlow Y scroll bacause log messages hide
# TODO 10 => Add missing token 2

import tkinter as tk
from helpers import checkCoinLimitHandler
from petri_models.water.water_model import water_transitions
from petri_models.water.water_gui import water_gui

# Global Variables
currentValue = 0
    
# def buy():
#     canvas.itemconfigure(token_TK_P3, state="hidden")
#     canvas.itemconfigure(token_TK_P5, state="normal")

#     buy_product_button.config(state="disabled")
#     cancel_product_button.config(state="disabled")

#     messageHandler("Το προϊόν έχει διανεμηθεί, η συναλλαγή ολοκληρώθηκε!")

# def cancel():
#     canvas.itemconfigure(token_TK_P3, state="hidden")
#     canvas.itemconfigure(token_TK_P4, state="normal")

#     buy_product_button.config(state="disabled")
#     cancel_product_button.config(state="disabled")

#     messageHandler("Συναλλαγή ακυρώθηκε!")

def run_petri_net():
    global currentValue

    productsList = {
        "water": {
            "name": "water",
            "value": 50
        },
        "icetea": {
            "name": "icetea",
            "value": 210
        },    
        "lemonade": {
            "name": "lemonade",
            "value": 160
        }
    }

    tokens = {
        "token_TK_P1": token_TK_P1,
        "token_TK_P3": token_TK_P3,
        "token_TK_P4": token_TK_P4,
        "token_TK_P5": token_TK_P5,
        "token_TK_P6": token_TK_P6,
        "token_TK_P7": token_TK_P7,
        "token_TK_P8": token_TK_P8,
        "token_TK_P9": token_TK_P9,
        "token_TK_P10": token_TK_P10,
    }

    currentValue += int(coin_var.get())
    checkCoinLimitHandler(drink_var, productsList, currentValue, insert_coin_button)
    
    if drink_var.get() == productsList["water"]["name"]:
        water_transitions(
            tokens, drink_var, coin_var, currentValue,
            productsList, canvas, water_radio_button,
            icetea_radio_button, lemonade_radio_btn,
            insert_coin_button, select_product_button,
            messages_text, coin_small_10, coin_small_20,
            coin_small_50, coin_one, coin_two, token_TK_P1,
            token_TK_P3, token_TK_P4, token_TK_P5, token_TK_P6,
            token_TK_P7, token_TK_P8, token_TK_P10,
        )

if __name__ == "__main__":
    root = tk.Tk()
    canvas = tk.Canvas(root, width=1000, height=300)
    canvas.pack()
    root.title("Petri net Αυτόματος Πωλητής")
    
    # if drink_var.get() == "null":
    water_gui(canvas, tk)

    # # create GUI token for water
    token_TK_P1 = canvas.create_oval(40, 85, 50, 95, fill='black', state="normal") 
    token_TK_P3 = canvas.create_oval(220, 85, 230, 95, fill="black", state="hidden")
    token_TK_P4 = canvas.create_oval(400, 35, 410, 45, fill="black", state="hidden")
    token_TK_P5 = canvas.create_oval(400, 135, 410, 145, fill="black", state="hidden")
    token_TK_P6 = canvas.create_oval(580, 35, 590, 45, fill="black", state="hidden")
    token_TK_P7 = canvas.create_oval(580, 135, 590, 145, fill="black", state="hidden")
    token_TK_P8 = canvas.create_oval(760, 85, 770, 95, fill="black", state="hidden")
    token_TK_P9 = canvas.create_oval(940, 85, 950, 95, fill="black", state="hidden")
    token_TK_P10 = canvas.create_oval(850, 170, 860, 180, fill="black", state="hidden")
    
    # Scrollbar
    messages_text = tk.Text(root)
    messages_text.pack(side=tk.LEFT, fill=tk.Y)

    scrollbar = tk.Scrollbar(root, command=messages_text.yview)
    messages_text.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Create a drink menu with radio buttons
    drink_var = tk.StringVar(value="null")
    drink_menu = tk.Frame(root)
    tk.Label(drink_menu, text="Menu").pack(anchor="c")
    tk.Label(drink_menu, text="Επιλέξτε ποτό:").pack(anchor="c")
    water_radio_button = tk.Radiobutton(drink_menu, text="Νερό (€0.50)", variable=drink_var, state="normal", value="water")
    icetea_radio_button = tk.Radiobutton(drink_menu, text="Παγωμένο τσάι (€2.10)", variable=drink_var, state="disabled", value="icetea")
    lemonade_radio_btn = tk.Radiobutton(drink_menu, text="Λεμονάδα (€1.60)", variable=drink_var, state="disabled", value="lemonade")
    water_radio_button.pack(anchor="c")
    icetea_radio_button.pack(anchor="c")
    lemonade_radio_btn.pack(anchor="c")
    drink_menu.pack(anchor="c")

    # Create a coin menu with radio buttons
    coin_var = tk.StringVar(value=0)
    coin_menu = tk.Frame(root)
    tk.Label(coin_menu, text="Εισάγετε νόμισμα:").pack(anchor="w")
    coin_small_10 = tk.Radiobutton(coin_menu, text="€0.10", variable=coin_var, state="disabled", value=10)
    coin_small_20 = tk.Radiobutton(coin_menu, text="€0.20", variable=coin_var, state="disabled", value=20)
    coin_small_50 = tk.Radiobutton(coin_menu, text="€0.50", variable=coin_var, state="disabled", value=50)
    coin_one = tk.Radiobutton(coin_menu, text="€1", variable=coin_var, state="disabled", value=100)
    coin_two = tk.Radiobutton(coin_menu, text="€2", variable=coin_var, state="disabled", value=200)
    coin_small_10.pack(anchor="c")
    coin_small_20.pack(anchor="c")
    coin_small_50.pack(anchor="c")
    coin_one.pack(anchor="c")
    coin_two.pack(anchor="c")
    coin_menu.pack(anchor="c")

    # create action buttons
    select_product_button = tk.Button(root, text="Επιλέξτε προϊόν", state="normal", command=run_petri_net)
    insert_coin_button = tk.Button(root, text="Εισάγετε κέρμα", state="disabled", command=run_petri_net)
    # buy_product_button = tk.Button(root, text="Αγορά", state="disabled", command=buy)
    # cancel_product_button = tk.Button(root, text="Ακύρωση", state="disabled", command=cancel)
    select_product_button.pack()
    insert_coin_button.pack()
    # buy_product_button.pack()
    # cancel_product_button.pack()

    root.mainloop()

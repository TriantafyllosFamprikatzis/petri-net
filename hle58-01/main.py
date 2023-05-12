
# TODO 1 => Cancel button must reset all states to 0
# TODO 6 => Improve design in tkinter
# TODO 7 => Create a README documentation for usage and exmplanation what P,T do and represent
# TODO 8 => Complete the modeling for IceTea and Lemonade

import tkinter as tk
from helpers import checkCoinLimitHandler, resetHandler
from petri_models.water.water_model import water_transitions
from petri_models.water.water_gui import water_gui

# Global Variables
currentValue = 0

waterTransitions = {
    "canRunTransition0": True,
    "prevTransition0": False,
    "prevTransition1": False,
    "prevTransition2": False,
    "prevTransition3": False,
    "prevTransition4": False,
    "prevTransition5": False,
    "prevTransition6": False,
    "prevTransition7": False,
    "prevTransition8": False,
    "prevTransition9": False,
    "prevTransition10": False
}

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

def run_petri_net():
    global currentValue

    currentValue += int(coin_var.get())

    # Dictionaries of tkinter objects
    coins = {
        "coin_small_10": coin_small_10,
        "coin_small_20": coin_small_20,
        "coin_small_50": coin_small_50,
        "coin_one": coin_one,
        "coin_two": coin_two,
    }

    buttons = {
        "water_radio_button": water_radio_button,
        "icetea_radio_button": icetea_radio_button,
        "lemonade_radio_btn": lemonade_radio_btn,
        "insert_coin_button": insert_coin_button,
        "select_product_button": select_product_button,
    }

    data = {
        "drink_var": drink_var,
        "coin_var": coin_var,
        "currentValue": currentValue,
        "productsList": productsList,
        "canvas": canvas,
        "messages_text": messages_text,
    }
    
    checkCoinLimitHandler(drink_var, productsList, currentValue, insert_coin_button)

    
    if drink_var.get() == productsList["water"]["name"]:
        water_transitions(tokens, waterTransitions, buttons, coins, **data)

if __name__ == "__main__":
    root = tk.Tk()
    canvas = tk.Canvas(root, width=1000, height=300)
    canvas.pack()
    root.title("Petri net Αυτόματος Πωλητής")
    
    # if drink_var.get() == "null":
    water_gui(canvas, tk)

    # # create GUI token
    token_TK_P1 = canvas.create_oval(40, 85, 50, 95, fill='black', state="normal") 
    token_TK_P2 = canvas.create_oval(220, 85, 230, 95, fill="black", state="hidden")
    token_TK_P3 = canvas.create_oval(400, 35, 410, 45, fill="black", state="hidden")
    token_TK_P4 = canvas.create_oval(400, 135, 410, 145, fill="black", state="hidden")
    token_TK_P5 = canvas.create_oval(580, 35, 590, 45, fill="black", state="hidden")
    token_TK_P6 = canvas.create_oval(580, 135, 590, 145, fill="black", state="hidden")
    token_TK_P7 = canvas.create_oval(760, 85, 770, 95, fill="black", state="hidden")

    tokens = {
        "token_TK_P1": token_TK_P1,
        "token_TK_P2": token_TK_P2,
        "token_TK_P3": token_TK_P3,
        "token_TK_P4": token_TK_P4,
        "token_TK_P5": token_TK_P5,
        "token_TK_P6": token_TK_P6,
        "token_TK_P7": token_TK_P7,
    }
    
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
    # reset_vending_machine_button = tk.Button(root, text="Ακύρωση", state="normal", command=lambda: resetHandler(canvas, drink_var, coin_var, waterTransitions, tokens))
    select_product_button.pack()
    insert_coin_button.pack()
    # reset_vending_machine_button.pack()

    root.mainloop()

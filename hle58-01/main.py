
# TODO 6 => Improve design in tkinter
# TODO 7 => Create a README documentation for usage and exmplanation what P,T do and represent
# TODO 8 => Complete the modeling for IceTea and Lemonade

import tkinter as tk
from helpers import checkCoinLimitHandler, resetHandler
from petri_models.water.water_model import water_transitions
from petri_models.water.water1_gui import water_gui

"""from petri_models.iced_tea.iced_tea_model import iced_tea_transitions
from petri_models.iced_tea.iced_tea_gui import iced_tea_gui
"""

"""from petri_models.lemonade.lemonade_model import lemonade_transitions
from petri_models.lemonade.lemonade_gui import lemonade_gui
"""

# Define Variables
currentValue = 0

tokens = {}

coins = {}

buttons = {}

data = {}

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
"""iced_teaTransitions = {
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
    "prevTransition10": False,
    "prevTransition11": False,
    "prevTransition12": False,
    "prevTransition13": False,
    "prevTransition14": False,
    "prevTransition15": False,
    "prevTransition16": False
"""

"""lemonadeTransitions = {
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
    "prevTransition10": False,
    "prevTransition11": False,
    "prevTransition12": False,
    "prevTransition13": False,
    "prevTransition14": False,
    "prevTransition15": False,
    "prevTransition16": False,
    "prevTransition17": False,
    "prevTransition18": False,
    "prevTransition19": False,
    "prevTransition20": False,
    "prevTransition21": False,
    "prevTransition22": False,
    "prevTransition23": False,
    "prevTransition24": False,
    "prevTransition25": False,
}
"""

productsList = {
    "water": {
        "name": "water",
        "value": 50
    },
    "icetea": {
        "name": "icetea",
        "value": 70
    },    
    "lemonade": {
        "name": "lemonade",
        "value": 110
    }
}

def run_petri_net():
    global currentValue
    # Increment currentValue by coin_var.get()
    currentValue += int(coin_var.get())

    # Set dictionaries for petrinet
    tokens = {
        "token_TK_P1": token_TK_P1,
        "token_TK_P2": token_TK_P2,
        "token_TK_P3": token_TK_P3,
        "token_TK_P4": token_TK_P4,
        "token_TK_P5": token_TK_P5,
        "token_TK_P6": token_TK_P6,
        "token_TK_P7": token_TK_P7,
        "token_TK_P8": token_TK_P8,
        "token_TK_P9": token_TK_P9,
        "token_TK_P10": token_TK_P10,
        "token_TK_P11": token_TK_P11,
        "token_TK_P12": token_TK_P12,
        "token_TK_P13": token_TK_P13,
    }
        
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
        "lemonade_radio_button": lemonade_radio_button,
        "insert_coin_button": insert_coin_button,
        "select_product_button": select_product_button,
        "reset_button": reset_button,
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

"""if drink_var.get() == productsList["icetea"]["name"]:
        icedtea_transitions(tokens, icedteaTransitions, buttons, coins, **data)
"""

"""if drink_var.get() == productsList["lemonade"]["name"]:
        lemonade_transitions(tokens, lemonadeTransitions, buttons, coins, **data)
"""

def run_reset():
    global currentValue
    currentValue = 0

    # Set dictionaries for reset
    tokens = {
        "token_TK_P1": token_TK_P1,
        "token_TK_P2": token_TK_P2,
        "token_TK_P3": token_TK_P3,
        "token_TK_P4": token_TK_P4,
        "token_TK_P5": token_TK_P5,
        "token_TK_P6": token_TK_P6,
        "token_TK_P7": token_TK_P7,
        "token_TK_P8": token_TK_P8,
        "token_TK_P9": token_TK_P9,
        "token_TK_P10": token_TK_P10,
        "token_TK_P11": token_TK_P11,
        "token_TK_P12": token_TK_P12,
        "token_TK_P13": token_TK_P13,
    }

    buttons = {
        "water_radio_button": water_radio_button,
        "icetea_radio_button": icetea_radio_button,
        "lemonade_radio_button": lemonade_radio_button,
        "insert_coin_button": insert_coin_button,
        "select_product_button": select_product_button,
        "reset_button": reset_button,
    }

    coins = {
        "coin_small_10": coin_small_10,
        "coin_small_20": coin_small_20,
        "coin_small_50": coin_small_50,
        "coin_one": coin_one,
        "coin_two": coin_two,
    }

    data = {
        "coin_var": coin_var,
        "drink_var": drink_var,
        "canvas": canvas,
        "messages_text": messages_text,
    }

    resetHandler(waterTransitions, tokens, buttons, coins, **data)

"""resetHandler(icedteaTransitions, tokens, buttons, coins, **data)
"""

"""resetHandler(lemonadeTransitions, tokens, buttons, coins, **data)
"""

if __name__ == "__main__":
    root = tk.Tk()
    canvas = tk.Canvas(root, width=1000, height=300)
    canvas.pack()
    root.title("Petri net Αυτόματος Πωλητής")
    
    # if drink_var.get() == "null":
    water_gui(canvas, tk)

    """icedtea_gui(canvas, tk)
    """

    """lemonade_gui(canvas, tk)
    """

    # Create GUI token
    token_TK_P1 = canvas.create_oval(15, 10, 45, 40, fill='red', state="normal")
    token_TK_P2 = canvas.create_oval(95, 75, 125, 105, fill="red", state="hidden")
    token_TK_P3 = canvas.create_oval(265,25,295,55, fill="red", state="hidden")
    token_TK_P4 = canvas.create_oval(265, 125, 295, 155, fill="red", state="hidden")
    token_TK_P5 = canvas.create_oval(425,25,455,55, fill="red", state="hidden")
    token_TK_P6 = canvas.create_oval(425,125,455,155, fill="red", state="hidden")
    token_TK_P7 = canvas.create_oval(585, 25, 615, 55, fill="red", state="hidden")
    token_TK_P8 = canvas.create_oval(585, 125, 615, 155, fill="red", state="hidden")
    token_TK_P9 = canvas.create_oval(745, 25, 775, 55, fill="red", state="hidden")
    token_TK_P10 = canvas.create_oval(745, 125, 775, 155, fill="red", state="hidden")
    token_TK_P11 = canvas.create_oval(905, 25, 935, 55, fill="red", state="hidden")
    token_TK_P12 = canvas.create_oval(905, 125, 935, 155, fill="red", state="hidden")
    token_TK_P13 = canvas.create_oval(970,75,1000,105, fill="red", state="hidden")

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
    icetea_radio_button = tk.Radiobutton(drink_menu, text="Παγωμένο τσάι (€0.70)", variable=drink_var, state="disabled", value="icetea")
    lemonade_radio_button = tk.Radiobutton(drink_menu, text="Λεμονάδα (€1.10)", variable=drink_var, state="disabled", value="lemonade")
    water_radio_button.pack(anchor="c")
    icetea_radio_button.pack(anchor="c")
    lemonade_radio_button.pack(anchor="c")
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
    reset_button = tk.Button(root, text="Ακύρωση", state="disabled", command=run_reset)
    select_product_button.pack()
    insert_coin_button.pack()
    reset_button.pack()

    root.mainloop()

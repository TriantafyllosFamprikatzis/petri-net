import tkinter as tk

def place_product():
    """Place the product in the machine."""
    if drink_var.get() == "null":
        return False
    else:
        return True

def insert_coin():
    """Insert a coin into the machine."""
    if coin_var.get() == "null":
        return False
    else:
        return True

def validate_coin():
    """Validate the inserted coin and product with the correct values"""
    if coin_var.get() == "1€" or coin_var.get() == "2€":
        return True
    else:
        return False

# Define the Petri net transitions
def transition1():
    if place_product() and insert_coin():
        return True
    else:
        return False

def transition2():
    if transition1() and validate_coin():
        return True
    else:
        return False
    
def messageHandler(message):
    petri_log_label = tk.Label(root, text=message)
    petri_log_label.pack()

def buy():
    canvas.itemconfigure(token_TK_P3, state="hidden")
    canvas.itemconfigure(token_TK_P5, state="normal")

    buy_product_button.config(state="disabled")
    cancel_product_button.config(state="disabled")

    messageHandler("Το προϊόν έχει διανεμηθεί, η συναλλαγή ολοκληρώθηκε!")

def cancel():
    canvas.itemconfigure(token_TK_P3, state="hidden")
    canvas.itemconfigure(token_TK_P4, state="normal")

    buy_product_button.config(state="disabled")
    cancel_product_button.config(state="disabled")

    messageHandler("Συναλλαγή ακυρώθηκε!")

def run_petri_net():
    if transition1():
        # Use the selected coin value
        coin_value = coin_var.get()

        canvas.itemconfigure(token_TK_P1, state="hidden")
        canvas.itemconfigure(token_TK_P2, state="hidden")

        water_radio_button.config(state="disabled")
        icetea_radio_button.config(state="disabled")
        lemonade_radio_btn.config(state="disabled")

        coin_one.config(state="disabled")
        coin_two.config(state="disabled")

        select_product_button.config(state="disabled")

        messageHandler(f"Το προϊόν προστέθηκε και εισαγωγή νομίσματος: {coin_value}")

    if transition2():
        canvas.itemconfigure(token_TK_P3, state="normal")
                
        buy_product_button.config(state="active")
        cancel_product_button.config(state="active")

        messageHandler("Το κέρμα έχει επικυρωθεί")

if __name__ == "__main__":
    root = tk.Tk()
    canvas = tk.Canvas(root, width=1024, height=500)
    canvas.pack()
    root.title("Petri net Αυτόματος Πωλητής")  

    # create GUI places and texts
    place_product_TK = canvas.create_oval(50, 50, 150, 150, outline='black', width=2)
    place_coin_TK = canvas.create_oval(250, 250, 350, 350, outline='black', width=2)
    place_validate_coin_TK = canvas.create_oval(450, 50, 550, 150, outline='black', width=2)
    place_cancel_TK = canvas.create_oval(650, 250, 750, 350, outline='black', width=2)
    place_complete_TK = canvas.create_oval(850, 50, 950, 150, outline='black', width=2)

    text1 = canvas.create_text(100, 100, text='P1')
    text2 = canvas.create_text(300, 300, text='P2')
    text4 = canvas.create_text(500, 100, text='P3')
    text6 = canvas.create_text(700, 300, text='P4')
    text7 = canvas.create_text(900, 100, text='P5')

    # create GUI transitions
    insert_coin_TK = canvas.create_rectangle(280, 50, 320, 150, outline='black', width=2)
    text3 = canvas.create_text(300, 100, text='T1')
    dispense_product_place_TK = canvas.create_rectangle(680, 50, 720, 150, outline='black', width=2)
    text5 = canvas.create_text(700, 100, text='T2')
    
    # create GUI token
    token_TK_P1 = canvas.create_oval(75, 75, 125, 125, fill='black', state="normal")
    token_TK_P2 = canvas.create_oval(275, 275, 325, 325, fill='black', state="normal")
    token_TK_P3 = canvas.create_oval(475, 75, 525, 125, fill="black", state="hidden")
    token_TK_P4 = canvas.create_oval(675, 275, 725, 325, fill="black", state="hidden")
    token_TK_P5 = canvas.create_oval(875, 75, 925, 125, fill="black", state="hidden")
    
    # create GUI arrows
    # arrow_coords = (150, 100, 100, 150)
    line1 = canvas.create_line(150, 100, 280, 100, arrow=tk.LAST)
    line2 = canvas.create_line(320, 100, 450, 100, arrow=tk.LAST)
    line3 = canvas.create_line(550, 100, 680, 100, arrow=tk.LAST)
    line4 = canvas.create_line(720, 100, 850, 100, arrow=tk.LAST)
    line5 = canvas.create_line(300, 250, 300, 150, arrow=tk.LAST)
    line6 = canvas.create_line(700, 150, 700, 250, arrow=tk.LAST)
    # canvas.create_line(*arrow_coords, arrow='last', width=2)

    # Create a drink menu with radio buttons
    drink_var = tk.StringVar(value="null")
    drink_menu = tk.Frame(root)
    tk.Label(drink_menu, text="Menu").pack(anchor="c")
    tk.Label(drink_menu, text="Επιλέξτε ποτό:").pack(anchor="c")
    water_radio_button = tk.Radiobutton(drink_menu, text="Νερό (€1)", variable=drink_var, state="normal", value="water")
    icetea_radio_button = tk.Radiobutton(drink_menu, text="Παγωμένο τσάι (€2)", variable=drink_var, state="normal", value="icetea")
    lemonade_radio_btn = tk.Radiobutton(drink_menu, text="Λεμονάδα (€1.5)", variable=drink_var, state="normal", value="lemonade")
    water_radio_button.pack(anchor="c")
    icetea_radio_button.pack(anchor="c")
    lemonade_radio_btn.pack(anchor="c")
    drink_menu.pack(anchor="c")

    # Create a coin menu with radio buttons
    coin_var = tk.StringVar(value="null")
    coin_menu = tk.Frame(root)
    tk.Label(coin_menu, text="Εισάγετε νόμισμα:").pack(anchor="w")
    coin_one = tk.Radiobutton(coin_menu, text="€1", variable=coin_var, state="normal", value="1€")
    coin_two = tk.Radiobutton(coin_menu, text="€2", variable=coin_var, state="normal", value="2€")
    coin_one.pack(anchor="c")
    coin_two.pack(anchor="c")
    coin_menu.pack(anchor="c")

    # create action buttons
    select_product_button = tk.Button(root, text="Επιλέξτε προϊόν", command=run_petri_net)
    buy_product_button = tk.Button(root, text="Αγορά", state="disabled", command=buy)
    cancel_product_button = tk.Button(root, text="Ακύρωση", state="disabled", command=cancel)
    select_product_button.pack()
    buy_product_button.pack()
    cancel_product_button.pack()

    root.mainloop()
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
    canvas = tk.Canvas(root, width=1350, height=600)
    canvas.pack()
    root.title("Petri net Αυτόματος Πωλητής")  

    # create GUI places and texts
    place_product_TK = canvas.create_oval(30, 70, 90, 130, outline='black', width=2)
    place_coin_TK = canvas.create_oval(155, 230, 215, 290, outline='black', width=2)
    place_validate_coin_TK = canvas.create_oval(470, 70, 530, 130, outline='black', width=2)
    place_cancel_TK = canvas.create_oval(1135, 220, 1195, 280, outline='black', width=2)
    place_complete_TK = canvas.create_oval(1260, 70, 1320, 130, outline='black', width=2)

    text1 = canvas.create_text(60, 100, text='P1')
    text2 = canvas.create_text(185, 260, text='P2')
    text4 = canvas.create_text(500, 100, text='P3')
    text6 = canvas.create_text(1165, 250, text='P4')
    text7 = canvas.create_text(1290, 100, text='P5')

    # create GUI transitions
    insert_coin_TK = canvas.create_rectangle(175, 60, 195, 140, outline='black', width=2)
    text3 = canvas.create_text(185, 100, text='T1')
    dispense_product_place_TK = canvas.create_rectangle(1155, 60, 1175, 140, outline='black', width=2)
    text5 = canvas.create_text(1165, 100, text='T2')
    
    # create GUI token
    token_TK_P1 = canvas.create_oval(50, 90, 70, 110, fill='black', state="normal")
    token_TK_P2 = canvas.create_oval(175, 250, 195, 270, fill='black', state="normal")
    token_TK_P3 = canvas.create_oval(490, 90, 510, 110, fill="black", state="hidden")
    token_TK_P4 = canvas.create_oval(1155, 240, 1175, 260, fill="black", state="hidden")
    token_TK_P5 = canvas.create_oval(1280, 90, 1300, 110, fill="black", state="hidden")

    # create GUI arrows
    line1 = canvas.create_line(95, 100, 170, 100, arrow=tk.LAST)
    line2 = canvas.create_line(200, 100, 275, 100, arrow=tk.LAST)
    line3 = canvas.create_line(1075, 100, 1150, 100, arrow=tk.LAST)
    line4 = canvas.create_line(1180, 100, 1255, 100, arrow=tk.LAST)
    line5 = canvas.create_line(185, 225, 185, 145, arrow=tk.LAST)
    line6 = canvas.create_line(1165, 145, 1165, 215, arrow=tk.LAST)

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
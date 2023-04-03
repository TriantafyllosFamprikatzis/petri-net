import tkinter as tk

def place_product():
    """Place the product in the machine."""
    return True

def insert_coin():
    """Insert a coin into the machine."""
    return True

def validate_coin():
    """Validate the inserted coin."""
    return True

def dispense_product():
    """Dispense the product."""
    return True

def return_change():
    """Return any change to the customer."""
    return True

# Define the Petri net transitions
def transition1():
    if place_product() and insert_coin():
        return True
    else:
        return False

def transition2():
    if validate_coin() and dispense_product():
        return True
    else:
        return False

def transition3():
    if return_change():
        return True
    else:
        return False

if __name__ == "__main__":
    root = tk.Tk()
    canvas = tk.Canvas(root, width=1024, height=500)
    canvas.pack()
    root.title("Petri net Αυτόματος Πωλητής")  

    # create GUI places 
    place_product_TK = canvas.create_oval(50, 50, 150, 150, outline='black', width=2)
    text1 = canvas.create_text(100, 100, text='P1')
    place_storage_TK = canvas.create_oval(250, 250, 350, 350, outline='black', width=2)
    text2 = canvas.create_text(300, 300, text='P2')
    insert_coin_TK = canvas.create_rectangle(280, 50, 320, 150, outline='black', width=2)
    text3 = canvas.create_text(300, 100, text='T1')
    validate_coin_place_TK = canvas.create_oval(450, 50, 550, 150, outline='black', width=2)
    text4 = canvas.create_text(500, 100, text='P3')
    dispense_product_place_TK = canvas.create_rectangle(680, 50, 720, 150, outline='black', width=2)
    text5 = canvas.create_text(700, 100, text='T2')
    abort_TK = return_change_TK = canvas.create_oval(650, 250, 750, 350, outline='black', width=2)
    text6 = canvas.create_text(700, 300, text='P4')
    return_change_TK = canvas.create_oval(850, 50, 950, 150, outline='black', width=2)
    text7 = canvas.create_text(900, 100, text='P5')

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

    # Define the Petri net places
    place_product_place = False
    insert_coin_place = False
    validate_coin_place = False
    dispense_product_place = False

    def messageHandler(message):
        petri_log_label = tk.Label(root, text=message)
        petri_log_label.pack()

    def run_petri_net():
        place_product_place = True
        select_product_button.destroy()

        if place_product_place:
            # Create a coin menu with radio buttons
            coin_var = tk.StringVar(value="€")
            coin_menu = tk.Frame(root)
            tk.Label(coin_menu, text="Εισάγετε νόμισμα:").pack(anchor="w")
            tk.Radiobutton(coin_menu, text="€1", variable=coin_var, value="1euro").pack(anchor="c")
            tk.Radiobutton(coin_menu, text="€2", variable=coin_var, value="2euro").pack(anchor="c")
            coin_menu.pack(anchor="c")

            insert_coin_place = True
            place_product_place = False

        if insert_coin_place:
            # Use the selected coin value
            coin_value = coin_var.get()
            if transition1():
                canvas.itemconfigure(token_TK_P1, state="hidden")
                canvas.itemconfigure(token_TK_P2, state="hidden")
                messageHandler(f"Το προϊόν προστέθηκε και εισαγωγή νομίσματος: {coin_value}")
                validate_coin_place = True
                insert_coin_place = False

        if place_product_place:
            insert_coin_place = True
            place_product_place = False

        if insert_coin_place:
            if transition1():
                canvas.itemconfigure(token_TK_P1, state="hidden")
                canvas.itemconfigure(token_TK_P2, state="hidden")
                messageHandler("Το προϊόν προστέθηκε και έγινε εισαγωγή νομίσματος.")
                validate_coin_place = True
                insert_coin_place = False   

        if validate_coin_place:
            if transition2():
                canvas.itemconfigure(token_TK_P3, state="normal")
                messageHandler("Το κέρμα έχει επικυρωθεί")
                dispense_product_place = True
                validate_coin_place = False

        if dispense_product_place:            
            if transition3():
                def buy():
                    canvas.itemconfigure(token_TK_P3, state="hidden")
                    canvas.itemconfigure(token_TK_P5, state="normal")

                    messageHandler("Το προϊόν έχει διανεμηθεί, η συναλλαγή ολοκληρώθηκε!")

                    buy_product_button.destroy()
                    cancel_product_button.destroy()

                def cancel():
                    canvas.itemconfigure(token_TK_P3, state="hidden")
                    canvas.itemconfigure(token_TK_P4, state="normal")

                    messageHandler("Συναλλαγή ακυρώθηκε!")
                    
                    buy_product_button.destroy()
                    cancel_product_button.destroy()

                buy_product_button = tk.Button(root, text="Αγορά", command=buy)
                buy_product_button.pack()
                cancel_product_button = tk.Button(root, text="Ακύρωση", command=cancel)
                cancel_product_button.pack()

    # Create a drink menu with radio buttons
    drink_var = tk.StringVar(value="water1euro")
    drink_menu = tk.Frame(root)
    tk.Label(drink_menu, text="Menu").pack(anchor="c")
    tk.Label(drink_menu, text="Επιλέξτε ποτό:").pack(anchor="c")
    tk.Radiobutton(drink_menu, text="Νερό (€1)", variable=drink_var, value="water1euro").pack(anchor="c")
    tk.Radiobutton(drink_menu, text="Παγωμένο τσάι (€2)", variable=drink_var, value="icetea2euro").pack(anchor="c")
    tk.Radiobutton(drink_menu, text="Λεμονάδα (€1.5)", variable=drink_var, value="lemonade1.5euro").pack(anchor="c")
    drink_menu.pack(anchor="c")

    select_product_button = tk.Button(root, text="Επιλέξτε προϊόν", command=run_petri_net)
    select_product_button.pack()

    root.mainloop()
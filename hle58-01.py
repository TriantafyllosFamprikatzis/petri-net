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
    insert_coin_TK = canvas.create_oval(250, 50, 350, 150, outline='black', width=2)
    validate_coin_place_TK = canvas.create_oval(450, 50, 550, 150, outline='black', width=2)
    dispense_product_place_TK = canvas.create_oval(650, 50, 750, 150, outline='black', width=2)
    return_change_TK = canvas.create_oval(850, 50, 950, 150, outline='black', width=2)

    # create GUI token
    token_TK = canvas.create_oval(75, 75, 125, 125, fill='black')

    # create GUI arrows
    # arrow_coords = (150, 100, 100, 150)
    # canvas.create_line(*arrow_coords, arrow='last', width=2)

    # Define the Petri net places
    place_product_place = False
    insert_coin_place = False
    validate_coin_place = False
    dispense_product_place = False
    return_change_place = False

    def move_token(x1, y1, x2, y2, message):
        token_x1, token_y1, token_x2, token_y2 = canvas.coords(token_TK)

        # Calculate the center of the  oval
        place_x = (x1 + x2) / 2
        place_y = (y1 + y2) / 2

        # Move the token to the center of the insert_coin_TK oval
        canvas.move(token_TK, place_x - (token_x1 + token_x2) / 2, place_y - (token_y1 + token_y2) / 2)

        # Display message transition
        petri_log_label = tk.Label(root, text=message)
        petri_log_label.pack()

    def run_petri_net():
        place_product_place = True

        if place_product_place:
            root.after(1000, lambda:move_token(250, 50, 350, 150, "Το προϊόν προστέθηκε"))
            insert_coin_place = True
            place_product_place = False

        if insert_coin_place:
            if transition1():
                root.after(2000, lambda:move_token(450, 50, 550, 150, "Έγινε εισαγωγή νομίσματος."))
                validate_coin_place = True
                insert_coin_place = False   

        if validate_coin_place:
            if transition2():
                root.after(3000, lambda:move_token(650, 50, 750, 150, "Το κέρμα έχει επικυρωθεί, το προϊόν έχει διανεμηθεί."))
                dispense_product_place = True
                validate_coin_place = False

        if dispense_product_place:
            if transition3():
                root.after(4000, lambda:move_token(850, 50, 950, 150, "Έδωσε ρέστα."))
                return_change_place = True
                dispense_product_place = False

        if return_change_place:
            completion_message = tk.Label(root, text="Συναλλαγή ολοκληρώθηκε!")
            root.after(5000, completion_message.pack)

    select_product_label = tk.Label(root, text="Επιλέξτε προϊόν")
    select_product_label.pack()
    select_product_button = tk.Button(root, text="submit", command=run_petri_net)
    select_product_button.pack()

    root.mainloop()
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
    place_product_TK = canvas.create_oval(30, 75, 60, 105, outline='black', width=2)#p1
    place_coin_TK = canvas.create_oval(120, 160, 150, 190, outline='black', width=2)#p2
    place_validate_coin_TK = canvas.create_oval(210, 75, 240, 105, outline='black', width=2)#p3
    place_10cent_TK = canvas.create_oval(390,25,420,55, outline='black', width=2) #p4
    place_20cent_TK = canvas.create_oval(390,125,420,155, outline='black', width=2) #p5 
    place_30cent_TK = canvas.create_oval(570,25,600,55, outline='black', width=2) #p6
    place_40cent_TK = canvas.create_oval(570,125,600,155, outline='black', width=2) #p7
    place_50cent_TK = canvas.create_oval(750, 75, 780, 105, outline='black', width=2) #p8
    place_complete_TK = canvas.create_oval(930, 75, 960, 105, outline='black', width=2)#p9
    place_cancel_TK = canvas.create_oval(840, 160, 870, 190, outline='black', width=2)#p10
    
    textp1 = canvas.create_text(45, 90, text='P1')
    textp2 = canvas.create_text(135, 175, text='P2')
    textp3 = canvas.create_text(225, 90, text='P3')
    textp4 = canvas.create_text(405, 40, text='P4')
    textp5 = canvas.create_text(405, 140, text='P5')
    textp6 = canvas.create_text(585, 40, text='P6')
    textp7 = canvas.create_text(585, 140, text='P7')
    textp8 = canvas.create_text(765, 90, text='P8')
    textp9 = canvas.create_text(945, 90, text='P9')
    textp10 = canvas.create_text(855, 175, text='P10')

    # create GUI transitions
    insert_coin_TK = canvas.create_rectangle(120, 80, 150, 100, outline='black', width=2)
    textcoin = canvas.create_text(135, 90, text='T0')
    #
    T1_TK = canvas.create_rectangle(480, 165, 510, 185, outline='black', width=2)#+50
    textt1 = canvas.create_text(495, 175, text='T1')
    T2_TK = canvas.create_rectangle(300, 30, 330, 50, outline='black', width=2)#+10
    textt2 = canvas.create_text(315, 40, text='T2')
    T3_TK = canvas.create_rectangle(300, 130, 330, 150, outline='black', width=2)#+20
    textt3 = canvas.create_text(315, 140, text='T3')
    T4_TK = canvas.create_rectangle(390, 80, 420, 100, outline='black', width=2)#+10+10
    textt4 = canvas.create_text(405, 90, text='T4')
    T5_TK = canvas.create_rectangle(480, 30, 510, 50, outline='black', width=2)#+10+20
    textt5 = canvas.create_text(495, 40, text='T5')
    T6_TK = canvas.create_rectangle(480, 80, 510, 100, outline='black', width=2)#+20+10
    textt6 = canvas.create_text(495, 90, text='T6')
    T7_TK = canvas.create_rectangle(480, 130, 510, 150, outline='black', width=2)#+20+20
    textt7 = canvas.create_text(495, 140, text='T7')
    T8_TK = canvas.create_rectangle(570, 80, 600, 100, outline='black', width=2)#30+10
    textt8 = canvas.create_text(585, 90, text='T8')
    T9_TK = canvas.create_rectangle(660, 30, 690, 50, outline='black', width=2)#30+20
    textt9 = canvas.create_text(675, 40, text='T9')
    T10_TK = canvas.create_rectangle(660, 130, 690, 150, outline='black', width=2)#40+10
    textt10 = canvas.create_text(675, 140, text='T10')
    dispense_product_place_TK = canvas.create_rectangle(840, 80, 870, 100, outline='black', width=2)
    textproduct = canvas.create_text(855, 90, text='T11')
    
    
    # create GUI token
    token_TK_P1 = canvas.create_oval(40, 85, 50, 95, fill='black', state="normal") 
    token_TK_P2 = canvas.create_oval(130, 170, 140, 180, fill='black', state="normal")
    token_TK_P3 = canvas.create_oval(220, 85, 230, 95, fill="black", state="hidden")
    token_TK_P4 = canvas.create_oval(400, 35, 410, 45, fill="black", state="hidden")
    token_TK_P5 = canvas.create_oval(400, 135, 410, 145, fill="black", state="hidden")
    token_TK_P6 = canvas.create_oval(580, 35, 590, 45, fill="black", state="hidden")
    token_TK_P7 = canvas.create_oval(580, 135, 590, 145, fill="black", state="hidden")
    token_TK_P8 = canvas.create_oval(760, 85, 770, 95, fill="black", state="hidden")
    token_TK_P9 = canvas.create_oval(940, 85, 950, 95, fill="black", state="hidden")
    token_TK_P10 = canvas.create_oval(850, 170, 860, 180, fill="black", state="hidden")


    # create GUI arrows
    
    line = canvas.create_line(70, 90, 110, 90, arrow=tk.LAST)#p1 - t0
    line = canvas.create_line(160, 90, 200, 90, arrow=tk.LAST) #t0 - p3
    line = canvas.create_line(135, 150, 135, 110, arrow=tk.LAST) #p2 - t0
    line = canvas.create_line(225, 115, 225, 175, 470, 175, arrow=tk.LAST)#p3-t1 830
    line = canvas.create_line(520, 175, 830, 175, arrow=tk.LAST)#t1-p10 830
    line = canvas.create_line(250, 80, 290, 50, arrow=tk.LAST)#p3-t2
    line = canvas.create_line(250, 100, 290, 130, arrow=tk.LAST)#p3-t3
    line = canvas.create_line(340, 40, 380, 40, arrow=tk.LAST)#t2-p4
    line = canvas.create_line(430, 40, 470, 40, arrow=tk.LAST)#p4-t5
    line = canvas.create_line(340, 140, 380, 140, arrow=tk.LAST)#t3-p5
    line = canvas.create_line(405, 60, 405, 75, arrow=tk.LAST)#p4-t4
    line = canvas.create_line(405, 105, 405, 120, arrow=tk.LAST)#t4-p5
    line = canvas.create_line(520, 40, 560, 40, arrow=tk.LAST)#t5-p6
    line = canvas.create_line(430, 140, 470, 140, arrow=tk.LAST)#p5-t7
    line = canvas.create_line(520, 140, 560, 140, arrow=tk.LAST)#t7-p7
    line = canvas.create_line(585, 60, 585, 75, arrow=tk.LAST)#p6-t8
    line = canvas.create_line(585, 105, 585, 120, arrow=tk.LAST)#t8-p7
    line = canvas.create_line(430, 130, 470, 100, arrow=tk.LAST)#p5-t6
    line = canvas.create_line(515, 90, 555, 60, arrow=tk.LAST)#t6-p6
    line = canvas.create_line(610, 40, 650, 40, arrow=tk.LAST)#p6-t9 
    line = canvas.create_line(610, 140, 650, 140, arrow=tk.LAST)#p7-t10
    line = canvas.create_line(700, 40, 740, 70, arrow=tk.LAST)#t9-p8
    line = canvas.create_line(700, 140, 740, 110, arrow=tk.LAST)#t10-p8
    line = canvas.create_line(790, 90, 830, 90, arrow=tk.LAST)#p8-t11
    line = canvas.create_line(880, 90, 920, 90, arrow=tk.LAST)#t11-p9
    line = canvas.create_line(855, 110, 855, 150, arrow=tk.LAST)#t11-p10
    
    # create GUI token
    token_TK_P1 = canvas.create_oval(40, 85, 50, 95, fill='black', state="normal") 
    token_TK_P2 = canvas.create_oval(130, 170, 140, 180, fill='black', state="normal")
    token_TK_P3 = canvas.create_oval(220, 85, 230, 95, fill="black", state="hidden")
    token_TK_P4 = canvas.create_oval(400, 35, 410, 45, fill="black", state="hidden")
    token_TK_P5 = canvas.create_oval(400, 135, 410, 145, fill="black", state="hidden")
    token_TK_P6 = canvas.create_oval(580, 35, 590, 45, fill="black", state="hidden")
    token_TK_P7 = canvas.create_oval(580, 135, 590, 145, fill="black", state="hidden")
    token_TK_P8 = canvas.create_oval(760, 85, 770, 95, fill="black", state="hidden")
    token_TK_P9 = canvas.create_oval(940, 85, 950, 95, fill="black", state="hidden")
    token_TK_P10 = canvas.create_oval(850, 170, 860, 180, fill="black", state="hidden")


    # create GUI arrows
    
    line = canvas.create_line(70, 90, 110, 90, arrow=tk.LAST)#p1 - t1
    line = canvas.create_line(160, 90, 200, 90, arrow=tk.LAST) #t1 - p3
    line = canvas.create_line(135, 150, 135, 110, arrow=tk.LAST) #p2 - t1
    line = canvas.create_line(250, 80, 290, 50, arrow=tk.LAST)#p3-t2
    line = canvas.create_line(250, 100, 290, 130, arrow=tk.LAST)#p3-t3
    line = canvas.create_line(340, 40, 380, 40, arrow=tk.LAST)#t2-p4
    line = canvas.create_line(430, 40, 470, 40, arrow=tk.LAST)#p4-t5
    line = canvas.create_line(340, 140, 380, 140, arrow=tk.LAST)#t3-p5
    line = canvas.create_line(405, 60, 405, 75, arrow=tk.LAST)#p4-t4
    line = canvas.create_line(405, 105, 405, 120, arrow=tk.LAST)#t4-p5
    line = canvas.create_line(520, 40, 560, 40, arrow=tk.LAST)#t5-p6
    line = canvas.create_line(430, 140, 470, 140, arrow=tk.LAST)#p5-t7
    line = canvas.create_line(520, 140, 560, 140, arrow=tk.LAST)#t7-p7
    line = canvas.create_line(585, 60, 585, 75, arrow=tk.LAST)#p6-t8
    line = canvas.create_line(585, 105, 585, 120, arrow=tk.LAST)#t8-p7
    line = canvas.create_line(430, 130, 470, 100, arrow=tk.LAST)#p5-t6
    line = canvas.create_line(515, 90, 555, 60, arrow=tk.LAST)#t6-p6
    line = canvas.create_line(610, 40, 650, 40, arrow=tk.LAST)#p6-t9 
    line = canvas.create_line(610, 140, 650, 140, arrow=tk.LAST)#p7-t10
    line = canvas.create_line(700, 40, 740, 70, arrow=tk.LAST)#t9-p8
    line = canvas.create_line(700, 140, 740, 110, arrow=tk.LAST)#t10-p8
    line = canvas.create_line(790, 90, 830, 90, arrow=tk.LAST)#p8-t11
    line = canvas.create_line(880, 90, 920, 90, arrow=tk.LAST)#t11-p9
    line = canvas.create_line(855, 110, 855, 150, arrow=tk.LAST)#t11-p10
    
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

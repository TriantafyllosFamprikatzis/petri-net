
from helpers import (
    messageHandler, calculateChangeHandler,
    numberConverterHandler, tokenHandler,
    remainingValueHandler
)

# Global variables
transitionStatus = str()
canRunTransition0 = True
prevTransition0 = False
prevTransition1 = False
prevTransition2 = False
prevTransition3 = False
prevTransition4 = False
prevTransition5 = False
prevTransition6 = False
prevTransition7 = False
prevTransition8 = False
prevTransition9 = False
prevTransition10 = False

# Define the Petri net transitions for water
def water_transitions(
        tokens, drink_var, coin_var, currentValue,
        productsList, canvas, messages_text, water_radio_button,
        icetea_radio_button, lemonade_radio_btn,
        insert_coin_button, select_product_button,
        coin_small_10, coin_small_20,
        coin_small_50, coin_one, coin_two, token_TK_P1,
        token_TK_P2, token_TK_P3, token_TK_P4, token_TK_P5,
        token_TK_P6, token_TK_P7,
):
    global canRunTransition0

    def transition0():
        global prevTransition0, transitionStatus, canRunTransition0
        if drink_var.get() != "null" and canRunTransition0:
            prevTransition0 = True
            transitionStatus = "T0"
            return True
        else:
            return False

    def transition1():
        global prevTransition0, prevTransition1, transitionStatus
        if currentValue >= productsList["water"]["value"] and prevTransition0:
            prevTransition0 = False
            prevTransition1 = True
            transitionStatus = "T1"
            return True
        else:
            return False
        
    def transition2():
        global prevTransition0, prevTransition2, transitionStatus
        if currentValue == 10 and prevTransition0:
            prevTransition0 = False
            prevTransition2 = True
            transitionStatus = "T2"
            return True
        else:
            return False

    def transition3():
        global prevTransition0, prevTransition3, prevTransition2, transitionStatus
        if currentValue == 20 and prevTransition0 and not prevTransition2:
            prevTransition0 = False
            prevTransition3 = True
            transitionStatus = "T3"
            return True
        else:
            return False

    def transition4():
        global prevTransition2, prevTransition4, transitionStatus
        if currentValue == 20 and prevTransition2:
            prevTransition2 = False
            prevTransition4 = True
            transitionStatus = "T4"
            return True
        else:
            return False
        
    def transition5():
        global prevTransition2, prevTransition5, transitionStatus
        if currentValue == 30 and prevTransition2:
            prevTransition2 = False
            prevTransition5 = True
            transitionStatus = "T5"
            return True
        else:
            return False

    def transition6():
        global prevTransition3, prevTransition6, prevTransition4, transitionStatus
        if currentValue == 30 and (prevTransition3 or prevTransition4):
            prevTransition3 = False
            prevTransition4 = False
            prevTransition6 = True
            transitionStatus = "T6"
            return True
        else:
            return False

    def transition7():
        global prevTransition3, prevTransition4, prevTransition7, transitionStatus
        if currentValue == 40 and (prevTransition3 or prevTransition4):
            prevTransition3 = False
            prevTransition4 = False
            prevTransition7 = True
            transitionStatus = "T7"
            return True
        else:
            return False

    def transition8():
        global prevTransition5, prevTransition6, prevTransition8, transitionStatus
        if currentValue == 40 and (prevTransition5 or prevTransition6):
            prevTransition5 = False
            prevTransition6 = False
            prevTransition8 = True
            transitionStatus = "T8"
            return True
        else:
            return False

    def transition9():
        global prevTransition5, prevTransition6, prevTransition9, transitionStatus, prevTransition5, prevTransition2
        if currentValue >= productsList["water"]["value"] and (prevTransition5 or prevTransition6 or prevTransition2 or prevTransition5):
            prevTransition5 = False
            prevTransition6 = False
            prevTransition9 = True
            transitionStatus = "T9"
            return True
        else:
            return False

    def transition10():
        global prevTransition7, prevTransition8, prevTransition10, transitionStatus, prevTransition7, prevTransition3
        if currentValue >= productsList["water"]["value"] and (prevTransition7 or prevTransition8 or prevTransition7, prevTransition3):
            prevTransition7 = False
            prevTransition8 = False
            prevTransition10 = True
            transitionStatus = "T10"
            return True
        else:
            return False

    if transition0() and canRunTransition0:
        canvas.itemconfigure(token_TK_P1, state="hidden")
        canvas.itemconfigure(token_TK_P2, state="normal")

        water_radio_button.config(state="disabled")
        icetea_radio_button.config(state="disabled")
        lemonade_radio_btn.config(state="disabled")

        coin_small_10.config(state="normal")
        coin_small_20.config(state="normal")
        coin_small_50.config(state="normal")
        coin_one.config(state="normal")
        coin_two.config(state="normal")

        insert_coin_button.config(state="normal")
        select_product_button.config(state="disabled")

        messageHandler(messages_text, f"{transitionStatus}: Το προϊόν προστέθηκε!")
        canRunTransition0 = False

    if transition1() or transition9() or transition10():
        canvas.itemconfigure(token_TK_P7, state="normal")
        tokenHandler(canvas, "token_TK_P7", tokens)

        # buy_product_button.config(state="active")
        # cancel_product_button.config(state="active")
        changeAmount = calculateChangeHandler(drink_var, productsList, currentValue)
        insertedAmount = numberConverterHandler(coin_var.get())
        messageHandler(messages_text, f"{transitionStatus}: Εισαγωγή νομίσματος: €{insertedAmount}, το ποσό συμπληρώθηκε, έδωσε ρέστα €{changeAmount}")
        messageHandler(messages_text, "Το προϊόν έχει κατανεμηθεί!")

    if transition2():
        canvas.itemconfigure(token_TK_P3, state="normal")
        tokenHandler(canvas,"token_TK_P3", tokens)
        remainingAmount = remainingValueHandler(drink_var, productsList, currentValue)
        insertedAmount = numberConverterHandler(coin_var.get())
        messageHandler(messages_text, f"{transitionStatus}: Εισαγωγή νομίσματος: €{insertedAmount}, υπολείπονται ακόμη €{remainingAmount}")
    
    if transition3() or transition4():
        canvas.itemconfigure(token_TK_P4, state="normal")
        tokenHandler(canvas,"token_TK_P4", tokens)
        remainingAmount = remainingValueHandler(drink_var, productsList, currentValue)
        insertedAmount = numberConverterHandler(coin_var.get())
        messageHandler(messages_text, f"{transitionStatus}: Εισαγωγή νομίσματος: €{insertedAmount}, υπολείπονται ακόμη €{remainingAmount}")

    if transition5() or transition6(): 
        canvas.itemconfigure(token_TK_P5, state="normal")
        tokenHandler(canvas,"token_TK_P5", tokens)
        remainingAmount = remainingValueHandler(drink_var, productsList, currentValue)
        insertedAmount = numberConverterHandler(coin_var.get())
        messageHandler(messages_text, f"{transitionStatus}: Εισαγωγή νομίσματος: €{insertedAmount}, υπολείπονται ακόμη €{remainingAmount}")

    if transition7() or transition8():
        canvas.itemconfigure(token_TK_P6, state="normal")
        tokenHandler(canvas,"token_TK_P6", tokens)
        remainingAmount = remainingValueHandler(drink_var, productsList, currentValue)
        insertedAmount = numberConverterHandler(coin_var.get())
        messageHandler(messages_text,f"{transitionStatus}: Εισαγωγή νομίσματος: €{insertedAmount}, υπολείπονται ακόμη €{remainingAmount}")
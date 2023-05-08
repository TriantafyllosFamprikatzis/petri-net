
from helpers import (
    messageHandler, calculateChangeHandler,
    numberConverterHandler, tokenHandler,
    remainingValueHandler
)

# Global variable
canRunTransition0 = True

def water_transitions(
        tokens, drink_var, coin_var, currentValue,
        productsList, canvas, water_radio_button,
        icetea_radio_button, lemonade_radio_btn,
        insert_coin_button, select_product_button,
        messages_text, coin_small_10, coin_small_20,
        coin_small_50, coin_one, coin_two, token_TK_P1,
        token_TK_P2, token_TK_P3, token_TK_P4, token_TK_P5,
        token_TK_P6, token_TK_P7,
):
    global canRunTransition0
    # Define the Petri net transitions for water
    def transition0():
        if drink_var.get() != "null":
            return True
        else:
            return False

    def transition1():
        if currentValue >= productsList["water"]["value"]:
            return True
        else:
            return False
        
    def transition2():
        if currentValue == 10:
            return True
        else:
            return False

    def transition3():
        if currentValue == 20:
            return True
        else:
            return False

    def transition4():
        if currentValue == 20:
            return True
        else:
            return False

    def transition5():
        if currentValue == 30:
            return True
        else:
            return False

    def transition6():
        if currentValue == 30:
            return True
        else:
            return False

    def transition7():
        if currentValue == 40:
            return True
        else:
            return False

    def transition8():
        if currentValue == 40:
            return True
        else:
            return False

    def transition9():
        if currentValue >= productsList["water"]["value"]:
            return True
        else:
            return False

    def transition10():
        if currentValue >= productsList["water"]["value"]:
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

        messageHandler(messages_text, "Το προϊόν προστέθηκε!")
        canRunTransition0 = False

    if transition1() or transition9() or transition10():
        canvas.itemconfigure(token_TK_P7, state="normal")
        tokenHandler(canvas, "token_TK_P7", tokens)

        # buy_product_button.config(state="active")
        # cancel_product_button.config(state="active")
        changeAmount = calculateChangeHandler(drink_var, productsList, currentValue)
        insertedAmount = numberConverterHandler(coin_var.get())
        messageHandler(messages_text, f"Εισαγωγή νομίσματος: €{insertedAmount}, το ποσό συμπληρώθηκε, έδωσε ρέστα €{changeAmount}")
        messageHandler(messages_text, "Το προϊόν έχει κατανεμηθεί!")

    if transition2():
        canvas.itemconfigure(token_TK_P3, state="normal")
        tokenHandler(canvas,"token_TK_P3", tokens)
        remainingAmount = remainingValueHandler(drink_var, productsList, currentValue)
        insertedAmount = numberConverterHandler(coin_var.get())
        messageHandler(messages_text, f"Εισαγωγή νομίσματος: €{insertedAmount}, υπολείπονται ακόμη €{remainingAmount}")
    
    if transition3() or transition4():
        canvas.itemconfigure(token_TK_P4, state="normal")
        tokenHandler(canvas,"token_TK_P4", tokens)
        remainingAmount = remainingValueHandler(drink_var, productsList, currentValue)
        insertedAmount = numberConverterHandler(coin_var.get())
        messageHandler(messages_text, f"Εισαγωγή νομίσματος: €{insertedAmount}, υπολείπονται ακόμη €{remainingAmount}")

    if transition5() or transition6(): 
        canvas.itemconfigure(token_TK_P5, state="normal")
        tokenHandler(canvas,"token_TK_P5", tokens)
        remainingAmount = remainingValueHandler(drink_var, productsList, currentValue)
        insertedAmount = numberConverterHandler(coin_var.get())
        messageHandler(messages_text, f"Εισαγωγή νομίσματος: €{insertedAmount}, υπολείπονται ακόμη €{remainingAmount}")

    if transition7() or transition8():
        canvas.itemconfigure(token_TK_P6, state="normal")
        tokenHandler(canvas,"token_TK_P6", tokens)
        remainingAmount = remainingValueHandler(drink_var, productsList, currentValue)
        insertedAmount = numberConverterHandler(coin_var.get())
        messageHandler(messages_text,f"Εισαγωγή νομίσματος: €{insertedAmount}, υπολείπονται ακόμη €{remainingAmount}")
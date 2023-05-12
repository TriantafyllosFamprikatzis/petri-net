
from helpers import (
    messageHandler, calculateChangeHandler,
    numberConverterHandler, tokenHandler,
    remainingValueHandler
)

# Global variables
transitionStatus = str()

# Define the Petri net transitions for water
def water_transitions(
        tokens, waterTransitions, buttons, coins, drink_var, coin_var, currentValue,
        productsList, canvas, messages_text,
):
    global transitionStatus

    def transition0():
        global transitionStatus
        if drink_var.get() != "null" and waterTransitions["canRunTransition0"]:
            waterTransitions["prevTransition0"] = True
            transitionStatus = "T0"
            return True
        else:
            return False
        
    def transition1():
        global transitionStatus
        if currentValue >= productsList["water"]["value"] and waterTransitions["prevTransition0"]:
            waterTransitions["prevTransition0"] = False
            waterTransitions["prevTransition1"] = True
            transitionStatus = "T1"
            return True
        else:
            return False
        
    def transition2():
        global transitionStatus
        if currentValue == 10 and waterTransitions["prevTransition0"]:
            waterTransitions["prevTransition0"] = False
            waterTransitions["prevTransition2"] = True
            transitionStatus = "T2"
            return True
        else:
            return False

    def transition3():
        global transitionStatus
        if currentValue == 20 and waterTransitions["prevTransition0"] and not waterTransitions["prevTransition2"]:
            waterTransitions["prevTransition0"] = False
            waterTransitions["prevTransition3"] = True
            transitionStatus = "T3"
            return True
        else:
            return False

    def transition4():
        global transitionStatus
        if currentValue == 20 and waterTransitions["prevTransition2"]:
            waterTransitions["prevTransition2"] = False
            waterTransitions["prevTransition4"] = True
            transitionStatus = "T4"
            return True
        else:
            return False
        
    def transition5():
        global transitionStatus
        if currentValue == 30 and waterTransitions["prevTransition2"]:
            waterTransitions["prevTransition2"] = False
            waterTransitions["prevTransition5"] = True
            transitionStatus = "T5"
            return True
        else:
            return False

    def transition6():
        global transitionStatus
        if currentValue == 30 and (waterTransitions["prevTransition3"] or waterTransitions["prevTransition4"]):
            waterTransitions["prevTransition3"] = False
            waterTransitions["prevTransition4"] = False
            waterTransitions["prevTransition6"] = True
            transitionStatus = "T6"
            return True
        else:
            return False

    def transition7():
        global transitionStatus
        if currentValue == 40 and (waterTransitions["prevTransition3"] or waterTransitions["prevTransition4"]):
            waterTransitions["prevTransition3"] = False
            waterTransitions["prevTransition4"] = False
            waterTransitions["prevTransition7"] = True
            transitionStatus = "T7"
            return True
        else:
            return False

    def transition8():
        global transitionStatus
        if currentValue == 40 and (waterTransitions["prevTransition5"] or waterTransitions["prevTransition6"]):
            waterTransitions["prevTransition5"] = False
            waterTransitions["prevTransition6"] = False
            waterTransitions["prevTransition8"] = True
            transitionStatus = "T8"
            return True
        else:
            return False

    def transition9():
        global transitionStatus
        if currentValue >= productsList["water"]["value"] and (waterTransitions["prevTransition5"] or waterTransitions["prevTransition6"] or waterTransitions["prevTransition2"] or waterTransitions["prevTransition5"]):
            waterTransitions["prevTransition5"] = False
            waterTransitions["prevTransition6"] = False
            waterTransitions["prevTransition9"] = True
            transitionStatus = "T9"
            return True
        else:
            return False

    def transition10():
        global transitionStatus
        if currentValue >= productsList["water"]["value"] and (waterTransitions["prevTransition7"] or waterTransitions["prevTransition8"] or waterTransitions["prevTransition7"], waterTransitions["prevTransition3"]):
            waterTransitions["prevTransition7"] = False
            waterTransitions["prevTransition8"] = False
            waterTransitions["prevTransition10"] = True
            transitionStatus = "T10"
            return True
        else:
            return False

    if transition0() and waterTransitions["canRunTransition0"]:
        canvas.itemconfigure(tokens["token_TK_P1"], state="hidden")
        canvas.itemconfigure(tokens["token_TK_P2"], state="normal")

        buttons["water_radio_button"].config(state="disabled")
        buttons["icetea_radio_button"].config(state="disabled")
        buttons["lemonade_radio_btn"].config(state="disabled")

        coins["coin_small_10"].config(state="normal")
        coins["coin_small_20"].config(state="normal")
        coins["coin_small_50"].config(state="normal")
        coins["coin_one"].config(state="normal")
        coins["coin_two"].config(state="normal")

        buttons["insert_coin_button"].config(state="normal")
        buttons["select_product_button"].config(state="disabled")

        messageHandler(messages_text, f"{transitionStatus}: Το προϊόν προστέθηκε!")
        waterTransitions["canRunTransition0"] = False
    # else if not water:
    #     buttons["water_radio_button"].config(state="normal")
    #     buttons["icetea_radio_button"].config(state="normal")
    #     buttons["lemonade_radio_btn"].config(state="normal")

    #     coins["coin_small_10"].config(state="disabled")
    #     coins["coin_small_20"].config(state="disabled")
    #     coins["coin_small_50"].config(state="disabled")
    #     coins["coin_one"].config(state="disabled")
    #     coins["coin_two"].config(state="disabled")

    #     buttons["insert_coin_button"].config(state="disabled")
    #     buttons["select_product_button"].config(state="normal")


    if transition1() or transition9() or transition10():
        canvas.itemconfigure(tokens["token_TK_P7"], state="normal")
        tokenHandler(canvas, "token_TK_P7", tokens)
        changeAmount = calculateChangeHandler(drink_var, productsList, currentValue)
        insertedAmount = numberConverterHandler(coin_var.get())
        messageHandler(messages_text, f"{transitionStatus}: Εισαγωγή νομίσματος: €{insertedAmount}, το ποσό συμπληρώθηκε, έδωσε ρέστα €{changeAmount}")
        messageHandler(messages_text, "Το προϊόν έχει κατανεμηθεί!")

    if transition2():
        canvas.itemconfigure(tokens["token_TK_P3"], state="normal")
        tokenHandler(canvas, "token_TK_P3", tokens)
        remainingAmount = remainingValueHandler(drink_var, productsList, currentValue)
        insertedAmount = numberConverterHandler(coin_var.get())
        messageHandler(messages_text, f"{transitionStatus}: Εισαγωγή νομίσματος: €{insertedAmount}, υπολείπονται ακόμη €{remainingAmount}")
    
    if transition3() or transition4():
        canvas.itemconfigure(tokens["token_TK_P4"], state="normal")
        tokenHandler(canvas, "token_TK_P4", tokens)
        remainingAmount = remainingValueHandler(drink_var, productsList, currentValue)
        insertedAmount = numberConverterHandler(coin_var.get())
        messageHandler(messages_text, f"{transitionStatus}: Εισαγωγή νομίσματος: €{insertedAmount}, υπολείπονται ακόμη €{remainingAmount}")

    if transition5() or transition6(): 
        canvas.itemconfigure(tokens["token_TK_P5"], state="normal")
        tokenHandler(canvas, "token_TK_P5", tokens)
        remainingAmount = remainingValueHandler(drink_var, productsList, currentValue)
        insertedAmount = numberConverterHandler(coin_var.get())
        messageHandler(messages_text, f"{transitionStatus}: Εισαγωγή νομίσματος: €{insertedAmount}, υπολείπονται ακόμη €{remainingAmount}")

    if transition7() or transition8():
        canvas.itemconfigure(tokens["token_TK_P6"], state="normal")
        tokenHandler(canvas, "token_TK_P6", tokens)
        remainingAmount = remainingValueHandler(drink_var, productsList, currentValue)
        insertedAmount = numberConverterHandler(coin_var.get())
        messageHandler(messages_text,f"{transitionStatus}: Εισαγωγή νομίσματος: €{insertedAmount}, υπολείπονται ακόμη €{remainingAmount}")
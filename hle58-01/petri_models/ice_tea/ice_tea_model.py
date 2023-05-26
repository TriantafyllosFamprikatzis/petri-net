
from helpers import (
    messageHandler, calculateChangeHandler,
    numberConverterHandler, tokenHandler,
    remainingValueHandler
)

# Global variables
transitionStatus = str()

# Define the Petri net transitions for icetea
def ice_tea_transitions(
        tokens, ice_teaTransitions, buttons, coins, drink_var, coin_var, currentValue,
        productsList, canvas, messages_text,
):
    global transitionStatus

    def transition0():
        global transitionStatus
        if drink_var.get() != "null" and ice_teaTransitions["canRunTransition0"]:
            ice_teaTransitions["prevTransition0"] = True
            transitionStatus = "T0"
            return True
        else:
            return False
        
    def transition1():
        global transitionStatus
        if currentValue >= productsList["ice_tea"]["value"] and ice_teaTransitions["prevTransition0"]:
            ice_teaTransitions["prevTransition0"] = False
            ice_teaTransitions["prevTransition1"] = True
            transitionStatus = "T1"
            return True
        else:
            return False
    
    def transition2():
        global transitionStatus
        if currentValue == 10 and ice_teaTransitions["prevTransition0"]:
            ice_teaTransitions["prevTransition0"] = False
            ice_teaTransitions["prevTransition2"] = True
            transitionStatus = "T2"
            return True
        else:
            return False

    def transition3():
        global transitionStatus
        if currentValue == 20 and ice_teaTransitions["prevTransition0"] and not ice_teaTransitions["prevTransition2"]:
            ice_teaTransitions["prevTransition0"] = False
            ice_teaTransitions["prevTransition3"] = True
            transitionStatus = "T3"
            return True
        else:
            return False

    def transition4():
        global transitionStatus
        if currentValue == 20 and ice_teaTransitions["prevTransition2"]:
            ice_teaTransitions["prevTransition2"] = False
            ice_teaTransitions["prevTransition4"] = True
            transitionStatus = "T4"
            return True
        else:
            return False
        
    def transition5():
        global transitionStatus
        if currentValue == 30 and ice_teaTransitions["prevTransition2"]:
            ice_teaTransitions["prevTransition2"] = False
            ice_teaTransitions["prevTransition5"] = True
            transitionStatus = "T5"
            return True
        else:
            return False

    def transition6():
        global transitionStatus
        if currentValue == 30 and (ice_teaTransitions["prevTransition3"] or ice_teaTransitions["prevTransition4"]):
            ice_teaTransitions["prevTransition3"] = False
            ice_teaTransitions["prevTransition4"] = False
            ice_teaTransitions["prevTransition6"] = True
            transitionStatus = "T6"
            return True
        else:
            return False

    def transition7():
        global transitionStatus
        if currentValue == 40 and (ice_teaTransitions["prevTransition3"] or ice_teaTransitions["prevTransition4"]):
            ice_teaTransitions["prevTransition3"] = False
            ice_teaTransitions["prevTransition4"] = False
            ice_teaTransitions["prevTransition7"] = True
            transitionStatus = "T7"
            return True
        else:
            return False

    def transition8():
        global transitionStatus
        if currentValue == 40 and (ice_teaTransitions["prevTransition5"] or ice_teaTransitions["prevTransition6"]):
            ice_teaTransitions["prevTransition5"] = False
            ice_teaTransitions["prevTransition6"] = False
            ice_teaTransitions["prevTransition8"] = True
            transitionStatus = "T8"
            return True
        else:
            return False

    def transition9():
        global transitionStatus
        if currentValue == 50 and (ice_teaTransitions["prevTransition5"] or ice_teaTransitions["prevTransition6"]):
            ice_teaTransitions["prevTransition5"] = False
            ice_teaTransitions["prevTransition6"] = False
            ice_teaTransitions["prevTransition9"] = True
            transitionStatus = "T9"
            return True
        else:
            return False

    def transition10():
        global transitionStatus
        if currentValue == 50 and (ice_teaTransitions["prevTransition7"] or ice_teaTransitions["prevTransition8"]):
            ice_teaTransitions["prevTransition7"] = False
            ice_teaTransitions["prevTransition8"] = False
            ice_teaTransitions["prevTransition10"] = True
            transitionStatus = "T10"
            return True
        else:
            return False

    def transition11():
        global transitionStatus
        if currentValue == 60 and (ice_teaTransitions["prevTransition7"] or ice_teaTransitions["prevTransition8"]):
            ice_teaTransitions["prevTransition7"] = False
            ice_teaTransitions["prevTransition8"] = False
            ice_teaTransitions["prevTransition11"] = True
            transitionStatus = "T11"
            return True
        else:
            return False

    def transition12():
        global transitionStatus
        if currentValue == 60 and (ice_teaTransitions["prevTransition9"] or ice_teaTransitions["prevTransition10"]):
            ice_teaTransitions["prevTransition9"] = False
            ice_teaTransitions["prevTransition10"] = False
            ice_teaTransitions["prevTransition12"] = True
            transitionStatus = "T12"
            return True
        else:
            return False

    def transition13():
        global transitionStatus
        if currentValue >= productsList["ice_tea"]["value"] and (ice_teaTransitions["prevTransition2"] or ice_teaTransitions["prevTransition3"] or ice_teaTransitions["prevTransition4"] or ice_teaTransitions["prevTransition5"] or ice_teaTransitions["prevTransition6"] or ice_teaTransitions["prevTransition7"] or ice_teaTransitions["prevTransition8"] or ice_teaTransitions["prevTransition9"] or ice_teaTransitions["prevTransition10"] or ice_teaTransitions["prevTransition15"]):
            ice_teaTransitions["prevTransition2"] = False
            ice_teaTransitions["prevTransition3"] = False
            ice_teaTransitions["prevTransition4"] = False
            ice_teaTransitions["prevTransition5"] = False
            ice_teaTransitions["prevTransition6"] = False
            ice_teaTransitions["prevTransition7"] = False
            ice_teaTransitions["prevTransition8"] = False
            ice_teaTransitions["prevTransition9"] = False
            ice_teaTransitions["prevTransition10"] = False
            ice_teaTransitions["prevTransition15"] = False
            ice_teaTransitions["prevTransition13"] = True
            transitionStatus = "T13"
            return True
        else:
            return False

    def transition14():
        global transitionStatus
        if currentValue >= productsList["ice_tea"]["value"] and (ice_teaTransitions["prevTransition11"] or ice_teaTransitions["prevTransition12"]):
            ice_teaTransitions["prevTransition11"] = False
            ice_teaTransitions["prevTransition12"] = False
            ice_teaTransitions["prevTransition14"] = True
            transitionStatus = "T14"
            return True
        else:
            return False
        
    def transition15():
        global transitionStatus
        if currentValue == 50 and ice_teaTransitions["prevTransition0"]:
            ice_teaTransitions["prevTransition0"] = False
            ice_teaTransitions["prevTransition15"] = True
            transitionStatus = "T15"
            return True
        else:
            return False

    def transition16():
        global transitionStatus
        if currentValue == 100 and (ice_teaTransitions["prevTransition0"] or ice_teaTransitions["prevTransition15"]):
            ice_teaTransitions["prevTransition15"] = False
            ice_teaTransitions["prevTransition16"] = True
            transitionStatus = "T16"
            return True
        else:
            return False

    if transition0() and ice_teaTransitions["canRunTransition0"]:
        canvas.itemconfigure(tokens["token_TK_P1"], state="hidden")
        canvas.itemconfigure(tokens["token_TK_P2"], state="normal")

        buttons["water_radio_button"].config(state="disabled")
        buttons["icetea_radio_button"].config(state="disabled")
        buttons["lemonade_radio_button"].config(state="disabled")

        coins["coin_small_10"].config(state="normal")
        coins["coin_small_20"].config(state="normal")
        coins["coin_small_50"].config(state="normal")
        coins["coin_one"].config(state="normal")
        coins["coin_two"].config(state="normal")

        buttons["insert_coin_button"].config(state="normal")
        buttons["select_product_button"].config(state="disabled")
        buttons["reset_button"].config(state="normal")

        messageHandler(messages_text, f"{transitionStatus}: Το προϊόν προστέθηκε!")
        ice_teaTransitions["canRunTransition0"] = False

    if transition1() or transition13() or transition14() or transition16():
        canvas.itemconfigure(tokens["token_TK_P13"], state="normal")
        tokenHandler(canvas, "token_TK_P13", tokens)
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

    if transition9() or transition10() or transition15() :
        canvas.itemconfigure(tokens["token_TK_P7"], state="normal")
        tokenHandler(canvas, "token_TK_P7", tokens)
        remainingAmount = remainingValueHandler(drink_var, productsList, currentValue)
        insertedAmount = numberConverterHandler(coin_var.get())
        messageHandler(messages_text,f"{transitionStatus}: Εισαγωγή νομίσματος: €{insertedAmount}, υπολείπονται ακόμη €{remainingAmount}")

    if transition11() or transition12():
        canvas.itemconfigure(tokens["token_TK_P8"], state="normal")
        tokenHandler(canvas, "token_TK_P8", tokens)
        remainingAmount = remainingValueHandler(drink_var, productsList, currentValue)
        insertedAmount = numberConverterHandler(coin_var.get())
        messageHandler(messages_text,f"{transitionStatus}: Εισαγωγή νομίσματος: €{insertedAmount}, υπολείπονται ακόμη €{remainingAmount}")


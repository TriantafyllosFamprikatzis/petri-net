
from helpers import (
    messageHandler, calculateChangeHandler,
    numberConverterHandler, tokenHandler,
    remainingValueHandler
)

# Global variables
transitionStatus = str()

# Define the Petri net transitions for icetea
def lemonade_transitions(
        tokens, lemonadeTransitions, buttons, coins, drink_var, coin_var, currentValue,
        productsList, canvas, messages_text,
):
    global transitionStatus

    def transition0():
        global transitionStatus
        if drink_var.get() != "null" and lemonadeTransitions["canRunTransition0"]:
            lemonadeTransitions["prevTransition0"] = True
            transitionStatus = "T0"
            return True
        else:
            return False
        
    def transition1():
        global transitionStatus
        if currentValue >= productsList["icetea"]["value"] and lemonadeTransitions["prevTransition0"]:
            lemonadeTransitions["prevTransition0"] = False
            lemonadeTransitions["prevTransition1"] = True
            transitionStatus = "T1"
            return True
        else:
            return False

    def transition21():
        global transitionStatus
        if currentValue == 50 and lemonadeTransitions["prevTransition0"]:
            lemonadeTransitions["prevTransition0"] = False
            lemonadeTransitions["prevTransition21"] = True
            transitionStatus = "T21"
            return True
        else:
            return False

    def transition22():
        global transitionStatus
        if currentValue == 100 and (lemonadeTransitions["prevTransition0"] or lemonadeTransitions["prevTransition9"] or lemonadeTransitions["prevTransition10"] or lemonadeTransitions["prevTransition21"]):
            lemonadeTransitions["prevTransition21"] = False
            lemonadeTransitions["prevTransition9"] = False
            lemonadeTransitions["prevTransition10"] = False
            lemonadeTransitions["prevTransition22"] = True
            transitionStatus = "T22"
            return True
        else:
            return False

    def transition23():
        global transitionStatus
        if currentValue == 100 and lemonadeTransitions["prevTransition0"]:
            lemonadeTransitions["prevTransition0"] = False
            lemonadeTransitions["prevTransition23"] = True
            transitionStatus = "T23"
            return True
        else:
            return False
        
    def transition2():
        global transitionStatus
        if currentValue == 10 and lemonadeTransitions["prevTransition0"]:
            lemonadeTransitions["prevTransition0"] = False
            lemonadeTransitions["prevTransition2"] = True
            transitionStatus = "T2"
            return True
        else:
            return False

    def transition3():
        global transitionStatus
        if currentValue == 20 and lemonadeTransitions["prevTransition0"] and not lemonadeTransitions["prevTransition2"]:
            lemonadeTransitions["prevTransition0"] = False
            lemonadeTransitions["prevTransition3"] = True
            transitionStatus = "T3"
            return True
        else:
            return False

    def transition4():
        global transitionStatus
        if currentValue == 20 and lemonadeTransitions["prevTransition2"]:
            lemonadeTransitions["prevTransition2"] = False
            lemonadeTransitions["prevTransition4"] = True
            transitionStatus = "T4"
            return True
        else:
            return False
        
    def transition5():
        global transitionStatus
        if currentValue == 30 and lemonadeTransitions["prevTransition2"]:
            lemonadeTransitions["prevTransition2"] = False
            lemonadeTransitions["prevTransition5"] = True
            transitionStatus = "T5"
            return True
        else:
            return False

    def transition6():
        global transitionStatus
        if currentValue == 30 and (lemonadeTransitions["prevTransition3"] or lemonadeTransitions["prevTransition4"]):
            lemonadeTransitions["prevTransition3"] = False
            lemonadeTransitions["prevTransition4"] = False
            lemonadeTransitions["prevTransition6"] = True
            transitionStatus = "T6"
            return True
        else:
            return False

    def transition7():
        global transitionStatus
        if currentValue == 40 and (lemonadeTransitions["prevTransition3"] or lemonadeTransitions["prevTransition4"]):
            lemonadeTransitions["prevTransition3"] = False
            lemonadeTransitions["prevTransition4"] = False
            lemonadeTransitions["prevTransition7"] = True
            transitionStatus = "T7"
            return True
        else:
            return False

    def transition8():
        global transitionStatus
        if currentValue == 40 and (lemonadeTransitions["prevTransition5"] or lemonadeTransitions["prevTransition6"]):
            lemonadeTransitions["prevTransition5"] = False
            lemonadeTransitions["prevTransition6"] = False
            lemonadeTransitions["prevTransition8"] = True
            transitionStatus = "T8"
            return True
        else:
            return False

    def transition9():
        global transitionStatus
        if currentValue == 50 and (lemonadeTransitions["prevTransition5"] or lemonadeTransitions["prevTransition6"]):
            lemonadeTransitions["prevTransition5"] = False
            lemonadeTransitions["prevTransition6"] = False
            lemonadeTransitions["prevTransition9"] = True
            transitionStatus = "T9"
            return True
        else:
            return False

    def transition10():
        global transitionStatus
        if currentValue == 50 and (lemonadeTransitions["prevTransition7"] or lemonadeTransitions["prevTransition8"]):
            lemonadeTransitions["prevTransition7"] = False
            lemonadeTransitions["prevTransition8"] = False
            lemonadeTransitions["prevTransition10"] = True
            transitionStatus = "T10"
            return True
        else:
            return False

    def transition11():
        global transitionStatus
        if currentValue == 60 and (lemonadeTransitions["prevTransition7"] or lemonadeTransitions["prevTransition8"]):
            lemonadeTransitions["prevTransition7"] = False
            lemonadeTransitions["prevTransition8"] = False
            lemonadeTransitions["prevTransition11"] = True
            transitionStatus = "T11"
            return True
        else:
            return False

    def transition12():
        global transitionStatus
        if currentValue == 60 and (lemonadeTransitions["prevTransition9"] or lemonadeTransitions["prevTransition10"] or lemonadeTransitions["prevTransition21"]):
            lemonadeTransitions["prevTransition9"] = False
            lemonadeTransitions["prevTransition10"] = False
            lemonadeTransitions["prevTransition12"] = True
            transitionStatus = "T12"
            return True
        else:
            return False

    def transition13():
        global transitionStatus
        if currentValue == 70 and (lemonadeTransitions["prevTransition9"] or lemonadeTransitions["prevTransition10"] or lemonadeTransitions["prevTransition21"]):
            lemonadeTransitions["prevTransition21"] = False
            lemonadeTransitions["prevTransition9"] = False
            lemonadeTransitions["prevTransition10"] = False
            lemonadeTransitions["prevTransition13"] = True
            transitionStatus = "T13"
            return True
        else:
            return False

    def transition14():
        global transitionStatus
        if currentValue == 70 and (lemonadeTransitions["prevTransition11"] or lemonadeTransitions["prevTransition12"]):
            lemonadeTransitions["prevTransition11"] = False
            lemonadeTransitions["prevTransition12"] = False
            lemonadeTransitions["prevTransition14"] = True
            transitionStatus = "T14"
            return True
        else:
            return False

    def transition15():
        global transitionStatus
        if currentValue == 80 and (lemonadeTransitions["prevTransition11"] or lemonadeTransitions["prevTransition12"]):
            lemonadeTransitions["prevTransition11"] = False
            lemonadeTransitions["prevTransition12"] = False
            lemonadeTransitions["prevTransition15"] = True
            transitionStatus = "T15"
            return True
        else:
            return False

    def transition16():
        global transitionStatus
        if currentValue == 80 and (lemonadeTransitions["prevTransition13"] or lemonadeTransitions["prevTransition14"]):
            lemonadeTransitions["prevTransition13"] = False
            lemonadeTransitions["prevTransition14"] = False
            lemonadeTransitions["prevTransition16"] = True
            transitionStatus = "T16"
            return True
        else:
            return False

    def transition17():
        global transitionStatus
        if currentValue == 90 and (lemonadeTransitions["prevTransition13"] or lemonadeTransitions["prevTransition14"]):
            lemonadeTransitions["prevTransition13"] = False
            lemonadeTransitions["prevTransition14"] = False
            lemonadeTransitions["prevTransition17"] = True
            transitionStatus = "T17"
            return True
        else:
            return False

    def transition18():
        global transitionStatus
        if currentValue == 90 and (lemonadeTransitions["prevTransition15"] or lemonadeTransitions["prevTransition16"]):
            lemonadeTransitions["prevTransition15"] = False
            lemonadeTransitions["prevTransition16"] = False
            lemonadeTransitions["prevTransition18"] = True
            transitionStatus = "T18"
            return True
        else:
            return False

    def transition19():
        global transitionStatus
        if currentValue == 100 and (lemonadeTransitions["prevTransition15"] or lemonadeTransitions["prevTransition16"]):
            lemonadeTransitions["prevTransition15"] = False
            lemonadeTransitions["prevTransition16"] = False
            lemonadeTransitions["prevTransition19"] = True
            transitionStatus = "T19"
            return True
        else:
            return False

    def transition20():
        global transitionStatus
        if currentValue == 100 and (lemonadeTransitions["prevTransition17"] or lemonadeTransitions["prevTransition18"]):
            lemonadeTransitions["prevTransition17"] = False
            lemonadeTransitions["prevTransition18"] = False
            lemonadeTransitions["prevTransition20"] = True
            transitionStatus = "T20"
            return True
        else:
            return False

    

    def transition24():
        global transitionStatus
        if currentValue >= productsList["lemonade"]["value"] and (lemonadeTransitions["prevTransition17"] or lemonadeTransitions["prevTransition18"]):
            lemonadeTransitions["prevTransition17"] = False
            lemonadeTransitions["prevTransition18"] = False
            lemonadeTransitions["prevTransition24"] = True
            transitionStatus = "T24"
            return True
        else:
            return False

    def transition25():
        global transitionStatus
        if currentValue >= productsList["lemonade"]["value"] and (lemonadeTransitions["prevTransition19"] or lemonadeTransitions["prevTransition20"] or lemonadeTransitions["prevTransition22"] or lemonadeTransitions["prevTransition23"]):
            lemonadeTransitions["prevTransition19"] = False
            lemonadeTransitions["prevTransition20"] = False
            lemonadeTransitions["prevTransition22"] = False
            lemonadeTransitions["prevTransition23"] = False
            lemonadeTransitions["prevTransition25"] = True
            transitionStatus = "T25"
            return True
        else:
            return False

    if transition0() and lemonadeTransitions["canRunTransition0"]:
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
        lemonadeTransitions["canRunTransition0"] = False

    if transition1() or transition24() or transition25():
        canvas.itemconfigure(tokens["token_TK_P13"], state="normal")
        tokenHandler(canvas, "token_TK_P13", tokens)
        changeAmount = calculateChangeHandler(drink_var, productsList, currentValue)
        insertedAmount = numberConverterHandler(coin_var.get())
        messageHandler(messages_text, f"{transitionStatus}: Εισαγωγή νομίσματος: €{insertedAmount}, το ποσό συμπληρώθηκε, έδωσε ρέστα €{changeAmount}")
        messageHandler(messages_text, "Το προϊόν έχει κατανεμηθεί!")

    if transition19() or transition20() or transition22() or transition23():
        canvas.itemconfigure(tokens["token_TK_P12"], state="normal")
        tokenHandler(canvas, "token_TK_P12", tokens)
        remainingAmount = remainingValueHandler(drink_var, productsList, currentValue)
        insertedAmount = numberConverterHandler(coin_var.get())
        messageHandler(messages_text, f"{transitionStatus}: Εισαγωγή νομίσματος: €{insertedAmount}, υπολείπονται ακόμη €{remainingAmount}")

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

    if transition21() or transition9() or transition10() :
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

    if transition13() or transition14():
        canvas.itemconfigure(tokens["token_TK_P9"], state="normal")
        tokenHandler(canvas, "token_TK_P9", tokens)
        remainingAmount = remainingValueHandler(drink_var, productsList, currentValue)
        insertedAmount = numberConverterHandler(coin_var.get())
        messageHandler(messages_text,f"{transitionStatus}: Εισαγωγή νομίσματος: €{insertedAmount}, υπολείπονται ακόμη €{remainingAmount}")

    if transition15() or transition16():
        canvas.itemconfigure(tokens["token_TK_P10"], state="normal")
        tokenHandler(canvas, "token_TK_P10", tokens)
        remainingAmount = remainingValueHandler(drink_var, productsList, currentValue)
        insertedAmount = numberConverterHandler(coin_var.get())
        messageHandler(messages_text,f"{transitionStatus}: Εισαγωγή νομίσματος: €{insertedAmount}, υπολείπονται ακόμη €{remainingAmount}")

    if transition17() or transition18():
        canvas.itemconfigure(tokens["token_TK_P11"], state="normal")
        tokenHandler(canvas, "token_TK_P11", tokens)
        remainingAmount = remainingValueHandler(drink_var, productsList, currentValue)
        insertedAmount = numberConverterHandler(coin_var.get())
        messageHandler(messages_text,f"{transitionStatus}: Εισαγωγή νομίσματος: €{insertedAmount}, υπολείπονται ακόμη €{remainingAmount}")
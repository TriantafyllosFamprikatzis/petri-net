

def tokenHandler(canvas, activeToken, tokens):
    """Hides all tokens except for the given argument"""
    for token_name, token in tokens.items():
        if token_name != activeToken:
            canvas.itemconfig(token, state="hidden")



def messageHandler(messages_text, message):
    """Shows label massage"""
    from main import tk
    messages_text.insert(tk.END, message + "\n")



def numberConverterHandler(integer):
    """Converts to 2 decimals and returns it as a string"""
    amount = int(integer)
    amount_str = "{:.2f}".format(amount / 100)
    return amount_str



def calculateChangeHandler(drink_var, productsList, currentValue):
    """Returns the change value"""
    result = int()

    if drink_var.get() == productsList["water"]["name"] and currentValue > productsList["water"]["value"]:
        result = currentValue - productsList["water"]["value"]
        return numberConverterHandler(result)
    if drink_var.get() == productsList["icetea"]["name"] and currentValue > productsList["icetea"]["value"]:
        result = currentValue - productsList["icetea"]["value"]                                           
        return numberConverterHandler(result)
    if drink_var.get() == productsList["lemonade"]["name"] and currentValue > productsList["lemonade"]["value"]:
        result = currentValue - productsList["lemonade"]["value"]
        return numberConverterHandler(result)
    else:
        return "0.00"
    


def checkCoinLimitHandler(drink_var, productsList, currentValue, insert_coin_button):
    """
    Checks if the limit of selected item is reached
    and hides the insert coin button
    """
    if drink_var.get() == productsList["water"]["name"]:
        if currentValue >= productsList["water"]["value"]:
            insert_coin_button.config(state="disabled")

    if drink_var.get() == productsList["icetea"]["name"]:
        if currentValue >= productsList["icetea"]["value"]:
            insert_coin_button.config(state="disabled")

    if drink_var.get() == productsList["lemonade"]["name"]:
        if currentValue >= productsList["lemonade"]["value"]:
            insert_coin_button.config(state="disabled")    



def remainingValueHandler(drink_var, productsList, currentValue):
    """Returns the remaining value"""
    result = int()

    if drink_var.get() == productsList["water"]["name"]:
        result = productsList["water"]["value"] - currentValue 
        return numberConverterHandler(result)

    if drink_var.get() == productsList["icetea"]["name"]:
        result = productsList["icetea"]["value"] - currentValue 
        return numberConverterHandler(result)

    if drink_var.get() == productsList["lemonade"]["name"]:
        result = productsList["lemonade"]["value"] - currentValue 
        return numberConverterHandler(result)
bitcoin_amount1 = 3.85
bitcoin_amount2 = 1
bitcoin_amount3 = 13


# Syntax for a function in python
def beef():
    print("Dayum, functions are cool!")


def bitcoin_to_usd(btc):
    amount = btc * 527
    print(amount)
    if 2000 < amount:
        print('That is a lot of US Currency')
    elif 2000 > amount:
        print('This is a good amount of money but not as many as the others.')


beef()
bitcoin_to_usd(bitcoin_amount1)
bitcoin_to_usd(bitcoin_amount2)
bitcoin_to_usd(bitcoin_amount3)
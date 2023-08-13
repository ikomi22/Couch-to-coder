balance = 1000  # money in users account
pin = 2025  # pin to authorize
withdraw_instruct = "W"
deposit_instruction = "D"


# login
input_pin = int(input('Enter your PIN: '))

# if pin is correct, withdraw or deposit
if input_pin == pin:
    print("SUCCESS! YOU CURRENTLY HAVE $",
          balance, "WITHDRAWAL(W) OR DEPOSIT(D)?")
    input_instruction = input()
# If withdrawing, subtract withdrawal amount from balance and display
    if input_instruction == withdraw_instruct:
        input_withdraw_amt = int(input('ENTER AMOUNT:'))
        print("WITHDRAWAL SUCCESS! YOU CURRENTLY HAVE",
              (balance-input_withdraw_amt))
 # If depositing, add  deposit amount to balance and display
    elif input_instruction == deposit_instruction:
        input_deposit_amt = int(input('ENTER AMOUNT:'))
        print("DEPOSIT SUCCESS! YOU CURRENTLY HAVE",
              (balance+input_deposit_amt))

# If pin is wrong, do not give access.
else:
    print("INVALID PIN")

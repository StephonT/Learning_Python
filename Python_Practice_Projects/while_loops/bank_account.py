balance = 100

while True:
    
    action = input("What would you like to do: (withdraw,deposit,exit) ")
    
    if action == 'deposit':
        amount = int(input("Enter the amount to deposit: "))
        
        balance += amount
        print(f"${amount} deposited. New Balance: ${balance}")
        
    elif action == 'withdraw':
        amount = int(input("Enter the amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds! Withdrawal denied.")
        else:
            balance -= amount
            print(f"${amount} withdrawn. New Balance: ${balance}")
        
    elif action == 'exit':
        print(f"Final Account Balance: ${balance}")
        break
    else:
        print("Invalid action. Please choose 'deposit', 'withdraw', or 'exit'")
        
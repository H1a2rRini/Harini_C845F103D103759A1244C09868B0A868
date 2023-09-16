class BankAccount:

  def __init__(self, account_number, account_holder_name, initial_balance):
    self._account_number = account_number
    self._account_holder_name = account_holder_name
    self._account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self._account_balance += amount
      return f"Deposited ${amount}. New balance is ${self._account_balance}."
    else:
      return "Invalid deposit amount."

  def withdraw(self, amount):
    if 0 < amount <= self._account_balance:
      self._account_balance -= amount
      return f"Withdrew ${amount}. New balance is ${self._account_balance}."
    else:
      return "Insufficient funds or invalid withdrawal amount."

  def display_balance(self):
    return f"Account balance for {self._account_holder_name}: ${self._account_balance}"


account_number = input("Enter account number: ")
account_holder_name = input("Enter account holder's name: ")
initial_balance = float(input("Enter initial balance: "))

account = BankAccount(account_number, account_holder_name, initial_balance)

while True:
  print("\nOptions:")
  print("1. Deposit")
  print("2. Withdraw")
  print("3. Display Balance")
  print("4. Exit")

  choice = input("Select an option (1/2/3/4): ")

  if choice == '1':
    amount = float(input("Enter the deposit amount: "))
    print(account.deposit(amount))
  elif choice == '2':
    amount = float(input("Enter the withdrawal amount: "))
    print(account.withdraw(amount))
  elif choice == '3':
    print(account.display_balance())
  elif choice == '4':
    print("Exiting the program.")
    break
  else:
    print("Invalid choice. Please select a valid option.")

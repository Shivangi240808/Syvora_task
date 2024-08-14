class DebtManager:
    def __init__(self):
        self.debts = {}

    def add_transaction(self, debtor, creditor, amount):
        if debtor not in self.debts:
            self.debts[debtor] = {}
        if creditor not in self.debts[debtor]:
            self.debts[debtor][creditor] = 0
        self.debts[debtor][creditor] += amount
        
        # Debugging: Print the current state of debts
        print(f"Transaction added: {debtor} owes {creditor} {amount}")
        print(f"Current debts: {self.debts}")

    def query_debt(self, person):
        total_debt = 0
        if person in self.debts:
            total_debt = sum(self.debts[person].values())
        return total_debt

    def query_money_owed(self, person):
        total_money_owed = 0
        for debtor in self.debts:
            if person in self.debts[debtor]:
                total_money_owed += self.debts[debtor][person]
        return total_money_owed

    def query_most_money_owed(self):
        max_money_owed = 0
        person_max_money_owed = None
        for person in self.debts:
            money_owed = self.query_money_owed(person)
            if money_owed > max_money_owed:
                max_money_owed = money_owed
                person_max_money_owed = person
        return person_max_money_owed, max_money_owed

    def query_most_debt(self):
        max_debt = 0
        person_max_debt = None
        for person in self.debts:
            debt = self.query_debt(person)
            if debt > max_debt:
                max_debt = debt
                person_max_debt = person
        return person_max_debt, max_debt

    # Ensure the run method is within the class
    def run(self):
        while True:
            command = input("Enter command: ").strip().split()
            if not command:
                continue
            
            # Check for the correct number of arguments based on the command
            if command[0] == "add_transaction":
                if len(command) != 4:
                    print("Error: add_transaction requires 3 arguments (debtor, creditor, amount).")
                    continue
                self.add_transaction(command[1], command[2], int(command[3]))
            elif command[0] == "query_debt":
                if len(command) != 2:
                    print("Error: query_debt requires 1 argument (person).")
                    continue
                print(f"Total debt for {command[1]}: {self.query_debt(command[1])}")
            elif command[0] == "query_money_owed":
                if len(command) != 2:
                    print("Error: query_money_owed requires 1 argument (person).")
                    continue
                print(f"Total money owed to {command[1]}: {self.query_money_owed(command[1])}")
            elif command[0] == "query_most_money_owed":
                person, amount = self.query_most_money_owed()
                print(f"Person with the most money owed: {person} ({amount})")
            elif command[0] == "query_most_debt":
                person, amount = self.query_most_debt()
                print(f"Person with the most debt: {person} ({amount})")
            elif command[0] == "exit":
                break
            else:
                print("Unknown command!")

# Example Usage
if __name__ == "__main__":
    manager = DebtManager()
    manager.run()
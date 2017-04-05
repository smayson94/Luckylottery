from collections import Counter
employee = {}


#Creates a new employee
def new_employee(fullName, numbers):
    employee[fullName] = numbers

#Lists the name name of the employee with thier lotto numbers
def list_employees(numbers):
    employeeNames = []
    for fullName, values in employee.iteritems():
        if numbers == values:
            employeeNames.append(fullName)
        return employeeNames
    
#Shows the numbers for the wining ticket
def winning_ticket():
    """
    Computes the winning ticket by finding the mode (most common) of each of
    the 6 numbers across all employees.
    """
    counters = [Counter([numbers[i] for numbers in employee.values()])
                for i in range(6)]  # Creates 1 counter for each of 6 slots
    winner = [counter.most_common(1)[0][0] for counter in counters]
    return winner

#runs the powerball program
def main():

    print ("Welcome to Powerball, to play pick a number from the list below \n")
    while True:

        print "##### HOW TO PLAY ####"
        print("\n 1. Add new Employee \n 2. List All employee entries \n 3. Draw winnning numbers for Powerballl \n 4. exit")

        try :
            pick = int(raw_input("Pick a number"))
        except:
            print "Oops!That was not a valid number.  Try again..."
            continue

        if pick == 1:
            fullName = raw_input("Enter Full Name")
            if fullName in employee.keys():
                print "The name you provided is already entered. Sorry"
                continue
            lotto_input = raw_input("Enter 5 numbers in range of 1-69 with spaces between each number")
            powerball_input = raw_input("Enter one Powerball number in range of 1-26 ")
            try:
                lotto_num = [int(n) for n in lotto_input.split()]
                powerball = int(powerball_input)
                #Checks to make sure user input is within the given requirements
                assert(len(lotto_num) == 5) 
                for num in lotto_num:
                    assert(num in range(1, 70))  
                assert(len(lotto_num) == len(set(lotto_num)))  
                assert(powerball in range(1, 27)) 
                
            except:
                print "Try again. Not the expected input"
                continue  
            
            numbers = lotto_num + [powerball]
            new_employee(fullName, numbers)

        elif pick == 2:
            print "All current entries:\n"
            for fullName, numbers in employee.iteritems():
                print fullName + ": " + "".join((str(n) + " " for n in numbers))

        elif pick == 3:
            winners = []
            fav_nums = winning_ticket()
            print "Powerball winning number: " + "".join((str(n) + " " for n in fav_nums)) + "\n"

        elif pick == 4:
            exit()
        

        else:
            print "Invalid selection!"
            continue








if __name__ == "__main__":
    main()

firstName="Wamey"
lastName="Miriam"
employeeId="emp122"
basicSalary=1000
allowance=5000
tax = 1000
pensionScheme = 3000


def calculateNetSalary():
    return basicSalary + allowance - tax - pensionScheme

netSalary = calculateNetSalary();

# toPrint = "Net Salary is {}"
print("Net Salary is {}".format(netSalary))


import math
import argparse

#Pass all the neceassry parameters to the script
parser = argparse.ArgumentParser(description="The program is a loan calculator")
parser.add_argument("--principal", type = int,
                    help="The principal loan amount")
parser.add_argument("--periods", type = int,
                    help="Duration of the loan")
parser.add_argument("--interest", type = float,
                    help="Intrest rate of the loan")
parser.add_argument("--type", type = str, choices = ["diff", "annuity"],
                    help="The type of payment calculation")
parser.add_argument("--payment", type = int,
                    help="Monthly payment")

args = parser.parse_args()

if args.interest == None or args.interest < 0:
    print("Incorrect parameters")
else:
    i = args.interest / 1200
    P = args.principal
    n = args.periods
    anu_payment = args.payment
    diff_month = []

    def num_of_months(P, anu_payment, i):
        return math.ceil(math.log(anu_payment / (anu_payment - (i * P)),(1 + i)))

    def loan_principal(A, n, i):
        return round(A / ((i * (1 + i) ** n) / ((1 + i) ** n - 1 )))

    def annuity_payment(P, n, i):
        return math.ceil(P * ((i * (1 + i) ** n) / ((1 + i) ** n - 1 )))

    def annuity_principal(A, n, i):
        return int(anu_payment / ((i * ((1 + i) ** n))/(((1 + i) ** n) -1)))

    def diff_payment(P, n, i):
        for m in range(1, n+1):
            D = math.ceil(P/n + i * (P - (P *(m - 1))/ n))
            diff_month.append(D)
        return diff_month

    if args.type == "annuity":
        if args.payment and args.periods:
            answer = annuity_principal(anu_payment, n, i)
            print("Your loan principal = {}!".format(answer))
            print("Overpayment = {}".format(anu_payment * n - answer))

        elif args.principal and args.payment:
            answer = num_of_months(P, anu_payment, i)
            if answer > 12 and answer % 12 != 0: 
                years = answer // 12
                months = answer % 12
                print("It will take {} years and {} months to replay the loan!".format(years, months))
            elif answer % 12 == 0:
                print("It will take {} {} to repay the loan!".format(answer // 12, "year" if answer == 1 else "years"))
            else:
                print("It will take {} {} to repay the loan!".format(answer, "month" if answer == 1 else "months"))
            print("Overpayment = {}".format(answer * anu_payment - P))


        elif args.principal and args.periods:
            answer = annuity_payment(P, n, i)
            print("\nYour annuity payment = {}!".format(answer))
            print("Overpayment = {}".format(answer * n - P))


    elif args.type == "diff":
        if args.principal and args.periods and args.interest:
            monthly_payment_list = diff_payment(P, n, i)
            for Idx, m in enumerate(monthly_payment_list, 1):
                print("Month " + str(Idx) + ": payment is {}".format(m))
        else:
            print("Incorrect parameters")
        print("Overpayment = {}".format(sum(monthly_payment_list) - P))


    elif args.type != "annuity" or "diff":
        print("Incorrect parameters")

        

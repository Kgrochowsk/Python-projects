import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()

arguments = [args.type, args.payment, args.principal, args.periods, args.interest]
counter = 0
is_negative = False

for x in arguments[1:5]:
    if x is None:
        counter += 1
    else:
        if float(x) < 0:
            is_negative = True

payment = 0
principal = 0
periods = 0
interest = 0


def differentiated_payment():
    sum_ = 0
    i = interest / (12 * 100)
    for m in range(periods):
        D = (principal - (principal * (m + 1 - 1)) / periods)
        D_m = principal / periods + i * D
        sum_ += D_m
        print("Month {}: payment is {}".format(m, round(D_m)))

    print("\nOverpayment = {}".format(math.ceil(sum_ - principal)))


def calculate_periods():
    i = interest / (12 * 100)
    n = math.ceil(math.log(payment / (payment - i * principal), 1 + i))
    years = n // 12
    months = n % 12
    if years == 0 and months < 2:
        print("It will take {} month to repay this loan!".format(months))
    elif years == 0 and months >= 2:
        print("It will take {} months to repay this loan!".format(months))
    elif years == 1 and months == 0:
        print("It will take {} year to repay this loan!".format(years))
    elif years >= 2 and months == 0:
        print("It will take {} years to repay this loan!".format(years))
    elif years == 1 and months < 2:
        print("It will take {} year and {} month to repay this loan!".format(years, months))
    elif years == 1 and months >= 2:
        print("It will take {} year and {} months to repay this loan!".format(years, months))
    elif years >= 2 and months < 2:
        print("It will take {} years and {} month to repay this loan!".format(years, months))
    else:
        print("It will take {} years and {} months to repay this loan!".format(years, months))
    return n


def annual_payment():
    i = interest / (12 * 100)
    annuity = principal * ((i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1))
    print("Overpayment = {}".format(annuity * periods - principal))
    return math.ceil(annuity)


def calculate_principal():
    i = interest / (12 * 100)
    principal = round(payment / ((i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1)))

    print("Your loan principal = {}!".format(round(principal)))

    return math.ceil(principal)


if counter > 1 or is_negative:
    print("Incorrect parameters")
else:
    if arguments[0] == "diff":
        if arguments[1] is not None or arguments[4] is None:
            print("Incorrect parameters")
        else:
            if arguments[1] is None:
                principal = float(arguments[2])
                periods = int(arguments[3])
                interest = float(arguments[4])
                differentiated_payment()
    elif arguments[0] == "annuity":
        if arguments[3] is None:
            payment = float(arguments[1])
            principal = float(arguments[2])
            interest = float(arguments[4])
            periods = calculate_periods()
            annual_payment()
        elif arguments[2] is None:
            payment = float(arguments[1])
            periods = int(arguments[3])
            interest = float(arguments[4])
            principal = calculate_principal()
            annual_payment()
        elif arguments[1] is None:
            periods = int(arguments[3])
            principal = float(arguments[2])
            interest = float(arguments[4])
            payment = annual_payment()
            print("Your annuity payment = {}!".format(payment))

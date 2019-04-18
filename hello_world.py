print("Is it a Prime Number? Check out!")

number_to_check = input("Your Number: ")



def number(number_to_check, factor=1):
    while int(number_to_check) > factor:
        if int(number_to_check) / factor != 0:
            factor += 1
            if int(number_to_check) == factor:
                return "It is Prime Number!"
        else:
            return "It isn't Prime Number!"


print(number(number_to_check, factor=1))


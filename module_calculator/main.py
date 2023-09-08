#Resit Tuition Fee Calculator

numofmodules = int(input("How many modules are you resitting? :"))

module_list = []

for i in range(numofmodules):
    module = input("Enter module name in the format of (COMP/MATH XXXX): ")
    module_list.append(module)

home_fee = 1156.25
comp1811_fee_home = 2312.50
intl_fee = 2018.75
comp1811_fee_intl = 4037.50

main_home_fee = 9250
main_intl_fee = 156150

total_fee = 0

home_or_intl = input("Are you a home or international student? (home/intl): ")
year2modules = input("Are you going to be resitting alongside your year 2 modules? (yes/no): ")

if home_or_intl == "home":
    for i in range(len(module_list)):
        if module_list[i] == "COMP1811":
            total_fee += comp1811_fee_home
        else:
            total_fee += home_fee
    if year2modules == "yes":
        total_fee += 9250
    else:
        print("Your total tuition fee is £", (round(total_fee, 2)))

elif home_or_intl == "intl":
    for i in range(len(module_list)):
        if module_list[i] == "COMP1811":
            total_fee += comp1811_fee_intl
        else:
            total_fee += intl_fee
    if year2modules == "yes":
        total_fee += 156150
    else:
        print("Your total tuition fee is £", (round(total_fee, 2)))

explanation = input("Would you like to know how the total fee was calculated? (yes/no): ")

if explanation == "yes":
    if year2modules == "no" and home_or_intl == "home":
        print("You've said that you're a HOME studentt and you're NOT resitting alongside your year 2 modules.")

        for i in range(len(module_list)):
            if module_list[i] == "COMP1811":
                print("You're resitting COMP1811, which costs £2312.50")
            else:
                print("You're resitting", module_list[i], "which is 15 credits costing £1156.25")
        print("Therefore, your total tuition fee is £", (round(total_fee, 2)))

    elif year2modules == "no" and home_or_intl == "intl":
        print("You've said that you're an INTERNATIONAL student and you're NOT resitting alongside your year 2 modules.")

        for i in range(len(module_list)):
            if module_list[i] == "COMP1811":
                print("You're resitting COMP1811, which costs £4037.50")
            else:
                print("You're resitting", module_list[i], "which is 15 credits costing £2018.75")
        print("Therefore, your total tuition fee is £", (round(total_fee, 2)))
    
    elif year2modules == "yes" and home_or_intl == "home":
        print("You've said that you're a HOME student and YOU ARE resitting alongside your year 2 modules.")

        for i in range(len(module_list)):
            if module_list[i] == "COMP1811":
                print("You're resitting COMP1811, which costs £2312.50")
            else:
                print("You're resitting", module_list[i], "which is 15 credits costing £1156.25")
        print("You're also resitting alongside your year 2 modules, which costs £9250")
        print("Therefore, your total tuition fee is £", (round(total_fee, 2)))

    elif year2modules == "yes" and home_or_intl == "intl":
        print("You've said that you're an INTERNATIONAL student and YOU ARE resitting alongside your year 2 modules.")

        for i in range(len(module_list)):
            if module_list[i] == "COMP1811":
                print("You're resitting COMP1811, which costs £4037.50")
            else:
                print("You're resitting", module_list[i], "which is 15 credits costing £2018.75")
        print("You're also resitting alongside your year 2 modules, which costs £156150")
        print("Therefore, your total tuition fee is £", (round(total_fee, 2)))


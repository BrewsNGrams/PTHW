def numbers_loop(x):
    numbers = []
    for num in range(x):
        print "At the top i is %d" % num
        numbers.append(num)

        print "Numbers now: ", numbers
        print "At the bottom i is %d" % num

    print "The numbers: "

    for num in numbers:
        print num

user_num = raw_input("Pick a number. Any number: ")

numbers_loop(int(user_num))


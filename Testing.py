def square_number():
    for number in range(51):
        answer = number * number
        print("{0:>2} * {1:>2} = {2:>6}".format(number,number,answer))
    return answer

save = square_number()

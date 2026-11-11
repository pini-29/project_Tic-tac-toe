def chek_num(num):
    if not isinstance(num,int) and (num < 0 or num > 9):
        return "Pleas choice a new number"
    return True

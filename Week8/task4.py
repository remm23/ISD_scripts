def pageSide(page):
    if checkSide(page):
        print(page)
    else:
        print("%60s%d" % (" ",page))

def checkSide(page):
    # if page is even then return true
    if page % 2 == 0:
        return True
    else:
        return False
    
pageSide(10) # true
pageSide(9)  # false
pageSide(8)  # true
pageSide(7)  # false
pageSide(6)  # true
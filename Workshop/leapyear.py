def leap_year( start, end):
    ly = []
    for year in range( start, end) :
        if year % 4 == 0 or year % 400 == 0 :
            if year % 100 != 0:
                ly.append(year)
    print(ly)
leap_year(2090,2200)

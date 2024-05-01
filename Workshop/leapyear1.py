def is_leap_year(year):
    """This function will check if the year is leap or not
    Return True if leap year and False otherwise
    """
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            return True
        elif year%100 == 0:
            return False
        return True
    return False



def leap_years(start, end):
    """
    This function returns a list of leap years between start and end
    """
    # approach: 1 for loops
    # result = []
    # for year in range(start, end+1):
    #     if is_leap_year(year):
    #         result.append(year)
    # approach 2: filters
    #result = list(filter(is_leap_year,range(start,end+1)))
    # approach 3: list comprehensions
    result = [ year for year in range(start,end+1) if is_leap_year(year)]
    print(result)
leap_years(2000,2150)
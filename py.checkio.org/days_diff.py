# import calendar as cal
from datetime import date
def days_diff(a, b):
    # d1 = cal.weekday(a[0],a[1],a[2])
    # d2 = cal.weekday(b[0],b[1],b[2])
    d1 = a[2]
    d2 = b[2]

    m1 = a[1]
    m2 = b[1]
    
    y1 = a[0]
    y2 = b[0]

    ret_day = 0
    ret_mon = 0
    ret_year = 0
    
    date.year()
    if d1 > d2:
        ret_day =  d1 - d2
    else:
        ret_day = d2 - d1    
    
    if m1 > m2:
        ret_mon = m1 - m2
    else:
        ret_mon = m2 - m1

    if y1 > y2:
        ret_year = y1 - y2
    else:
        ret_year = y2 - y1       

    ret_day =  ret_year * 365 + ret_mon * 30 + ret_day  

    return ret_day       
   
if __name__ == "__main__":
    print("Example:")
    print(days_diff((1982, 4, 19), (1982, 4, 22)))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    # assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    print("Coding complete? Click 'Check' to earn cool rewards!")
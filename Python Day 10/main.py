# Functions with Outputs

def my_function(): 
    result = 3 * 2
    return result

output = my_function()

def format_name(f_name, l_name): 
    if f_name == "" or l_name == "": 
        return "You didn't provide valid inputs"   
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"Result: {formatted_f_name} {formatted_l_name}"
    
# formatted_string = format_name("sean", "unland")
# print(formatted_string)
print(format_name(input("What is your first name? "), input("What is your last name?")))

##########CODING EXERCISE#################

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
              return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month): 
    
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if is_leap(year) and month == 2: 
      return 29
  return month_days[month - 1]
      

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
#######################################

def format_name(f_name, l_name): 
    # Doc Strings 6 quotations """"""
    """Take a first and last name and format it to return the title case version"""
    if f_name == "" or l_name == "": 
        return "You didn't provide valid inputs"   
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"Result: {formatted_f_name} {formatted_l_name}"

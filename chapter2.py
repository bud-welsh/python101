first_string = 'This is created with single quotes'
second_string = "This is created with double quotes"
third_string = '''This is a 
triple quote string I 
wrote on multiple lines'''
fourth_string = """Wrote this string
on multiple lines with 
double quotes this time"""

print(first_string)
print(second_string)
print(third_string)
print(fourth_string)

single_quote = 'This is how we have "double quotes" in a string.'
double_quote = "An air comma is this string's single quote."
triple_quote = '''"That's what" - She'''
triple_quote_again = """"That's what" - She"""

print(single_quote)
print(double_quote)
print(triple_quote)
print(triple_quote_again)

my_number = 123 # This is an integer
my_number_string = str(my_number) # This makes the integer a string
print(type(my_number))
print(type(my_number_string))

# Concatination
string_one = "Attention! Attention Please! "
string_two = "Get your pencils and scorecards ready. "
string_three = string_one + string_two
print(string_three)

# String Methods
string_one_upper = string_one.upper()
print(string_one_upper)
# print(dir(string_one_upper))
# print(help(string_one.capitalize))
# string_one_capitalize = string_one.capitalize
# print(string_one_capitalize)



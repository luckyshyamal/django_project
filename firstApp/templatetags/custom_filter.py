from django import template

register = template.Library() 

def f3upper(values):
    return values[:3].upper() + values[3:]

def f1upper(value):
    return value.title()

def reverseall(value):
    return value[::-1]

def count_char(value,letter):
    if not isinstance(value,str):
        return 'Error: Input must be a string'
    return value.lower().count(letter)
register.filter('f3upper',f3upper)
register.filter('f1upper',f1upper)
register.filter('reverseall',reverseall)
register.filter('count_letter',count_char)
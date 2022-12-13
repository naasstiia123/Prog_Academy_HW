import re

#1
def check(data: str, pattern):

    '''
    Check if string match with RE
    :param data: String which will check
    :param pattern: RE with which will compare
    :return: Boolean meaning of checking
    '''

    if not isinstance(data, str):
        raise TypeError
    res = re.search(pattern, data)
    return bool(res)

pattern_example = r'[Rr][Bb]+[Rr]$'
a = check('Hello world rBBr', pattern_example)
print(a)


#2
def check(number: str | int):

    '''
    Check if number can be a cards number that must have 16 digit symbols
    :param number: Number which will check for valid
    :return: Boolean answer
    '''

    if isinstance(number, int):
        number = str(number)
    if not isinstance(number, str):
        raise TypeError
    pattern = r'^\d{4}-?\d{4}-?\d{4}-?\d{4}$'
    res = re.match(pattern, number)
    return bool(res)

a = check('1234-4142-5156-4852')
b = check(1234567887654321)
print(a)
print(b)


#3
def check(email: str):

    '''
    Check if email match with requirements:
    -at least 1 digit
    -at least 1 letter in upper case
    -at least 1 letter in lower case
    -symbols '-' and '_' but not on 1st position
    -symbol '-' only 1 time
    :param email: email
    :return: Boolean answer
    '''
if not isinstance(email, str):
        raise TypeError
    patterns = (r'^[^\W\s_]+', r'[0-9]+', r'[A-Z]+', r'[a-z]+', r'_*', r'-?', r'@{1}\w+\.{1}\w+$')
    pattern_2 = r'-{1,}[\w\W]+-{1,}'
    pattern_3 = r'@+[\w\W]+@+'
    pattern_4 = r'\.+[\w\W]+\.+'
    pattern_5 = r'[^\w\s@.-]'
    for item in patterns:
        check_1 = re.search(item, email)
        if not check_1:
            return False
    check_2 = re.search(pattern_2, email)
    check_3 = re.search(pattern_3, email)
    check_4 = re.search(pattern_4, email)
    check_5 = re.search(pattern_5, email)
    if check_2 or check_3 or check_4 or check_5:
        return False

    return True

a = check('8bH-olla4__@gmail.com')
print(a)
    

#4
def check(login):

    '''
    Check login to requirement 2-10 symbols only digits with letter
    :param login: login
    :return: Boolean answer
    '''

    if not isinstance(login, str):
        raise TypeError
    pattern = r'^\w[^_+-.,?\\/]{2,10}$'
    res = re.match(pattern, login)
    return bool(res)

a = check('jfJ2ggbgfg1')
print(a)

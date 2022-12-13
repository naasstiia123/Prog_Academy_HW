import re

#1
def check(data: str, pattern):

    '''
    Check if string match with RE
    :param data: String which will check
    :param pattern: RE with which will compare
    :return: Match list
    '''

    if not isinstance(data, str):
        raise TypeError
    res = re.findall(pattern, data)
    return res

pattern_example = r'R[Bb]+[Rr]'
a = check('Hello RbbR world RBBr', pattern_example)
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
    pattern = r'^\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}$'
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
    patterns = (r'^[^\W\s_]+', r'\w+', r'_*', r'-?', r'@\w+(\.\w+)+$')
    pattern_5 = r'[^\w\s@.-]'
    for item in patterns:
        check_1 = re.search(item, email)
        if not check_1:
            return False
    if check_5:
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

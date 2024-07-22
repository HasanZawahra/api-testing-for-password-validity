
class data:
    valid = 'ab1!Cdefgh1'
    valid_statement = "Password is valid! Sign-in successful."
    not_containing_at_least_2_letters = '987123##!@#'
    not_containing_at_least_2_letters_statement = 'Password must contain at least two letters.'
    not_containing_at_least_1_number = 'hasanZwahra@#!'
    not_containing_at_least_1_number_statement = 'Password must contain at least one number.'
    not_containing_at_least_1_special_char = 'dtSoa123localhost'
    not_containing_at_least_1_special_char_statement = 'Password must contain at least one special character.'
    short_password = '123D@sad1t'
    short_password_statement ='Password must be longer than 10 characters.'
    not_containing_at_least_1_uppercase = 'eab1!cdefgh'
    not_containing_at_least_1_uppercase_statement = 'Password must contain at least one uppercase letter.'
    not_containing_at_least_1_lowercase = 'EAB1!CDEFGH'
    not_containing_at_least_1_lowercase_statement = 'Password must contain at least one lowercase letter.'
    long_password = '1234567890!@#$%^&*()ASdfgh'
    long_password_statement = 'Password must not be longer than 25 characters'
    has_repeated_sequences = '0599571137!As'
    has_repeated_sequences_statement = 'Password must not contain consecutive repeated characters.'

class fields :
    password = "password"


class status_codes :
    OK = 200
    NOT_FOUND= 404

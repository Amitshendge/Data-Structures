import PatternError as Error
import re
from LoggerHandler import logger

def regex(string):
    patt = r'([0-9]{2,})+(\s[0-9]{10})+'
    matches = re.fullmatch(patt,string)
    if matches :
        print('Phone Number is Valid')
        logger.info(f"executed Successfully {string}")
    else:
        try:
            raise Error.PatternError(f'Wrong Pttern Entered {string}')
        except Error.PatternError as e:
            print(e)
            logger.error(e)

if __name__ == '__main__':
    user_input = input('Enter Valid Phone Number : ')
    regex(user_input)

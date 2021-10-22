import PatternError as Error
import re
from LoggerHandler import logger

def regex(string):
    patt = r'(?=.*[A-Z])(?=.*[0-9]).{8,}'
    matches = re.fullmatch(patt,string)
    if matches :
        print('PassWord is Valid')
        logger.info(f"executed Successfully {string}")
    else:
        try:
            raise Error.PatternError(f'Wrong Pttern Entered {string}')
        except Error.PatternError as e:
            print(e)
            logger.error(e)

if __name__ == '__main__':
    print('minimum 8 char, atleast 1 Uppercase, atleast one number')
    user_input = input('Enter Valid New PassWord : ')
    regex(user_input)

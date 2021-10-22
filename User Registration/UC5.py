import PatternError as Error
import re
from LoggerHandler import logger

def regex(string):
    patt = r'(.{8,})+'
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
    user_input = input('Enter Valid New PassWord minimum 8 char : ')
    regex(user_input)

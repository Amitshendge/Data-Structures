import PatternError as Error
import re
from LoggerHandler import logger

def regex(string):
    patt = r'^[A-Z][a-z]{3,30}'
    matches = re.fullmatch(patt,string)
    if matches :
        print('Second name is Valid')
        logger.info(f"executed Successfully {string}")
    else:
        try:
            raise Error.PatternError('Wrong Pttern Entered least 4 len and only first alphabet capital')
        except Error.PatternError as e:
            print(e)
            logger.error(e)

if __name__ == '__main__':
    user_input = input('Enter Valid Second Name : ')
    regex(user_input)

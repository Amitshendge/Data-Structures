import PatternError as Error
import re
from LoggerHandler import logger

def regex(string):
    patt = r'([A-Za-z0-9_+\-!#$%^&*]{3,})+(\.[A-Za-z0-9]{3,})*(\@[a-zA-Z1-9]{1,}\.)+([a-zA-Z]{2,})+(\.[a-zA-Z]{2,})*'
    matches = re.fullmatch(patt,string)
    if matches :
        print('Email id is Valid')
        logger.info(f"executed Successfully {string}")
    else:
        try:
            raise Error.PatternError(f'Wrong Pttern Entered {string}')
        except Error.PatternError as e:
            print(e)
            logger.error(e)

if __name__ == '__main__':
    user_input = input('Enter Valid Email id : ')
    regex(user_input)

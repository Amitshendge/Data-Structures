import PatternError as Error
from LoggerHandler import logger
import re
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
    sample_list = ['abc@yahoo.com','abc-100@yahoo.com','abc.100@yahoo.com','abc111@abccom','abc-100@abc.net','abc.100@abc.com.au','abc@1.com','abc@gmail.com.com','abc+100@gmail.com']
    # user_input = input('Enter Valid Email id : ')
    for i in sample_list:
        regex(i)
        

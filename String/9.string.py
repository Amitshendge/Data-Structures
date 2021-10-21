import textwrap

def formatted(string):
    return (textwrap.fill(string, width=50))


if __name__ =='__main__':
    sample_text = '''
    Note: This is a system-generated e-mail, please do not reply to it. *** This message is intended only for the person or entity to which it is addressed and may contain confidential and/or privileged information. If you have received this message in error, please notify the sender immediately and delete this message from your system. ***.
    '''
    print()
    print(formatted(sample_text))
    print()
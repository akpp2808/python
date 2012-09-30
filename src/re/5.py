import re

def get_accept_language_code(string):
    '''
        HTTP Accept-Language header parsing
        return lang code in lower case or empty string if cannot parse
    '''
    if isinstance(string, str):
        match = re.search('(^[a-z]{2})\s*-\s*[a-zA-Z]{2}', string)
        return match and match.group(1)
    return ''


print get_accept_language_code('1ad-ad')
#print '1'
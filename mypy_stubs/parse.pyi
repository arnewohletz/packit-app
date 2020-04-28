#!/usr/bin/env python  # [module parse]

## DATA ##

__version__ = '1.8.4'
# None
__all__ = ['parse', 'search', 'findall', 'with_pattern']
# None


## FUNCTIONS ##

def findall(format, string, pos=0, endpos=None, extra_types=None, evaluate_result=True, case_sensitive=False):
    """
    Search "string" for all occurrences of "format".
    
    You will be returned an iterator that holds Result instances
    for each format match found.
    
    Optionally start the search at "pos" character index and limit the search
    to a maximum index of endpos - equivalent to search(string[:endpos]).
    
    If ``evaluate_result`` is True each returned Result instance has two attributes:
    
     .fixed - tuple of fixed-position values from the string
     .named - dict of named values from the string
    
    If ``evaluate_result`` is False each returned value is a Match instance with one method:
    
     .evaluate_result() - This will return a Result instance like you would get
                          with ``evaluate_result`` set to True
    
    The default behaviour is to match strings case insensitively. You may match with
    case by specifying case_sensitive=True.
    
    If the format is invalid a ValueError will be raised.
    
    See the module documentation for the use of "extra_types".
    """
    raise NotImplementedError()

def parse(format, string, extra_types=None, evaluate_result=True, case_sensitive=False):
    """
    Using "format" attempt to pull values from "string".
    
    The format must match the string contents exactly. If the value
    you're looking for is instead just a part of the string use
    search().
    
    If ``evaluate_result`` is True the return value will be an Result instance with two attributes:
    
     .fixed - tuple of fixed-position values from the string
     .named - dict of named values from the string
    
    If ``evaluate_result`` is False the return value will be a Match instance with one method:
    
     .evaluate_result() - This will return a Result instance like you would get
                          with ``evaluate_result`` set to True
    
    The default behaviour is to match strings case insensitively. You may match with
    case by specifying case_sensitive=True.
    
    If the format is invalid a ValueError will be raised.
    
    See the module documentation for the use of "extra_types".
    
    In the case there is no match parse() will return None.
    """
    raise NotImplementedError()

def search(format, string, pos=0, endpos=None, extra_types=None, evaluate_result=True, case_sensitive=False):
    """
    Search "string" for the first occurrence of "format".
    
    The format may occur anywhere within the string. If
    instead you wish for the format to exactly match the string
    use parse().
    
    Optionally start the search at "pos" character index and limit the search
    to a maximum index of endpos - equivalent to search(string[:endpos]).
    
    If ``evaluate_result`` is True the return value will be an Result instance with two attributes:
    
     .fixed - tuple of fixed-position values from the string
     .named - dict of named values from the string
    
    If ``evaluate_result`` is False the return value will be a Match instance with one method:
    
     .evaluate_result() - This will return a Result instance like you would get
                          with ``evaluate_result`` set to True
    
    The default behaviour is to match strings case insensitively. You may match with
    case by specifying case_sensitive=True.
    
    If the format is invalid a ValueError will be raised.
    
    See the module documentation for the use of "extra_types".
    
    In the case there is no match parse() will return None.
    """
    raise NotImplementedError()

def with_pattern(pattern, regex_group_count=None):
    """
    Attach a regular expression pattern matcher to a custom type converter
    function.
    
    This annotates the type converter with the :attr:`pattern` attribute.
    
    EXAMPLE:
        >>> import parse
        >>> @parse.with_pattern(r"\d+")
        ... def parse_number(text):
        ...     return int(text)
    
    is equivalent to:
    
        >>> def parse_number(text):
        ...     return int(text)
        >>> parse_number.pattern = r"\d+"
    
    :param pattern: regular expression pattern (as text)
    :param regex_group_count: Indicates how many regex-groups are in pattern.
    :return: wrapped function
    """
    raise NotImplementedError()



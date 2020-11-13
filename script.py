import sys
import concurrent.futures
from collections.abc import Iterable

def concurrent_func(fn, iterator):

    if not hasattr(fn, '__call__'):
        raise TypeError(f'{sys._getframe().f_code.co_name} accepts a function as the first argument')

    if not isinstance(iterator, Iterable):
        raise TypeError(f'{sys._getframe().f_code.co_name} accepts an iterator as the second argument')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(fn, iterator)
        return results

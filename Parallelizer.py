import concurrent.futures
import os
from functools import wraps


def make_parallel(thread_multiple=3):
    """
        Decorator used to decorate any function which needs to be paralleled.
        After the input of the function should be a list in which each element is a instance of input fot the normal function.
        You can also pass in keyword arguments separately.
    :param thread_multiple:
    :return:
    """
    def sub_wrapper(func):
        @wraps(func)
        def wrapper(lst, **kwargs):
            number_of_workers = int(os.cpu_count() * thread_multiple)
            if len(lst) < number_of_workers:
                number_of_workers = len(lst)

            if number_of_workers:
                if number_of_workers == 1:
                    result = [func(lst[0])]
                else:
                    result = []
                    with concurrent.futures.ThreadPoolExecutor(max_workers=number_of_workers) as executer:
                        bag = {executer.submit(func, i, **kwargs): i for i in lst}
                        for future in concurrent.futures.as_completed(bag):
                            result.append(future.result())
            else:
                result = []
            return result
        return wrapper
    return sub_wrapper

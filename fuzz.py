import logging
from hypothesis import given, settings
from hypothesis.strategies import integers, floats, text, lists, dictionaries

logging.basicConfig(filename='fuzz.log', level=logging.DEBUG)

# Create an empty fuzz.log file if it doesn't exist
with open('fuzz.log', 'a') as f:
    pass

test_cases = [
    ('int', int, integers()),
    ('float', float, floats(allow_nan=False)),
    ('str', str, text()),
    ('list', list, lists(integers())),
    ('dict', dict, dictionaries(text(), integers()))
]

def run_tests():
    for func_name, func, strategy in test_cases:
        @settings(max_examples=10)
        @given(strategy)
        def test(value):
            result = func(value)
            assert isinstance(result, type(func()))

            log_message = f"{func_name}({value!r}) = {result!r}"
            print(log_message)
            logging.debug(log_message)
        test()

if __name__ == "__main__":
    run_tests()

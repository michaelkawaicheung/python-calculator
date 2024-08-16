import unittest
import importlib
from calculator.calculator import add, subtract

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_all_functions_have_test_cases(self):
        calculator_module = importlib.import_module("calculator.calculator")
        functions = [func for func in dir(calculator_module) if callable(getattr(calculator_module, func))]
        test_functions = [func for func in dir(TestCalculator) if func.startswith("test_")]

        for function_name in functions:
            if function_name not in test_functions and not function_name.startswith("__"):
                self.fail(f"No test case found for function {function_name}")

if __name__=='__main__':
    unittest.main()
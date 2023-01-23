import pytest

import src.fizzbuzz as fizzbuzz

class TestFizzBuzz_convert_function:


    def test_int_case(self):
        assert fizzbuzz.convert_int2fizzbuzz(1) == "1"
        assert fizzbuzz.convert_int2fizzbuzz(13) == "13" 
        assert fizzbuzz.convert_int2fizzbuzz(49) == "49"

    def test_fizz_case(self):
        assert fizzbuzz.convert_int2fizzbuzz(3) == "Fizz"
        assert fizzbuzz.convert_int2fizzbuzz(6) == "Fizz"
        assert fizzbuzz.convert_int2fizzbuzz(9) == "Fizz"

    def test_buzz_case(self):
        assert fizzbuzz.convert_int2fizzbuzz(5) == "Buzz"
        assert fizzbuzz.convert_int2fizzbuzz(10) == "Buzz"
        assert fizzbuzz.convert_int2fizzbuzz(20) == "Buzz"

    def test_fizzbuzz_case(self):
        assert fizzbuzz.convert_int2fizzbuzz(15) == "FizzBuzz"

    def test_0のときは0を返す(self):
        assert fizzbuzz.convert_int2fizzbuzz(0) == "0"
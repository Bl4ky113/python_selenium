#!/usr/bin/python

from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTests
from search_tests import SearchTests
from extra_tests import ExtraTests

assertions_result = TestLoader().loadTestsFromTestCase(AssertionsTests)
search_results = TestLoader().loadTestsFromTestCase(SearchTests)
extra_results = TestLoader().loadTestsFromTestCase(ExtraTests)

smoke_test = TestSuite([assertions_result, search_results, extra_results])

kwargs = {
    "output": "smoke-report"
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)

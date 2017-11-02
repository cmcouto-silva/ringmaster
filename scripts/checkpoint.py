#!/usr/bin/env python
"""
Inject a testing checkpoint into the build process.
"""

import re
import subprocess
import sys

from pause import ask_to_continue


TRUE = 't'
FALSE = 'f'
TEST_OUT = 'tests/test.out'


def has_error(line):
    """Determines if a line contains an error message."""
    return 'error' in line.lower()


def test(line):
    """Returns test and its result if line contains a test, else None."""
    match = re.search(f'^([^,]*),([{TRUE}{FALSE}])$', line)
    if match:
        test, res = match.group(1), match.group(2)
        return test, res


class TestAccountant(object):
    """Tallies results of a test."""
    
    def __init__(self, instream, outstream, quiet=False):
        self.streams = {'in': instream, 'out': outstream}   
        categories = ['errors', 'tests', 'failed']
        self.accounts = {cat: [] for cat in categories}
        self.quiet = quiet
        self.clean = True
    
    def collect(self):
        """Collect errors, tests, and failed tests from the output of some tests."""
        for line in self.streams['in']:
            
            if not self.quiet:
                self.streams['out'].write(line)
            
            if has_error(line):
                self.accounts['errors'].append(line)
                self.clean = False
            
            has_test = test(line)
            if has_test:
                test_name, res = has_test
                self.accounts['tests'].append(test_name)
                if res == FALSE:
                    self.accounts['failed'].append(test_name)
                    self.clean = False
    
    @property
    def nerrors(self):
        """The number of errors encountered."""
        return len(self.accounts['errors'])
    
    @property
    def ntests(self):
        """The number of tests encountered."""
        return len(self.accounts['tests'])
    
    @property
    def nfailed(self):
        """The number of tests that failed."""
        return len(self.accounts['failed'])
    
    def report(self):
        """Report on the results of the tests."""
        out = self.streams['out']
        
        # General tallies
        status = f'{self.ntests} tests run, {self.nerrors} errors, {self.nfailed} tests failed'
        out.write(f'{status}\n\n')
        
        # Lines on which an error was detected
        if self.nerrors > 0:
            out.write('Errors:\n')
            for error in self.accounts['errors']:
                out.write(f'{error}\n')
            out.write('\n')
        
        # Names of failed tests
        if self.nfailed > 0:
            out.write('Failed tests:\n')
            for failed_test in self.accounts['failed']:
                out.write(f'{failed_test}\n')
            out.write('\n')


def main(dirty=False, strict=False, quiet=False):
    """Process tests from a test output file, conditionally pause execution on failure."""
    # Would just redirect test output to stdin, but want to reserve that for user input.
    
    tests = TestAccountant(instream=open(TEST_OUT), outstream=sys.stdout, quiet=quiet)
    tests.collect()
    tests.report()
    
    if dirty:
        sys.exit(0)
    
    if strict and not tests.clean:
        print('Errors or failures encountered in strict mode; halting')
        sys.exit(1)
    
    if not tests.clean:
        sys.exit(ask_to_continue())


if __name__ == '__main__':
    flags = {flag: True for flag in sys.argv[1:]}
    main(**flags)


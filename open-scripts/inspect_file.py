from __future__ import annotations

import importlib.util
from os import path
from typing import List, TextIO
import re


HEADER_LENGTH = 80

LINE_LENGTH_LIMIT = 120


def print2(*args, indent=0, tabs='    ', **kwargs):
    print(tabs * indent, end='')
    print(*args, **kwargs)


def inspect_method(inspection_name):
    def inspect(func):
        def wrapper(*args, **kwargs):
            padding_length = (HEADER_LENGTH - len(inspection_name) - 1) // 2
            print('-' * HEADER_LENGTH)
            print('|' + ' ' * padding_length + inspection_name.upper() + ' ' * padding_length + '|')
            print('-' * HEADER_LENGTH)
            return func(*args, **kwargs)
        
        return wrapper
    
    return inspect


class InspectFile:
    PRIVATE_OUTSIDE_PATTERN = re.compile(r'\b((?!self)\w)+\._[^_](\w+?)\b')
    PUBLIC_INSIDE_PATTERN = re.compile(r'(self\.[^_]\w*)\s*=')
    CAMEL_CASE = re.compile(r'\b(self\._?)?[a-z]+(([A-Z][0-9a-z]+)+)\b')
    BAD_FOR_NAME = re.compile(r'for\s+[a-zA-Z]\s+in\s+((?!range).)+\s*:')
    BAD_NAME = re.compile(r'^\s*\b((((?![xy])[a-z]){1,2}\s*,\s*)*((?![xy])[a-z]){1,2})\b\s*=')
    
    def __init__(self, *files: TextIO[str]):
        """
        Constructor
        Parameters:
            files: file objects to be inspected, returned by open()
        """
        self._files_content = {}
        for file in files:
            self._files_content[file.name] = file.readlines(), file.read()
        self._files = files
    
    def _test_simple(self, test_call, indent=0):
        for filename, (lines, content) in self._files_content.items():
            print2(f"File: {path.basename(filename)}", indent=indent)
            okay = test_call(lines, content, indent=indent + 1)
            if okay:
                print2("OK", indent=indent + 1)
    
    @inspect_method('Line organisation')
    def test_line_length(self, indent=0):
        self._test_simple(self._test_line_length, indent=indent)
    
    @inspect_method('Naming')
    def test_naming(self, indent=0):
        self._test_simple(self._test_naming, indent=indent)
    
    @inspect_method('Docstrings')
    def test_docstring(self):
        pass
    
    @inspect_method('Encapsulation')
    def test_encapsulation(self, indent=0):
        self._test_simple(self._test_encapsulation, indent=indent)
    
    @staticmethod
    def _test_line_length(lines, content, indent=0):
        okay = True
        for line_num, line in enumerate(lines):
            if len(line) > LINE_LENGTH_LIMIT:
                print2(f"Line {line_num + 1} has {len(line)} characters.", indent=indent)
                print2(f"{line.strip()}", indent=indent + 1)
                okay = False
        return okay
    
    @classmethod
    def _test_encapsulation(cls, lines, content, indent=0):
        okay = True
        for line_num, line in enumerate(lines):
            private_outside = cls.PRIVATE_OUTSIDE_PATTERN.finditer(line)
            public_inside = cls.PUBLIC_INSIDE_PATTERN.finditer(line)
            for match in private_outside:
                print2(f'Access private attributes {match.group(0)}, line {line_num}',
                       indent=indent)
                okay = False
            for match in public_inside:
                print2(f'Allow using public attributes {match.group(1)}, line {line_num}',
                       indent=indent)
                okay = False
        return okay
    
    @classmethod
    def _test_naming(cls, lines, content, indent=0):
        okay = True
        for line_num, line in enumerate(lines):
            camel_case = cls.CAMEL_CASE.finditer(line)
            for match in camel_case:
                print2(f"camelCase: {match.group(0)}, line {line_num}", indent=indent)
                okay = False
            bad_for_name = cls.BAD_FOR_NAME.search(line)
            if bad_for_name:
                okay = False
                print2(f"Bad for name: {bad_for_name.group(0)}, line {line_num}", indent=indent)
            bad_name = cls.BAD_NAME.search(line)
            if bad_name:
                okay = False
                print2(f"Potential bad variable name: {bad_name.group(1)}, line {line_num}",
                       indent=indent)
        return okay
    
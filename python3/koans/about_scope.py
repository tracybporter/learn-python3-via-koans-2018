#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

from . import jims
from . import lisas

counter = 0  # Global


class AboutScope(Koan):
    #
    # NOTE:
    #   Look in jims.py and lisas.py to see definitions of Dog used
    #   for this set of tests
    #

    def test_dog_is_not_available_in_the_current_scope(self):
        with self.assertRaises(NameError): fido = Dog()

    def test_you_can_reference_nested_classes_using_the_scope_operator(self):
        jimmy = jims.Dog()
        # name 'jims' module name is taken from jims.py filename

        amy = lisas.Dog()
        self.assertEqual('jims dog', jimmy.identify())
        self.assertEqual('lisas dog', amy.identify())

        self.assertEqual(False, type(jimmy) == type(amy))
        self.assertEqual(False, jims.Dog == lisas.Dog)

    # ------------------------------------------------------------------

    class str:
        pass

    def test_bare_bones_class_names_do_not_assume_the_current_scope(self):
        self.assertEqual(False, AboutScope.str == str)

    def test_nested_string_is_not_the_same_as_the_system_string(self):
        self.assertEqual(False, self.str == type("HI"))

    def test_str_without_self_prefix_stays_in_the_global_scope(self):
        self.assertEqual(True, str == type("HI"))

    def test_str_with_self_prefix_and_file_prefix(self):
        self.assertEqual(True, AboutScope.str == self.str)

    # ------------------------------------------------------------------

    PI = 3.1416  # But only if you addly shaped circles

    def test_constants_are_defined_with_an_initial_uppercase_letter(self):
        self.assertAlmostEqual(3.1416, self.PI)
        # Note, floating point numbers in python are not precise.
        # assertAlmostEqual will check that it is 'close enough'

    def test_constants_are_assumed_by_convention_only(self):
        # a.k.a. there are no constants in python
        self.PI = "rhubarb"
        self.assertEqual('rhubarb', self.PI)
        # There aren't any real constants in python. Its up to the developer
        # to keep to the convention and not modify them.

    # ------------------------------------------------------------------

    def increment_using_local_counter(self, counter):
        counter = counter + 1

    def increment_using_global_counter(self):
        global counter
        counter = counter + 1

    def test_incrementing_with_local_counter(self):
        global counter
        start = counter
        self.increment_using_local_counter(start)
        self.assertEqual(False, counter == start + 1) # 1 != 2

    def test_incrementing_with_global_counter(self):
        global counter
        start = counter
        self.increment_using_global_counter()
        self.assertEqual(True, counter == start + 1)

    # ------------------------------------------------------------------

    def local_access(self):
        stuff = 'eels'

        def from_the_league():
            stuff = 'this is a local shop for local people'
            return stuff

        return from_the_league()

    def nonlocal_access(self):
        stuff = 'eels'

        def from_the_boosh():
            nonlocal stuff
            return stuff

        return from_the_boosh()

    def test_getting_something_locally(self):
        self.assertEqual('this is a local shop for local people', self.local_access())

    def test_getting_something_nonlocally(self):
        self.assertEqual('eels', self.nonlocal_access())

    # ------------------------------------------------------------------

    global deadly_bingo
    deadly_bingo = [4, 8, 15, 16, 23, 42]

    def test_global_attributes_can_be_created_in_the_middle_of_a_class(self):
        self.assertEqual(42, deadly_bingo[5])

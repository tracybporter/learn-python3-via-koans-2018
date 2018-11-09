#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutComprehension(Koan):

    # Basic syntax: [ expression for item in list if conditional ]

    def test_creating_lists_with_list_comprehensions(self):
        feast = ['lambs', 'sloths', 'orangutans', 'breakfast cereals',
                 'fruit bats']

        comprehension = [delicacy.capitalize() for delicacy in feast]

        self.assertEqual('Lambs', comprehension[0])
        self.assertEqual('Orangutans', comprehension[2])

    def test_filtering_lists_with_list_comprehensions(self):
        feast = ['spam', 'sloths', 'orangutans', 'breakfast cereals',
                 'fruit bats']

        comprehension = [delicacy for delicacy in feast if len(delicacy) > 6]

        self.assertEqual(5, len(feast))
        self.assertEqual(3, len(comprehension))

    def test_unpacking_tuples_in_list_comprehensions(self):
        list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]
        comprehension = [skit * number for number, skit in list_of_tuples]

        # string multiplication is interesting
        self.assertEqual('lumberjack', comprehension[0])
        self.assertEqual('spamspamspamspam', comprehension[2])

    def test_double_list_comprehension(self):
        list_of_eggs = ['poached', 'fried']
        list_of_meats = ['sausage', 'ham', 'bacon']

        comprehension = ['{0} egg and {1}'.format(egg, meat) for egg in list_of_eggs for meat in list_of_meats]

        self.assertEqual('poached egg and sausage', comprehension[0])
        self.assertEqual('poached egg and ham', comprehension[1])
        self.assertEqual(6, len(comprehension))

    def test_creating_a_set_with_set_comprehension(self):
        comprehension = {x for x in 'aabbbcccc'}

        self.assertEqual({'a', 'b', 'c'}, comprehension)  # remember that set members are unique

    def test_creating_a_dictionary_with_dictionary_comprehension(self):
        dict_of_weapons = {'first': 'fear', 'second': 'surprise',
                           'third': 'ruthless efficiency', 'fourth': 'fanatical devotion',
                           'fifth': None}

        dict_comprehension = {k.upper(): weapon for k, weapon in dict_of_weapons.items() if weapon}

        self.assertEqual(5, len(dict_of_weapons))
        self.assertEqual(4, len(dict_comprehension))
        self.assertEqual(False, 'first' in dict_comprehension)
        self.assertEqual(True, 'FIRST' in dict_comprehension)
        self.assertEqual('fear', dict_comprehension['FIRST'])

import unittest

from .views import (
    parse_event
)


class ParseEventTest(unittest.TestCase):

    def test_returns_correct_result(self):
        event = parse_event('I just won a lottery #update @all')
        self.assertEqual(event.text, 'I just won a lottery')
        self.assertEqual(event.category, 'update')
        self.assertEqual(event.person, 'all')

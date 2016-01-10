import unittest

from .views import (
    parse_event, add_event_to_storage, get_10_by_category, get_10_by_person,
    get_10_by_time
)


class ParseEventTest(unittest.TestCase):

    def test_returns_correct_result(self):
        event = parse_event('I just won a lottery #update @all')
        self.assertEqual(event.text, 'I just won a lottery')
        self.assertEqual(event.category, 'update')
        self.assertEqual(event.person, 'all')

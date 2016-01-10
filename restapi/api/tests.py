import unittest

from .views import (
    parse_event, add_event_to_storage
)
from .models import data


def check_the_storage(item_to_search, storage=data):
    """Check if the in-memory storage has the item

    Args:
        item_to_search (namedtuple): event tuple (text, category, person)
        storage (list): in-memory storage

    Returns:
        bool: True or False
    """
    for event in storage:
        if all((
            event.text == item_to_search.text,
            event.category == item_to_search.category,
            event.person == item_to_search.person
        )):
            return True
    return False


class ParseEventTest(unittest.TestCase):

    def test_returns_correct_result(self):
        event = parse_event('I just won a lottery #update @all')
        self.assertEqual(event.text, 'I just won a lottery')
        self.assertEqual(event.category, 'update')
        self.assertEqual(event.person, 'all')


class AddEventTest(unittest.TestCase):

    def test_correctly_adds_event_to_storage(self):
        event1 = parse_event('text #category @person')
        event2 = parse_event('hello world #category @person')
        add_event_to_storage(event1)
        self.assertTrue(check_the_storage(event1))
        self.assertFalse(check_the_storage(event2))

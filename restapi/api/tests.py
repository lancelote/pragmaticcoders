import unittest

from .views import (
    parse_event, add_event_to_storage,
    get_10_by_category
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


class TestGet10ByCategory(unittest.TestCase):

    def setUp(self):
        events = [
            'text1 #category1 @person1',
            'text2 #category1 @person2',
            'text3 #category1 @person3',
            'text4 #category1 @person4',
            'text5 #category1 @person5',
            'text6 #category2 @person6',
            'text7 #category1 @person7',
            'text8 #category1 @person8',
            'text9 #category1 @person9',
            'text10 #category1 @person10',
            'text11 #category1 @person11',
            'text12 #category1 @person12',
            'text13 #category1 @person12',
        ]
        for event in events:
            add_event_to_storage(parse_event(event))

    def test_return_correct_result(self):
        last_10_by_category = get_10_by_category('category1')
        self.assertEqual(len(last_10_by_category), 10)

        to_old = parse_event('text1 #category1 @person1')
        wrong_category = parse_event('text6 #category2 @person6')
        last_event = parse_event('text12 #category1 @person12')
        sample_event = parse_event('text8 #category1 @person8')

        self.assertFalse(check_the_storage(to_old, last_10_by_category))
        self.assertFalse(check_the_storage(wrong_category, last_10_by_category))
        self.assertTrue(check_the_storage(last_event, last_10_by_category))
        self.assertTrue(check_the_storage(sample_event, last_10_by_category))


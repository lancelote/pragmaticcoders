# pylint: disable=invalid-name, no-member

import unittest
import json

from django.test import TestCase

from .views import (
    parse_event, add_event_to_storage,
    get_10_by_category, get_10_by_person, get_10_by_time
)
from .models import data


def check_the_storage(item_to_search, storage=None):
    """Check if the in-memory storage has the item

    Args:
        item_to_search (namedtuple): event tuple (text, category, person)
        storage (list): in-memory storage

    Returns:
        bool: True or False
    """
    if storage is None:
        storage = data
    for event in storage:
        if all((event.text == item_to_search.text,
                event.category == item_to_search.category,
                event.person == item_to_search.person)):
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


class TestGet10ByPerson(unittest.TestCase):

    def setUp(self):
        events = [
            'text1 #category1 @person1',
            'text2 #category2 @person1',
            'text3 #category3 @person1',
            'text4 #category4 @person1',
            'text5 #category5 @person1',
            'text6 #category6 @person2',
            'text7 #category7 @person1',
            'text8 #category8 @person1',
            'text9 #category9 @person1',
            'text10 #category10 @person1',
            'text11 #category11 @person1',
            'text12 #category12 @person1',
        ]
        for event in events:
            add_event_to_storage(parse_event(event))

    def test_return_correct_result(self):
        last_10_by_person = get_10_by_person('person1')
        self.assertEqual(len(last_10_by_person), 10)

        to_old = parse_event('text1 #category1 @person1')
        wrong_person = parse_event('text6 #category6 @person2')
        last_event = parse_event('text12 #category12 @person1')
        sample_event = parse_event('text7 #category7 @person1')

        self.assertFalse(check_the_storage(to_old, last_10_by_person))
        self.assertFalse(check_the_storage(wrong_person, last_10_by_person))
        self.assertTrue(check_the_storage(last_event, last_10_by_person))
        self.assertTrue(check_the_storage(sample_event, last_10_by_person))


class TestGet10ByTime(unittest.TestCase):

    def setUp(self):
        events = [
            'text1 #category1 @person1',
            'text2 #category2 @person2',
            'text3 #category3 @person3',
            'text4 #category4 @person4',
            'text5 #category5 @person5',
            'text6 #category6 @person6',
            'text7 #category7 @person7',
            'text8 #category8 @person8',
            'text9 #category9 @person9',
            'text10 #category10 @person10',
            'text11 #category11 @person11',
            'text12 #category12 @person12',
        ]
        for event in events:
            add_event_to_storage(parse_event(event))

    def test_returns_correct_result(self):
        last_10_by_time = get_10_by_time()
        self.assertEqual(len(last_10_by_time), 10)

        to_old1 = parse_event('text1 #category1 @person1')
        to_old2 = parse_event('text2 #category2 @person2')
        first = parse_event('text3 #category3 @person3')
        sample = parse_event('text8 #category8 @person8')
        last = parse_event('text12 #category12 @person12')

        self.assertFalse(check_the_storage(to_old1, last_10_by_time))
        self.assertFalse(check_the_storage(to_old2, last_10_by_time))
        self.assertTrue(check_the_storage(first, last_10_by_time))
        self.assertTrue(check_the_storage(sample, last_10_by_time))
        self.assertTrue(check_the_storage(last, last_10_by_time))


class APITest(TestCase):

    def test_post(self):
        url = '/api/event/'
        content = 'application/json'
        event = json.dumps({'event': 'I just won a lottery #update @all'})

        response = self.client.post(url, content_type=content, data=event)
        self.assertEqual(response.status_code, 201)

        event_answer = json.loads(response.content.decode('utf-8'))
        self.assertEqual(event_answer['text'], 'I just won a lottery')
        self.assertEqual(event_answer['category'], 'update')
        self.assertEqual(event_answer['person'], 'all')

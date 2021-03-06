import re
import json

from django.http import HttpResponse

from .models import Event, data

PATTERN = re.compile(r'^([\w\s]+) #(\w+) @(\w+)$')


def parse_event(event):
    """Parse event string

    Args:
        event (str): 'I just won a lottery #update @all'

    Returns:
        Event: Event instance
    """
    # ToDo : Multiple categories and persons
    try:
        text, category, person = re.match(PATTERN, event).groups()
    except AttributeError:
        return False
    return Event(text, category, person)


def add_event_to_storage(event):
    """Adds event to im-memory storage

    Args:
        event (Event): Event instance

    Returns:
        None
    """
    data.append(event)


def get_10_by_category(category):
    """Return list of 10 last events by given category

    Args:
        category (str): Category to search

    Returns:
        list: last 10 events by given category
    """
    last_10_events_by_category = []
    for i in range(len(data) - 1, -1, -1):
        if len(last_10_events_by_category) == 10:
            break
        if data[i].category == category:
            last_10_events_by_category.append(data[i])
    return last_10_events_by_category


def get_10_by_person(person):
    """Return list of 10 last events by given person

    Args:
        person (str): Person to search

    Returns:
        list: last 10 events by given person
    """
    last_10_events_by_person = []
    for i in range(len(data) - 1, -1, -1):
        if len(last_10_events_by_person) == 10:
            break
        if data[i].person == person:
            last_10_events_by_person.append(data[i])
    return last_10_events_by_person


def get_10_by_time():
    """Return list of 10 last events

    Returns:
        list: last 10 events
    """
    last_10_events_by_time = []
    for i in range(len(data) - 1, -1, -1):
        if len(last_10_events_by_time) == 10:
            break
        else:
            last_10_events_by_time.append(data[i])
    return last_10_events_by_time


def post_event(request):
    """Add event from request to storage

    Args:
        request: HTTP request

    Returns:
        HTTP response with json data
    """
    if request.method == 'POST':
        content_type = 'application/json'
        try:
            event_request = json.loads(request.body.decode('utf-8'))
        except ValueError:
            answer = json.dumps({'error': 'Please provide event JSON'})
            status_code = 400
        else:
            event = parse_event(event_request['event'])

            if event is False:
                answer = json.dumps({'error': 'Wrong event format'})
                status_code = 400
            else:
                add_event_to_storage(event)
                answer = json.dumps({
                    'text': event.text,
                    'category': event.category,
                    'person': event.person,
                    'time': event.time
                })
                status_code = 201
        return HttpResponse(answer, content_type, status_code)


def last_10_by_category(request, category):
    """Return last 10 events by given category as HTTP response with json

    Args:
        request: HTTP request
        category (str): Event category to search for

    Returns:
        HTTP response with json data
    """
    if request.method == 'GET':
        events = get_10_by_category(category)
        answer = json.dumps([event.__dict__ for event in events])
        return HttpResponse(answer, content_type='application/json')


def last_10_by_person(request, person):
    """Return last 10 events by given person as HTTP response with json

    Args:
        request: HTTP request
        person (str): Event person to search for

    Returns:
        HTTP response with json data
    """
    if request.method == 'GET':
        events = get_10_by_person(person)
        answer = json.dumps([event.__dict__ for event in events])
        return HttpResponse(answer, content_type='application/json')


def last_10_by_time(request):
    """Return last 10 events by time as HTTP response with json

    Args:
        request: HTTP request

    Returns:
        HTTP response with json data
    """
    if request.method == 'GET':
        events = get_10_by_time()
        answer = json.dumps([event.__dict__ for event in events])
        return HttpResponse(answer, content_type='application/json')

[![Requirements Status](https://requires.io/github/lancelote/pragmaticcoders/requirements.svg?branch=master)](https://requires.io/github/lancelote/pragmaticcoders/requirements/?branch=master)
[![Build Status](https://travis-ci.org/lancelote/pragmaticcoders.svg?branch=master)](https://travis-ci.org/lancelote/pragmaticcoders)

# Add event

- URL: /api/event/
- HTTP Method: POST

## Example Request

```
{
    "event": "I just won a lottery #update @all"
}
```

## Example Response

```
{
    "text": "I just won a lottery",
    "category": "update",
    "person": "all",
    "time": "04.08.2015 - 16:23:42"
}
```

# Get 10 last by Category

- URL: /api/category/category_name/
- HTTP Method: GET

## Example Response

```
[
    {
        "text": "Hello world",
        "category": "update",
        "person": "world",
        "time": "04.08.2015 - 16:23:42"
    },
    {
        "text": "I just won a lottery",
        "category": "update",
        "person": "all",
        "time": "01.01.2016 - 12:00:00"
    },
    ...
]
```

# Get 10 last by Person

- URL: /api/person/person_name/
- HTTP Method: GET

# Get 10 last by Time

- URL: /api/time/
- HTTP Method: GET

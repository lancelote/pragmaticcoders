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
    "time": "01.01.2016 - 12:00"
}
```

# Get 10 last by Category

- URL: /api/category/<category_name>/
- HTTP Method: GET

# Get 10 last by Person

- URL: /api/person/<person_name>/
- HTTP Method: GET

# Get 10 last by Time

- URL: /api/time/
- HTTP Method: GET

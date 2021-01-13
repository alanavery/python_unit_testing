cities = [
    {
        'name': 'Chicago',
        'state': 'Illinois'
    },
    {
        'name': 'Austin',
        'state': 'Texas'
    },
    {
        'name': 'Portland',
        'state': 'Oregon'
    },
]


def locate_city(target):
    for city in cities:
        if city['name'] == target:
            return city['state']
    return 'That city does not exist.'

from chalice import Chalice

app = Chalice(app_name='global_slackination')

countries = {
    'western_australia': {
        'bordering': [],
        'continent': 'oceania'
    },
    'eastern_australia': {
        'bordering': [],
        'continent': 'oceania'
    },
    'new_guinea': {
        'bordering': [],
        'continent': 'oceania'
    },
    'indonesia': {
        'bordering': [],
        'continent': 'oceania'
    },
    'siam': {
        'bordering': [],
        'continent': 'asia'
    },
    'china': {
        'bordering': [],
        'continent': 'asia'
    },
    'india': {
        'bordering': [],
        'continent': 'asia'
    },
    'mongolia': {
        'bordering': [],
        'continent': 'asia'
    },
    'japan': {
        'bordering': [],
        'continent': 'asia'
    },
    'kamchatka': {
        'bordering': [],
        'continent': 'asia'
    },
    'yakutsk': {
        'bordering': [],
        'continent': 'asia'
    },
    'irkutsk': {
        'bordering': [],
        'continent': 'asia'
    },
    'siberia': {
        'bordering': [],
        'continent': 'asia'
    },
    'ural': {
        'bordering': [],
        'continent': 'asia'
    },
    'afghanistan': {
        'bordering': [],
        'continent': 'asia'
    },
    'middle_east': {
        'bordering': [],
        'continent': 'asia'
    },
    'egypt': {
        'bordering': [],
        'continent': 'africa'
    },
    'east_africa': {
        'bordering': [],
        'continent': 'africa'
    },
    'north_africa': {
        'bordering': [],
        'continent': 'africa'
    },
    'congo': {
        'bordering': [],
        'continent': 'africa'
    },
    'south_africa': {
        'bordering': [],
        'continent': 'africa'
    },
    'madagascar': {
        'bordering': [],
        'continent': 'africa'
    },
    'brazil': {
        'bordering': [],
        'continent': 'south_america'
    },
    'argentina': {
        'bordering': [],
        'continent': 'south_america'
    },
    'peru': {
        'bordering': [],
        'continent': 'south_america'
    },
    'venezuela': {
        'bordering': [],
        'continent': 'south_america'
    },
    'central_america': {
        'bordering': [],
        'continent': 'north_america'
    },
    'western_united_states': {
        'bordering': [],
        'continent': 'north_america'
    },
    'eastern_united_states': {
        'bordering': [],
        'continent': 'north_america'
    },
    'ontario': {
        'bordering': [],
        'continent': 'north_america'
    },
    'quebec': {
        'bordering': [],
        'continent': 'north_america'
    },
    'alberta': {
        'bordering': [],
        'continent': 'north_america'
    },
    'alaska': {
        'bordering': [],
        'continent': 'north_america'
    },
    'northwest_territory': {
        'bordering': [],
        'continent': 'north_america'
    },
    'greenland': {
        'bordering': [],
        'continent': 'north_america'
    },
    'great_britain': {
        'bordering': [],
        'continent': 'europe'
    },
    'iceland': {
        'bordering': [],
        'continent': 'europe'
    },
    'scandanavia': {
        'bordering': [],
        'continent': 'europe'
    },
    'west_europe': {
        'bordering': [],
        'continent': 'europe'
    },
    'north_europe': {
        'bordering': [],
        'continent': 'europe'
    },
    'south_europe': {
        'bordering': [],
        'continent': 'europe'
    },
    'ukraine': {
        'bordering': [],
        'continent': 'europe'
    }
}


@app.route('/')
def index():
    return {'hello': 'world'}

from chalice import Chalice
import os
import time
import re
import json

from slackclient import SlackClient

app = Chalice(app_name='global_slackination')

sc = SlackClient('xoxb-317583176002-488108846711-kxuLuBeTboOiIPRb5IgqgN9U')
channel = 'general'

countries = {
    'western_australia': {
        'bordering': ['indonesia', 'new_guinea', 'eastern_australia'],
        'continent': 'oceania'
    },
    'eastern_australia': {
        'bordering': ['new_guinea', 'indonesia'],
        'continent': 'oceania'
    },
    'new_guinea': {
        'bordering': ['indonesia', 'western_australia', 'eastern_australia'],
        'continent': 'oceania'
    },
    'indonesia': {
        'bordering': ['western_australia', 'new_guinea'],
        'continent': 'oceania'
    },
    'siam': {
        'bordering': ['india', 'china', 'indonesia'],
        'continent': 'asia'
    },
    'china': {
        'bordering': ['india', 'siam', 'mongolia', 'siberia', 'ural', 'afghanistan'],
        'continent': 'asia'
    },
    'india': {
        'bordering': ['siam', 'china', 'afghanistan', 'middle_east'],
        'continent': 'asia'
    },
    'mongolia': {
        'bordering': ['japan', 'irkutsk', 'china', 'siberia', 'kamchatka'],
        'continent': 'asia'
    },
    'japan': {
        'bordering': ['mongolia', 'kamchatka'],
        'continent': 'asia'
    },
    'kamchatka': {
        'bordering': ['yakutsk', 'irkutsk', 'mongolia', 'japan', 'alaska'],
        'continent': 'asia'
    },
    'yakutsk': {
        'bordering': ['kamchatka', 'irkutsk', 'siberia'],
        'continent': 'asia'
    },
    'irkutsk': {
        'bordering': ['siberia', 'mongolia', 'yakutsk', 'kamchatka'],
        'continent': 'asia'
    },
    'siberia': {
        'bordering': ['ural', 'irkutsk', 'yakutsk', 'mongolia', 'china'],
        'continent': 'asia'
    },
    'ural': {
        'bordering': ['afghanistan', 'china', 'siberia', 'ukraine'],
        'continent': 'asia'
    },
    'afghanistan': {
        'bordering': ['ukraine', 'china', 'india', 'ural', 'middle_east'],
        'continent': 'asia'
    },
    'middle_east': {
        'bordering': ['ukraine', 'india', 'egypt', 'afghanistan', 'east_africa', 'south_europe'],
        'continent': 'asia'
    },
    'egypt': {
        'bordering': ['north_africa', 'east_africa', 'middle_east', 'south_europe'],
        'continent': 'africa'
    },
    'east_africa': {
        'bordering': ['egypt', 'middle_east', 'madagascar', 'congo', 'south_africa', 'north_africa'],
        'continent': 'africa'
    },
    'north_africa': {
        'bordering': ['egypt', 'east_africa', 'congo', 'south_europe', 'west_europe', 'brazil'],
        'continent': 'africa'
    },
    'congo': {
        'bordering': ['north_africa', 'east_africa', 'south_africa'],
        'continent': 'africa'
    },
    'south_africa': {
        'bordering': ['congo', 'madagascar', 'east_africa'],
        'continent': 'africa'
    },
    'madagascar': {
        'bordering': ['east_africa', 'south_africa'],
        'continent': 'africa'
    },
    'brazil': {
        'bordering': ['peru', 'venezuela', 'argentina', 'north_africa'],
        'continent': 'south_america'
    },
    'argentina': {
        'bordering': ['brazil', 'peru'],
        'continent': 'south_america'
    },
    'peru': {
        'bordering': ['brazil', 'argentina', 'venezuela'],
        'continent': 'south_america'
    },
    'venezuela': {
        'bordering': ['peru', 'brazil', 'central_america'],
        'continent': 'south_america'
    },
    'central_america': {
        'bordering': ['venezuela', 'western_united_states', 'eastern_united_states'],
        'continent': 'north_america'
    },
    'western_united_states': {
        'bordering': ['central_america', 'eastern_united_states', 'alberta', 'ontario'],
        'continent': 'north_america'
    },
    'eastern_united_states': {
        'bordering': ['quebec', 'ontario', 'western_united_states', 'central_america'],
        'continent': 'north_america'
    },
    'ontario': {
        'bordering': ['eastern_united_states', 'western_united_states', 'quebec', 'greenland', 'alberta', 'northwest_territory'],
        'continent': 'north_america'
    },
    'quebec': {
        'bordering': ['greenland', 'eastern_united_states', 'ontario'],
        'continent': 'north_america'
    },
    'alberta': {
        'bordering': ['ontario', 'western_united_states', 'northwest_territory', 'alaska'],
        'continent': 'north_america'
    },
    'alaska': {
        'bordering': ['northwest_territory', 'alberta', 'kamchatka'],
        'continent': 'north_america'
    },
    'northwest_territory': {
        'bordering': ['alaska', 'alberta', 'ontario', 'greenland'],
        'continent': 'north_america'
    },
    'greenland': {
        'bordering': ['quebec', 'ontario', 'northwest_territory', 'iceland'],
        'continent': 'north_america'
    },
    'great_britain': {
        'bordering': ['iceland', 'scandanavia', 'north_europe', 'west_europe'],
        'continent': 'europe'
    },
    'iceland': {
        'bordering': ['greenland', 'scandanavia', 'great_britain'],
        'continent': 'europe'
    },
    'scandanavia': {
        'bordering': ['ukraine', 'north_europe', 'great_britain', 'iceland'],
        'continent': 'europe'
    },
    'west_europe': {
        'bordering': ['great_britain', 'north_europe', 'south_europe', 'north_africa'],
        'continent': 'europe'
    },
    'north_europe': {
        'bordering': ['great_britain', 'south_europe', 'west_europe', 'ukraine', 'scandanavia'],
        'continent': 'europe'
    },
    'south_europe': {
        'bordering': ['egypt', 'north_africa', 'middle_east', 'ukraine', 'north_europe', 'west_europe'],
        'continent': 'europe'
    },
    'ukraine': {
        'bordering': ['afghanistan', 'middle_east', 'scandanavia', 'north_europe', 'south_europe', 'ural'],
        'continent': 'europe'
    }
}

# class Territory(object):
#     name
#
# class Player(object):
#     name
#     territories
#     cards
#
# class Game(object):
#     active



@app.route('/', methods=['GET', 'POST'])
def index():
    print('zz')
    request = app.current_request

    request_body = request.__dict__.get('_body')
    payload = json.loads(request_body)
    event = payload.get('event')

    #Check to see if game is already currently active
    if 'start game' in event.get('text', ''):
        return sc.api_call(
            "chat.postMessage",
            channel='general',
            text='Starting a game of Risk, How Many Players?',
        )

    #

    return {'payload': 'challenge'}

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'rust',
    'phil' : 'python'
}

please_poll = ['edward', 'martin', 'maik', 'carla', 'jen']

for name in please_poll:
    if name in favorite_languages.keys():
        print(f'Thanks for taking the poll {name.title()}')
    else:
        print(f'Hey {name.title()}, please take the poll.')
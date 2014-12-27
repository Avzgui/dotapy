__author__ = 'antoine'


import requests
from BeautifulSoup import BeautifulSoup

r = requests.get('http://playdota.com/heroes/admiral')

hero = {
        'id': 1,
        'name': '',
        'surname': '',
        'MainStat': '',
        'baseAgility': '',
        'baseStrength': '',
        'baseIntelligence': '',
        'gainAgility': '',
        'gainStrength': '',
        'gainIntelligence': '',
        'affiliation': '',
        'damage': '',
        'armor': '',
        'moveSpeed': '',
        'attackRange': '',
        'attackAnimation': '',
        'CastingAnimation': '',
        'BaseAttackTime': '',
        'MissileSpeed': '',
        'SightRange': '',
        'introduction': '',
    }


if r.status_code == 200:
    print('Ok:')
    soup = BeautifulSoup(r.text)
    name = soup.findAll('h1')
    name = BeautifulSoup(name).find('img',attrs={'alt':True})

    surname = [h2.text for h2 in soup.findAll('h1', attrs={'class': 'class'})]
    description = soup.find(id="info").p.text
    print(name)
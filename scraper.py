__author__ = 'antoine'


import requests, re, json
from bs4 import BeautifulSoup

#r = requests.get('http://playdota.com/heroes/admiral')
# we dont spam playdota.com
r = open("test.html",'r')


str = re.compile("^Strength")
a = re.compile("^Agility")
i = re.compile("^Intelligence")

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
        'damageMin': '',
        'damageMax': '',
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

def extract(s):
    l = []
    try:
        concat = ''
        if(str.match(s)):
            hero['baseStrength'] = re.findall("Strength (\d+)", s)[0]
            if re.findall("\+ [-+]?[0-9]*\.?[0-9]+$", s).__len__() == 1:
                hero['gainStrength'] = re.findall("[-+]?[0-9]*\.?[0-9]+$", s)[0]
            else:
                hero['gainStrength'] =  re.findall("\+ (\d+)", s)[0]
        elif(a.match(s)):
            hero['baseAgility'] = re.findall("Agility (\d+)", s)[0]
            if re.findall("\+ [-+]?[0-9]*\.?[0-9]+$", s).__len__() == 1:
                hero['gainAgility'] = re.findall("[-+]?[0-9]*\.?[0-9]+$", s)[0]
            else:
                hero['gainAgility'] =  re.findall("\+ (\d+)", s)[0]
        elif(i.match(s)):
            hero['baseIntelligence'] = re.findall("Intelligence (\d+)", s)[0]
            if re.findall("\+ [-+]?[0-9]*\.?[0-9]+$", s).__len__() == 1:
                hero['gainIntelligence'] = re.findall("[-+]?[0-9]*\.?[0-9]+$", s)[0]
            else:
                hero['gainIntelligence'] =  re.findall("\+ (\d+)", s)[0]
    except ValueError:
        pass
    return l




#if r.status_code == 200:
print('Ok:')
soup = BeautifulSoup(r)
hLeft = soup.find('div',attrs={'class':'hLeft'})
hRight = soup.find('div',attrs={'class':'hRight'})

hero['name'] = hLeft.h1.findAll('img',attrs={'alt':True})[0]['alt']
hero['surname'] = [h2.text for h2 in soup.findAll('h1', attrs={'class': 'class'})][0]
hero['introduction'] = soup.find(id="info").p.text

all = [h2.text for h2 in hLeft.findAll('li')]

advanced = soup.findAll('ul', attrs={'class':'adv'})

#for strong_tag in advanced:
#    for li in strong_tag:
#       print '(',li, ')'



#------------------------------
# Extract base and gain stats
total = []
for test in all:
    extract(test)
#------------------------------




print json.dumps(hero, indent=4, sort_keys=True)

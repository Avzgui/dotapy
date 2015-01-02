__author__ = 'antoine'


import requests, re, json
from BeautifulSoup import BeautifulSoup

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
    for t in s.split():
        try:
            if(t.isdigit()):
                l.append(t)
            elif(str.match(t)):
                hero['baseStrength'] = re.findall("Strength(\d+)", t)[0]
            elif(a.match(t)):
                hero['baseAgility'] = re.findall("Agility(\d+)", t)[0]
            elif(i.match(t)):
                hero['baseIntelligence'] = re.findall("Intelligence(\d+)", t)[0]
            else:
                l.append(float(t))
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

advanced = hRight.findAll('ul', attrs={'class':'adv'})

for tu in advanced[0]:
    if tu.li is not None:
        print tu.li



#------------------------------
total = []
for test in all:
    total.append(extract(test))

hero['gainStrength'] = total[0][0]
hero['gainIntelligence'] = total[1][0]
hero['gainAgility'] = total[2][0]

#------------------------------




print json.dumps(hero, indent=4, sort_keys=True)

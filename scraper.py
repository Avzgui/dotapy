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
        'BaseAttackTime': '',
        'MissileSpeed': '',
        'SightRange': '',
        'introduction': '',
        'background': '',
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
hero['background'] = soup.find(id="info").findAll('p')[1].text

all = [h2.text for h2 in hLeft.findAll('li')]

advanced = soup.findAll('ul', attrs={'class':'adv'})

advStats = []
for ul in advanced:
    for li in ul:
        if "\n" not in li:
            if re.findall("^ Affiliation",li.text).__len__() == 1:
                hero['affiliation'] =  li.label.next_sibling.strip()
            if re.findall("^ Damage",li.text).__len__() == 1:
                hero['damageMin'] = re.split("-",li.label.next_sibling.strip())[0].strip()
                hero['damageMax'] =  re.split("-",li.label.next_sibling.strip())[1].strip()
            if re.findall("^ Armor",li.text).__len__() == 1:
                hero['armor'] =  li.label.next_sibling.strip()
            if re.findall("^ Movespeed",li.text).__len__() == 1:
                hero['moveSpeed'] =  li.label.next_sibling.strip()
            if re.findall("^ Missile Speed:",li.text).__len__() == 1:
                hero['MissileSpeed'] =  li.label.next_sibling.strip()
            if re.findall("^ Sight Range",li.text).__len__() == 1:
                hero['SightRangeDay'] =  re.split("/",li.label.next_sibling.strip())[0].strip()
                hero['SightRangeNight'] =  re.split("/",li.label.next_sibling.strip())[1].strip()
            if re.findall("^ Base Attack Time",li.text).__len__() == 1:
                hero['BaseAttackTime'] =  li.label.next_sibling.strip()
            if re.findall("^ Casting Animation",li.text).__len__() == 1:
                hero['CastingAnimationPoint'] =  re.split("/",li.label.next_sibling.strip())[0].strip()
                hero['CastingAnimationBackswing'] =  re.split("/",li.label.next_sibling.strip())[1].strip()
            if re.findall("^ Attack Animation",li.text).__len__() == 1:
                hero['attackAnimationPoint'] =  re.split("/",li.label.next_sibling.strip())[0].strip()
                hero['attackAnimationBackswing'] =  re.split("/",li.label.next_sibling.strip())[1].strip()
            if re.findall("^ Attack Range",li.text).__len__() == 1:
                hero['attackRangeValue'] =  re.split("\(",li.label.next_sibling.strip())[0].strip()
                hero['attackRangeType'] =  re.split("\)",re.split("\(",li.label.next_sibling.strip())[1].strip())[0]





#------------------------------
# Extract base and gain stats
total = []
for test in all:
    extract(test)
#------------------------------




print json.dumps(hero, indent=4, sort_keys=True)

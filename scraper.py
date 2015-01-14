__author__ = 'antoine'

from app.models import Hero
import requests, re, json
from app import db, models
from bs4 import BeautifulSoup

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
    'attackRangeType': '',
    'attackRangeValue': '',
    'moveSpeed': '',
    'BaseAttackTime': '',
    'missileSpeed': '',
    'sightRangeDay': '',
    'sightRangeNight': '',
    'introduction': '',
    'background': '',
    'attackAnimationBackswing': '',
    'attackAnimationPoint': '',
}

def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)


def addInDB(h):
    u = models.Hero(name=h['name'],
                    surname=h['surname'],
                    background=h['background'],
                    introduction=h['introduction'],
                    baseStrength=h['baseStrength'],
                    baseAgility=h['baseAgility'],
                    baseIntelligence=h['baseIntelligence'],
                    gainStrength=h['gainStrength'],
                    gainAgility=h['gainAgility'],
                    gainIntelligence=h['gainIntelligence'],
                    affiliation=h['affiliation'],
                    armor=h['armor'],
                    moveSpeed=h['moveSpeed'],
                    damageMin=h['damageMin'],
                    damageMax=h['damageMax'],
                    missileSpeed=h['missileSpeed'],
                    # sightRangeDay=h['sightRangeDay'],
                    # sightRangeNight=h['sightRangeNight'],
                    baseAttackTime=h['baseAttackTime'],
                    castingAnimationPoint=h['castingAnimationPoint'],
                    castingAnimationBackswing=h['castingAnimationBackswing'],
                    attackAnimationPoint=h['attackAnimationPoint'],
                    attackAnimationBackswing=h['attackAnimationBackswing'],
                    attackRangeValue=h['attackRangeValue'],
                    attackRangeType=h['attackRangeType']
    )
    db.session.add(u)
    db.session.commit()
    print 'insert bdd ok'


str = re.compile("^Strength")
a = re.compile("^Agility")
i = re.compile("^Intelligence")


def extract(s):
    l = []
    try:
        concat = ''
        if (str.match(s)):
            hero['baseStrength'] = float(re.findall("Strength (\d+)", s)[0])
            if re.findall("\+ [-+]?[0-9]*\.?[0-9]+$", s).__len__() == 1:
                hero['gainStrength'] = float(re.findall("[-+]?[0-9]*\.?[0-9]+$", s)[0])
            else:
                hero['gainStrength'] = float(re.findall("\+ (\d+)", s)[0])
        elif (a.match(s)):
            hero['baseAgility'] = float(re.findall("Agility (\d+)", s)[0])
            if re.findall("\+ [-+]?[0-9]*\.?[0-9]+$", s).__len__() == 1:
                hero['gainAgility'] = float(re.findall("[-+]?[0-9]*\.?[0-9]+$", s)[0])
            else:
                hero['gainAgility'] = float(re.findall("\+ (\d+)", s)[0])
        elif (i.match(s)):
            hero['baseIntelligence'] = float(re.findall("Intelligence (\d+)", s)[0])
            if re.findall("\+ [-+]?[0-9]*\.?[0-9]+$", s).__len__() == 1:
                hero['gainIntelligence'] = float(re.findall("[-+]?[0-9]*\.?[0-9]+$", s)[0])
            else:
                hero['gainIntelligence'] = float(re.findall("\+ (\d+)", s)[0])
    except ValueError:
        pass
    return l


r = requests.get('http://www.playdota.com/heroes')

if r.status_code == 200:
    print('All Hero :')
    soup = BeautifulSoup(r.text)
    div = soup.findAll('div', attrs={'class': 'herolist'})

    for ul in div:
        for li in ul.findAll('li'):
            url = "http://www.playdota.com" + li.a['href']
            r = requests.get(url)

            if r.status_code == 200:
                print('Parsing du Hero :' + url)
                soup = BeautifulSoup(r.text)
                hLeft = soup.find('div', attrs={'class': 'hLeft'})
                hRight = soup.find('div', attrs={'class': 'hRight'})

                hero['name'] = hLeft.h1.findAll('img', attrs={'alt': True})[0]['alt']
                hero['surname'] = [h2.text for h2 in soup.findAll('h1', attrs={'class': 'class'})][0]
                hero['introduction'] = soup.find(id="info").p.text
                hero['background'] = soup.find(id="info").findAll('p')[1].text

                all = [h2.text for h2 in hLeft.findAll('li')]

                advanced = soup.findAll('ul', attrs={'class': 'adv'})

                # ------------------------------
                # Extract base and gain stats
                total = []
                for test in all:
                    extract(test)
                #------------------------------

                advStats = []
                for ul in advanced:
                    for li in ul:
                        if "\n" not in li:
                            if re.findall("^ Affiliation", li.text).__len__() == 1:
                                hero['affiliation'] = li.label.next_sibling.strip()
                            if re.findall("^ Damage", li.text).__len__() == 1:
                                hero['damageMin'] = num(re.split("-", li.label.next_sibling.strip())[0].strip())
                                hero['damageMax'] = num(re.split("-", li.label.next_sibling.strip())[1].strip())
                            if re.findall("^ Armor", li.text).__len__() == 1:
                                hero['armor'] = num(li.label.next_sibling.strip())
                            if re.findall("^ Movespeed", li.text).__len__() == 1:
                                hero['moveSpeed'] = num(li.label.next_sibling.strip())
                            if re.findall("^ Missile Speed:", li.text).__len__() == 1:
                                hero['missileSpeed'] = li.label.next_sibling.strip()
                            if re.findall("^ Base Attack Time", li.text).__len__() == 1:
                                hero['baseAttackTime'] = num(li.label.next_sibling.strip())
                            if re.findall("^ Casting Animation", li.text).__len__() == 1:
                                hero['castingAnimationPoint'] = num(re.split("/", li.label.next_sibling.strip())[0].strip())
                                hero['castingAnimationBackswing'] = num(re.split("/", li.label.next_sibling.strip())[1].strip())
                            if re.findall("^ Attack Animation", li.text).__len__() == 1:
                                hero['attackAnimationPoint'] = num(re.split("/", li.label.next_sibling.strip())[0].strip())
                                hero['attackAnimationBackswing'] = num(re.split("/", li.label.next_sibling.strip())[1].strip())
                            if re.findall("^ Attack Range", li.text).__len__() == 1:
                                attackRange = re.split("\(", li.label.next_sibling.strip())[0]
                                hero['attackRangeValue'] = num(re.split("\(", li.label.next_sibling.strip())[0].strip())
                                if attackRange.__len__() == 1:
                                   hero['attackRangeType'] = re.split("\)", re.split("\(", li.label.next_sibling.strip())[1].strip())[0]

                                addInDB(hero)
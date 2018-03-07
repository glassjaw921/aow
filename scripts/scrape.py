import bs4, requests, csv
req = requests.get('http://www.espn.com/nfl/team/roster/_/name/dal/dallas-cowboys')
soup = bs4.BeautifulSoup(req.text, 'html.parser')

table_data_list = soup.findAll('tr', {'class':'oddrow'})

for i in table_data_list:
    listicle = i.findAll('td')
    grabbing = True
    while grabbing:
        for j in listicle:
            NO = listicle[0].text
            NAME = listicle[1].text
            POS = listicle[2].text
            AGE = listicle[3].text
            HT = listicle[4].text
            WT = listicle[5].text
            exp = listicle[6].text
            college = listicle[7].text
            stats = [NO, NAME, POS, AGE, HT, WT, exp, college]
            with open('test.csv', 'a', newline='') as s:
                writer = csv.writer(s)
                writer.writerow(stats)
            break
        grabbing = False

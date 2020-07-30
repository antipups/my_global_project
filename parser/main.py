import re
import util
import requests
import bs4


def parse():
    html = requests.get('https://blog.python.org/').text
    soup = bs4.BeautifulSoup(html, 'html.parser')
    news = soup.findAll('div', attrs={'class': "date-outer"})
    for new in news:
        date = new.find('h2', attrs={'class': "date-header"}).text
        title = new.find('h3', attrs={'class': "post-title entry-title"}).text[1:-1]
        data = re.sub(r'\n{2,100}', '\n', new.find('div', attrs={'class': "post-body entry-content"}).text)
        print(data)
        # util.insert_in_db(date, title, data)


if __name__ == '__main__':
    parse()
import requests
import bs4


def download(url, output_filename):
    url_object = requests.get(url)
    if url_object.status_code == 200:
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(url_object.text)


def make_pretty(url, output_filename):
    url_object = requests.get(url)
    if url_object.status_code == 200:
        website = bs4.BeautifulSoup(url_object.text, features='html.parser')
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(website.prettify())


def find_paragraphs(url, output_filename):
    url_object = requests.get(url)
    if url_object.status_code == 200:
        website = bs4.BeautifulSoup(url_object.text, features='html.parser')
        texts = website.find_all('p')
        with open(output_filename, 'w', encoding='utf-8') as file:
            for text in texts:
                file.write(str(text))
                file.write('\n')


def find_links(url, output_filename):
    attributes = []
    url_object = requests.get(url)
    if url_object.status_code == 200:
        website = bs4.BeautifulSoup(url_object.text, features='html.parser')
        links = website.find_all('a')
        for link in links:
            attributes.append(link.get('href'))
        with open(output_filename, 'w', encoding='utf-8') as file:
            for attr in attributes:
                file.write(attr)
                file.write('\n')

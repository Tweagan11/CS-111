import requests
import bs4
import sys

def scavenge(url, tag, s_attr):
    r = requests.get(url)
    if r.status_code == 200:
        website = bs4.BeautifulSoup(r.content, 'html.parser')
        result = website.find(tag, {s_attr:True})
        if result:
            attr_value = result.get(s_attr)
            if s_attr == "final":
                with open(outfile, 'w') as of:
                    of.write(attr_value)

            else:
                parsed_values = attr_value.split(',')
                scavenge(parsed_values[0], parsed_values[1], parsed_values[2])



if __name__ == "__main__":
    website_url = sys.argv[1]
    tag = sys.argv[2]
    attr = sys.argv[3]
    outfile = sys.argv[4]
    scavenge(website_url, tag, attr)


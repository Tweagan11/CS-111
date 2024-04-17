import RequestGuard
import sys
import matplotlib.pyplot as plt
import bs4
import requests
from urllib.parse import urljoin

class LinkAnalyzer:
    def __init__(self, initial_url, output_path1, output_path2):
        self.initial_url = initial_url
        self.links_to_visit = [initial_url]
        self.visited_links = set()
        self.link_counter = {}
        self.guard = RequestGuard.RequestGuard(initial_url)
        self.output_path1 = output_path1
        self.output_path2 = output_path2

    def run(self):
        while self.links_to_visit:
            current_link = self.links_to_visit.pop(0)
            print(current_link)
            if self.can_visit(current_link):
                self.visit_link(current_link)
        self.output_results()

    def can_visit(self, current_link):
        if self.guard.can_follow_link(current_link) and current_link not in self.visited_links:
            return True
        return False

    def visit_link(self, url):
        self.visited_links.add(url)
        page = requests.get(url)
        html = bs4.BeautifulSoup(page.content, 'html.parser')
        for tag in html.find_all('a'):
            href = tag.get('href')
            if href and not href == 'javascript:history.back()' and not href.startswith('mailto'):
                full_url = self.fix_url(url, href)
                if full_url not in self.visited_links:
                    self.links_to_visit.append(full_url)
                self.link_counter[full_url] = self.link_counter.get(full_url, 0) + 1

    def fix_url(self, base_link, relative_url):
        base_link = base_link.split('#')[0].split('?')[0]  # Existing cleaning steps
        absolute_url = urljoin(base_link, relative_url)
        absolute_url = absolute_url.split('#')[0]  # Remove '#' and following content
        return absolute_url

    def output_results(self):
        links = list(self.link_counter.keys())
        counts = list(self.link_counter.values())
        bins = [i for i in range(1, max(counts))]
        v1, v2, v3 = plt.hist(counts)
        print(v1)
        print(v2)
        plt.show()
        with open(self.output_path1, 'w') as of:
            plt.savefig(of)




if __name__ == "__main__":
    command, arg2, arg3, arg4 = sys.argv[1:]
    link = LinkAnalyzer('https://cs111.byu.edu/proj/proj4/assets/page1.html', arg3, arg4)
    link.run()


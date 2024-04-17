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
        self.link_counter = {initial_url: 1}
        self.guard = RequestGuard.RequestGuard(initial_url)
        self.output_path1 = output_path1
        self.img_change = output_path2

    def c_run(self):
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
            # self.link_counter[href] = self.link_counter.get(href, 0) + 1
            if not href == 'javascript:history.back()' and not href.startswith('mailto'):
                full_url = self.fix_url(url, href)
                print(full_url)
                self.link_counter[full_url] = self.link_counter.get(full_url, 0) + 1
                if full_url not in self.visited_links:
                    self.links_to_visit.append(full_url)


    def fix_url(self, base_link, relative_url):
        base_link = base_link.split('#')[0].split('?')[0]  # Existing cleaning steps
        absolute_url = urljoin(base_link, relative_url)
        absolute_url = absolute_url.split('#')[0]  # Remove '#' and following content
        return absolute_url

    def output_results(self):
        links = list(self.link_counter.keys())
        print(links)
        counts = list(self.link_counter.values())
        print(counts)
        print(self.link_counter)
        print(max(counts))
        bins = [i for i in range(1, (max(counts) + 2))]
        print(bins)
        v1, v2, v3 = plt.hist(counts, bins=bins)
        print(v1)
        print(v2)
        plt.savefig(self.output_path1)
        with open(self.img_change, 'w') as of:
            for i in range(len(v1)):
                of.write(f'{v2[i]},{v1[i]}\n')




if __name__ == "__main__":
    command, arg2, arg3, arg4 = sys.argv[1:]
    if command == '-c':
        link = LinkAnalyzer(arg2, arg3, arg4)
        link.c_run()
    if command == '-p':



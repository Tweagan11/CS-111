import requests
import bs4
import re

class RequestGuard():
    def __init__(self, domain):
        self.domain = domain
        self.forbidden = []
        self.parse_robots()

    def can_follow_link(self, url):
        # Using regex to extract the domain from the URL
        pattern = re.compile(r"^(?:https?:\/\/)?(?:www\.)?([^\/]+)")
        match = pattern.search(url)
        if match:
            domain = match.group(0)
            print(domain)
            # Compare the extracted domain with the original domain
            if domain == self.domain:
                # Check if URL is not in forbidden links
                for forbidden in self.forbidden:
                    if url.startswith(self.domain + forbidden):
                        return False
                return True
        return False
    def make_get_request(self, *args, **kwargs):
        if self.can_follow_link(args[0]):
            return requests.get(args[0])
        return None
    def parse_robots(self):
        url = requests.get(self.domain + '/robots.txt')
        disallow = False
        for line in url.text.split():
            if disallow:
                self.forbidden.append(line)
                disallow = False
            if line == "Disallow:":
                disallow = True

def get_request_guard():
    guard = RequestGuard("https://cs111.byu.edu")
    # Mocking a different robots.txt
    guard.forbidden = ['/data', '/images', '/lectures']
    return guard

if __name__ == '__main__':
    guard = get_request_guard()
    print(guard.can_follow_link('https://cs111.byu.edu/HW/HW01'))
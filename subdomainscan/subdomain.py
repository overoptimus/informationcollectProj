import re
import requests
import random
import bs4
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


class SubdomainUtil:
    def __init__(self, domain):
        domain = str(domain)
        if domain.startswith('https://'):
            domain = domain.lstrip('https://')
        elif domain.startswith('http://'):
            domain = domain.lstrip('http://')
        if domain.startswith('www.'):
            domain = domain.lstrip('www.')
        print(domain)
        self.domain = domain
        self.result = {}
        self.final_result = []
        self.subdomain_list = []
        self.title_list = []
        self.only_subdomain = []

    def open_url(self, page):
        # chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        # driver = webdriver.Chrome('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe',
        #                           chrome_options=chrome_options)
        # url = 'https://cn.bing.com/search?q=site:' + self.domain + '&first=' + str(page)
        # try:
        #     driver.set_page_load_timeout(20)
        #     driver.get(url)
        #
        #     WebDriverWait(driver, 40)
        #     html = driver.page_source
        #     driver.quit()
        #     return html
        # except TimeoutException as e:
        #     print('time out for contact')
        #     return None
        headers = {
            # ':authority': 'cn.bing.com',
            # ':method': 'GET',
            # ':path': '/search?q=site:qq.com&first=1',
            # ':scheme': 'https',
            # 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            # 'accept-encoding': 'gzip,deflate,br',
            # 'accept-language': 'zh,en;q=0.9,zh-CN;q=0.8',
            # 'cache-control': 'no-cache',
            # 'cookie': 'MUID=0BD4C9DDE822677414DBC502EC2266FC;SRCHD=AF=NOFORM;SRCHUID=V=2&GUID=B4EAA0A866F0440B964F5C3966DDBB6B&dmnchg=1;MUIDB=0BD4C9DDE822677414DBC502EC2266FC;SNRHOP=I=&TS=;ipv6=hit=1559563828630&t=4;EDGE_S=mkt=zh-cn&SID=0CD7F66FFB7965AE340BFB1FFAA16494;SRCHUSR=DOB=20190529&T=1559560299000;SS=SID=0CD7F66FFB7965AE340BFB1FFAA16494&HV=1559560291&bIm=539;SRCHHPGUSR=CW=1440&CH=434&DPR=1.25&UTC=480&WTS=63695157091',
            # 'pragma': 'no-cache',
            # 'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        }
        proxies = [
            {
                'https': '115.53.17.109:9999'
            },
            {
                'https': '112.87.71.175:9999'
            },
            {
                'https': '112.87.69.55:9999'
            },
            {
                'https': '115.239.240.230:808'
            },
            {
                'https': '112.85.148.251:9999'
            },
            {
                'https': '117.84.218.29:8118'
            },
            {
                'https': '112.85.130.241:9999'
            },
            {
                'https': '175.148.73.239:1133'
            },
            {
                'https': '112.85.131.232:9999'
            },
            {
                'https': '123.115.240.148:8118'
            }
        ]
        url = 'https://cn.bing.com/search?q=site:' + self.domain + '&first=' + str(page)

        print(url)
        html = ''
        try:
            res = requests.get(url, headers=headers, proxies=random.choice(proxies), timeout=3)
            html = res.text
            print(html.find('qq.com'))
        except Exception as e:
            print(e)
            # res = requests.get(url, headers=headers, proxies=random.choice(proxies), timeout=3)
            # html = res.text
        # print(html)
        return html

    def open_url1(self):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        }
        proxies = [
            {
                'https': '115.53.17.109:9999'
            },
            {
                'https': '112.87.71.175:9999'
            },
            {
                'https': '112.87.69.55:9999'
            },
            {
                'https': '115.239.240.230:808'
            },
            {
                'https': '112.85.148.251:9999'
            },
            {
                'https': '117.84.218.29:8118'
            },
            {
                'https': '112.85.130.241:9999'
            },
            {
                'https': '175.148.73.239:1133'
            },
            {
                'https': '112.85.131.232:9999'
            },
            {
                'https': '123.115.240.148:8118'
            }
        ]
        url = 'https://alexa.chinaz.com/' + self.domain

        print(url)
        html = ''
        try:
            res = requests.get(url, headers=headers, timeout=3)
            html = res.text
            print(html.find('qq.com'))
        except Exception as e:
            print(e)
            # res = requests.get(url, headers=headers, proxies=random.choice(proxies), timeout=3)
            # html = res.text
        # print(html)
        return html

    def find_all1(self, res):
        html = res
        if html is None:
            return None
        else:
            soup = bs4.BeautifulSoup(html, 'html.parser')
            soup = soup.find('div', class_='mt1 subOlist h70 sOlist')
            uls = soup.find_all('ul')
            return uls

    def deal_ul(self, uls):
        pattern = r'.*?' + self.domain
        prog = re.compile(pattern)
        for ul in uls:
            target = ul.li.text
            if prog.match(target) is not None:
                self.final_result.append(target)


    def find_all(self, res):
        html = res
        if html is None:
            return None
        else:
            pattern = r'<a target="_blank" href="(.*?)" h=".*?">(.*?)</a>'
            prog = re.compile(pattern)
            targets = prog.findall(html)
            # print(targets)
            return targets

    # def deal_targets(self, targets):
    #     for (subdomain, title) in targets:
    #         self.subdomain_list.append(subdomain)
    #         self.title_list.append(title)
    #         subdomain_dict = {
    #             subdomain: title
    #         }
    #         self.result.append(subdomain_dict)

    def deal_targets2(self, targets):
        if targets is not None:
            for (subdomain, title) in targets:
                self.only_subdomain.append(subdomain)
        self.only_subdomain = list(set(self.only_subdomain))

    def deal_targets(self, targets):
        if targets is not None:
            for (subdomain, title) in targets:
                if len(self.result.keys()) > 0:
                    if subdomain not in self.result.keys():
                        self.result[subdomain] = title
                else:
                    self.result[subdomain] = title

    def clean_result(self):
        if len(self.result) > 0:
            self.result.clear()
        if len(self.final_result) > 0:
            self.final_result.clear()

    def get_result(self):
        for key in self.result.keys():
            subdomain_dict = {
                'subdomain': key,
                'title': self.result[key]
            }
            self.final_result.append(subdomain_dict)
        return self.final_result

import requests
from threading import Thread, activeCount
import queue
import time
from urllib.parse import urlparse, urljoin

# global url
url = ''
file_ext = ''
status_codes = [200, 403, 404, 302, 301]
webdict = 'static\dirscan\dics\dirs.txt'
result = []
queue = queue.Queue()
thread_num = 40


def getUrl(url1):
    global url
    if url1.startswith("http"):
        url = url1
    else:
        # url = "http://" + url1
        url = "http://" + url1


def getFile_EXT(file_ext1):
    global file_ext
    file_ext = file_ext1


def scan_url_exists(queue_url):
    # print(queue_url.strip())
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0(Macintosh; Inter Mac OS X 10.11; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Accept-Language': 'en,zh-CN;q=0.8,zh;q=0.5,en-US;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://www.google.com'
    }
    try:
        req = requests.get(queue_url.strip(), timeout=3, headers=headers)
        print(req.status_code)
        if req.status_code in status_codes:
            result.append({
                'url': queue_url,
                'status': str(req.status_code)
            })
    except Exception as e:
        pass


def open_pathfile():
    global webdict
    with open(webdict, 'r') as f:
        alllines = f.readlines()
        for line in alllines:
            # print(type(line))
            if url.endswith('/'):
                if line.startswith('/'):
                    queue.put((url + line[1:].replace('%EXT%', file_ext)).strip())
                else:
                    queue.put((url + line.replace('%EXT%')).strip())
            else:
                if line.endswith('/'):
                    queue.put((url + line.replace('%EXT%', file_ext)).strip())
                else:
                    queue.put((url + '/' + line.replace('%EXT%', file_ext)).strip())


def start():
    i = 1
    global thread_num
    open_pathfile()
    while queue.qsize() > 0:
        # print(queue.get())
        if activeCount() < int(thread_num):
            print('start scan!' + str(i))
            i += 1
            Thread(target=scan_url_exists, args=(queue.get(),)).start()
        else:
            time.sleep(1)
    return result


def clean_result():
    global result
    result = []

#
#
# if __name__ == '__main__':
#     getUrl('1111111111111')
#     print(url)

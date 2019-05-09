# import gevent
# from gevent import monkey
# monkey.patch_all()
import sys
import hashlib
import json
import time
# from gevent.queue import Queue
import queue
import requests
from threading import Thread, activeCount




class gwhatweb(object):
    thread_num = 40
    resultList = []

    def __init__(self, url):
        self.tasks = queue.Queue()
        self.url = url.rstrip("/")
        with open('static\cmsdistinguish\other\data.json', encoding='utf-8') as fp:
            webdata = json.load(fp, encoding='utf-8')
            for i in webdata:
                self.tasks.put(i)
        # fp = open('data.json')
        # webdata = json.load(fp)
        # for i in webdata:
        #     self.tasks.put(i)
        # fp.close()
        print("webdata total:%d" % len(webdata))

    def _GetMd5(self, body):
        m2 = hashlib.md5()
        m2.update(body.encode("utf-8"))
        return m2.hexdigest()

    def _clearQueue(self):
        while not self.tasks.empty():
            self.tasks.get()

    def _worker(self):
        data = self.tasks.get()
        test_url = self.url + data["url"]
        print(test_url)
        rtext = ''
        try:
            r = requests.get(test_url, timeout=10)
            if (r.status_code != 200):
                return
            rtext = r.text
            if rtext is None:
                return
        except:
            rtext = ''

        if data["re"]:
            print('开始执行判断' + str(rtext.find(data['re'])))
            if (rtext.find(data["re"]) != -1):
                cms = data["name"]
                result = {
                    'cms': cms,
                    'judge': test_url,
                    're': data['re']
                }
                self.resultList.append(result)
                print("CMS:%s Judge:%s re:%s" % (result, test_url, data["re"]))
                self._clearQueue()
                return True
        else:
            md5 = self._GetMd5(rtext)
            if (md5 == data["md5"]):
                cms = data["name"]
                result = {
                    'cms': cms,
                    'judge': test_url,
                    're': data['re']
                }
                self.resultList.append(result)
                print("CMS:%s Judge:%s md5:%s" %(result, test_url, data["md5"]))
                self._clearQueue()
                return True

    def _boss(self):
        while not self.tasks.empty():
            self._worker()

    def whatweb(self, maxsize=100):
        i = 1
        start = time.process_time()
        print('thread_num is ' + str(self.thread_num))
        # allr = [gevent.spawn(self._boss) for i in range(maxsize)]
        # gevent.joinall(allr)
        while not self.tasks.empty():
            if activeCount() < int(self.thread_num):
                print('thread start' + str(self.tasks.qsize()))
                i += 1
                Thread(target=self._boss).start()
                # print('thread end')
            else:
                time.sleep(1)
        end = time.process_time()
        print("cost: %f s" % (end - start))
        return self.resultList

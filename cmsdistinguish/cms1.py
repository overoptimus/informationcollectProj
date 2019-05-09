import requests
import json
url = input('请输入要识别的url地址：')
def what_cms(url):
    headers = {
        'Content-Type':'application/x-www-form-urlencoded'
    }
    post = {
        'hash':'0eca8914342fc63f5a2ef5246b7a3b14_7289fd8cf7f420f594ac165e475f1479',
        'url':url,
    }
    # 该url无法获取，放弃，换另一种方法
    # 有一种想法是通过抓包软件，获取请求的url，在进行构造
    r = requests.post('http://whatweb.bugscanner.com/what/', data=post, headers=headers)
    return r.text
    # dic = json.loads(r.text)
    # if dic['cms'] == '':
    #     return '未识别'
    # else:
    #     return dic['cms']




if __name__ == '__main__':
    print(url)
    print(what_cms(url))

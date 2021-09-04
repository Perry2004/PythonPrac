import requests
import re 
import os
import urllib.parse

#get page content
def get_page_html (page_url):
    headers = {
        'Referer': 'https://image.baidu.com/search/index?tn=baiduimage',
        'User-Agent': 'Safari/14.2'
    }
    try:
        r = requests.get(page_url, headers=headers)
        if r.status_code == 200:
            r.encoding = r.apparent_encoding
            return r.text
        else:
            print("Request failed")
    except Exception as e:
        print(e)

#get image address
def parse_result (text):
    url_real = re.findall ('"thumbURL":"(.*?)",', text)
    return url_real

#get binary data of images
def get_image_content (url_real):
    headers = {
        'Referer': url_real,
        'User-Agent': 'Safari/14.2'
    }
    try:
        r = requests.get(url_real, headers=headers)
        if r.status_code == 200:
            r.encoding = r.apparent_encoding
            return r.content
        else:
            print ("Request failed")
    except Exception as e:
        print(e)

#save picture data to folder
def save_pic(url_real, content):
    root = '/Users/zhuyipeng/crawler/'
    path = root + url_real.split ('/')[-1]
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        with open(path, 'wb') as f:
            f.write(content)
            print("Picture {} Saved as {}".format(url_real, path))
    else:
        pass

def main():
    keyword = input("Keyword: ")
    keyword_quote = urllib.parse.quote(keyword)
    depth = int(input("Pages: "))
    for i in range (depth):
        url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp-result&queryWord+=&cl=2&lm=-1&ie=utf-8&oe-utf-8&adpicid-&st=-1&word={}&z=&ic=0&s=&&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&step_word={}&pn={}&rn=30&gsm=1e&1541136876386='.format(keyword_quote, keyword_quote, i * 30)
        html = get_page_html (url)
        real_urls = parse_result(html)
        for real_url in real_urls:
            content = get_image_content(real_url)
            save_pic (real_url,content)
    print ("Operation finished. Saved {} pictures about {}.".format (depth*30, keyword))

if __name__ == '__main__':
    main()    

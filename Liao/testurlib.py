import requests

r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
r.url # 实际请求的URL
'https://www.douban.com/search?q=python&cat=1001'
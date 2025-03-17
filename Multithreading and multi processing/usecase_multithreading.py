''' scenario :web scraping 
web scraping involves making numerous network requests to fetch web pages.These are I/O bound tasks because they
spend a lot of time waiting for the responses from servers.Multithreading improves the performance by allowing 
multiple web pages to be fetched concurrently.''' 


'''

https://python.langchain.com/docs/introduction/
https://python.langchain.com/docs/tutorials/
https://python.langchain.com/docs/concepts/
'''


import threading
import requests
from bs4 import BeautifulSoup


urls=[
'https://python.langchain.com/docs/introduction/',
'https://python.langchain.com/docs/tutorials/',
'https://python.langchain.com/docs/concepts/'

]

def fetch_contents(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f'feteched {len(soup.text)} characters from {url}')

threads=[]

for url in urls:
    thread=threading.Thread(target=fetch_contents,args=(url,))
    threads.append(thread)
    thread.start()

for thread  in threads:
    thread.join()
print('All information is extracted ')

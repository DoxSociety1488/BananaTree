from colorama import init, Fore
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
init()
def Opening():
    txte = Fore.YELLOW + '''
██████╗░░█████╗░███╗░░██╗░█████╗░███╗░░██╗░█████╗░  ████████╗██████╗░███████╗███████╗
██╔══██╗██╔══██╗████╗░██║██╔══██╗████╗░██║██╔══██╗  ╚══██╔══╝██╔══██╗██╔════╝██╔════╝
██████╦╝███████║██╔██╗██║███████║██╔██╗██║███████║  ░░░██║░░░██████╔╝█████╗░░█████╗░░
██╔══██╗██╔══██║██║╚████║██╔══██║██║╚████║██╔══██║  ░░░██║░░░██╔══██╗██╔══╝░░██╔══╝░░
██████╦╝██║░░██║██║░╚███║██║░░██║██║░╚███║██║░░██║  ░░░██║░░░██║░░██║███████╗███████╗
╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝  ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚══════╝
===========|Telegram: gd23c|==========
===========|Discord: gd23c|===========
=======|Github: DoxSociety1488|=======
[INFO] Banana Tree is a simple and fast open source web crawler.
'''
    for p in txte:
        time.sleep(0.005)
        print(p, end='', flush=True)
def Starting():
    url = input('Enter the url to crawl: ')
    web_crawler(url)
def web_crawler(url, depth=10):
    visited = set()
    queue = [(url, 0)]

    while queue:
        current_url, current_depth = queue.pop(0)
        
        if current_url in visited or current_depth > depth:
            continue
        
        visited.add(current_url)
        print(Fore.RED + "Banana tree CRAWLING:", current_url)
        
        try:
            response = requests.get(current_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            for link in soup.find_all('a', href=True):
                absolute_url = urljoin(current_url, link['href'])
                queue.append((absolute_url, current_depth + 1))
        except Exception as e:
            print("Error:", e)
    
Opening()
Starting()

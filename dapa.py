#Coded By Painlover
#Mass Da/Pa Checker 
import requests,re,os,random,sys,time,json
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from bs4 import BeautifulSoup
from time import time as timer
from colorama import Fore

def Banner():
    clear = '\x1b[0m'
    colors = [36, 32, 34, 35, 31, 37]

    x = '''

               __
              / _)
     _/\/\/\_/ /
   _|         /
 _|  (  | (  |
/__.-'|_|--|_|  
=============
[ Mass DA PA Checker Modified by Painlover ]
	[ https://github.com/ibnudz ]
'''
    for N, line in enumerate(x.split('\n')):
        sys.stdout.write('\x1b[1;%dm%s%s\n' % (random.choice(colors), line, clear))
        time.sleep(0.05)
Banner()

def checking(don):
    done = don.rstrip()
    #print(done)
    data = {
    'links[]': done,
    'url': '1',
    'domain': '0'
    }
    try:
        ten = requests.post("https://www.softo.org/ajax/dacheck", data = data)
        tenx = ten.content
        if '[]' in tenx:
            print("[!] Tidak Valid")
        else:
            da = re.findall('"domain_auth": (.*?),', tenx)
            pa = re.findall('"page_auth": (.*?),', tenx)
            ss = re.findall('"spam_score": (.*?),', tenx)
            tb = re.findall('"total_links": (.*?),', tenx)
            mr = re.findall('"m_rank": (.*?),', tenx)
            hasil = "[+] "+str(done)+"    | DA: "+str(da[0])+" | PA: "+str(pa[0])+" | MR: "+str(mr[0])+" | SS: "+str(ss[0])+"% | TB: "+str(tb[0])+" |"
            print(hasil)
            with open('ResultDaPa.txt', 'a') as o:
                o.writelines(hasil + '\n')
            pass
    except:
        pass
            
def Main():
        try:
            #print("\n\t | DA PA Checker Modified by Painlover | ")
            #print("\n\t | GitHub : https://github.com/ibnudz |")
            dom = raw_input("\n\nInput List Domain \t: ")
            thread = raw_input("Threads (Input 1) \t: ")
            print("\n\n")
            doms = open(dom, 'r').read().splitlines()
            pool = Pool(int(thread))
            results = pool.map(checking, doms)
        except:
            pass
        
if __name__ == '__main__':
	Main()
from itertools import groupby
import os
import colorama
from colorama import Fore,Back,Style 
import argparse
dir=""
banner="""
                  ▄▄  ▄▄▄▄▄▄▄▄                                ▄▄        ▄▄
       ██        ██   ▀▀▀▀▀███                        ██       █▄        █▄
      ██        ██        ██▀    ▄████▄    ██▄████  ███████     █▄        █▄
     ██        ██       ▄██▀    ██▄▄▄▄██   ██▀        ██         █▄        █▄
    ▄█▀       ▄█▀      ▄██      ██▀▀▀▀▀▀   ██         ██          █▄        █
   ▄█▀       ▄█▀      ███▄▄▄▄▄  ▀██▄▄▄▄█   ██         ██▄▄▄        █▄        █▄
  ▄█▀       ▄█▀       ▀▀▀▀▀▀▀▀    ▀▀▀▀▀    ▀▀          ▀▀▀▀         █▄        █▄
 """
colorama.init()
def parse():
 global dir,reverse,alphabet,output,clean,fast
 print(banner)
 parser = argparse.ArgumentParser(description="Password combiner")
 parser.add_argument("dir",help='Directory with worldlists')
 parser.add_argument("-r",'--reverse', help="Reverse wordlist",action="store_true")
 parser.add_argument("-a",'--alphabet', help="Sort by alphavet",action="store_true")
 parser.add_argument("-o",'--output',help="Write output to file",default="output.txt")
 parser.add_argument('-c','--clear',help="Clear all dublicates in wordlists (works only with '-a' or 'r' arguments)",action='store_true') 
 parser.add_argument("-f",'--fast',help="Fast filter(filtering only input wordlists not output wordlist(recommended))",action='store_true')
 args = parser.parse_args()
 dir=args.dir
 reverse=args.reverse
 alphabet=args.alphabet
 output=args.output
 clean=args.clear
 fast=args.fast
def main():
 parse()
 read_wordlists(dir)
def read_wordlists(dir):
 list=[]
 if os.path.isdir(dir):
  print(Fore.GREEN+"Found {} wordlists".format(os.listdir(dir))+Fore.RESET)
  if fast == True:  
   for wordlist in os.listdir(dir):
    with open(os.path.join(dir,wordlist),'r',errors='ignore') as file_reader:
     list+=file_reader.read().split('\n')
     print (Fore.GREEN+"Loaded {} wordlist".format(wordlist)+Fore.RESET)
     save(filter(list))
     list=[]
  else:
   for wordlist in os.listdir(dir):
    with open(os.path.join(dir,wordlist),'r',errors="ignore") as files:
     list+=files.read().split('\n')
    print (Fore.GREEN+"Loaded {} wordlist...".format(wordlist)+Fore.RESET)
   save(filter(list))  
 else:
  print (Fore.RED+"Directory isn't found"+Fore.RESET)
  exit()
def filter(list):
 if alphabet == True:
  print(Fore.GREEN+"Sorting by alphabet..."+Fore.RESET)
  list.sort()
 if reverse == True:
  print(Fore.GREEN+"Reversing..."+Fore.RESET)
  list.sort(reverse=True)
 if clean == True:
  print(Fore.GREEN+"Cleaning..."+Fore.RESET)
  list=[el for el, _ in groupby(list)]
 return list 
def read_buffer():
 #buffer_list=[]
 with open('buffer.txt','r',errors='ignore') as buffer:
  #buffer_list=buffer.read().split('\n')
  return buffer.read().split('\n') 
  #return buffer_list
#def write_buffer(word):
# with open('buffer.txt','a',errors="ignore") as buffer_writer:
#  buffer_writer.write(word.strip()+'\n')
def save(list):
 with open(output,'a',errors='ignore') as saver:
  #saver.write(str([value for value in list if value]))
  for value in list:
   if value:
    saver.write(value.strip()+'\n')
  print(Fore.GREEN+"New wordlist was saved in {}".format(output)+Fore.RESET)
  if fast != True:
   exit()
  else:
   pass
try:
 main()
except KeyboardInterrupt:
 exit()

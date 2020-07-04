# password_combiner
Simple script which filters and combines wordlist on Python 3             
# INSTALL:                      
git clone https://github.com/zertmark/password_combiner.git && cd password_combiner && pip3 install argparse            
# NEW:                             
1) Bug fix                  
# RUN:                           
python3 password_combiner.py -h             
usage: password_combiner.py [-h] [-r] [-a] [-o OUTPUT] [-c] [-f] dir                       
                
Password combiner                
                   
positional arguments:
  dir                   Directory with worldlists                      

optional arguments:
  -h, --help            show this help message and exit                
  -r, --reverse         Reverse wordlist                      
  -a, --alphabet        Sort by alphavet                                
  -o OUTPUT, --output OUTPUT              
                        Write output to file                  
  -c, --clear           Clear all dublicates in wordlists (works only with '-a' or 'r' arguments)                    
  -f, --fast            Fast filter(filtering only input wordlists not output wordlist(recommended))                  


#! /bin/python3
#! Created by : ItsBarathr
#! Name : dnsmap
#! Version 1.0

# packages
import requests
import argparse


# Banner of this tool
def Banner():
    print("""
                                              .
                                 (@            @%
                               %@@             /@@,
                              @@@(              @@@(
                            .@@@@.              @@@@.
                            @@   .                *@&
                 @*         *@@@@@@#        *@@@@@@(          @
               .@@         #@@@@@@@@@.     @@@@@@@@@&         @@*
               @@@         @@@@@@@@@@@    @@@@@@@@@@@         %@@*
              &@@@         @@@@@@@@@@@@  %@@@@@@@@@@@         @@@@
              @@@%@        %@@@@@@@@@@@  @@@@@@@@@@@@        &@@@@,
              @ @@@@@%      @@@@@@@@@@&  /@@@@@@@@@@       @@@@@ @,
              ,@@@@@@@@@,    (@@@@@@@@    %@@@@@@@%     @@@@@@@@@/
              %@@@@@@@@@@@      (@@*        ,&@#      (@@@@@@@@@@@
              ,@@@@@@@@@@@@           /%%/           %@@@@@@@@@@@#
               %@@@@@@@@@@@(       @@@@@@@@@@&      ,@@@@@@@@@@@@
                *@@@@@@@@@@%     .@@@@@@@@@@@@@     /@@@@@@@@@@@
                  %@@@@@@@@     (@@@@@@@@@@@@@@@     @@@@@@@@@
                     ,#&#    ,@@@@@@@@@@%@@@@@@@@%    ,@@@&.
                        *@@@@@@@@@@@@@     %@@@@@@@@@@@,
                      ,@@@@@@@@@@@@@*       @@@@@@@@@@@@@.
                     @@@@@@@@@@@@@/  dnsmap  @@@@@@@@@@@@@@
                      @@@@@@@@@@@@@@  1.0   @@@@@@@@@@@@@@@
                       @@@@@@@@@&@@@        @@@@@@@@@@@@@@.
                         *@@@@@@@(@@@@#@@@@@@@@@@@@@@@#
                               #@@@@@@@@@@@@@@@@%
                                 .@@@@@@@@@@@@.
                                   @@@@@@@@@/
                                    @@@@@@@.
                                    /@@@@@
                                     @@@@
                                     .@@.

                                    dnsmap
                                 version 1.0
                                """)

# Scanner function
def Scanner(domain_name, subdomain_list):
    # calling Banner() function
    Banner()
    
    print("Scaning started...")
    for subdomain in subdomain_list:
        url = f"https://{subdomain}.{domain_name}"
        try:
            requests.get(url)
            print(f'[+] {url}')
            
        except requests.ConnectionError:
            pass
        
# main function 
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("domain", help="Get domain name")
    parser.add_argument("-w", "--wordlist", help="Enter the wordlist path")
   
    args = parser.parse_args()
    domain = args.domain
    wordlist = args.wordlist
    
    if wordlist is not None:
        with open(wordlist, 'r') as file:
            name = file.read()
            subdomain = name.splitlines()
            Scanner(domain,subdomain)
    else:
        # defult wordlist
        with open('wordlists/dnsmap.txt','r') as file:
            name = file.read()
            subdomain = name.splitlines()
        Scanner(domain,subdomain)
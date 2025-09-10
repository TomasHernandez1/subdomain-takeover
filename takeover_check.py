import shodan
import re
import subprocess
import sys
from datetime import datetime
import time

api_key = 'change this with a shodan api key'

def get_cname_records(domain):
    shodan_client = shodan.Shodan(api_key)
    time.sleep(1)
    try:
        domain_info = shodan_client.dns.domain_info(domain)
        cnames = [record['value'] for record in domain_info['data'] if record['type'] == 'CNAME']
        return cnames
    except shodan.APIError as e:
        print(f"Errore di Shodan: {e}")
        return []

def get_domain_expiration(domain):
    try:
        result = subprocess.run(['whois', domain], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        whois_output = result.stdout

        match = re.search(r'Expir\w*\sDate:\s+(\d{4}-\d{2}-\d{2})', whois_output)
        if match:
            return match.group(1)
        else:
            return 'UNASSIGNABLE'
    except Exception as e:
        return f'Errore: {e}'

def check_domain_expiration(domain):
    cnames = get_cname_records(domain)
    checked_cnames = set()  
    today = datetime.now().date()  

    for cname in cnames:
        if cname not in checked_cnames:
            expiration_date = get_domain_expiration(cname)
            if expiration_date != 'UNASSIGNABLE':
                expiration_date_obj = datetime.strptime(expiration_date, '%Y-%m-%d').date()
                if expiration_date_obj < today:
                    print(f'{cname}: {expiration_date} SUBDOMAIN TAKEOVER!')
                else:
                    print(f'{cname}: {expiration_date}')
            else:
                print(f'{cname}: {expiration_date}')
            checked_cnames.add(cname)  

def main(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            domain = line.strip()
            if domain:
                print(f'Checking domain: {domain}')
                check_domain_expiration(domain)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Utilizzo: python script.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)

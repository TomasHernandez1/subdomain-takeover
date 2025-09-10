# subdomain-takeover
subdomain-takeover is a program designed to check for the Subdomain Takeover vulnerability over a list of domains.

# Features
- Retrieves CNAME records using Shodan’s API and runs whois lookups on discovered CNAMEs.
- Extracts the domain expiration date and highlights expired domains → takeover risk
- Supports batch domain checks from a file

# Usage
1. Create a text file with the domains you want to check (one per line), for example domains.txt:

example.com
\ntest.com
\ndomain.org

5. Run the script and pass the file as an argument:
```bash
python3 subdomain_takeover.py <domains.txt>
```

# Output example
```bash
Checking domain: example.com
sub.example.com: 2025-07-10
sub2.example.com: 2023-05-01 SUBDOMAIN TAKEOVER!
```

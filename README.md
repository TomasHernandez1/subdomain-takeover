# subdomain-takeover
subdomain-takeover is a program designed to check for the Subdomain Takeover vulnerability over a list of domains.

# Features
- Retrieves CNAME records using Shodan’s API and runs whois lookups on discovered CNAMEs.
- Extracts the domain expiration date and highlights expired domains → takeover risk
- Supports batch domain checks from a file

# Usage
python3 subdomain_takeover.py <domains.txt>

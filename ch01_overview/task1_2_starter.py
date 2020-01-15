"""

       task1_2_starter.py

For this task, you are to manually extract the domain name out of the URLs
mentioned on our slide.  The URLs are:

https://docs.python.org/3/
https://www.google.com?gws_rd=ssl#q=python
http://localhost:8005/contact/501


 Additional Hints:
   1. Prompt for a URL input
        Example:
                    user_input_str = input('Enter a value: ')

   2. Check if URL begins with any of the prefixes by using .startswith()
      If it does, capture the remaining part of the URL using slicing
        Example:
                 value = 'hello world'
                 if value.startswith('hello')
                     remaining = value[len('hello'):]

  3. Repeat this task for the suffixes.  Use .find() for the
     suffixes.  find() returns a -1 for items not found in the string
     For example:
                 value = 'hello world'
                 position = value.find('world')
                 remaining = value[:position]
"""


prefixes = ['http://', 'https://']
suffixes = [':', '/', '?']
url = input ('Enter URL with http/s://: ')

for prefix in prefixes:
    if url.startswith(prefix):
        domain = url[len(prefix):]

for suffix in suffixes:
    position = domain.find(suffix)
    if position != -1:
        domain = domain[:position]

print(domain)


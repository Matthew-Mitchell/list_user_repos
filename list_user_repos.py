import sys
from github_api import *

"""To be run from the command line, passing in an argument for the desired username.
For example, you might execute:
```python list_user_repos.py "Matthew-Mitchell"```
In order to print the [public] repositories for the user Matthew-Mitchell.
"""
username = sys.argv[1]
print_usr_repos(username)
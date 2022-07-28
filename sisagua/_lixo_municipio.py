#!/usr/bin/env python
# coding: utf-8

import os
import sys
from src.sisagua.lixo_git_api import *

try:
    sys.path.append(os.path.expanduser('~/Codes'))
    from my_vault.credentials_github import credential
    credential = credential['API_TOKEN_GITHUB']
except Exception as e:
    print(e)
    print('Fora do PC local')
    credential = os.environ['API_TOKEN_GITHUB']

# Parameters
list_cities = get_cities(cred=credential)
print(list_cities)

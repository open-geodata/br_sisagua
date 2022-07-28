#!/usr/bin/env python
# coding: utf-8

import os
import sys
from github import Github

try:
    sys.path.append(os.path.expanduser('~/Codes'))
    from my_vault.credentials_github import credential
except Exception as e:
    print(e)
    print('Fora do PC local')


def get_cities(cred):
    """
    Pega lista de cidades que estão no repositório br_sisagua
    :return: Lista de Cidades
    """
    token = os.getenv('API_TOKEN_GITHUB', cred)
    g = Github(token)
    list_paths = []
    repo = g.get_repo('open-geodata/br_sisagua')
    for content in repo.get_contents(path=os.path.join('data', 'output')):
        if content.type == 'dir':
            list_paths.append(os.path.basename(content.path))

    list_paths.sort()
    return list_paths


if __name__ == '__main__':
    lst = get_cities(cred=credential['API_TOKEN_GITHUB'])
    print(lst)

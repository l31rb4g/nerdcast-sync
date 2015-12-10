#!/usr/bin/python
#encoding: utf-8
import re
import json
import requests
from subprocess import check_output


dir = '/media/l31rb4g/38586AAE586A6A98/MP3/Nerdcast'
link = 'http://jovemnerd.com.br/json-busca-nerdcast/'
print('>>> Buscando lista completa de Nerdcasts...')
nerdcast_list = json.loads(requests.post(link, data={'operation': 'getAll'}).text)

for url in nerdcast_list:
    print('\n+' + ('-' * (len(url['title']) + 2)) + '+')
    print('| ' + url['title'] + ' |')
    print('+' + ('-' * (len(url['title']) + 2)) + '+')

    html = requests.get(url['href']).text
    mp3_url = re.findall('<a href="(.*)" data-player', html)[0]
    filename = re.sub('.*/([^\/]+)$', r'\1', mp3_url)
    if dir[-1:] != '/':
        dir += '/'
    target = dir + filename

    output = check_output(['wget', '--quiet', '--show-progress', '--continue', '-O', target, mp3_url])
    if output:
        print(output)
    print('>>> Nerdcast sincronizado!')

print('DONE!')

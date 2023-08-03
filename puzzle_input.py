import requests
import gin
import advent_config

# TODO: add args to pass in session cookie



cookies = {
    'session': f'{advent_config.session_cookie}',
}


response = requests.get('https://adventofcode.com/2022/day/1/input', cookies=cookies)
print(response.text) 

import os

def get_base_url():

    env = os.environ.get('ENV', 'test')

    if env == 'test':
        return 'https://store.steampowered.com/'
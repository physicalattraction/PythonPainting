import os.path
import random
import string
from enum import Enum

import requests

from utils import img_dir


class Sprite(Enum):
    male = 1
    female = 2
    human = 3
    identicon = 4
    initials = 5
    bottts = 6
    avataaars = 7
    jdenticon = 8
    gridy = 9
    micah = 10


AVATAR_DIR = os.path.join(img_dir(), 'avatar')
os.makedirs(AVATAR_DIR, exist_ok=True)


def random_string(size: int, allowed_chars: str = string.ascii_letters):
    return ''.join(random.choice(allowed_chars) for _ in range(size))


def download_avatar(sprite: Sprite, seed: str = ''):
    if not seed:
        seed = random_string(10)
    url = f'https://avatars.dicebear.com/api/{sprite.name}/{seed}.svg'
    response = requests.get(url)
    sprite_dir = os.path.join(AVATAR_DIR, sprite.name)
    os.makedirs(sprite_dir, exist_ok=True)
    output_file = os.path.join(sprite_dir, f'{seed}.svg')
    with open(output_file, 'wb') as f:
        f.write(response.content)
        print(f'Successfully downloaded and saved {output_file}')


def download_avatars():
    for p in Sprite:
        for _ in range(10):
            download_avatar(p)


if __name__ == '__main__':
    download_avatars()

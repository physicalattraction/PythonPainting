"""
Download avatars from DiceBear or Multiavatar

https://avatars.dicebear.com/docs/http-api
https://multiavatar.com/
"""

import os.path
import random
import string
from enum import Enum
from time import sleep

import requests

from utils import img_dir


class DiceBearSprite(Enum):
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


AVATAR_ROOT_DIR = os.path.join(img_dir(), 'avatar')
os.makedirs(AVATAR_ROOT_DIR, exist_ok=True)


def random_string(size: int, allowed_chars: str = string.ascii_letters):
    return ''.join(random.choice(allowed_chars) for _ in range(size))


def save_as_file(url: str, output_file: str):
    """
    Download the contents from url and save it as filename

    :param url: URL to download the avatar from
    :param output_file: Full path to file to write
    """

    response = requests.get(url)
    with open(output_file, 'wb') as f:
        f.write(response.content)
        print(f'Successfully downloaded from {url} and saved {output_file}')


def download_dice_bear_avatar(sprite: DiceBearSprite, seed: str = ''):
    if not seed:
        seed = random_string(10)
    url = f'https://avatars.dicebear.com/api/{sprite.name}/{seed}.svg'
    sprite_dir = os.path.join(AVATAR_ROOT_DIR, sprite.name)
    os.makedirs(sprite_dir, exist_ok=True)
    output_file = os.path.join(sprite_dir, f'{seed}.svg')
    save_as_file(url, output_file)


def download_multiavatar(seed: str = ''):
    if not seed:
        seed = random_string(10)
    url = f'https://api.multiavatar.com/{seed}.svg'
    multiavatar_dir = os.path.join(AVATAR_ROOT_DIR, 'multiavatar')
    os.makedirs(multiavatar_dir, exist_ok=True)
    output_file = os.path.join(multiavatar_dir, f'{seed}.svg')
    save_as_file(url, output_file)


def download_avatars():
    for p in DiceBearSprite:
        for _ in range(10):
            download_dice_bear_avatar(p)
    for _ in range(20):
        download_multiavatar()
        # Multiavatar has a call limit of 10 per minute
        sleep(6)


if __name__ == '__main__':
    download_avatars()

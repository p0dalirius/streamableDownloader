#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : streamableDownloader.py
# Author             : Podalirius (@podalirius_)
# Date created       : 13 Jan 2022

import os
import requests
from bs4 import BeautifulSoup
import argparse


def b_filesize(size):
    units = ['B', 'kB', 'MB', 'GB', 'TB', 'PB']
    k = 0
    for k in range(len(units)):
        if size < (1024 ** (k + 1)):
            break
    return "%4.2f %s" % (round(size / (1024 ** (k)), 2), units[k])


def parseArgs():
    parser = argparse.ArgumentParser(description="Download videos hosted on streamable from their link.")

    parser.add_argument("-u", "--url", default=None, required=True, help="Streamable URL")
    parser.add_argument("-o", "--output-file", default=None, required=False, type=str, help="Output file")
    parser.add_argument("-v", "--verbose", default=False, action="store_true", help="Verbose mode. (default: False)")

    return parser.parse_args()


if __name__ == '__main__':
    options = parseArgs()

    r = requests.get(options.url)
    soup = BeautifulSoup(r.content, "lxml")

    sources = {}

    meta = soup.find('meta', attrs={"property": "og:video"})
    if meta is not None:
        sources["og_video"] = meta['content']

    meta = soup.find('meta', attrs={"property": "og:video:url"})
    if meta is not None:
        sources["og_video_url"] = meta['content']

    meta = soup.find('meta', attrs={"property": "og:video:secure_url"})
    if meta is not None:
        sources["og_video_secure_url"] = meta['content']

    if options.verbose:
        print("[>] Extracted video urls:")
        if "og_video" in sources.keys():
            print("  - og_video: %s" % sources["og_video"])
        if "og_video_url" in sources.keys():
            print("  - og_video_url: %s" % sources["og_video_url"])
        if "og_video_secure_url" in sources.keys():
            print("  - og_video_secure_url: %s" % sources["og_video_secure_url"])

    for source_name in sources.keys():
        url = sources[source_name]
        r = requests.head(url)
        if r.headers["Content-Type"] in ["video/mp4"]:

            total_size = 0
            if 'Content-Length' in r.headers.keys():
                total_size = str(r.headers['Content-Length'])

            if options.output_file is not None:
                filename = options.output_file
            else:
                filename = os.path.basename(url).split("?")[0]

            print("[>] Downloading to %s ..." % os.path.basename(filename))
            total_size = 0
            with requests.get(url, stream=True) as r:
                with open(filename, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=16 * 1024):
                        f.write(chunk)
                        total_size += len(chunk)
            print("[>] Downloaded %s to %s ..." % (b_filesize(total_size), os.path.basename(filename)))
            break
        else:
            print("Unknown Content-Type %s for source '%s', skipping" % (r.headers['Content-Type'], source_name))

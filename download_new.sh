#!/usr/bin/bash

.venv/bin/python new_videos.py |\
  xargs youtube-dl -o "/mnt/pidrive/youtube/%(uploader)s/%(title)s.%(ext)s" --add-metadata --write-thumbnail

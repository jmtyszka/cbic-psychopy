#!/bin/bash

cd /folder/containing/mp4/segments/of/ForrestGump

for FILE in *.mp4; do
  ffmpeg \
  -i "$FILE" \
  -ss 00:00:00 \
  -to 00:05:00 \
  -map 0:v -map 0:a:0 \
  -map_metadata -1 \
  -vf scale=1280:-1 \
  -c:a aac -vbr 5 \
  -c:v libx264 -preset slow -crf 22 \
  -filter:v fps=30 \
  -copyts \
  -y \
  "${FILE%.*}_5min_repeat.mp4"
done

#!/bin/bash
# Split The Grand Budapest Hotel into approx 20 min segments
# Adapted from https://github.com/mvdoc/budapest-fmri-data/blob/master/scripts/preprocessing-stimulus/split_movie.sh

mp4_fname="Budapest_720p30_Timestamped.mp4"
splits_fname="Budapest_Exact_Splits.tsv"

while read -r clip start stop dur; do
  echo "Clip ${clip} Start: ${start} Stop: ${stop} Duration: ${dur}"
  ffmpeg  \
    -i Budapest_720p30_Timestamped.mp4 \
    -ss "${start}" \
    -to "${stop}" \
    -map_metadata -1 \
    -af compand="0|0:1|1:-90/-900|-70/-70|-30/-9|0/-3:6:0:0:0" \
    -c:a aac -vbr 5 \
    -c:v copy \
    -copyts \
    -y \
    Budapest_"${clip}".mp4 < /dev/null
done < ${splits_fname}

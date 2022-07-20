#!/bin/bash
# Create 30s soundcheck videos for each video segment
#
# AUTHOR : Joud Mar'i
# DATES  : 2022-04-18 Mike Tyszka Update path handling, add file loop, refactor variables

segs_dir="../Segments"

# Get first segment - use this for all sound checks
seg0_fname=`ls ${segs_dir}/*_0.mp4 | head -n 1`
echo "Sound check source segment : ${seg0_fname}"

# Loop over all movie segments
for seg_fname in ${segs_dir}/*_[0-9].mp4
do

    echo "Creating soundcheck for ${seg_fname}"
    
    check_fname=${seg_fname/.mp4/_soundcheck.mp4}

    ffmpeg \
        -i "${seg0_fname}" \
        -ss 00:00:00 \
        -to 00:00:30 \
        -c:a copy \
        -c:v copy \
        -copyts \
        -y \
        "${check_fname}"
    
done

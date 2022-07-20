#!/bin/bash
# Create 5 min repeats and 30s sound checks for each movie segment
#
# AUTHOR : Joud Mar'i
# DATES  : 2022-04-18 Mike Tyszka Update path handling, add file loop, refactor variables

segs_dir="../Segments"
reps_dir="../Repeats"

mkdir -p ${reps_dir}

# Loop over all movie segments
for seg_fname in ${segs_dir}/*_[0-9].mp4
do

    # Construct repeat filename
    seg_bname=$(basename ${seg_fname})
    seg_check_fname=${seg_fname/.mp4/_soundcheck.mp4}
    rep_bname=${seg_bname/.mp4/R.mp4}
    rep_fname=${reps_dir}/${rep_bname}
    rep_check_fname=${rep_fname/.mp4/_soundcheck.mp4}

    echo "Creating 5 min repeat for ${seg_bname} > ${rep_bname}"

    # Create repeat clip from first 5 mins of movie segment
    ffmpeg \
        -i "${seg_fname}" \
        -ss 00:00:00 \
        -to 00:05:00 \
        -c:a copy \
        -c:v copy \
        -copyts \
        -y \
        "${rep_fname}"
  
    echo "Creating soundcheck for ${rep_bname} > ${rep_check_fname}"

    # Copy and rename segment sound check to repeats folder
    cp ${seg_check_fname} ${rep_check_fname}
  
done

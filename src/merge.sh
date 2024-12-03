#!/bin/bash




 conda activate illumina
# # I really feel like this should be condensed into a script run multiple times with command line arguments
# # but I just want to get it working first

# set -ue                               # stop on error, if unset variable is accessed
# # trailing forward slash on these is not optional, and IDK why
# source_dir1="/projects/bgmp/shared/groups/2024/novel-fluor/shared/upload/BGMP_2024/BLUE/NovaSeq_GC3F_7125/"
# source_dir2="/projects/bgmp/shared/groups/2024/novel-fluor/shared/upload/BGMP_2024/RED/NovaSeq_GC3F_7124/"
# # This is the lowest directory I can write to in shared/upload
# # TODO: Change to dat folder 
# destination_dir1="/projects/bgmp/shared/groups/2024/novel-fluor/shared/upload/NovaSeq_merged/blue/" 
# destination_dir2="/projects/bgmp/shared/groups/2024/novel-fluor/shared/upload/NovaSeq_merged/red/" 
# # Read in file names in pairs
# # Why is this in quotes
# # Why isn't this prefaced with $
# the_files=("$source_dir1"*.fastq.gz)

# mkdir -p "$destination_dir1" 
# for ((i=0; i<${#the_files[@]}; i+=2)); do
#     # Access the current element and the next one
#     if [[ ${the_files[i]} =~ "R1" && ${the_files[i+1]} =~  "R2" ]]; then
#         # string slicing to name output files
#         sliced_filename=${the_files[i]%%R1*}  # slices string and keeps what occurs before r1
#         full_filename="${destination_dir1}${sliced_filename##*NovaSeq_GC3F_7125/}"
#         #echo output_filename 
#         bbmerge.sh -in1=${the_files[i]} -in2=${the_files[i+1]} -out="${full_filename}MERGED.fastq" \
#         -outu1="${full_filename}R1_rejected.fastq" -outu2="${full_filename}R2_rejected.fastq" 
#         #echo $full_filename
#     else
#         echo "Item 1: ${the_files[i]} and Item 2: ${the_files[i+1]} can't be processed."
#     fi
# done

# echo "One down, one to go"

# the_other_files=("$source_dir2"*.fastq.gz)

# mkdir -p "$destination_dir2" 
# for ((i=0; i<${#the_other_files[@]}; i+=2)); do
#     # Access the current element and the next one
#     if [[ ${the_other_files[i]} =~ "R1" && ${the_other_files[i+1]} =~  "R2" ]]; then
#         sliced_filename=${the_other_files[i]%%R1*}  # slices string and keeps what occurs before r1
#         full_filename="${destination_dir2}${sliced_filename##*NovaSeq_GC3F_7124/}"
#         bbmerge.sh -in1=${the_other_files[i]} -in2=${the_other_files[i+1]} -out="${full_filename}MERGED.fastq" \
#         -outu1="${full_filename}R1_rejected.fastq" -outu2="${full_filename}R2_rejected.fastq"
#     else
#         echo "Item 1: ${the_other_files[i]} and Item 2: ${the_other_files[i+1]} can't be processed."
#     fi
# done





input_dir="$1"
output_dir="$2"

# Loop through all files matching the pattern (adjust as needed)
for file1 in "${input_dir}"*"_R1.fastq.gz"; do
  file2="${file1/_R1.fastq.gz/_R2.fastq.gz}"
  
  # Extract base name from R1 filename (assuming consistent naming)
  base_name="${file1%_R1.fastq.gz}"
  
  # Run bbmerge.sh
  bbmerge.sh -in1="$file1" -in2="$file2" \
      -out="${output_dir}/${base_name}_MERGED.fastq.gz" \
      -outu1="${output_dir}/${base_name}_R1_rejected.fastq.gz" \
      -outu2="${output_dir}/${base_name}_R2_rejected.fastq.gz"
done
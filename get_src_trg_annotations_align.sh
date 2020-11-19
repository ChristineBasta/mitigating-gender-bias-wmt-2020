



# Get target genders
python scripts/python/generate_genders.py --lang es \
--source data/iwslt-es/train.en-es.es \
--output data/iwslt-es/iwslt.genders.txt

#get alignments of the file

# Align
FAST_ALIGN_BASE=/home/christine/fast_align
trans_fn=data/iwslt-es/trial
align_fn=forward.en-es.align

$FAST_ALIGN_BASE/build/fast_align -i $trans_fn  -d -o -v > $align_fn

Get EN genders by aligning $LANG genders to EN corpus
#it gets the gender of the target
#python "$PYTHON_SCR"/align_genders.py \
#      --target "$file".tc.en \
#      --source_genders "$file".genders."$LANG" \
#      --source_target_alignment $alignments_folder/"$file"."$LANG"-en.align \
#      >"$file".genders.en




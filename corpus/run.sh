python src/tokenize_enja.py < enja.tsv > tokenized.tsv
cat tokenized.tsv \
    | python src/length_filter.py \
    | python src/ratio_filter.py \
    | python src/overlap_filter.py \
    | python src/vocab_filter.py \
    > filtered.tsv 
python src/split_corpus.py < filtered.tsv

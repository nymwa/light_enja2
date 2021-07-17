#!/bin/bash

set -eux

fairseq-interactive data-bin \
    --buffer-size 1024 \
    --batch-size 128 \
    --path checkpoints/checkpoint30.pt \
    --beam 5 \
    --lenpen 0.6 \
    < test.en \
    | grep '^H' \
    | cut -f 3 \
    | python src/decode.py \
    | tee output.txt \
    | sacrebleu corpus/test.ja


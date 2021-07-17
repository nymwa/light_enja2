set -ex

TRAIN_EN=corpus/train.en
TRAIN_JA=corpus/train.ja
VALID_EN=corpus/valid.en
VALID_JA=corpus/valid.ja
TEST_EN=corpus/test.en

cat $TRAIN_EN $TRAIN_JA > train.enja
python src/learn.py --input train.enja --prefix bpe --vocab-size 4000 --character-coverage 0.9995 --threads 1

encode () {
    python src/encode.py --model bpe.model
}

encode < $TRAIN_EN > train.en
encode < $TRAIN_JA > train.ja
encode < $VALID_EN > valid.en
encode < $VALID_JA > valid.ja
encode < $TEST_EN > test.en

fairseq-preprocess -s en -t ja \
    --trainpref train \
    --validpref valid \
    --destdir data-bin \
    --joined-dictionary


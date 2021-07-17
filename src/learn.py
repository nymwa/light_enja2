from argparse import ArgumentParser
import sentencepiece as spm

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--input')
    parser.add_argument('--prefix')
    parser.add_argument('--vocab-size', type = int, default = 4000)
    parser.add_argument('--character-coverage', type = float, default = 0.9995)
    parser.add_argument('--threads', type = int, default = 1)
    args = parser.parse_args()

    spm.SentencePieceTrainer.Train(
            input = args.input,
            model_prefix = args.prefix,
            model_type = 'bpe',
            vocab_size = args.vocab_size,
            character_coverage = args.character_coverage,
            num_threads = args.threads)


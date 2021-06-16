import tokenizers


# Paths
TOKENIZER_PATH = '/content/kaggle_tweet/src/1st_level/roberta_tokenizer'
TRAINING_FILE = '/content/kaggle_tweet/data/train_folds.csv'
TEST_FILE = '/content/kaggle_tweet/data/test.csv'
SUB_FILE = '/content/kaggle_tweet/data/sample_submission.csv'
MODEL_SAVE_PATH = '/content/kaggle_tweet/src/1st_level/roberta_base/model_save'
TRAINED_MODEL_PATH = '/content/kaggle_tweet/src/1st_level/roberta_base/model_save'

# Model config
MODEL_CONFIG = 'deepset/roberta-base-squad2'

# Model params
SEED = 25
N_FOLDS = 5
EPOCHS = 4
LEARNING_RATE = 4e-5
PATIENCE = None
EARLY_STOPPING_DELTA = None
TRAIN_BATCH_SIZE = 32
VALID_BATCH_SIZE = 32
MAX_LEN = 96  # actually = 86
print(f'{TOKENIZER_PATH}/vocab.json')
TOKENIZER = tokenizers.ByteLevelBPETokenizer.from_file(
    vocab_filename=f'{TOKENIZER_PATH}/vocab.json',
    merges_filename=f'{TOKENIZER_PATH}/merges.txt',
    lowercase=True,
    add_prefix_space=True)
HIDDEN_SIZE = 768
N_LAST_HIDDEN = 12
HIGH_DROPOUT = 0.5
SOFT_ALPHA = 0.6
WARMUP_RATIO = 0.25
WEIGHT_DECAY = 0.001
USE_SWA = False
SWA_RATIO = 0.9
SWA_FREQ = 30

import re
import math
import numpy as np

class Jaccard:

    def __init__(self) -> None:
        pass

    def calc(A,B):
    
        A = A.split()
        B = B.split()
        len_intersect = len(set(A) & set(B))
        len_union = len(set(A) | set(B))

        if len_union > 0:
            return len_intersect / len_union
        else:
            return "len_union == 0"
        

class TF_IDF:

    def __init__(self) -> None:
        pass

class BM25:

    def __init__(self) -> None:
        pass


"""
# used for unseen words in training vocabularies
UNK = None
# sentence start and end
SENTENCE_START = "<s>"
SENTENCE_END = "</s>"

# Train Vocab Path
TRAIN_VOCAB = "train.vocab.txt"

def read_sentences_from_file(file_path):
    '''
        read the files.
    '''
    with open(file_path, "r") as f:
        return [re.split("\s+", line.rstrip('\n')) for line in f]

class UnigramLanguageModel:
    def __init__(self, sentences, mode="collection", smoothing=False, log=False):
        '''
            sentences: sentences of the dataset
            mode: whether this language model is for the whole corpus/collection or just a single document
            smoothing: add-one smoothing
        '''
        
        self.smoothing = smoothing
        self.mode = mode
        # Enable class wide logging
        self.logging = log

        # Init unknown word count
        self.unknown_word_count = 0

        # Load training/base vocab
        self.trained_vocab = {}
        terms = self.read_train_vocab()
    
        for term in terms:
            if smoothing:
                self.trained_vocab[term] = 1
            else:
                self.trained_vocab[term] = 0
            
        # Initialize model with the training vocab
        self.vocab_tf = self.trained_vocab
        
        # Extract words from input data
        words = []
        for sentence in sentences:
            words.extend(sentence)
        words = [word for word in words if ((word != SENTENCE_START) and (word != SENTENCE_END))]
        
        if mode != "collection":
            self.doc_size = len(words)
        else:
            self.corpus_size = len(words)

        # Create the model
        for word in words:
            if word in self.vocab_tf: # If word is not UNK
                self.vocab_tf[word] += 1
            else:
                if self.logging:
                    print(word, f"was not found in base vocabulary, it has been added now (along {self.unknown_word_count} others)!")
                self.unknown_word_count += 1
                if smoothing:
                    self.vocab_tf[word] = 2
                else:
                    self.vocab_tf[word] = 1


    def read_train_vocab(train_vocab_path = TRAIN_VOCAB):
        with open(TRAIN_VOCAB, 'r') as file:
            text = file.read()
            terms = text.split()
            return terms
        
    def calculate_unigram_probability(self, word):
        '''
            calculate unigram probability of a word
        '''
        N = self.corpus_size if self.mode == "collection" else self.doc_size 
        if self.smoothing:
            return self.vocab_tf[word] / (N + self.unknown_word_count)
        else:
            return self.vocab_tf[word] / (N)
            
    
    def calculate_sentence_probability(self, sentence, normalize_probability=True):
        '''
            calculate score/probability of a sentence or query using the unigram language model.
            sentence: input sentence or query
            normalize_probability: If true then log of probability is not computed. Otherwise take log2 of the probability score.
        '''

        words = []
        for sentence in sentence:
            words.extend(sentence)
        words = [word for word in words if ((word != SENTENCE_START) and (word != SENTENCE_END))]

        # Taking care of the edge case: Term in qury but not in vocab of train vocab or doc vocab

        for word in words:
            if word not in self.vocab_tf:
                if self.logging:
                    print(word, f"was not found in base vocabulary, it has been added now (along {self.unknown_word_count} others)!")
                self.unknown_word_count += 1
                
                if self.smoothing:
                    self.vocab_tf[word] = 1
                else:
                    self.vocab_tf[word] = 0

        sentence_prob = 1
        for word in words:
            sentence_prob *= self.calculate_unigram_probability(word)

    
        if normalize_probability:
            return sentence_prob
        else:
            return math.log2(sentence_prob) if sentence_prob != 0 else 0
"""     
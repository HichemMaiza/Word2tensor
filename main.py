# as part of an upwork project
import gensim

def main():
    """A function that transfrom word word2vec into tsv & bytes files
    """
    # Load model 
    model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
    # define output files 
    tensorsfp = 'GoogleNews-vectors-negative300.tsv' 
    metadatafp = 'GoogleNews-vectors-negative300.bytes'
    # Write data to files 
    with open( tensorsfp, 'w+') as tensors:
        with open( metadatafp, 'w+') as metadata:
            for word in model.index2word:
                encoded=word.encode('utf-8')
                metadata.write(encoded + '\n')
                vector_row = '\t'.join(map(str, model[word]))
                tensors.write(vector_row + '\n') 

if __name__ == '__main__':
    main()
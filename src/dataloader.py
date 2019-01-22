import numpy as np
import pandas as pd
from enumerator import SmilesEnumerator

class DataLoder:

    def __init__(self, df, batch_size):
        self.batch_size = batch_size
        self.data_size = len(df)
        self.first = df['first'].values
        self.second = df['second'].values
        self.sme = SmilesEnumerator()

    def __call__(self):
        firsts, seconds = self.sample_random_batch()
        firsts = self.random_transform(firsts)
        seconds = self.random_transform(seconds)
        # split
        # mask
        return firsts, seconds

    def sample_random_batch(self):
      '''
        function: Random transformation for SMILES. It may take some time.
        outputs: 
          firsts: A list of smiles
          seconds: A list of smiles. Same as firsts or not
          labels: A list of booleans indicating same or not
      '''
        rand = np.random.rand()
        rands = np.random.choice(self.data_size, self.batch_size, replace=False)
        firsts = self.first[rands]
        if rand<0.5: # Same molcules
            seconds = self.first[rands]
            labels = [1]*self.batch_size # Same
        else: # Different molecules
            seconds = self.second[rands]
            label = [0]*self.batch_size # Different
        return firsts, seconds, labels

    def random_transform(self, smiles):
      '''
        function: Random transformation for SMILES. It may take some time.
        input: A list of smiles
        output: A list of randomized smiles
      '''
        return [self.sme.randomize_smiles(sm) for sm in smiles]

    def mask(self, smiles):


    def split(self, smiles):
        return [' '.join(sm) for sm in smiles]


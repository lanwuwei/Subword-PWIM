import numpy as np
import torch
import sys

if torch.cuda.is_available():
 model=torch.load('./saved_dir/char_CNN_unigram.pkl')
else:
 model=torch.load('./saved_dir/char_CNN_unigram.pkl',map_location=lambda storage, loc: storage)

sent1=str(sys.argv[1]).split()
sent2=str(sys.argv[2]).split()

try:
 a,_=model(sent1,sent2,0)
except:
 pass

output = np.exp(a.data[0].cpu().numpy())
print('Paraphrase probability: '+str(output[1]))


## Subword-PWIM
This repository contains code and data used in the following [paper](https://arxiv.org/abs/1805.08297):

	@inproceedings{lan2018subword,
	  author     = {Lan, Wuwei and Xu, Wei},
  	  title      = {Character-based Neural Networks for Sentence Pair Modeling},
  	  booktitle  = {Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT)},
  	  year       = {2018}
  	} 
The original PWIM is from this [paper](http://www.aclweb.org/anthology/N16-1108):

	@inproceedings{he-lin:2016:N16-1,
	  author     = {He, Hua  and  Lin, Jimmy},
  	  title      = {Pairwise Word Interaction Modeling with Deep Neural Networks for Semantic Similarity Measurement},
  	  booktitle  = {Proceedings of the 2016 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT)},
  	  year       = {2016}
  	} 

## A few notes
1. This repositiory only contains MSRP dataset, here is [Twitter-URL](https://github.com/lanwuwei/language-net) here and [PIT-2015](https://github.com/cocoxu/SemEval-PIT2015).
2. We follow this [code](https://github.com/stanfordnlp/treelstm/blob/master/scripts/preprocess-sick.py) to do data preprocessing.
3. The model was implemented with PyTorch 0.4.0 and Torchtext 0.1.1 .
4. Sample command to run: python main.py, you can check main.py to add more arguments.
5. There is a demo you try (download [save_dir](https://drive.google.com/drive/folders/1h4uW-kho6dmnuPc5xYdf059FiNw0TRES?usp=sharing) first): 
   python -W ignore demo.py 'do you know where my book is' 'i cannot find my book, do you know where is it'

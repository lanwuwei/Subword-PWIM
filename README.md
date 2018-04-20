## Subword-PWIM
This repository contains code and data used in the following paper:

	@inproceedings{lan2018subword,
	  author     = {Lan, Wuwei and Xu, Wei},
  	title      = {Character-based Neural Networks for Sentence Pair Modeling},
  	booktitle  = {Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},
  	year       = {2018}
  	} 

## A few notes
1. This repositiory only contains MSRP dataset, here is [Twitter-URL](https://github.com/lanwuwei/language-net) here and [PIT-2015](https://github.com/cocoxu/SemEval-PIT2015).
2. We follow this [code](https://github.com/stanfordnlp/treelstm/blob/master/scripts/preprocess-sick.py) to do data preprocessing.
3. The model was implemented with PyTorch 0.4.0 .
4. Sample command to run: python main.py, you can check main.py to add more arguments.

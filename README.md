# smearcampaign
[![arXiv](http://img.shields.io/badge/arXiv-1510.00008-blue.svg?style=flat)](http://arxiv.org/abs/1510.00008)
[![DOI](https://zenodo.org/badge/142075113.svg)](https://zenodo.org/badge/latestdoi/142075113)

A repository containing the paper, data and notebooks for the __Kepler Smear Campaign__, a study of the brightest stars in the _Kepler_ field not observed conventionally by _Kepler_, but which we have retrieved with [smear photometry](https://arxiv.org/abs/1510.00008). 

The core science of this first paper is a study of the brightest red giants in the _Kepler_ field, using asteroseismology jointly with spectroscopy from the Tillinghast Reflector Échelle Spectrograph (TRES) to obtain chemical abundances. These stars will be important as benchmarks for surveys such as APOGEE. We present these together with a catalogue of the other bright stars in the _Kepler_ field and a determination of the variability class of each. 

All lightcurves will be made available as High-Level Science Products (HLSPs) on the Mikulski Archive for Space Telescopes (MAST) upon publication.

## Citation

If you wish to use light curves not available through MAST please offer coauthorship to members of the __Kepler Smear Campaign__. 

Please cite our forthcoming paper as Pope et al. (in prep), together with the original smear paper, using the following BibTeX:

	@ARTICLE{2016MNRAS.455L..36P,
	   author = {{Pope}, B.~J.~S. and {White}, T.~R. and {Huber}, D. and {Murphy}, S.~J. and 
		{Bedding}, T.~R. and {Caldwell}, D.~A. and {Sarai}, A. and {Aigrain}, S. and 
		{Barclay}, T.},
	    title = "{Photometry of very bright stars with Kepler and K2 smear data}",
	  journal = {\mnras},
	archivePrefix = "arXiv",
	   eprint = {1510.00008},
	 primaryClass = "astro-ph.IM",
	 keywords = {asteroseismology, techniques: photometric, stars: individual: HR 8500, 70 Aqr, HD 178875, stars: variables: general},
	     year = 2016,
	    month = jan,
	   volume = 455,
	    pages = {L36-L40},
	      doi = {10.1093/mnrasl/slv143},
	   adsurl = {http://adsabs.harvard.edu/abs/2016MNRAS.455L..36P},
	  adsnote = {Provided by the SAO/NASA Astrophysics Data System}
	}

## Code

The `keplersmear` source code used to produce these light curves is available at https://github.com/benjaminpope/keplersmear under a GPLv3 license. We regret that this has some difficult dependencies which may make it impractical at present for you to install. 
# smearcampaign
[![arXiv](http://img.shields.io/badge/arXiv-1510.00008-blue.svg?style=flat)](http://arxiv.org/abs/1510.00008)
[![DOI](https://zenodo.org/badge/142075113.svg)](https://zenodo.org/badge/latestdoi/142075113)

A repository containing the paper, data and notebooks for the __Kepler Smear Campaign__, a study of the brightest stars in the _Kepler_ field not observed conventionally by _Kepler_, but which we have retrieved with [smear photometry](https://arxiv.org/abs/1510.00008). 

The core science of this first paper is a study of the brightest red giants in the _Kepler_ field, using asteroseismology jointly with spectroscopy from the Tillinghast Reflector Échelle Spectrograph (TRES) to obtain chemical abundances. These stars will be important as benchmarks for surveys such as APOGEE. We present these together with a catalogue of the other bright stars in the _Kepler_ field and a determination of the variability class of each. 

All lightcurves are being ingested as High-Level Science Products (HLSPs) on the Mikulski Archive for Space Telescopes (MAST), and will be available [here](http://archive.stsci.edu/doi/resolve/resolve.html?doi=10.17909/t9-4sgf-9c19) and in this repository under data/release.

## Citation

If you wish to use light curves not available through MAST please offer coauthorship to members of the __Kepler Smear Campaign__. 

Please cite our paper using the following BibTeX:

	@ARTICLE{2019arXiv190509831P,
	   author = {{Pope}, B.~J.~S. and {Davies}, G.~R. and {Hawkins}, K. and {White}, T.~R. and 
		{Stokholm}, A. and {Bieryla}, A. and {Latham}, D.~W. and {Lucey}, M. and 
		{Aerts}, C. and {Aigrain}, S. and {Antoci}, V. and {Bedding}, T.~R. and 
		{Bowman}, D.~M. and {Caldwell}, D.~A. and {Chontos}, A. and 
		{Esquerdo}, G.~A. and {Huber}, D. and {Jofre}, P. and {Murphy}, S.~J. and 
		{van Reeth}, T. and {Silva Aguirre}, V. and {Yu}, J.},
	    title = "{The Kepler Smear Campaign: Light curves for 102 Very Bright Stars}",
	  journal = {arXiv e-prints},
	archivePrefix = "arXiv",
	   eprint = {1905.09831},
	 primaryClass = "astro-ph.SR",
	 keywords = {Astrophysics - Solar and Stellar Astrophysics, Astrophysics - Earth and Planetary Astrophysics, Astrophysics - Instrumentation and Methods for Astrophysics},
	     year = 2019,
	    month = may,
	   adsurl = {https://ui.adsabs.harvard.edu/abs/2019arXiv190509831P},
	  adsnote = {Provided by the SAO/NASA Astrophysics Data System}
	}

Could you please also cite it together with the original smear paper:

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
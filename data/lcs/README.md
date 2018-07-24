# lcs

This folder contains all the light curves from the **Kepler Smear Campaign**. 

They are 'combined' in the sense that there are two smear registers: 'virtual' and 'masked'. In cases where the star is extremely bright and/or near the edge of the chip, the direct saturation bleed column from the star can hit one or the other smear register and ruin the smear data. We automatically determine when this is the case and use both or just one of the smear registers for our light curve accordingly.

We have used the Oxford *Kepler* cotrending correction package `KeplerSC` (https://github.com/OxES/OxKeplerSC) to correct systematics in these light curves on a quarter-by-quarter basis. This is quite suboptimal in some cases, as stars can show real variability on quarter-long timescales! We accordingly save columns FLUX, FLUX_CORR_4 and FLUX_CORR_8 to include raw, 4-CBV-corrected and 8-CBV-corrected light curves. In cases where variability is expected to only be at high frequencies, we recommend FLUX_CORR_8; otherwise, we recommend 4 or none, as you can determine by eye.
The Jupyter Notebooks in this directory are for development and testing of
the results figures generation modules of the Salish Sea model nowcast system.

The links below are to static renderings of the notebooks via
[nbviewer.jupyter.org](https://nbviewer.jupyter.org/).
Descriptions under the links below are from the first cell of the notebooks
(if that cell contains Markdown or raw text).

* ##[hindcast-averages-sum_dfc.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/hindcast-averages-sum_dfc.ipynb)  
    
* ##[surfacewavemixingferry.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/surfacewavemixingferry.ipynb)  
    
* ##[Untitled.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/Untitled.ipynb)  
    
* ##[SummaryDocument.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/SummaryDocument.ipynb)  
    
    **Big List of Things**  
    ** VAT tests **  
    * Lots of model runs with varying horizontal and vertical time steps were done. It was decided to have the horizontal time step at 40s and veritcal time step at 2s [spreadsheet](https://docs.google.com/spreadsheets/d/1WqElPNd6KNrRubxgBGumVZ3DDPo6x8SE0uec44fLRKI/edit#gid=0)  
      
    **surface wave mixing tests**  
          
    | Test       | rn_crban | rn_charn | nn+z0_met | rn_avm0 | rn_avt0 |  
    |------------|----------|----------|-----------|---------|---------|  
    | base case  |  100     | 70 000   |     2     | 1e-6    |  1e-6   |  
    | Test A     |  150     | 20 000   |      1    | 1e-6    |  1e-6   |  
    | Test B     |  100     | 70 000   |       1   | 1e-6    |  1e-6   |  
    | base case2 |  100     | 70 000   |        2  | 1e-5    |  1e-5   |  
    | Test A2    |  150     | 20 000   |    1      | 1e-5    |  1e-5   |  
    |   Test B2  |  100     | 70 000   |     1     | 1e-5    |  1e-5   |  
      
    * Three month model runs were done with different parametrization of surface wave mixing on the Salish Sea configuration from Mar 7 to June 4, 2017.   
      
    * ferry comparisons [notebook 1](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/surfacewavemixingferry-Copy1.ipynb) [notebook 2](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/surfacewavemixingferry-Copy2.ipynb)  
    * Fraser River CTD comparison [notebook 1](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/util/CTDvsSurfaceWaveMixingTests.ipynb) [notebook 2](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/util/CTDvsSurfaceWaveMixingTests-Copy1.ipynb)  
    * looking at haloclines [notebook 1](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/surface-wave-mixing-haloclines.ipynb) [notebook 2](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/surface-wave-mixing-haloclines-2.ipynb)  
    **climatology**  
    * seasonal averages were made for top 30m temperature, salinity, sumdfc, sumgrme, and sumpp. Temperature and salinity also has climatology for the deepest cell. Available at `/results/SalishSea/climatology`.   
    * made by editing [this](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/NCO-3monDeepMeans-NowcastGreen-2017.ipynb)  
    **current predictions**  
    * SalishSeaAGRIF was run with the Haro Strait child grid with  
        * no winds  
        * climatology for tides  
        * climatology for rivers  
    * results [notebook](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/swiftsureAGRIF-zoomed-SEA.ipynb)  
    **Ariane experiments**  
    * Ariane experiments were done in hopes of validating the residence time stated in the Carrying Capacity Report. A select number of particles were released at the same time and left to wander for a month. Experiments were done for four different months[notebook](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/142f3e60a2fc919222f4d3d3e0453a021c04090b/notebooks/Ariane/BaynesSoundParticles.ipynb)  
    * Particles were released in Campbell River and left to wander for a month. We then counted where the particles ended up [notebook](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/142f3e60a2fc919222f4d3d3e0453a021c04090b/notebooks/CampbellRiverParticlesMore.ipynb)  
    **Model Evaluation**  
    * refer to [documentation](http://salishsea-meopar-docs.readthedocs.io/en/latest/NEMO36ModelEvaluation201702/index.html)  
    **SMELT diagnostic**  
    * Si vs N plots done for whole domain seperated by month for 2015 [notebook](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/smelt_diag/SiVsN.ipynb)  
    * time series of depth profiles were done for a location in Central Strait, Northern Strait, and Juan de Fuca for silicon, biogenic silicon, ammonium, nitrate, PON, DON, meesozooplankton, ciliates, diatoms, and flagellates [notebook](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/smelt_diag/depth-profile-time-series.ipynb)  
    * thalweg plots of ammonium, nitrate, excess Si, and limiting variables and rate limiting variable for diatoms, $Mesodinium$, and flagellates.    
      * 2015 [notebook](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/smelt_diag/LimitationAlongThalweg2015_w_NLim.NO.NH.ipynb)  
      * 2016 [notebook](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/smelt_diag/LimitationsAlongThalweg2016_w_NLim.NO.NH.ipynb)  
      * 2017 [notebook](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/smelt_diag/LimitationAlongThalweg2017_w_NLim.NO.NH.ipynb)  
      * video [notebook](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/smelt_diag/LimitingVariableVideo.ipynb)  
    * playing with rates [spreadsheet](https://docs.google.com/spreadsheets/d/1ZNkdVeFlW1hLMzBN0szDCwUNQjDsMLBnRdou52bdYcQ/edit#gid=1482259918)  
      * base [notebook](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/smelt_diag/CitizenScienceNutrients-surface-01feb-02may.ipynb)  
      * SiRatio1 [notebook](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/smelt_diag/CitizenScienceNutrients-SiRatio1.ipynb)  
      * SiRatio1.5 [notebook](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/smelt_diag/CitizenScienceNutrients-SiRatio1_5.ipynb)  
      * SiRatio2.2 [notebook](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/smelt_diag/CitizenScienceNutrients-SiRatio2_2.ipynb)  
      * SlowDiat [notebook](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/smelt_diag/CitizenScienceNutrients-slowdiat.ipynb)  
      * NewRiverSi [notebook](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/smelt_diag/CitizenScienceNutrients-NewRiverSi.ipynb)  
      * HalfSat [notebook](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/smelt_diag/CitizenScienceNutrients-HalfSat.ipynb)  
      * RateAndHalfSat [notebook](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/smelt_diag/CitizenScienceNutrients-RateAndHalfSat.ipynb)  
    **SalishSeaLake**  
    * constant analytical wind tests [notebook](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/SalishSeaLake//density-over-different-winds.ipynb)  
    * varying analytical winds tests 24-48-70 [notebook](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/SalishSeaLake//24-48-70-winds.ipynb)  
    * tracking density 1023.3 in nowcast [notebook](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/SalishSeaLake//nowcast-1023.3-animations.ipynb)  
    * added passive tracer with features  
      * Big Three thalweg videos [notebook](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/SalishSeaLake//BigThreeThalweg.ipynb)  
      * surface videos, pretty plots, and statistical analysis [notebook](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/SalishSeaLake//SUMMARY.ipynb)  


* ##[LimitationsAlongThalweg2.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/LimitationsAlongThalweg2.ipynb)  
    
* ##[hindcast-averages-sum_pp.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/hindcast-averages-sum_pp.ipynb)  
    
* ##[Limitations_along_thalweg.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/Limitations_along_thalweg.ipynb)  
    
* ##[citizensience.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/citizensience.ipynb)  
    
* ##[NCO-3monDeepMeans-NowcastGreen-2017.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/NCO-3monDeepMeans-NowcastGreen-2017.ipynb)  
    
* ##[Accessing-CTD-data.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/Accessing-CTD-data.ipynb)  
    
    How to access CTD data: a short guide  

* ##[hindcast-averages.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/hindcast-averages.ipynb)  
    
* ##[surface-wave-mixing-haloclines-2.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/surface-wave-mixing-haloclines-2.ipynb)  
    
* ##[GridToMap.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/GridToMap.ipynb)  
    
* ##[NCO-3monMeans-NowcastGreen-2017.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/NCO-3monMeans-NowcastGreen-2017.ipynb)  
    
* ##[surfacewavemixingferry-Copy1.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/surfacewavemixingferry-Copy1.ipynb)  
    
* ##[NCO-3monMeans-NowcastGreen-2015.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/NCO-3monMeans-NowcastGreen-2015.ipynb)  
    
* ##[surface-wave-mixing-haloclines.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/surface-wave-mixing-haloclines.ipynb)  
    
* ##[Wind_wth_coastline-May42017.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/Wind_wth_coastline-May42017.ipynb)  
    
    **Wind with Coastline**  
    **May 4, 2014**  

* ##[LimitationAlongThalweg2015_w_NLim.NO.NH.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/LimitationAlongThalweg2015_w_NLim.NO.NH.ipynb)  
    
* ##[Build-use-matrix.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/Build-use-matrix.ipynb)  
    
* ##[surfacewavemixingferry-Copy2.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/surfacewavemixingferry-Copy2.ipynb)  
    
* ##[averaged-over-30m.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/averaged-over-30m.ipynb)  
    
* ##[CHECKERBOARD.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/CHECKERBOARD.ipynb)  
    
* ##[Sandbox-May32017.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/Sandbox-May32017.ipynb)  
    
    **Sandbox**  
      
    **May 3, 2017**  
      


* ##[salmon-stats.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/salmon-stats.ipynb)  
    
    **salmon stats**  

* ##[Ariane-sandbox.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/Ariane-sandbox.ipynb)  
    
* ##[LimitationAlongThalweg2015.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/LimitationAlongThalweg2015.ipynb)  
    
* ##[Looking-at-tidal-height.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/Looking-at-tidal-height.ipynb)  
    
    **Tidal Heights in Nov-Dec, 2014**  
    **May 5, 2017**  

* ##[LimitationAlongThalweg2017_w_NLim.NO.NH.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/LimitationAlongThalweg2017_w_NLim.NO.NH.ipynb)  
    
* ##[swiftsure2.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/swiftsure2.ipynb)  
    
* ##[ferrysalinityvsnowcastgreen.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/ferrysalinityvsnowcastgreen.ipynb)  
    
* ##[swiftsureAGRIF.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/swiftsureAGRIF.ipynb)  
    
* ##[Bathymetry201702newnew.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/Bathymetry201702newnew.ipynb)  
    
    Looking at del  

* ##[LimitationsAlongThalweg2016_w_NLim.NO.NH.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/LimitationsAlongThalweg2016_w_NLim.NO.NH.ipynb)  
    
* ##[NCO-3monMeans-NowcastGreen-2016.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/NCO-3monMeans-NowcastGreen-2016.ipynb)  
    
* ##[turn-stats.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/turn-stats.ipynb)  
    
    **turn stats**  

* ##[CampbellRiverParticlesMore.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/CampbellRiverParticlesMore.ipynb)  
    
* ##[swiftsureAGRIF-zoomed-SEA.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/swiftsureAGRIF-zoomed-SEA.ipynb)  
    
* ##[swiftsureAGRIF-zoomed.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/swiftsureAGRIF-zoomed.ipynb)  
    
* ##[seasonal-averaged-plume.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/seasonal-averaged-plume.ipynb)  
    
* ##[hindcast-averages-sum_grme.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/hindcast-averages-sum_grme.ipynb)  
    
* ##[surface-mixing-comparisons.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/surface-mixing-comparisons.ipynb)  
    
    Comparing different values for surface mixing parameters.   

* ##[Updating.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/Updating.ipynb)  
    
    Updating old notebook to include hindcast.  

* ##[LatLonGenerator.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/LatLonGenerator.ipynb)  
    
* ##[all_years_averages_check.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/all_years_averages_check.ipynb)  
    
* ##[LimitationAlongThalweg2017.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/LimitationAlongThalweg2017.ipynb)  
    
* ##[SOG-stats.ipynb](https://nbviewer.jupyter.org/urls/bitbucket.org/salishsea/analysis-vicky/raw/tip/notebooks/SOG-stats.ipynb)  
    
    **SOG stats**  


##License

These notebooks and files are copyright 2013-2019
by the Salish Sea MEOPAR Project Contributors
and The University of British Columbia.

They are licensed under the Apache License, Version 2.0.
https://www.apache.org/licenses/LICENSE-2.0
Please see the LICENSE file for details of the license.

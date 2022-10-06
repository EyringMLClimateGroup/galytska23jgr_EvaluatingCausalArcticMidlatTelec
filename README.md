10.2022 @Evgenia Galytska (EG), Institute of Enviromental Physics (IUP), University of Bremen and Deutsches Zentrum für Luft- und Raumfahrt (DLR), Institut für Physik der Atmosphäre, Oberpfaffenhofen, Germany

This repository presents a sample of the causal model evaluation (CME) of Arctic-midlatitude teleconnections. The Jupyter Notebooks reproduce most of the figures on the paper "galytska22_jgr_arctic-midlatitude-telecon".

# **I. Installation of required packages **

#### **1.**  Install ESMValTool.

To install the ESMValTool, follow the official documentation here: <https://docs.esmvaltool.org/en/latest/quickstart/installation.html>

To reproduce the data used in this study, run the recipe _**cme_galytska22jgr.**_

#### 2. Install Tigramite to use PCMCI+.

Follow the official GitHub repository for the installation instructions: <https://github.com/jakobrunge/tigramite>

It is the User's responsibility to install the Tigramite package. 

# **II. Preparation for the analysis**

Please, follow the official tutorial to get acquainted with the application of the PCMCI+ algorithm from Tigramite package. 

<https://github.com/jakobrunge/tigramite/blob/master/tutorials/tigramite_tutorial_pcmciplus.ipynb>

To reproduce the causal graphs from **_Galtytska et al., 2022_** manuscript use the following parameters:

* For a conditional independence test  - linear partial correlation (`ParCorr`) and `significance='analytic'`, then the null distribution is assumed to be Student's t. 
* `mask_type = ‘y“` when testing different seasons, for example winter (December-January-February, DJF)
* maximum time delay `tau_max = 5 and`significance threshold `pc_alpha = 0.01`. 
* Once causal graphs are calculated 

#### **1.**  Download this repository.

```
git clone https://github.com/EyringMLClimateGroup/galytska22jgr_CME_arctic-midlat_teleconnections

```

#### **2.**  Create the environment from the environment.yml file and activate it.

```
conda env create --name my_env --file environment.yml
conda activate my_env

```

# **III. Causal model evaluation**

##### Data_preparation.ipynb

Use this code as an example to produce a dictionary with the results based on PCMCI+ calculations. 

##### 

##### Summaries_for_causal_model_evaluation.ipynb

Use this code to reproduce the number of climate models that simulate identical connections as detected from observations. The output is saved in a .txt file and represents the values in hexagons in **Fig. 4** and/or **Fig. 7**. This script also reproduces the summary of causal and contemporaneous links, see **Fig.5 in Galytska et al., 2022, JGR** and** Figs. S2, S3, S5-S7 in the supporting information in Galytska et al., 2022, JGR. **



##### F1-score_correlation_heatmap.ipynb

Use this script to reproduce **Fig. 6 from Galytska et al., 2022, JGR**.



##### F1-score_individual_networks.ipynb

Use this script to reproduce **Fig. 8 from Galytska et al., 2022, JGR**.







##### [OBS_CMIP6_pcmciplus.ipynb](../main/OBS_CMIP6_pcmciplus.ipynb):

1. In the **first code cell** (1st not counting markdown cells): **Remove the hashtag (#)** at the beginning of last **four** lines in the **Imports cell** (e.g. `from tigramite`...)
2. In the **third code cell** (3rd not counting markdown cells): **Change the path_to_data** accroding to where it is stored (i.e. **replace 'path_to_data' in the first two lines**)
3. In the **sixth code cell** (6th not counting markdown cells): **Change the path_to_data** accroding to where it is stored (i.e. **replace 'path_to_data' in the second line**)

##### [F1_score.ipynb](../main/F1_score.ipynb) and [Ensemble_graphs.ipynb](../main/Ensemble_graphs.ipynb):

1. In the **first code cell** (1st not counting markdown cells): **Remove the hashtag (#)** at the beginning of last line in the **Imports cell** (e.g. `from tigramite import plotting as tp`)

##### [Spatial_correlation.ipynb](../main/Spatial_correlation.ipynb):

1. In the **third code cell** (3rd not counting markdown cells): **Change the path_to_data** accroding to where it is stored (i.e. **replace 'path_to_data' in the first two lines**)
2. In the **fourth code cell** (4th not counting markdown cells): **Change the path_to_data** accroding to where it is stored (i.e. **replace 'path_to_data' in the fourth line**)



---

# **V. RESULTS**

##### Results from running Jupyter notebooks will be in the corresponding directory, identifies at each notebook.

          To refer to figures from the paper, please see overview_figures to locate the notebook needed to reproduce a specific plot. 

---

# **REFERENCES**:

> ESMValTool: Eyring et al., 2020: [Earth System Model Evaluation Tool (ESMValTool) v2.0 – an extended set of large-scale diagnostics for quasi-operational and comprehensive evaluation of Earth system models in CMIP.](https://gmd.copernicus.org/articles/13/3383/2020/)
>
> [PCMCI+: J. Runge (2020): Discovering contemporaneous and lagged causal relations in autocorrelated nonlinear time series datasets. Proceedings of the 36th Conference on Uncertainty in Artificial Intelligence, UAI 2020,Toronto, Canada, 2019, AUAI Press, 2020.](http://auai.org/uai2020/proceedings/579_main_paper.pdf)



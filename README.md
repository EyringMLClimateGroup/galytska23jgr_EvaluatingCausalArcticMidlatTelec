# CME_arctic-midlat_teleconnections

This repository presents a sample of the causal model evaluation (CME) of Arctic-midlatitude teleconnections. This repository is part of the manuscript submitted to JGR: Atmospheres.

It is available on ArXiV: 
Corresponding DOI: 

## I. Installation of required packages 

#### 1.  Install ESMValTool.

To install ESMValTool, please follow the official documentation here: <https://docs.esmvaltool.org/en/latest/quickstart/installation.html>. To reproduce and analyze data used in this study, run the recipe _**cme_galytska22jgr.**_

#### 2. Install Tigramite and use PCMCI+.

Follow the official GitHub repository for the installation instructions: <https://github.com/jakobrunge/tigramite>. It is the User's responsibility to install the Tigramite package. 

Please, follow the official tutorial to get acquainted with the application of the PCMCI+ algorithm from the Tigramite package. 

<https://github.com/jakobrunge/tigramite/blob/master/tutorials/tigramite_tutorial_pcmciplus.ipynb>

To reproduce the causal graphs from **_Galtytska et al., 2022_** manuscript use the following parameters:

* For a conditional independence test  - linear partial correlation (`ParCorr`) and `significance="analytic"`, then the null distribution is assumed to be Student's t. 
* `mask_type = "y“` when testing different seasons, for example winter (December-January-February, DJF)
* maximum time delay `tau_max = 5 and`significance threshold `pc_alpha = 0.01`. 

## II. Preparation for the analysis

#### 1.  Download this repository.

```
git clone https://github.com/EyringMLClimateGroup/galytska22jgr_CME_arctic-midlat_teleconnections

```

#### 2.  Create the environment from the environment.yml file and activate it.

```
conda env create --name my_env --file environment.yml
conda activate my_env

```

Install anaconda ipykernel (if needed) and create a new kernel for Jupyter Notebook

```
conda install -c anaconda ipykernel
python -m ipykernel install --user --name=my_env

```

## III. Causal model evaluation

##### Data_preparation.ipynb

Use this code as an example to produce a dictionary with the results based on PCMCI+ calculations. 

1. In the **first code cell** uncomment the lines associated with the import of tigramite and related modules (e.g. `import tigramite`, `from tigramite import ...`)
2. Modify the **second code cell** based on the models (`model_names`), actors (`actors`), seasons (`masking_list`), maximum lag in months (`max_timelag`), and the significance threshold (`pc_alpha`). 
3. Provide in **the third code cell** the path to the base folder (`base_folder`), which serves as the output folder. The results will be structured and saved in this folder. 
4. We suggest reading original data from observations and CMIP6 models into a dictionary with the structure as suggested in the **forths cell code**.
5. In the **sevenths cell code** uncomment the code related to tigramite plotting. Decide (with `True` or `False`) whether you would like to save the original causal graphs (`plot_Causal_Graphs`)  and the dictionary with the output from tigramite (`save_orig_dict`). 

##### Summaries_for_causal_model_evaluation.ipynb

Use this code to reproduce the number of climate models that simulate identical connections as detected from observations. The output is saved in a .txt file and represents the values in hexagons in **Fig. 4** and/or **Fig. 7**. This script also reproduces the summary of causal and contemporaneous links, see **Fig.5 in Galytska et al., 2022, JGR** and ** Figs. S2, S3, S5-S7 in the supporting information in Galytska et al., 2022, JGR. **

1. Modify the **second code cell** based on the models (`model_names`), actors (`actors`), seasons (`masking_list`), maximum lag in months (`max_timelag`), and the significance threshold (`pc_alpha`). 
2. Load the dictionaries, saved as the output from **Data_preparation.ipynb** notebook or alternatively the dictionary with the `results` from the application of Tigramite on specific datasets (see the last code cell in **Data_preparation.ipynb** notebook for more tips). 

##### F1-score_correlation_heatmap.ipynb

Use this script to reproduce **Fig. 6 from Galytska et al., 2022, JGR**.

1. In the **first code cell** modify the path to the `base_folder` and read in the dictionary with the output from Tigramite calculations.

##### F1-score_individual_networks.ipynb

Use this script to reproduce **Fig. 8 from Galytska et al., 2022, JGR**.

1. In the **first code cell** if needed modify the seasons (`masking_list`) and the significance threshold (`pc_alpha`). 
2. In the **second code cell** modify the path to the `base_folder` and read in the dictionary with the output from Tigramite calculations.
3. In the **fifth code cell** modify the output path to save the figure.

## V. RESULTS

Results from running Jupyter notebooks will be saved into the corresponding directory, identified at each Notebook. To refer to figures from the paper, please see `list_of_figures.txt` to locate the notebook needed to reproduce a specific plot. 

## References

1. Eyring, V., Bock, L., Lauer, A., Righi, M., Schlund, M., Andela, B., and others: Earth System Model Evaluation Tool (ESMValTool) v2.0 – an extended set of large-scale diagnostics for quasi-operational and comprehensive evaluation of Earth system models in CMIP, Geosci. Model Dev., 13, 3383–3438, <https://doi.org/10.5194/gmd-13-3383-2020>, 2020.
2. Runge. J.: Discovering contemporaneous and lagged causal relations in autocorrelated nonlinear time series datasets. Proceedings of the 36th Conference on Uncertainty in Artificial Intelligence, UAI 2020, Toronto, Canada, 2019, AUAI Press, <https://github.com/mlresearch/v124/blob/gh-pages/runge20a/runge20a.pdf>, 2020.





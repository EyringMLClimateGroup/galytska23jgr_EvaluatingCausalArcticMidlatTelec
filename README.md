# Evaluating causal Arctic-midlatitude teleconnections in CMIP6

This repository presents a sample of the causal model evaluation (CME) of Arctic-midlatitude teleconnections in observational datasets and CMIP6 simulations. This repository is part of the manuscript submitted to JGR: Atmospheres.

It is available on ArXiV: 

Corresponding DOI: 

## **I. Preparation of the data with ESMValTool**
#### **Step 1.**  Install ESMValTool.
To install ESMValTool, please follow the [official documentation](https://docs.esmvaltool.org/en/latest/quickstart/installation.html) and/or [ESMValTool Tutorial](https://tutorial.esmvaltool.org/). 
#### **Step 2.**  Run ESMValTool recipe [_**recipe_galytska23jgr.yml**_](https://docs.esmvaltool.org/en/latest/recipes/recipe_galytska23jgr.html#recipe-galytska23jgr).

This step reproduces data used in this study. 

## **II. Preparation for the analysis**

#### **Step 3.**  Download this repository.

```
git clone https://github.com/EyringMLClimateGroup/galytska23jgr_EvaluatingCausalArcticMidlatTelec

cd galytska23jgr_EvaluatingCausalArcticMidlatTelec
```

#### **Step 4.** Create the environment from the environment.yml file and activate it.

```
conda env create --name my_env --file environment.yml
conda activate my_env
```
Install anaconda ipykernel (if needed) and create a new kernel for Jupyter Notebook

```
conda install -c anaconda ipykernel
python -m ipykernel install --user --name=my_env
```
Keep this environment activated and proceed with the **Step 5**.
#### **Step 5.** Install Tigramite and use PCMCI+.
In the activated environment from the **Step 4** install Tigramite. 

To install Tigramite follow the official [GitHub repository](https://github.com/jakobrunge/tigramite) for the installation instructions. It is the User's responsibility to install the Tigramite package. Please, follow the [official Tigramite tutorials](https://github.com/jakobrunge/tigramite/tree/master/tutorials) to get acquainted with the application of the PCMCI+ algorithm from the Tigramite package. 

To reproduce the causal graphs from **_Galytska et al., 2023_** manuscript use the following parameters:

* For a conditional independence test  - linear partial correlation (`ParCorr`) and `significance='analytic'`, then the null distribution is assumed to be Student's t. 
* `mask_type = ‘y“` when testing different seasons, for example winter (December-January-February, DJF)
* maximum time delay `tau_max = 5 and` significance threshold `pc_alpha = 0.01`. 

## **III. Causal model evaluation**

#### [Data_preparation.ipynb](Data_preparation.ipynb)

Use this notebook as an example to produce a dictionary with the results based on PCMCI+ calculations. 

1. In the **first notebook cell** uncomment the lines associated with the import of tigramite and related modules (e.g. `import tigramite`, `from tigramite import ...`)
2. Modify the **second notebook cell** based on the models (`model_names`), actors (`actors`), seasons (`masking_list`), maximum lag in months (`max_timelag`), and the significance threshold (`pc_alpha`). 
3. Provide in **the third notebook cell** the path to the base folder (`base_folder`), which serves as the output folder. The results will be structured and saved in this folder. 
4. We suggest reading original data from observations and CMIP6 models into a dictionary with the structure as suggested in the **forths notebook cell**.
5. In the **sevenths notebook cell** uncomment the code related to Tigramite plotting.  Decide whether you would like to save the original causal graphs (`plot_Causal_Graphs`) and the dictionary with the output from Tigramite (`save_orig_dict`), insert `True` or `False`. 

#### [Summaries_for_causal_model_evaluation.ipynb](Summaries_for_causal_model_evaluation.ipynb)

Use this notebook to reproduce the number of climate models that simulate identical connections as detected from observations. The output is saved in a .txt file and represents the values in hexagons in **Fig. 4** and/or **Fig. 7**. This notebook also reproduces the summary of causal and contemporaneous links, see **Fig.5 in Galytska et al., 2023, JGR** and **Figs. S5, S6, S8-S10** in the supporting information.

1. Modify the **second notebook cell** based on the models (`model_names`), variables (`variables`), seasons (`masking_list`), maximum lag in months (`max_timelag`), and the significance threshold (`pc_alpha`). 
2. Load the dictionaries, saved as the output from **Data_preparation.ipynb** notebook or alternatively the dictionary with the `results` from the application of Tigramite on specific datasets (see the last code cell in **Data_preparation.ipynb** notebook for more tips). 

#### [F1-score_correlation_heatmap.ipynb](F1-score_correlation_heatmap.ipynb)

Use this notebook to reproduce **Fig. 6 from Galytska et al., 2023, JGR**.

1. In the **first notebook cell** modify the path to the `base_folder` and read in the dictionary with the output from Tigramite calculations.

#### [F1-score_individual_networks.ipynb](F1-score_individual_networks.ipynb)

Use this notebook to reproduce **Fig. 8 from Galytska et al., 2023, JGR**.

1. In the **first notebook cell** if needed modify the seasons (`masking_list`) and the significance threshold (`pc_alpha`). 
2. In the **second notebook cell** modify the path to the `base_folder` and read in the dictionary with the output from Tigramite calculations.
3. In the **fifth notebook cell** modify the output path to save the figure.

## **IV. RESULTS**

Results from running Jupyter notebooks will be saved into the corresponding directory, identified at each Notebook. To refer to figures from the paper, please see `list_of_figures.txt` to locate the notebook needed to reproduce each specific plot. 

## **References**

1. Eyring, V., Bock, L., Lauer, A., Righi, M., Schlund, M., Andela, B., and others: Earth System Model Evaluation Tool (ESMValTool) v2.0 – an extended set of large-scale diagnostics for quasi-operational and comprehensive evaluation of Earth system models in CMIP, Geosci. Model Dev., 13, 3383–3438, <https://doi.org/10.5194/gmd-13-3383-2020>, 2020.
2. Runge. J.: Discovering contemporaneous and lagged causal relations in autocorrelated nonlinear time series datasets. Proceedings of the 36th Conference on Uncertainty in Artificial Intelligence, UAI 2020, Toronto, Canada, 2019, AUAI Press, <https://github.com/mlresearch/v124/blob/gh-pages/runge20a/runge20a.pdf>, 2020.



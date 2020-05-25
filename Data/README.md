
The "Data" folder stores

1) The raw data

This should be downloaded from the Zenodo Repository 

https://doi.org/10.5281/zenodo.3673744

leading to the three folders:

hashtags_frequency_day/
hashtags_frequency_hour/
hashtags_frequency_minutes/

2) Intermediate data set required to generate Figures 1-5 in the paper.

These datasets are generated from the raw data by running the "aggregate_data.ipynb" notebook located in the folder ../notebooks/

The file "combined_data_firstDay.csv" contains the counts of hashtags with more than 100 appearances in the first day of our dataset. It is used as an example in the notebook "model_fitting.ipynb"
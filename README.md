Welcome to this repository! In it, you will find files related to shallow convection in the Tropical Eastern Pacific, and how that influences deeper convection in the West Pacific. This project was done at the University of Washington with the help and guidance of Dennis Hartmann.

Because there are a number of files, I have suggested an order in which I think the Jupyter Notebooks should be run:
- seasonal_mass_flux
- xarray_annual_cycle
- eofs_seasonal_mass_flux
- hovmoller
- create_pcs_from_eofs


This repository relies heavily on [ERA-Interim](https://apps.ecmwf.int/datasets/data/interim-full-moda/levtype=pl/) monthly means data. None of it is available in this repository, but you can download it for yourself following the link provided. I have included a script in this repository, `erai_global_moda_script.py`, that will do it for you once you have an account. If you use the Anaconda distribution, I would advise creating a virtual environment to use this program because it will downgrade your verion of Python to 2.7. However, per the ECMWF's own website: "ERA Interim is being phased out. Users are strongly advised to migrate to ERA5. The last date to be made available in ERA Interim will be 31 August 2019, which will be released at the end of October 2019."


# SEBAL Soil Heat Flux Python Package

This package provides a Python implementation of the soil heat flux (G) calculation from the Surface Energy Balance Algorithm for Land (SEBAL) model. SEBAL is a remote sensing-based approach for estimating evapotranspiration and energy balance components at the land surface. The soil heat flux is a key part of the energy balance and is calculated using net radiation, surface temperature, NDVI, and albedo.

Gregory H. Halverson (they/them)<br>
[gregory.h.halverson@jpl.nasa.gov](mailto:gregory.h.halverson@jpl.nasa.gov)<br>
NASA Jet Propulsion Laboratory 329G

## Features

- Implements the SEBAL soil heat flux (G) calculation using empirical relationships.
- Accepts both numpy arrays and Raster objects for input data.
- Includes vegetation correction based on NDVI.

## Installation

Install the `SEBAL-soil-heat-flux` package from PyPi using pip:

```fish
pip install SEBAL-soil-heat-flux
```

## Usage

Import the main function and use it with your raster or numpy array data:

```python
from SEBAL_soil_heat_flux import calculate_SEBAL_soil_heat_flux

G = calculate_SEBAL_soil_heat_flux(Rn, ST_C, NDVI, albedo)
```

Where:
- `Rn`: Net radiation at the surface
- `ST_C`: Surface temperature in Celsius
- `NDVI`: Normalized Difference Vegetation Index
- `albedo`: Surface albedo

## References

Bastiaanssen, W. G. M., Menenti, M., Feddes, R. A., & Holtslag, A. A. M. (1998). A remote sensing surface energy balance algorithm for land (SEBAL): 1. Formulation. *Journal of Hydrology*, 212-213, 198–212. https://doi.org/10.1016/S0022-1694(98)00253-4

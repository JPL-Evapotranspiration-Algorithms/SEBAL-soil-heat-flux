from typing import Union

import numpy as np
import rasters as rt
from rasters import Raster

def calculate_SEBAL_soil_heat_flux(
        Rn: Union[Raster, np.ndarray], 
        ST_C: Union[Raster, np.ndarray], 
        NDVI: Union[Raster, np.ndarray], 
        albedo: Union[Raster, np.ndarray]) -> Union[Raster, np.ndarray]:
    """
    Calculates the soil heat flux (G) in the Surface Energy Balance Algorithm for Land (SEBAL) model.

    The formula used is a simplification of the more complex relationship between these variables in the energy balance at the surface.

    Parameters:
        Rn (np.ndarray or Raster): Net radiation at the surface.
        ST_C (np.ndarray or Raster): Surface temperature in Celsius.
        NDVI (np.ndarray or Raster): Normalized Difference Vegetation Index, indicating the presence and condition of vegetation.
        albedo (np.ndarray or Raster): Measure of the diffuse reflection of solar radiation.

    Returns:
        np.ndarray or Raster: The soil heat flux (G), a key component in the energy balance.

    Reference:
        Bastiaanssen, W. G. M., Menenti, M., Feddes, R. A., & Holtslag, A. A. M. (1998).
        A remote sensing surface energy balance algorithm for land (SEBAL): 1. Formulation.
        Journal of Hydrology, 212-213, 198–212. https://doi.org/10.1016/S0022-1694(98)00253-4
    """
    # Empirical coefficients used in the calculation
    coeff1 = 0.0038
    coeff2 = 0.0074
    
    # Vegetation cover correction factor
    NDVI_correction = 1 - 0.98 * NDVI ** 4
    
    # Calculation of the soil heat flux (G)
    G = Rn * ST_C * (coeff1 + coeff2 * albedo) * NDVI_correction
    
    G = rt.clip(G, 0, None)

    return G

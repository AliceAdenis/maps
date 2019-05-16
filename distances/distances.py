import numpy as np

from numba import double
from numba.decorators import jit, autojit


@jit(nopython=True)
def distance_great_circle(u, v, r=1.):
    """ Fast great-circle path distance using Haversine formula
    (at least faster than geopy.distance.distance but less accurate)

    Parameters
    ----------
    u : tuple
        (latitude, logitude) of first point
    v : tuple
        (latitude, logitude) of second point
    r : float
        radius of the sphere (set to 1.0 for a result in radian and to
        6335.439 for a result in km upon the Earth)

    Returns
    -------
    float
        approximation of the great-circle path distance
    """

    lat_1, lon_1 = u
    lat_2, lon_2 = v
    lat_1, lon_1, lat_2, lon_2 = lat_1*np.pi/180, lon_1*np.pi/180, lat_2*np.pi/180, lon_2*np.pi/180

    d_lon = np.abs(lon_1 - lon_2)

    A = np.power(np.cos(lat_2)*np.sin(d_lon), 2)
    B = np.power(np.cos(lat_1)*np.sin(lat_2) - np.sin(lat_1)*np.cos(lat_2)*np.cos(d_lon), 2)
    C = np.sin(lat_1)*np.sin(lat_2) + np.cos(lat_1)*np.cos(lat_2)*np.cos(d_lon)

    return r*np.arctan(np.sqrt(A + B) / C)

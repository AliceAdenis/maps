import numpy as np


def distance_great_circle(u,v):
    """ Fast great-circle path distance using Haversine formula
    (at least faster than geopy.distance.distance but less accurate)
    """

    lat_1, lon_1 = u
    lat_2, lon_2 = v
    lat_1, lon_1, lat_2, lon_2 = lat_1*np.pi/180, lon_1*np.pi/180, lat_2*np.pi/180, lon_2*np.pi/180

    d_lon = np.abs(lon_1 - lon_2)

    A = np.power(np.cos(lat_2)*np.sin(d_lon), 2)
    B = np.power(np.cos(lat_1)*np.sin(lat_2) - np.sin(lat_1)*np.cos(lat_2)*np.cos(d_lon), 2)
    C = np.sin(lat_1)*np.sin(lat_2) + np.cos(lat_1)*np.cos(lat_2)*np.cos(d_lon)

    return np.arctan(np.sqrt(A + B) / C)


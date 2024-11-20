# Building Height Estimation

This repository demonstrates a Python-based project to estimate building heights using pixel coordinates and drone flight parameters. The project involves calculating pixel size, determining distances between coordinates, and deriving the average height of a building based on Ground Sampling Distance (GSD) and flight height.

## Features

    •    Pixel Size Calculation: Computes the pixel size based on Ground Sampling Distance (GSD) and drone flight height.
    •    Distance Measurement: Calculates the distance between consecutive pixel pairs in meters.
    •    Average Distance Computation: Derives an average distance from multiple coordinate pairs.
    •    Building Height Estimation: Estimates the height of a building using the calculated average distance and flight height.
    
## Why This Project?

Estimating building heights is an essential aspect of urban planning, construction monitoring, and remote sensing. This project provides a simplified yet practical implementation of height estimation using fundamental parameters such as GSD and pixel coordinates. It serves as a foundation for more advanced calculations and integrations in photogrammetry.

## How It Works

The project follows a structured pipeline:
    1.    Pixel Size Calculation: Computes the size of each pixel in meters based on the GSD and flight height.
    2.    Distance Calculation: Measures distances between consecutive pixel coordinates in meters.
    3.    Average Distance Computation: Aggregates all distances to calculate an average value.
    4.    Height Estimation: Uses the average distance and drone flight height to estimate the building’s height.
    
## Requirements

To run the project, ensure you have the following installed:
    •    Python 3.8+
    •    Libraries: math
    
## Example Output

Pixel size: 0.000089 meters
Distances between pixel pairs: [12.45, 15.67, 10.23, 13.56]
Average distance: 13.48 meters
Estimated building height: 1213.20 meters


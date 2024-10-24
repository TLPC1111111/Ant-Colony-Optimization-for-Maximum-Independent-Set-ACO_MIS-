# Ant Colony Optimization for Maximum Independent Set (ACO_MIS)

This project implements the Ant Colony Optimization (ACO) algorithm to solve the Maximum Independent Set (MIS) problem in a graph. The MIS problem is a classic problem in graph theory where the goal is to find the largest subset of vertices such that no two vertices in the subset are adjacent.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Components](#components)
- [License](#license)

## Features

- Random generation of graph nodes and edges.
- Visualization of the graph and the computed independent sets.
- Configurable parameters for the ACO algorithm.
- Supports input from datasets.

## Requirements

- Python 3.6+
- Required packages:
  - `argparse`
  - `random`
  - `matplotlib`
  - `keyboard`
  - `pandas`
  - `scikit-learn`
  - `tqdm`

You can install the required packages using pip:

```bash
pip install matplotlib pandas scikit-learn tqdm
```

## Installation
1.Clone the repository:

```bash
git clone https://github.com/yourusername/ACO_MIS.git
cd ACO_MIS
```

## Usage
To run the ACO algorithm, execute the following command:

```bash
python main.py --points_num <number_of_points> --ants_num <number_of_ants> --max_iteration <max_iterations> --rho <evaporation_coefficient> --alpha <pheromone_weight> --beta <heuristic_weight> --Q <constant> --max_x <max_x_coordinate> --min_x <min_x_coordinate> --max_y <max_y_coordinate> --min_y <min_y_coordinate>
```

## Example
```bash
python main.py --points_num 20 --ants_num 6 --max_iteration 150 --rho 0.3 --alpha 3 --beta 5 --Q 10 --max_x 300 --min_x 0 --max_y 300 --min_y 0
```

## Parameters

- **points_num**:The number of points (nodes) in the graph. Default is 20.
- **ants_num**: The number of ants used in the algorithm. Default is 6.
- **max_iteration**: The maximum number of iterations for the algorithm. Default is 150.
- **rho**: Evaporation coefficient of pheromones. Default is 0.3.
- **alpha**: Weight of pheromones. Default is 3.
- **beta**: Weight of heuristic value. Default is 5.
- **Q**: A constant used in pheromone update. Default is 10.
- **max_x, min_x**: Maximum and minimum x-coordinates for node generation.
- **max_y, min_y**: Maximum and minimum y-coordinates for node generation.

## Components
- main.py: The main entry point for executing the ACO algorithm.
- ACO_of_MIS.py: Contains the implementation of the ACO algorithm to solve the MIS problem.
- init_support.py: Handles the initialization of data and constructs the necessary edges based on input data.
- Utilize.py: Contains utility functions for initializing points, edges, and calculating heuristic values.
- README.md: Documentation for the project.











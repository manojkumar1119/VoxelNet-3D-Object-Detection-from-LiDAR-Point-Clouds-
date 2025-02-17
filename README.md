## Overview
This repository contains an implementation of **VoxelNet**, a 3D object detection framework that directly operates on sparse LiDAR point clouds. The network eliminates the need for hand-crafted feature engineering by learning discriminative features end-to-end, achieving state-of-the-art accuracy on the KITTI 3D object detection benchmark.  

## Key Features
- **End-to-End Learning:** Integrates feature extraction and 3D bounding box prediction.  
- **Voxel Feature Encoding (VFE):** Encodes local 3D shape information within each voxel.  
- **Sparse Tensor Representation:** Efficiently processes sparse point clouds, reducing memory usage.  
- **Region Proposal Network (RPN):** Outputs 3D bounding boxes and classification scores.  

## Architecture
The VoxelNet architecture consists of three main components:  
1. **Feature Learning Network:** Encodes each voxel using stacked VFE layers.  
2. **Convolutional Middle Layers:** Aggregate spatial context using 3D convolutions.  
3. **Region Proposal Network (RPN):** Outputs 3D bounding boxes and classification scores.  

## Installation
To set up the project, follow these steps:  
```bash
# Clone the repository
git clone ..

# Navigate to the project directory
cd .

# Install dependencies
pip install -r requirements.txt


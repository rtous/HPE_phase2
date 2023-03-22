# HPE Phase 2

- Render animations from a known dataset (e.g. Panoptic)
- Explore weak points of Flashback project:
	- Best 3D HPE from monocular video (specially movie clips, with truncations, etc.).
	- Revise universal configurable 3D model (Meta Human, etc.)
	- Revise retargetting (hands, inevitable loss blend shapes?)
	- Revise shaders
	- Multiperson
- A library for common tasks
	- shape-to-skeleton regression (SMPL joint regressor matrix)
		- 
	- skeleton pkl to json util
	-  

## Panoptic dataset

- CMU Panoptic (includes hands)
- http://domedb.perception.cs.cmu.edu/
- toolbox: https://github.com/CMU-Perceptual-Computing-Lab/panoptic-toolbox
- Monocular dataset: http://domedb.perception.cs.cmu.edu/mtc.html
- coco19 keypoint definition

### Setup Panoptic dataset

git clone https://github.com/CMU-Perceptual-Computing-Lab/panoptic-toolbox
cd panoptic-toolbox

./scripts/getData.sh 171204_pose1_sample

This script will create a folder "./171204_pose1_sample" and download the following files.

	- 171204_pose1_sample/hdVideos/hd_00_XX.mp4 #synchronized HD video files (31 views)
	- 171204_pose1_sample/vgaVideos/KINECTNODE%d/vga_XX_XX.mp4 #synchrponized VGA video files (480 views)
	- 171204_pose1_sample/calibration_171204_pose1_sample.json #calibration files
	- 171204_pose1_sample/hdPose3d_stage1_coco19.tar #3D Body Keypoint Data (coco19 keypoint definition)
	- 171204_pose1_sample/hdFace3d.tar #3D Face Keypoint Data
	- 171204_pose1_sample/hdHand3d.tar #3D Hand Keypoint Data

## SoA key points

- SMPL (no hands, no face) still SoA
- Latest mostly get shape, then kinematics (easily with SMPL joint regressor matrix)
- still challenges on single image 3D HPE. Video-based works too, but they inherit most limitations of the image-based.
- multi-person can be solved with single-person in a top-down approach
- many latest works focusing on crowds (AMASS dataset)

## SoA stack (latest on top)

- Panoptic paper: [Monocular Total Capture: Posing Face, Body, and Hands in the Wild](http://domedb.perception.cs.cmu.edu/mtc.html)
	- Hands and face :-)
	- Interesting use of 2D part orientation
	- Failure with truncation (the paper says)

- [SMPL-IK: Learned Morphology-Aware Inverse Kinematics for AI,Driven Artistic Workflows](https://arxiv.org/pdf/2208.08274.pdf)
	- Includes an SMPL retargetting strategy :-)
- EasyMocap and 

- Video explaining SMPL in detail: https://www.youtube.com/watch?v=rzpiSYTrRU0

## LOG stack

- check 
- check panoptic dataset to see if I can render animations with flashback from there
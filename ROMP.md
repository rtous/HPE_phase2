# ROMP

https://github.com/Arthur151/ROMP

## Installation

#Do not need to clone the repo!
#Here
python3 -m venv romp_venv
source romp_venv/bin/activate
pip install --upgrade setuptools numpy cython lap
pip install --upgrade pip wheel
pip install opencv-python==3.4.13.47
pip install --upgrade simple-romp

romp --mode=video --calc_smpl --render_mesh -i=demo_images/ -o=output

ALTERATIVE (install from sources):

git clone https://github.com/Arthur151/ROMP.git
cd ROMP
python3 -m venv romp_venv
source romp_venv/bin/activate
python setup.py install

## Usage

SEE: https://github.com/Arthur151/ROMP/blob/master/simple_romp/README.md


open /Applications/Python\ 3.8/Install\ Certificates.command

romp --mode=video --calc_smpl --render_mesh -i=demo/images -o=output
bev -m video -i /path/to/image/folder/ -o /path/to/output/folder/

OVER CHARADE DATASET:

(probably breaks with .png, I changed to .jpg)

romp --mode=video --calc_smpl --render_mesh -i=/Users/rtous/DockerVolume/charade_full/input/imagesJPG/ -o=output

bev -m video -i /path/to/image/folder/ -o /path/to/output/folder/
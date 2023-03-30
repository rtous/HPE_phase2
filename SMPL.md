# SMPL

3D pose format:
	- 72 values = 3*24, 24 joint ROTATIONS
	- ROATION: 3 values: axis-angle format (a 3D vector that traverses the object like a chicken and an angle that rotates it). The 3D vector is the axis, but it does not have magnitude 1, instead, the magnitude of the vector is the rotation angle.
	- ROTATIONS with respect the SMPL T-Pose. Because of the inner rotations of bones, these rotations do not work if directly applied to an arbitrary 3D model (need to either (a) adapt the rig to the SMPL rig or (b) re-rig the model with SMPL rig)

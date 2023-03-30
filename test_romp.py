import romp
import cv2
import numpy as np

def exportPose(pose_detached, global_orient, camera_center, camera_pose, filename="/Users/rtous/DockerVolume/flashback/data/smplfifyx/output.json"):
    JOINT_NAMES = [
        'pelvis',
        'left_hip',
        'right_hip',
        'spine1',
        'left_knee',
        'right_knee',
        'spine2',
        'left_ankle',
        'right_ankle',
        'spine3',
        'left_foot',
        'right_foot',
        'neck',
        'left_collar',
        'right_collar',
        'head',
        'left_shoulder',
        'right_shoulder',
        'left_elbow',
        'right_elbow',
        'left_wrist',
        'right_wrist',
    	'L_Hand',#'jaw',
        'R_Hand'#'left_eye_smplhf',
        #'right_eye_smplhf',
        #'left_index1',
        #'left_index2',
        #'left_index3',
        #'left_middle1',
        #'left_middle2',
        #'left_middle3',
        #'left_pinky1',
        #'left_pinky2',
        #'left_pinky3',
        #'left_ring1',
        #'left_ring2',
        #'left_ring3',
        #'left_thumb1',
        #'left_thumb2',
        #'left_thumb3',
        #'right_index1',
        #'right_index2',
        #'right_index3',
        #'right_middle1',
        #'right_middle2',
        #'right_middle3',
        #'right_pinky1',
        #'right_pinky2',
        #'right_pinky3',
        #'right_ring1',
        #'right_ring2',
        #'right_ring3',
        #'right_thumb1',
        #'right_thumb2',
        #'right_thumb3'
    ]
    print("\t\033[95m 1) Exporting pose into "+filename+"\033[0m ")
    import json
    smplx_json = "" 

    smplx_json += "{"

    #global_orient
    smplx_json += "\"global_orient\":"+json.dumps(global_orient.tolist())+","

    #camera
    smplx_json += "\"camera\":"
    smplx_json += "{\"camera_center\": "+json.dumps(camera_center.tolist())+","
    smplx_json += " \"camera_pose\":"+json.dumps(camera_pose.tolist())+"},"

    #rotations
    smplx_json += "\"compact_axis_angle_rotations\":"
    smplx_json += "{"
    for i, n in enumerate(JOINT_NAMES):
        smplx_json += "\""+n+"\""+": ["+str(pose_detached[i*3])+", "+str(pose_detached[i*3+1])+", "+str(pose_detached[i*3+2])+"]"
        if i<len(JOINT_NAMES)-1:
            smplx_json += ","
        #print("\""+n+"\""+": ["+str(pose_detached[i*3])+", "+str(pose_detached[i*3+1])+", "+str(pose_detached[i*3+2])+"],")
    smplx_json += "} " 
    
    smplx_json += "} "

    print(smplx_json)
    json_file = open(filename, 'w')
    j = json.loads(smplx_json)
    json.dump(j, json_file, indent=1)
    json_file.close()



def processPose(global_orient, joints, camera_pose, cam_trans, h, w):
	#print("processPose...")
	#print("\t received num joints:", joints.shape)
	#print("global_orient:", global_orient)
	#print("joints:", joints)
	#print("camera_pose:", camera_pose)
	#print("cam_trans:", cam_trans)
	
	#Code from flashback_smplifyx:
	focal_length=5000.
	camera_center = np.array([w, h]) * 0.5
	cam_trans[0] *= -1.0
	camera_pose = np.eye(4)
	camera_pose[:3, 3] = cam_trans
	exportPose(joints, global_orient, camera_center, camera_pose, filename="output.json")

settings = romp.main.default_settings 
romp_model = romp.ROMP(settings)
#romp_model.settings.calc_smpl = True
im = cv2.imread('demo_images/test.jpg')
h, w, c = im.shape
print("Processing image...")
outputs = romp_model(im) # please note that we take the input image in BGR format (cv2.imread).
#Alternative: read from file
#outputs = np.load("output/test.npz", allow_pickle=True)['results'][()]

n = outputs['joints'].shape[0] #num characters
print("Number of characters: ", outputs['joints'].shape[0])

#poses, trans = np.zeros((n, 72)), np.zeros((n, 3))
#for i in range(0, n):
#	poses[i] = outputs[i]['smpl_thetas']
#	trans[i] = outputs[i]['cam_trans']

print("Keys in outputs: ")
for keys, value in outputs.items():
   print(keys)

#print("outputs", outputs)
#print("outputs.shape", outputs.shape)
#print("outputs['global_orient']", outputs['global_orient'])
#print("outputs['cam']", outputs['cam'])
#print("outputs['pose']", outputs['pose'])
#print("outputs['joints']", outputs['joints'])
#print("outputs['cam_trans']", outputs['cam_trans'])

print("outputs['pose'][0].shape = ", outputs['joints'][0].shape)

print("outputs['joints'][0].shape = ", outputs['joints'][0].shape)
#"We generate 2D/3D position of 71 joints from estimated 3D body meshes."
#"The 71 joints are 24 SMPL joints + 30 extra joints + 17 h36m joints:""




i = 0
joints_sliced = outputs['joints'][i][0:24]
joints_sliced_flatten = joints_sliced.flatten()
print("joints_sliced_flatten.shape", joints_sliced_flatten.shape)
print("joints_sliced_flatten = ", joints_sliced_flatten)
processPose(outputs['global_orient'][i], joints_sliced_flatten, outputs['cam'][i], outputs['cam_trans'][i], h, w)



#if self.settings.calc_smpl:
# 	outputs = self.smpl_parser(outputs, root_align=self.settings.root_align) 
#	outputs.update(body_mesh_projection2image(outputs['joints'], outputs['cam'], vertices=outputs['verts'], input2org_offsets=image_pad_info))
# outputs['cam_trans'] = convert_cam_to_3d_trans(outputs['cam'])


#In this tool it imports the generated npz into a Blender character
#checking https://github.com/Arthur151/ROMP/blob/master/simple_romp/tools/convert2fbx.py
#check also: https://github.com/Arthur151/ROMP/blob/master/simple_romp/romp/main.py

#frame_results = np.load(input_path, allow_pickle=True)['results'][()]
#sequence_results = np.load(input_path, allow_pickle=True)['sequence_results'][()] 
#poses, trans = np.zeros((len(frame_names), 72)), np.zeros((len(frame_names), 3))
#pose = poses[source_index]
#mat_rots = [Rodrigues(rod_rot) for rod_rot in rod_rots]



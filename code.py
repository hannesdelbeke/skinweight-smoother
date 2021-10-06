import maya.api.OpenMaya as om
import maya.api.OpenMayaAnim as omanim
import maya.api.OpenMayaRender as omrender
import pymel.core as pm


def get_data():
    frames = []

    # run this on every frame (optimise run every x frames)
    for f in frames:
        # bones
        get_bone_transforms()

        # skinning
        get_skin_data()

    # save this data to disk


def get_bone_transforms_bind_pose():
    # lets naively assume frame 0 is the default pose for now

    # todo go to frame 0

    get_bone_transforms()


def get_bone_transforms():
    # default values pos 0 rot 0 scale 1

    # if we get global data we dont need to recalc data based on parents
    # global rotate, scale, pos
    joints = pm.ls(type='joint')

    # bone   pos (x y z) rot (x y z) scale (x y z)
    # bone1
    # bone2
    # ...

    # prune unused later?
    pass


def get_skin_data():
    # get skin data for every vert.
    # influence per vert for every bone
    # vert bone1 bone2 bone3 ...
    # vtx1  0.5   0.1    0   ...
    # vtx2  0     0.9    0.1 ...
    # ...

    # save this to disk
    pass

# pass to scikit for grad descent setup

# for every vert calc separately
# vtx 1 bone1 0.5*pos_function, bone2 0.1*pos_function, ...
# after running pos function we get a new numpy array, with pos of verts.
# multiply these pos with the skinweights. and average them.
# compare with actual pos and calc the error

# now for the optimisation part. only use 2 bones and calc deformation.
# try variation all 4 bones with each other, lowest deformation wins!
# bone 12 13 14 23 24 34


def pos_function(vertex_pos, joint_pos, joint_rot, joint_scale, joint_pos_bind, joint_rot_bind, joint_scale_bind):
    # input bindpose position vert, bind transforms bone, transforms bone current frame
    # magic function here using matrix

    # original pos
    # difference in joint and joint bind
    # joint_pos - joint_pos_bind: float, int?
    # joint_rot - joint_rot_bind: float, order of rotation! euler or quaternion
    # joint_scl - joint_scl_bind: float, default 1

    # if we are in position 2 in bind, and 5 on a frame, we moved 3
    # 5 - 2 = 3 (pos - bind_pos = pos_offset)
    # new_vert_pos = vert_pos + 3

    # rotation 10 in bind, rotation 90 on a frame
    # rot - bind_rot = 80 (rot_offset)
    # new_vert_rot = vert_rot + rot_offset
    # we prob have to rotate using matrix since we need to offset the position with rotation

    # scale 1 in bind, scale 1.3 on a frame
    # 1.3 / 1 = 1.3
    # scale position matrix, 1.3 size
    # 1.3 x 5 = 6.5 new_pos_scale_applied

    # return new_pos x y z

    pass

# import maya.api.OpenMaya as om
# import maya.api.OpenMayaAnim as omanim
# import maya.api.OpenMayaRender as omrender
import pymel.core as pm
import skin

def get_data(animated_mesh_node=None, frame_count=40):

    # hardcode hack to save time testing
    nodes = pm.ls('GEO')
    print(nodes)
    animated_mesh_node = pm.listRelatives(nodes[0], type='transform')[0]
    print(animated_mesh_node)

    name = str(animated_mesh_node.name())
    skincluster_name = skin.findRelatedSkinCluster(name)
    skincluster = pm.ls(skincluster_name, type='skinCluster')[0]
    print(skincluster)
    # skincluster(animated_mesh_node)

    # skinning
    skin_weights = get_skin_data(animated_mesh_node, skincluster)

    transform_data = None
    # run this on every frame (optimise run every x frames)
    for frame in range(frame_count):

        # move frame
        pm.currentTime(frame)

        # lets assume all joints for now. later get joints from skin data

        # joints
        transform_data = get_joint_transforms(animated_mesh_node)



    # save this data to disk

    print(transform_data)


def get_joint_transforms_bind_pose():
    # lets naively assume frame 0 is the default pose for now

    # todo go to frame 0

    get_joint_transforms()


def get_joint_transforms(mesh_node):
    # default values pos 0 rot 0 scale 1

    # if we get global data we dont need to recalc data based on parents
    # global rotate, scale, pos
    joints = pm.ls(type='joint')

    joint_pos = {x.nodeName() : (x.getTranslation(), x.getOrientation(), x.getScale()) for x in joints}  # uses nodename so bug if same name
    return joint_pos
    # joint   pos (x y z) rot (x y z) scale (x y z)
    # joint1
    # joint2
    # ...

    # prune unused later?
    pass

# # todo openmaya skincluster get https://forums.autodesk.com/t5/maya-programming/can-t-find-skincluster-attached-to-mesh-object/td-p/6681259
# def get_skin_cluster_from_mesh(mesh_node):
#     # get skin cluster
#
#     # jnt = pm.ls(sl=True)[0]
#     skinCluster = None
#     for node in mesh_node.connections():
#         if node.nodeType() == pm.nt.skinCluster:
#             skinCluster = node
#             break
#     if skinCluster:
#         print(skinCluster)
#
#     # # see https://discourse.techart.online/t/maya-python-findrelatedskincluster/2673/3
#     # import cmds
#     # cluster_name = cmds.mel.eval('findRelatedSkinCluster ' + animated_mesh_node.name())
#     # #pm.findRelatedSkinCluster(animated_mesh_node)



def get_skin_data(animated_mesh_node, skincluster):
    # info on openmaya skincluster code https://www.artstation.com/blogs/benmorgan/72rD/maya-python-api-gettingsetting-skin-weights
    skincluster_MObject = skin.getSkinCluster(skincluster.name()) # skincluster name to openmaya skincluster object
    mesh_dag = skin.pynode_to_dag(animated_mesh_node)
    joints, weights = skin.get_skin_weights(mesh_dag, skincluster_MObject)


    # get skin data for every vert.
    # influence per vert for every joint
    # vert joint1 joint2 joint3 ...
    # vtx1  0.5   0.1    0   ...
    # vtx2  0     0.9    0.1 ...
    # ...

    # save this to disk
    pass

# pass to scikit for grad descent setup

# for every vert calc separately
# vtx 1 joint1 0.5*pos_function, joint2 0.1*pos_function, ...
# after running pos function we get a new numpy array, with pos of verts.
# multiply these pos with the skinweights. and average them.
# compare with actual pos and calc the error

# now for the optimisation part. only use 2 joints and calc deformation.
# try variation all 4 joints with each other, lowest deformation wins!
# joint 12 13 14 23 24 34


def pos_function(vertex_pos, joint_pos, joint_rot, joint_scale, joint_pos_bind, joint_rot_bind, joint_scale_bind):
    # input bindpose position vert, bind transforms joint, transforms joint current frame
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









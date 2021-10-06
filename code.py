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

    pass


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
    pass

# pass to scikit for grad descent setup
# for every vert calc separately
# vtx 1 bone1 0.5*pos_function, bone2 0.1*pos_function, ...

def pos_function(pos, rot, scale):
    # magic function here using matrix
    pass
import maya.api.OpenMaya as om
import maya.api.OpenMayaAnim as omanim
import maya.api.OpenMayaRender as omrender


def get_data():

    frames = []

    # run this on every frame
    for f in frames:
        # bones
        get_bone_transforms()

        # skinning
        get_skin_data()

    pass


def get_bone_transforms():
    # default values pos 0 rot 0 scale 1

    # if we get global data we dont need to recalc data based on parents
    #global rotate, scale, pos

    # prune unused later?
    pass


def get_skin_data():
    # get skin data for every vert.
    pass

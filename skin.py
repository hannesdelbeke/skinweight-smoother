#https://www.artstation.com/blogs/benmorgan/72rD/maya-python-api-gettingsetting-skin-weights

import maya.api.OpenMaya as om
import maya.api.OpenMayaAnim as omanim
import maya.api.OpenMayaRender as omrender
#import cmds

print('import code')

def getSkinCluster(self, dag):
    """A convenience function for finding the skinCluster deforming a mesh.

    params:
      dag (MDagPath): A MDagPath for the mesh we want to investigate.
    """

    # useful one-liner for finding a skinCluster on a mesh
    skin_cluster = cmds.ls(cmds.listHistory(dag.fullPathName()), type="skinCluster")

    if len(skin_cluster) > 0:
      # get the MObject for that skinCluster node if there is one
      sel = om.MSelectionList()
      sel.add(skin_cluster[0])
      skin_cluster_obj = om.MObject()
      sel.getDependNode(0, skin_cluster_obj)

      return skin_cluster[0], skin_cluster_obj

    else:
      raise RuntimeError("Selected mesh has no skinCluster")


# ============================
def SOMEAWESOMEFUNCTION():
    return 1


# ============================
def select_verts():

    # original_sel = om.MSelectionList()
    # om.MGlobal.getActiveSelectionList(original_sel)

    # ============================
    cmds.select(cmds.polyListComponentConversion(toVertex=True))


    # get the selected mesh and components
    sel = om.MSelectionList()
    om.MGlobal.getActiveSelectionList(sel)


    if not sel.length():
        return


    selected_components = om.MObject()
    dag = om.MDagPath()
    sel.getDagPath(0, dag, selected_components)


    dag.extendToShape()


    if dag.apiType() != 296:
        om.MGlobal.displayError("Selection must be a polygon mesh.")
        return

    # ============================
    skin_cluster, skin_cluster_obj = getSkinCluster(dag)
    # ============================

    # doing this can speed up iteration and also allows you to undo all of this
    cmds.skinPercent(skin_cluster, pruneWeights=0.005)

    mFnSkinCluster = omanim.MFnSkinCluster(skin_cluster_obj)

    influence_objects = om.MDagPathArray()
    # returns a list of the DagPaths of the joints affecting the mesh
    mFnSkinCluster.influenceObjects(influence_objects)
    influence_count_util = om.MScriptUtil(influence_objects.length())

    # c++ utility needed for the get/set weights functions
    influence_count_ptr = influence_count_util.asUintPtr()
    influence_count = influence_count_util.asInt()
    influence_indices = om.MIntArray()

    # create an MIntArray that just counts from 0 to inf_count
    for i in range(0, influence_count):
      influence_indices.append(i)

    old_weights = om.MDoubleArray()
    # don't use the selected_components MObject we made since we want to get the weights for each vertex
    # on this mesh, not just the selected one
    empty_object = om.MObject()
    mFnSkinCluster.getWeights(dag, empty_object, old_weights, influence_count_ptr)

    # new_weights just starts as a copy of old_weights
    new_weights = om.MDoubleArray(old_weights)

    # ============================

    # iterate over the selected verts
    itVerts = om.MItMeshVertex(dag, selected_components)

    while not itVerts.isDone():
        this_vert_weight_index = itVerts.index() * inf_count
        vert_weights = list(new_weights[this_vert_weight_index: this_vert_weight_index + inf_count])

        # makes the weights for the closest vertex equal to the outer vertex
        new_weights[this_vert_weight_index: this_vert_weight_index + inf_count] = SOMEAWESOMEFUNCTION()

        itVerts.next()

    # set weights all at once
    mFnSkinCluster.setWeights(dag, empty_object, influence_indices, new_weights, True, old_weights)

    # om.MGlobal.setActiveSelectionList(original_sel)

# select_verts()


# copy from gltools https://github.com/bungnoid/glTools/blob/master/utils/skinCluster.py
import maya.cmds as mc
import maya.mel as mm
def findRelatedSkinCluster(geometry):
    '''
    Return the skinCluster attached to the specified geometry
    @param geometry: Geometry object/transform to query
    @type geometry: str
    '''
    # Check geometry
    if not mc.objExists(geometry):
        raise Exception('Object ' + geometry + ' does not exist!')
    # Check transform
    if mc.objectType(geometry) == 'transform':
        try:
            geometry = mc.listRelatives(geometry, s=True, ni=True, pa=True)[0]
        except:
            raise Exception('Object ' + geometry + ' has no deformable geometry!')

    # Determine skinCluster
    skin = mm.eval('findRelatedSkinCluster "' + geometry + '"')
    if not skin:
        skin = mc.ls(mc.listHistory(geometry), type='skinCluster')
        if skin: skin = skin[0]
    if not skin: skin = ''

    # Return result
    return skin
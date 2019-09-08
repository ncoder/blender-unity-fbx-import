import bpy
import os
import glob


class BulkImport_Operator(bpy.types.Operator):
    bl_idname = "view3d.bulk_import"
    bl_label = "Bulk Import from folder"
    bl_description = "Import all FBX files in a folder"

    def execute(self, context):
        # scripts current path
        #dirpath = os.path.dirname(os.path.abspath(__file__))
        dirpath = "/Users/ncoder/Hero/Assets/PolygonCity/Models/"

        f = ""
        for f in glob.glob(dirpath + "*.fbx"):
            print(f)

            # default scale of 100 applied to unity fbx import. Unity assumes that
            # the model was created with maya with units in CM. converts to meters.
            bpy.ops.import_scene.fbx(filepath=f, global_scale=100)

        return {'FINISHED'}

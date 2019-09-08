# dedupe materials, assuming that .xxx numercial suffix is a dupe of the one without it

import bpy


class DedupeMat_Operator(bpy.types.Operator):
    bl_idname = "view3d.dedupe_mat"
    bl_label = "Dedupe all materials by name"
    bl_description = "uses the material prefix and assumes it is the same"

    def execute(self, context):
        mats = bpy.data.materials

        for obj in bpy.data.objects:
            for slt in obj.material_slots:
                part = slt.name.rpartition('.')
                if part[2].isnumeric() and part[0] in mats:
                    slt.material = mats.get(part[0])

        return {'FINISHED'}

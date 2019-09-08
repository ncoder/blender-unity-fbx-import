import bpy


class WK_PT_Panel(bpy.types.Panel):
    bl_idname = "WK_PT_Panel"
    bl_label = "WK"
    bl_category = "Generic"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator('view3d.bulk_import')
        row = layout.row()
        row.operator('view3d.dedupe_mat')
        row = layout.row()
        row.operator('view3d.layout_objects')

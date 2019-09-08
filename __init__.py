from . panel import WK_PT_Panel
from . layout import Layout_Operator
from . dedupemat import DedupeMat_Operator
from . bulkimport import BulkImport_Operator
import bpy


bl_info = {
    "name": "Web import export tools",
    "category": "Generic",
    "location": "View3D",
    "blender": (2, 80, 0)
}


classes = (
    WK_PT_Panel,
    Layout_Operator,
    DedupeMat_Operator,
    BulkImport_Operator
)
register, unregister = bpy.utils.register_classes_factory(classes)

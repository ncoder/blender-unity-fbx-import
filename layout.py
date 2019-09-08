import bpy
import math


class Layout_Operator(bpy.types.Operator):
    bl_idname = "view3d.layout_objects"
    bl_label = "Layout objects"
    bl_description = "Layout all object in the scene on a X,Y grid"

    def execute(self, context):
        # use root objects
        objects = list(filter(lambda x: x.parent ==
                              None, bpy.context.scene.objects))

        count = len(objects)
        side = round(math.sqrt(count))

        stride = 20
        xstart = -side*stride/2
        ystart = -side*stride/2
        i = 0

        for o in objects:

            x = xstart + round(i % side) * stride
            y = ystart + round(i / side) * stride

            print(o.name + " at " + str(x) + " " + str(y))
            o.location.x = x
            o.location.y = y

            i += 1

        return {'FINISHED'}

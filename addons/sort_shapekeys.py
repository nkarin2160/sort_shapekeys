bl_info = {
    "name": "Sort Shapekeys",
    "author": "gogo",
    "version": (0, 0, 1),
    "blender": (2, 83, 0),
    "description": "Sort shapekeys",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "https://github.com/3str6/sort_shapekeys",
    "category": "3D View"
}


import bpy
from bpy.types import (
    Panel,
)
from bpy.props import (
    PointerProperty,
)

sort_list = [
    "Basis",    # 一番上は必ずBasisにすること
    "browInnerUp",
    "browDown_L",
    "browDown_R",
    "browOuterUp_L",
    "browOuterUp_R",
    "eyeLookUp_L",
    "eyeLookUp_R",
    "eyeLookDown_L",
    "eyeLookDown_R",
    "eyeLookIn_L",
    "eyeLookIn_R",
    "eyeLookOut_L",
    "eyeLookOut_R",
    "eyeBlink_L",
    "eyeBlink_R",
    "eyeSquint_L",
    "eyeSquint_R",
    "eyeWide_L",
    "eyeWide_R",
    "cheekPuff",
    "cheekSquint_L",
    "cheekSquint_R",
    "noseSneer_L",
    "noseSneer_R",
    "jawOpen",
    "jawForward",
    "jawLeft",
    "jawRight",
    "mouthFunnel",
    "mouthPucker",
    "mouthLeft",
    "mouthRight",
    "mouthRollUpper",
    "mouthRollLower",
    "mouthShrugUpper",
    "mouthShrugLower",
    "mouthClose",
    "mouthSmile_L",
    "mouthSmile_R",
    "mouthFrown_L",
    "mouthFrown_R",
    "mouthDimple_L",
    "mouthDimple_R",
    "mouthUpperUp_L",
    "mouthUpperUp_R",
    "mouthLowerDown_L",
    "mouthLowerDown_R",
    "mouthPress_L",
    "mouthPress_R",
    "mouthStretch_L",
    "mouthStretch_R",
    "tongueOut",
]


def check_list(target_object):
    missing_list = []
    for shapekey_name in sort_list:
        target_index = target_object.data.shape_keys.key_blocks.find(shapekey_name)
        if target_index == -1:
            missing_list.append(shapekey_name)
    
    return missing_list


def move_to_index(target_index, source_index):
    diff = target_index - source_index
    diff_abs = abs(diff)
    if diff < 0:
        for i in range(diff_abs):
            bpy.ops.object.shape_key_move(type='DOWN')
    elif diff > 0:
        for i in range(diff_abs):
            bpy.ops.object.shape_key_move(type='UP')
    else:
        None


class SRTSPK_OT_check(bpy.types.Operator):
    bl_idname = "srtspk.check"
    bl_label = "Sort"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "Check list"

    @classmethod
    def poll(cls, context):
        return context.object and context.object.data.shape_keys

    def execute(self, context):
        target_object = context.object
        missing_list = check_list(target_object)
        self.report({'WARNING'}, "Missing: " + str(missing_list))

        return {'FINISHED'}


class SRTSPK_OT_create_missings(bpy.types.Operator):
    bl_idname = "srtspk.create_missings"
    bl_label = "Create Missings"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "Create missing shapekeys"

    @classmethod
    def poll(cls, context):
        return context.object and context.object.data.shape_keys

    def execute(self, context):
        target_object = context.object
        missing_list = check_list(target_object)
        
        for shapekey_name in missing_list:
            target_object.shape_key_add(name=shapekey_name, from_mix=False)
            
        return {'FINISHED'}


class SRTSPK_OT_sort(bpy.types.Operator):
    bl_idname = "srtspk.sort"
    bl_label = "Sort"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "Sort shapekeys"

    @classmethod
    def poll(cls, context):
        return context.object and context.object.data.shape_keys

    def execute(self, context):
        # props = context.scene.srtspk
        target_object = context.object
        missing_list = check_list(target_object)
        if missing_list:
            self.report({'WARNING'}, "Missing: " + str(missing_list))
            return {'CANCELLED'}

        for source_index, shapekey_name in enumerate(sort_list):
            target_index = target_object.data.shape_keys.key_blocks.find(shapekey_name)
            target_object.active_shape_key_index = target_index
            move_to_index(target_index, source_index)
            
        return {'FINISHED'}


class SRTSPK_PT_main(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "For VRoid"
    bl_label = "Sort Shapekeys"
    bl_idname = "SRTSPK_PT_main"
    bl_context = 'objectmode'
    
    def draw(self, context):
        layout = self.layout
        layout.operator(SRTSPK_OT_check.bl_idname, text="Check")
        layout.operator(SRTSPK_OT_create_missings.bl_idname, text="Create Missings")
        layout.operator(SRTSPK_OT_sort.bl_idname, text="Sort")


classes = (
    SRTSPK_OT_sort,
    SRTSPK_OT_check,
    SRTSPK_OT_create_missings,
    SRTSPK_PT_main,
)


def register():
    for i in classes:
        bpy.utils.register_class(i)


def unregister():
    for i in classes:
        bpy.utils.unregister_class(i)


if __name__ == "__main__":
    register()
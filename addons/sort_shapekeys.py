bl_info = {
    "name": "Sort Shapekeys",
    "Original author": "gogo",
    "Edited by": "nkarin",    
    "version": (1, 0, 1),
    "blender": (2, 83, 0),
    "description": "Sort shapekeys",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "https://github.com/3str6/sort_shapekeys",
    "category": "3D View"
}


import bpy
from bpy.props import (
    PointerProperty,
    EnumProperty,
)

sort_LiveLink = [
    "ベース",    # 一番上は必ずBasisにすること
    "eyeBlinkLeft",
    "eyeLookDownLeft",
    "eyeLookInLeft",
    "eyeLookOutLeft",
    "eyeLookUpLeft",
    "eyeSquintLeft",
    "eyeWideLeft",
    "eyeBlinkRight",
    "eyeLookDownRight",
    "eyeLookInRight",
    "eyeLookOutRight",
    "eyeLookUpRight",
    "eyeSquintRight",
    "eyeWideRight",
    "jawForward",
    "jawLeft",
    "jawRight",
    "jawOpen",
    "mouthClose",
    "mouthFunnel",
    "mouthPucker",
    "mouthLeft",
    "mouthRight",
    "mouthSmileLeft",
    "mouthSmileRight",
    "mouthFrownLeft",
    "mouthFrownRight",
    "mouthDimpleLeft",
    "mouthDimpleRight",
    "mouthStretchLeft",
    "mouthStretchRight",
    "mouthRollLower",
    "mouthRollUpper",
    "mouthShrugLower",
    "mouthShrugUpper",
    "mouthPressLeft",
    "mouthPressRight",
    "mouthLowerDownLeft",
    "mouthLowerDownRight",
    "mouthUpperUpLeft",
    "mouthUpperUpRight",
    "browDownLeft",
    "browDownRight",
    "browInnerUp",
    "browOuterUpLeft",
    "browOuterUpRight",
    "cheekPuff",
    "cheekSquintLeft",
    "cheekSquintRight",
    "noseSneerLeft",
    "noseSneerRight",
    "tongueOut",
    "headYaw",
    "headPitch",
    "headRoll",
    "leftEyeYaw",
    "leftEyePitch",
    "leftEyeRoll",
    "rightEyeYaw",
    "rightEyePitch",
    "rightEyeRoll",
]

sort_iFacialMocap = [
    "ベース",    # 一番上は必ずBasisにすること
    "browInnerUp",
    "browDownLeft",
    "browDownRight",
    "browOuterUpLeft",
    "browOuterUpRight",
    "eyeLookUpLeft",
    "eyeLookUpRight",
    "eyeLookDownLeft",
    "eyeLookDownRight",
    "eyeLookInLeft",
    "eyeLookInRight",
    "eyeLookOutLeft",
    "eyeLookOutRight",
    "eyeBlinkLeft",
    "eyeBlinkRight",
    "eyeSquintLeft",
    "eyeSquintRight",
    "eyeWideLeft",
    "eyeWideRight",
    "cheekPuff",
    "cheekSquintLeft",
    "cheekSquintRight",
    "noseSneerLeft",
    "noseSneerRight",
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
    "mouthSmileLeft",
    "mouthSmileRight",
    "mouthFrownLeft",
    "mouthFrownRight",
    "mouthDimpleLeft",
    "mouthDimpleRight",
    "mouthUpperUpLeft",
    "mouthUpperUpRight",
    "mouthLowerDownLeft",
    "mouthLowerDownRight",
    "mouthPressLeft",
    "mouthPressRight",
    "mouthStretchLeft",
    "mouthStretchRight",
    "tongueOut",
]

def check_list(target_object, sort_list):
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
        props = context.scene.srtspk
        target_object = context.object
        if props.sort_type == "LiveLink":
            sort_list = sort_LiveLink
        else:
            sort_list = sort_iFacialMocap

        missing_list = check_list(target_object, sort_list)
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
        props = context.scene.srtspk
        target_object = context.object
        if props.sort_type == "LiveLink":
            sort_list = sort_LiveLink
        else:
            sort_list = sort_iFacialMocap

        missing_list = check_list(target_object, sort_list)
        
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
        props = context.scene.srtspk
        target_object = context.object
        if props.sort_type == "LiveLink":
            sort_list = sort_LiveLink
        else:
            sort_list = sort_iFacialMocap
        
        missing_list = check_list(target_object, sort_list)
        if missing_list:
            self.report({'WARNING'}, "Missing: " + str(missing_list))
            return {'CANCELLED'}

        for source_index, shapekey_name in enumerate(sort_list):
            target_index = target_object.data.shape_keys.key_blocks.find(shapekey_name)
            target_object.active_shape_key_index = target_index
            move_to_index(target_index, source_index)
        
        target_object.active_shape_key_index = 0
            
        return {'FINISHED'}


class SRTSPK_PT_main(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "For VRoid"
    bl_label = "Sort Shapekeys"
    bl_idname = "SRTSPK_PT_main"
    bl_context = 'objectmode'
    
    def draw(self, context):
        props = context.scene.srtspk
        layout = self.layout
        layout.prop(props, property="sort_type", text="Type")
        layout.operator(SRTSPK_OT_check.bl_idname, text="Check")
        layout.operator(SRTSPK_OT_create_missings.bl_idname, text="Create Missings")
        layout.operator(SRTSPK_OT_sort.bl_idname, text="Sort")


class SRTSPK_props(bpy.types.PropertyGroup):
    sort_type_input = (
        ("LiveLink", "LiveLink", ""),      # (識別子, UI表示名, 説明文)
        ("iFacialMocap", "iFacialMocap", ""),
    )
    sort_type: EnumProperty(
        name="Sort Type",
        description="Sort Type",
        items=sort_type_input,
    )


classes = (
    SRTSPK_OT_sort,
    SRTSPK_OT_check,
    SRTSPK_OT_create_missings,
    SRTSPK_PT_main,
    SRTSPK_props,
)


def register():
    for i in classes:
        bpy.utils.register_class(i)

    bpy.types.Scene.srtspk = PointerProperty(type=SRTSPK_props)


def unregister():
    del bpy.types.Scene.srtspk
    for i in classes:
        bpy.utils.unregister_class(i)


if __name__ == "__main__":
    register()

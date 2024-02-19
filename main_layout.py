bl_info = {
    "name": "Implant",
    "description": "Test addon",
    "version": (0, 2),
    "blender": (2, 93, 0),
    "category": "Metalmed",
}

import bpy


class OBJECT_OT_grid_fill(bpy.types.Operator):
    """Applies grid fill to the active object with specified span"""
    bl_idname = "object.grid_fill"
    bl_label = "Grid Fill"

    span: bpy.props.IntProperty(
        name="Span",
        description="Number of grid cells",
        default=8,
        min=1,
        max=50,
    )

    def execute(self, context):
        active_object = context.active_object

        if active_object and active_object.type == 'MESH':
            bpy.ops.object.mode_set(mode='EDIT')  # Ensure Edit Mode
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.fill_grid(span=self.span)  # Perform grid fill
            bpy.ops.object.mode_set(mode='OBJECT')  # Return to Object Mode
        else:
            self.report({'ERROR'}, "No mesh object selected")
        return {'FINISHED'}


class custom_panel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "METALMED"
    bl_label = "Metalmed"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("mesh.primitive_cube_add", text="Add Cube")
        row = layout.row()
        row.operator("mesh.primitive_ico_sphere_add", text="Add Ico Sphere")
        row = layout.row()
        row.operator("object.shade_smooth", text="Shade Smooth")
        row = layout.row()
        row.operator("object.grid_fill", text="Grid Fill")

        # Add column for span value
 
        col = row.column()
        col.label("Span:")  # Add a label for clarity
        col.prop(self, "span")  # Use `layout.column()` for better alignment


def register():
    bpy.utils.register_class(OBJECT_OT_grid_fill)
    bpy.utils.register_class(custom_panel)


def unregister():
    bpy.utils.unregister_class(custom_panel)
    bpy.utils.unregister_class(OBJECT_OT_grid_fill)


if __name__ == "__main__":
    register()

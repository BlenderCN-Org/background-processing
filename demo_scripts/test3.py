import bpy
import bmesh
import time

# NOTE: If 'use_blend_file' property enabled in 'add_job' call, reference blend data from source file directly.
# NOTE: Else, pull objects and meshes from source file using 'appendFrom(data_type:str, data_name:str)'.
appendFrom("Object", objName)
source_ob = bpy.data.objects.get(objName)

meta_data = bpy.data.metaballs.new('Volume Data')
meta_obj = bpy.data.objects.new('Volume Object', meta_data)

for v in source_ob.data.vertices:
    mb = meta_data.elements.new(type='BALL')
    mb.radius = 1.5
    mb.co = v.co

scn = bpy.context.scene
scn.objects.link(meta_obj)
scn.update()

out_me = meta_obj.to_mesh(scn, apply_modifiers=True, settings='PREVIEW')
out_ob = bpy.data.objects.new('Volume Mesh Object', out_me)
scn.objects.link(out_ob)

bpy.data.objects.remove(meta_obj, do_unlink=True)
bpy.data.metaballs.remove(meta_data)

# set 'data_blocks' equal to list of object data to be sent back to the Blender host
data_blocks = [out_ob]

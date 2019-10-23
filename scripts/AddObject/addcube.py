# --------------------------------------------------------
# Note:                                                                                                                                                   
#     - This is the Python code used in Script Manager.                                                                                                                                                 
# Compatible:                                                                                                                                         
#     - Win / Mac                                                                                                                                 
#     - R17, R18, R19, R20, R21                                                                                                                                
# --------------------------------------------------------


import c4d

# Main function
def main():
    cube = c4d.BaseObject(c4d.Ocube)
    cube.SetRelPos(c4d.Vector(0))
    cube[c4d.PRIM_CUBE_LEN,c4d.VECTOR_X] = 100
    cube[c4d.PRIM_CUBE_LEN,c4d.VECTOR_Y] = 100
    cube[c4d.PRIM_CUBE_LEN,c4d.VECTOR_Z] = 100
    cube[c4d.PRIM_CUBE_SUBX] = 3
    cube[c4d.PRIM_CUBE_SUBY] = 3
    cube[c4d.PRIM_CUBE_SUBZ] = 3
    doc.InsertObject(cube)
    doc.SetActiveObject(cube)
    c4d.CallCommand(12236) # Make Editable
    c4d.CallCommand(17105) # Gouraud Shading (Lines)


# Execute main()
if __name__=='__main__':
    main()

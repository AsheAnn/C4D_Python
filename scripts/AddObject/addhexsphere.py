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
    sph = c4d.BaseObject(c4d.Osphere)
    sph.SetRelPos(c4d.Vector(0))
    sph[c4d.PRIM_SPHERE_RAD] = 100
    sph[c4d.PRIM_SPHERE_SUB] = 96
    sph[c4d.PRIM_SPHERE_TYPE] = 2
    doc.InsertObject(sph)
    doc.SetActiveObject(sph)
    c4d.CallCommand(12236) # Make Editable
    c4d.CallCommand(17105) # Gouraud Shading (Lines)

# Execute main()
if __name__=='__main__':
    main()

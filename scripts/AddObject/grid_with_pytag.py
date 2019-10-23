# --------------------------------------------------------
# Note:                                                                                                                                                   
#     - This is the Python code used in Script Manager.                                                                                                                                                 
# Compatible:                                                                                                                                         
#     - Win / Mac                                                                                                                                 
#     - R21                                                                                                                                
# --------------------------------------------------------

import c4d

# Main function
def main():
    grid = c4d.BaseObject(c4d.Oplane) # Create Grid
    grid.SetRelPos(c4d.Vector(0)) # Set position
    grid[c4d.PRIM_PLANE_WIDTH] = 100
    grid[c4d.PRIM_PLANE_HEIGHT] = 100
    grid[c4d.PRIM_PLANE_SUBW] = 1
    grid[c4d.PRIM_PLANE_SUBH] = 1
    grid[c4d.PRIM_AXIS] = 2
    doc.InsertObject(grid) # Insert Grid
    doc.SetActiveObject(grid) # Select Grid
    c4d.CallCommand(12236) # Make Editable
    c4d.CallCommand(100004788, 50058) # New Python Tag


# Execute main()
if __name__=='__main__':
    main()

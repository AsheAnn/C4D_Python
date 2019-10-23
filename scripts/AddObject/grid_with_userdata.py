# --------------------------------------------------------
# Note:                                                                                                                                                   
#     - This is the Python code used in Script Manager.                                                                                                                                                 
# Compatible:                                                                                                                                         
#     - Win / Mac                                                                                                                                 
#     - R17, R18, R19, R20, R21                                                                                                                                
# --------------------------------------------------------


import c4d
from c4d import gui

# Add userdata group
def AddUserDataGroup(obj, name):
    gc = c4d.GetCustomDataTypeDefault(c4d.DTYPE_GROUP)
    gc[c4d.DESC_NAME] = name
    gc[c4d.DESC_PARENTGROUP] = c4d.DescID(0)
    obj.SetUserDataContainer([c4d.ID_USERDATA, 1], gc)

# Add userdata
def AddUserData(obj, name, id, Dtye, step, min, max):
    bc = c4d.GetCustomDataTypeDefault(Dtye) # Create default container
    bc[c4d.DESC_NAME] = name  # Rename the entry
    bc[c4d.DESC_MIN] = min  # Set min value
    bc[c4d.DESC_MAX] = max  # Set max value
    bc[c4d.DESC_STEP] = step # Set step value
    bc[c4d.DESC_CUSTOMGUI] = 1000489 # Set float slider
    bc[c4d.DESC_MINSLIDER] = min # Set min value slider
    bc[c4d.DESC_MAXSLIDER] = max # Set man value slider

    parentGroup = c4d.DescID(c4d.DescLevel(c4d.ID_USERDATA), c4d.DescLevel(1, c4d.DTYPE_GROUP, 0)) # 1 is my secondary Group ID
    bc.SetData(c4d.DESC_PARENTGROUP, parentGroup)

    obj.SetUserDataContainer([c4d.ID_USERDATA, id], bc) # Add userdata container


# Main function
def main():
    grid = c4d.BaseObject(c4d.Oplane)
    grid.SetRelPos(c4d.Vector(0))
    grid[c4d.PRIM_PLANE_WIDTH] = 100
    grid[c4d.PRIM_PLANE_HEIGHT] = 100
    grid[c4d.PRIM_PLANE_SUBW] = 1
    grid[c4d.PRIM_PLANE_SUBH] = 1
    grid[c4d.PRIM_AXIS] = 2
    doc.InsertObject(grid)
    doc.SetActiveObject(grid)
    c4d.CallCommand(12236) # Make Editable
    c4d.CallCommand(100004788, 50058) # New python Tag
    
    doc.SetActiveObject(grid)
    AddUserDataGroup(grid, "Setting")
    AddUserData(grid,"X",2, c4d.DTYPE_REAL, 0.001, 0, 1)
    AddUserData(grid,"Y",3, c4d.DTYPE_REAL, 0.001, 0, 1)
    AddUserData(grid,"Interation",4, c4d.DTYPE_LONG, 1, 0, 10)



# Execute main()
if __name__=='__main__':
    main()

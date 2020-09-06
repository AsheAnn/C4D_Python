# ----------------------------------------------------------------------
# Note:                                                                                                                                                   
#     - This is the Python code used in Script Manager.                                                                                                                                                  ##
# Compatible:                                                                                                                                         
#     - Win / Mac                                                                                                                                 
#     - R19, R20, R21                                                                                                                                
# ----------------------------------------------------------------------


import c4d

# Main 
def main():
    # Large Icons
    c4d.CallCommand(100004708, 100004708) 
    
    # merge object
    fn = "preset://Convertor.lib4d/Convertor"
    c4d.documents.MergeDocument(doc, fn, c4d.SCENEFILTER_OBJECTS)
    c4d.EventAdd()

# Execute main()
if __name__=='__main__':
    main()

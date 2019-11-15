# ----------------------------------------------------------------------
# Note:                                                                                                                                                   
#     - This is the Python code used in Script Manager.                                                                                                                                                  ##
# Compatible:                                                                                                                                         
#     - Win / Mac                                                                                                                                 
#     - R21                                                                                                                                
# ----------------------------------------------------------------------


import c4d

# Main function
def main():
    c4d.CallCommand(100004708, 100004708) # Large Icons
    c4d.CallCommand(100004788, 50058) # New Python Tag


# Execute main()
if __name__=='__main__':
    main()
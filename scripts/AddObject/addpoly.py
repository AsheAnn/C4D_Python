# This is python code used in script manager.
import c4d


# Main function
def main():
    pos_0 = c4d.Vector(-100,0,-100)
    pos_1 = c4d.Vector(-100,0,100)
    pos_2 = c4d.Vector(100,0,100)
    pos_3 = c4d.Vector(100,0,-100)
    pos = [pos_0, pos_1, pos_2, pos_3]
    mypoly = c4d.BaseObject(c4d.Opolygon) # Create an empty polygon object
    mypoly.ResizeObject(4,1) # New number of points, New number of polygons

    for i in range(0, 4):
        mypoly.SetPoint(i, pos[i])

    mypoly.SetPolygon(0, c4d.CPolygon(0, 1, 2, 3)) # The Polygon's index, Polygon's points

    doc.InsertObject(mypoly,None,None)
    mypoly.Message(c4d.MSG_UPDATE)

    c4d.EventAdd()

# Execute main()
if __name__=='__main__':
    main()

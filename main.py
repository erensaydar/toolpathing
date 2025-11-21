import toolpathing_2D
import toolpathing_3D

def main():

    # PLEASE UNCOMMENT THE DESIRED FUNCTION ONLY (THERE ARE 4 OPTIONS)

    #toolpathing_2D.custom_toolpath_2D() #plots 2D custom toolpath
    toolpathing_2D.canned_toolpath_2D(start_x=4, start_y=4, length=4, step=2, turns=4) #plots 2D curved zigzag pattern
    #toolpathing_3D.canned_toolpath_3D(radius=4, turns=5, height=10, x_center=5, y_center=0, z_center=0) #plots the helix in 3D
    #toolpathing_3D.canned_interactive_toolpath() #interactive helix with t value input for parameter equation changing with a slider

if __name__ == "__main__":
    main()
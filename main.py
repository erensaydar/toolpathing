import toolpathing_2D
import toolpathing_3D

def main():
    #toolpathing_2D.custom_toolpath_2D() #plots 2D 
    #toolpathing_3D.canned_toolpath_3D() #plots the helix in 3D
    toolpathing_3D.canned_interactive_toolpath() #interactive helix with t value input for parameter equation changing with a slider

if __name__ == "__main__":
    main()
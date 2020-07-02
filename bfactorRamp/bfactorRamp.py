'''
Info

bfactorRamp_v1.0
Author: Erik Breslmayr; April 2020
    
- bfactorRamp colors the molecule of choise in regard of bfactors provided in the pdb file and adds a color legend starting from the lowest to the highest bfactor. 
- Additionally some styling features are included, for nicer visualization
'''
from pymol import cmd, stored
def bfactorRamp( mol, color1="blue", color2="red", color3="yellow", cartoon="off", cartoon_putty="off", invcolor="grey40", style="off", fancy="off" ):
    '''
DESCRIPTION
    
    Version: bfactorRamp_v1.0
    Author : Erik Breslmayr; April 2020
    
    - bfactorRamp colors the molecule of choise in regard of bfactors provided in the pdb file and adds a color legend starting from the lowest to the highest bfactor. 
    - Additionally some styling features are included, for nicer visualization
    
    Usage: bfactorRamp mol, color1, color2, color3, cartoon=on or off, cartoon_putty=on or off, invcolor=color, style=on or off, fancy=on or off
    
    mol = any object selection (within one single object!)
    color1,2,3 (optional) = three colors, first for lowest, second for middle and third for highest bfactors
    cartoon (optional) = on or off -> enbales cartoon representation
    cartoon_putty (optional) = on or off -> enbales cartoon_putty representation
    invcolor (optional) = add color, which should represent not selected atoms
    style (optional) = styles the cartoon representation in regard of helix oval length and width
    fancy = changes to fancy helices representaton
    
    Defaults:
    - spectrum colors: blue, red, yellow
    - cartoon:         off
    - cartoon_putty:   off
    - invcolor:        grey40 
    - style:           off
    - fancy:           off
    
    Examples: 
    > bfactorRamp objectName -> uses all defaults
    > bfactorRamp objectName, red, green, grey -> changes the colors for the spectrum
    > bfactorRamp objectName, cartoon=on -> turns cartoon representation on
    > bfactorRamp objectName, cartoon=on -> turns cartoon_putty representation on
    > bfactorRamp objectName, invcolor=green -> changes the color of the not selected region to green
    > bfactorRamp objectName, style=on -> changes helices style and not selected region will be transparent
    > bfactorRamp objectName, fancy=on -> changes helices style to fancy and not selected region will be transparent
    '''
    obj=cmd.get_object_list(mol)[0]
    range=cmd.spectrum("b", "%s %s %s"%(color1, color2, color3), mol)
    cmd.select("invSele","!%s" % (mol))
    cmd.color(invcolor, "invSele")
    cmd.ramp_new("ramp", obj, range, color=["%s"%(color1), "%s"%(color2), "%s"%(color3)])
    #reset styles
    cmd.set("cartoon_transparency", 0, "enabled")
    cmd.set("cartoon_oval_length", 1.2, obj)
    cmd.set("cartoon_oval_width", 0.25, obj)
    cmd.set("cartoon_fancy_helices", 0, obj)
    cmd.set("cartoon_highlight_color", -1, obj)
    
    if cartoon=="on":
	cmd.show_as("cartoon", mol)
	cmd.dss(obj, 1)
	cmd.recolor()
    if cartoon_putty=="on":
	cmd.show_as("cartoon", mol)
	cmd.cartoon("putty", mol)
	cmd.recolor()
    if style=="on":
	cmd.set("cartoon_transparency", 0.5, "invSele")
        cmd.set("cartoon_oval_length", 0.8, obj)
        cmd.set("cartoon_oval_width", 0.2, obj)
    if fancy=="on":
        cmd.set("cartoon_transparency", 0.5, "invSele")
        cmd.set("cartoon_highlight_color", invcolor, obj)
        cmd.set("cartoon_fancy_helices", 1, obj)

    #Output for screen
    print "for help type: help bfactorRamp"
    print ""
    print "Minimum bfactor: %s | Maximum bfactor: %s" % (range[0], range[1])
    print ""
    print "Following settings were taken:"
    print "- mol           : %s" % (obj)
    print "- color1,2,3    : %s, %s, %s" % (color1, color2, color3)
    print "- cartoon       : %s" % (cartoon) 
    print "- cartoon_putty : %s" % (cartoon_putty)
    print "- invcolor      : %s" % (invcolor)
    print "- style         : %s" % (style)
    print "- fancy         : %s" % (fancy)
    
    return (color1, color2, color3)

cmd.extend( "bfactorRamp", bfactorRamp )
import glob
names_filenames_sc = lambda: cmd.Shortcut(cmd.get_names() + glob.glob('*'))
cmd.auto_arg[0]['bfactorRamp'] = [names_filenames_sc, 'filename or object name', '']

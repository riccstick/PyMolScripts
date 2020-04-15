# bfactorRamp
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


## Sample Images 
<img src="/samplePics/bfactorRamp2.png" alt="Highlighted bfactors"
	title="whole protein bfactors highlighted" width="400" />
<img src="/samplePics/bfactorRamp1.png" alt="Highlighted region"
	title="loop region highlighted" width="400" />

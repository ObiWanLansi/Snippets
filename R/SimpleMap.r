library(mapdata)
library(maps)
library(RColorBrewer)

###############################################################################

map('world2Hires','Germany', col = "wheat",bg = "white", names = TRUE, fill =TRUE )
map.axes()
grid()
title("Deutschland")

###############################################################################

map( fill = TRUE, col = brewer.pal(9,"Greens"))
map.axes()
title("Erde")

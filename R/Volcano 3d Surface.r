library(rgl)

z <- 5 * volcano
x <- 10 * (1:nrow(z))
y <- 10 * (1:ncol(z))

zlim <- range(z)
zlen <- zlim[2] - zlim[1] + 1

colourlut <- terrain.colors(zlen)
col <- colourlut[ z - zlim[1] + 1 ]

rgl.open()
rgl.surface(x,y,z,color=col,black="lines")

# Dürfen wir natürlich nicht machen da sonst das Fenster wieder geschlossen wird
#rgl.close()

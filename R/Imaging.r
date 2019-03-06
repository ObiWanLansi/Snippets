library(imager)

file <- system.file('extdata/parrots.png',package='imager')
parrots <- load.image(file)
parrots
#width(parrots)
#height(parrots)

#------------------------------------------------------------------------------

# Original Image
plot(parrots)

#------------------------------------------------------------------------------

# Simple grayscale
plot(grayscale(parrots))

#------------------------------------------------------------------------------

#Blurry parrots ...
plot(isoblur(parrots,10))

#------------------------------------------------------------------------------

#Edge detector along x-axis ...
plot(deriche(parrots,2,order=2,axis="x"))

#Chain operations using the pipe operator (from magrittr)
deriche(parrots,2,order=2,axis="x") %>% deriche(2,order=2,axis="y") %>% plot

#------------------------------------------------------------------------------

#Histogramms
imrow(R(parrots),10) %>% plot(main="Red channel along 10th row",type="l")
imcol(R(parrots),10) %>% plot(main="Red channel along 10th line",type="l")

grayscale(parrots) %>% hist(main="Luminance values in parrots picture",breaks = 256)

#------------------------------------------------------------------------------

library(ggplot2)
library(dplyr)

bdf <- as.data.frame(parrots)
bdf <- mutate(bdf,channel=factor(cc,labels=c('R','G','B')))
ggplot(bdf,aes(value,col=channel))+geom_histogram(bins=30)+facet_wrap(~ channel)


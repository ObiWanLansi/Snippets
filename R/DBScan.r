library(dbscan)

#par(bg="#F0F0F0")

data(iris)
iris <- as.matrix(iris[,1:4])


## example data from fpc
set.seed(665544)

n <- 100

x <- cbind(
    x = runif(10, 0, 10) + rnorm(n, sd = 0.2),
    y = runif(10, 0, 10) + rnorm(n, sd = 0.2)
)

plot(x)

#plot(x, col=res$cluster + 1L)

res <- dbscan::dbscan(x, eps = .4, minPts = 2)
points(x, col=res$cluster + 1L)



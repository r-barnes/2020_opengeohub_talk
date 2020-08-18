#!/usr/bin/env Rscript
library(dplyr)
library(ggplot2)

dat = read.csv("temp/building_distances.csv")

dat = dat %>% arrange(dist_to_bus)

p = ggplot(dat, aes(x=x, y=y)) + geom_point(aes(color=dist_to_bus))

ggsave("results/distances_map.png", p)
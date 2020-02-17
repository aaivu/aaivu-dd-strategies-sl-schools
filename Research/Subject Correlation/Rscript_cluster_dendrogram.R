install.packages('psych', repos='http://cran.us.r-project.org')


grade_6 <- read.csv("/home/adeesha/Documents/Research/grade_6_performance.csv")
grade_7 <- read.csv("/home/adeesha/Documents/Research/grade_7_performance.csv")
grade_8 <- read.csv("/home/adeesha/Documents/Research/grade_8_performance.csv")

library(psych)


pdf("grade_6_hclust.pdf")
plot(hclust(dist(abs(cor(na.omit(grade_6))))))
dev.off()

pdf("grade_7_hclust.pdf")
plot(hclust(dist(abs(cor(na.omit(grade_7))))))
dev.off()

pdf("grade_8_hclust.pdf")
plot(hclust(dist(abs(cor(na.omit(grade_8))))))
dev.off()


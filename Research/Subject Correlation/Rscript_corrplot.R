#install.packages('corrplot')
#install.packages('Hmisc', repos='http://cran.us.r-project.org')
#install.packages('ggpubr', repos='http://cran.us.r-project.org')


grade_6 <- read.csv("marks_mean_grade_6.csv")
grade_7 <- read.csv("marks_mean_grade_7.csv")
grade_8 <- read.csv("marks_mean_grade_8.csv")


grade_6 <- subset(grade_6, select = -X)
grade_7 <- subset(grade_7, select = -X)
grade_8 <- subset(grade_8, select = -X)


res_6 <- round(cor(grade_6, use="complete.obs", method="kendall"),2)
res_7 <- round(cor(grade_7, use="complete.obs", method="kendall"),2)
res_8 <- round(cor(grade_8, use="complete.obs", method="kendall"),2)

library(corrplot)
col_pallet=colorRampPalette(c("red","pink","lightpink","lightblue","blue"))(200)

pdf("grade_6_correlation.pdf")
corrplot(res_6, method="color",type="upper", number.cex = .7,addCoef.col = "black", order="alphabet",tl.col="black",cl.lim=c(0,1),col=col_pallet,is.corr=FALSE,title="Grade 6",mar=c(0,0,2,0))
dev.off()

pdf("grade_7_correlation.pdf")
corrplot(res_7, method="color", type="upper", number.cex = .7,addCoef.col = "black", order="alphabet",tl.col="black",cl.lim=c(0,1),col=col_pallet,is.corr=FALSE,title="Grade 7",mar=c(0,0,2,0))
dev.off()

pdf("grade_8_correlation.pdf")
corrplot(res_8,method="color", type="upper", number.cex = .7,addCoef.col = "black", order="alphabet",tl.col="black",cl.lim=c(0,1),col=col_pallet,is.corr=FALSE,title="Grade 8",mar=c(0,0,2,0))
dev.off()

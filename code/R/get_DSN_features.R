# 安装并加载所需的包
install.packages("ggplot2")
library(ggplot2)

# 从CSV文件中读取数据
data <- read.csv("all_data.csv")

size_attribute <- data$DSN.size

density_attribute <- data$DSN.density

bridge_attribute <- data$DSN.bridges

k_stars_attribute <- data$DSN.k.stars..k.3.


# 创建一个4x4的图形布局
layout(matrix(c(1, 2, 3, 4), nrow = 2))

# 绘制第一个子图
p1 <- hist(size_attribute, main = "", xlab = "", ylab = "number of projects", col = "grey", xlim = c(0,6000), ylim = c(0, 140))
title(xlab = "(a) DIstribution of DSN size", line = 4)
text(p1$mids, counts_size, labels = counts_size, pos = 3, cex = 0.8, col = "black")


# 绘制第二个子图
p2 <- hist(density_attribute, main = "", xlab = "", ylab = "number of projects", col = "grey", ylim = c(0, 193))
title(xlab = "(b) DIstribution of DSN density", line = 4)
text(p2$mids, counts_density, labels = counts_density, pos = 3, cex = 0.8, col = "black")

# 绘制第三个子图
p3 <- hist(bridge_attribute, main = "", xlab = "", ylab = "number of projects", col = "grey", ylim = c(0, 85))
title(xlab = "(c) DIstribution of DSN bridge", line = 4)
text(p3$mids, counts_bridge, labels = counts_bridge, pos = 3, cex = 0.8, col = "black")

# 绘制第四个子图
p4 <- hist(k_stars_attribute, main = "", xlab = "", ylab = "number of projects", col = "grey", xlim = c(0,500), ylim = c(0, 130))
title(xlab = "(d) DIstribution of DSN k_stars (k=3)", line = 4)
text(p4$mids, counts_k_stars, labels = counts_k_stars, pos = 3, cex = 0.8, col = "black")




# 安装并加载所需的包
install.packages("ggplot2")
library(ggplot2)

# 从CSV文件中读取数据
data <- read.csv("all_data.csv")

# 选择某个特定属性列
stibility_attribute <- data$DSN.stability

# 设置区间的数量和范围
num_bins <- 10
bin_range <- c(min(stibility_attribute), max(stibility_attribute))

another_bin_range <- c(min(aother_attribute), max(aother_attribute))

counts_stability <- hist(stibility_attribute, plot = FALSE)$counts

p1 <- barplot(stibility_attribute, xlab = "", ylab = "DSN stability")

p2 <- hist(stibility_attribute, main = "", xlab = "DSN stability", ylab = "number of projects", col = "grey", breaks = seq(0.00, 0.14, by = 0.01), ylim = c(0, max(hist(stibility_attribute)$counts) + 1)) + text(p2$mids, counts_stability, labels = counts_stability, pos = 3, cex = 0.8, col = "black")



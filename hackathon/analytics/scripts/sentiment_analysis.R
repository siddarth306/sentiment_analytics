suppressMessages(suppressWarnings(library(sentiment)))
args <- commandArgs(trailingOnly = TRUE)
fileName <- args[1]
data <- readChar(fileName, file.info(fileName)$size)
df <- data.frame(data)
textdata <- df[df$data, ]
textdata = gsub("[[:punct:]]", "", textdata)
textdata = gsub("[[:punct:]]", "", textdata)
textdata = gsub("[[:digit:]]", "", textdata)
textdata = gsub("http\\w+", "", textdata)
textdata = gsub("[ \t]{2,}", "", textdata)
textdata = gsub("^\\s+|\\s+$", "", textdata)
try.error = function(x)
{
  y = NA
  try_error = tryCatch(tolower(x), error=function(e) e)
  if (!inherits(try_error, "error"))
    y = tolower(x)
  return(y)
}
textdata = sapply(textdata, try.error)
textdata = textdata[!is.na(textdata)]
names(textdata) = NULL
class_pol = classify_polarity(textdata, algorithm="bayes")
polarity = class_pol[,4]
total_positive <- 0
total_negative = 0
for (ii in  class_pol[,"POS"]) {
  total_positive = total_positive + as.numeric(ii)
}
for (ii in  class_pol[,"NEG"]) {
  total_negative = total_negative + as.numeric(ii)
}
cat(total_positive)
cat('\n')
cat(total_negative)

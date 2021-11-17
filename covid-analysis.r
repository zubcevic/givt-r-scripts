# Load required library packages from specified CRAN repo
if(!require(tidyverse)) install.packages("tidyverse",repos = "https://mirror.lyrahosting.com/CRAN/")
library(tidyverse)

start_date = "2020-07-01"
end_date = "2022-01-01"

covid_feed <- "https://lcps.nu/wp-content/uploads/covid-19-datafeed.csv"
download.file(covid_feed, "covid19.csv")

covid <-read.table("covid19.csv",header=T,sep=",")
covid$day <- as.POSIXct(covid$Datum, format="%d-%m-%Y")

covid <- filter(covid, day >= as.Date(start_date), day <= as.Date(end_date))

plot(as.Date(covid$day),covid$IC_Bedden_COVID, type = "l",col = 2,xlim=as.Date(c(start_date, end_date)), ylim=c(0,3200), xlab = "Datum", ylab="# Bedden", col.axis="blue", font.axis=3, cex.axis=1)
lines(as.Date(covid$day),covid$IC_Bedden_Non_COVID, type = "l",col = 3)
lines(as.Date(covid$day),covid$Kliniek_Bedden, type = "l",col = 4)
legend("topright", c("IC_Bedden_COVID", "IC_Bedden_Non_COVID","Kliniek_Bedden"), lty = 1, col = 2:4)

ggplot(data = covid) + 
  geom_line(aes(x = as.Date(day), y = IC_Bedden_COVID), color = "red") +
  geom_line(aes(x = as.Date(day), y = IC_Bedden_Non_COVID), color = "green") +
  geom_line(aes(x = as.Date(day), y = Kliniek_Bedden), color = "blue") +
  xlab('Datum') +
  ylab('Aantal bedden') +
  scale_x_date(breaks = seq(as.Date(start_date), as.Date(end_date), by="2 month"), date_labels = "%b\n%Y") 

legend("topright", legend = c("IC_Bedden_COVID", "IC_Bedden_Non_COVID","Kliniek_Bedden"), fill=c("red","green","blue"))

browseURL("Rplots.pdf")

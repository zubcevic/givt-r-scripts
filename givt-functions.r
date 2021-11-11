# Load required library packages from specified CRAN repo
if(!require(tidyverse)) install.packages("tidyverse",repos = "https://mirror.lyrahosting.com/CRAN/")
if(!require(dplyr)) install.packages("dplyr",repos = "https://mirror.lyrahosting.com/CRAN/")
library(tidyverse)
library(dplyr)

givts_per_periode <- function(givt_all,periode) {

givt_all$Datum.begin <- as.POSIXct(givt_all$Datum.begin,format="%d-%m-%Y")
givt_all$period <- cut(givt_all[,"Datum.begin"], breaks=periode)

Collecte1 <- givt_all %>% filter(str_detect(Toewijzing, var_Collecte1_label)&!str_detect(Toewijzing, var_Collecte2_label)) %>% filter(!is.na(Brutobedrag),!is.na(Aantal.giften)) %>% group_by(period) %>% summarise(totaalKerk=sum(as.numeric(str_replace(Brutobedrag,',','.'))))
Collecte2 <- givt_all %>% filter(str_detect(Toewijzing, var_Collecte2_label)) %>% filter(!is.na(Brutobedrag),!is.na(Aantal.giften)) %>% group_by(period) %>% summarise(totaalDiaconie=sum(as.numeric(str_replace(Brutobedrag,',','.'))))
Collectes_per_Period <- merge(Collecte1, Collecte2, by.x="period",by.y="period")

return(Collectes_per_Period)
}

givts_plot <- function(givt_all,periode) {
Collectes <- givts_per_periode(givt_all,periode)
myplot <- barplot(t(Collectes[,2:3]), main=var_Main_label, xlab=var_X_axis_label, ylab=var_Y_axis_label, col=c(var_Collecte1_color,var_Collecte2_color), beside = T, names.arg=Collectes[order(as.Date(as.character(Collectes[,1]), "%Y-%m-%d")),1], las=1) 
legend("topleft", legend = c(var_Collecte1_label, var_Collecte2_label), fill = c(var_Collecte1_color,var_Collecte2_color))
mysubtitle = paste(var_Subtitle_label,periode,dep="")
mtext(side = 3, line = 0.25, at = 1, adj = -0.8, mysubtitle)
return(myplot)
}




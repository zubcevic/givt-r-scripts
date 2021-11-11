# Load functions
source("givt-functions.r")

# Define global variables
var_Main_label <<- "Collectes via GIVT"
var_Subtitle_label <<- "Bruto opbrengst per "
var_Collecte1_label <<- "1e Collecte"
var_Collecte2_label <<- "2e Collecte"
var_X_axis_label <<- "Maand"
var_Y_axis_label <<- "Bedrag in EUR"
var_Collecte1_color <<- "green"
var_Collecte2_color <<- "red"

# Load data
if(interactive()) {
#print("In interactive mode")
var_Filename <- readline(prompt="Enter filename to load: > ")
} else {
#print("Not in interactive mode")
cat("Enter filename to load: > ")
var_Filename <- readLines("stdin", 1)
}
givt_sample_data <-read.table(var_Filename,header=T,sep=";")

# Plot graph 1
dev.new()
png("givt-sample-1.png")
givts_plot(givt_sample_data,'month')
dev.off()
browseURL("givt-sample-1.png")

# Plot graph 2
dev.set(dev.next())
png("givt-sample-2.png")
givts_plot(givt_sample_data,'quarter')
dev.off()
browseURL("givt-sample-2.png")



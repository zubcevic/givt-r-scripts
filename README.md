# R scripts for analyzing GIVT data

This repository contains some scripts to analyze data that is exported from the GIVT dashboard.

## Prerequisites

+ Install R from [The R project](https://www.r-project.org). 
+ Tested with version 4.1.2 on MacOS, 11-11-2021.
+ Download a sample .csv export from the [GIVT dashboard](https://cloud.givtapp.net/#/).

## Contents

+ [givt-functions.r](givt-functions.r) contains library functions
+ [givt-sample.r](givt-sample.r) contains sample graph calls and menu to load the data

## Example usage

    echo sample.csv | Rscript givt-sample.r


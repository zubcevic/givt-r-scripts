const dateParser = d3.timeParse("%d-%m-%Y");

/* Use async in order to really load and be able to filter the data */
async function loadGivt() {
    //var initialdata = d3.csvParse(d3.select('#data_csv').text());
    const datasetOriginalText = await d3.text("./sample.csv");
    var dsv = d3.dsvFormat(';')
    datasetOriginal = dsv.parse(datasetOriginalText);
    
    /* process dates and add column */
    datasetOriginal.forEach(function(d, i) {
        d.date = dateParser(d['Datum begin']);
        d.month = d3.timeMonth(d.date);
    });
    console.log(datasetOriginal);

    /* filter rows with desired column values */
    collecte1 = datasetOriginal.filter(function(row) {
        return row['Toewijzing'] == '1e Collecte';
    });
    collecte2 = datasetOriginal.filter(function(row) {
        return row['Toewijzing'] == '2e Collecte';
    });
    
    /* construct new object from desired values */
    const datasetFiltered = new Object();
    datasetFiltered.collecte1 = collecte1;
    datasetFiltered.collecte2 = collecte2
    
    testdata = d3.rollup(datasetFiltered.collecte1, 
        v => {return {values: {len: v.length, Brutobedrag:d3.sum(v, d => d.Brutobedrag)}}; },
        d => {return {key: d.month}}
       )
    datasetFiltered.testdata = testdata;
    console.log(datasetFiltered);
    
    return datasetFiltered;
}
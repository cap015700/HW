d3.json('avghpi.json', function (error, data) {

    
// //To make the drop-down
//     filteredData = data;
//     strState = "KS" //the strState is what the drop-down call will be
//     filteredData.forEach(element => {
//         if (data.State === strState) { 
//             data = (row => row.STATE(strState))

//         }
//     });
    
// function dateclick() {
//     filtered_data = [];
//     for (let row of data) {
//       if (column.STATE === 'KS') {
//         filtered_data.push(row);
//       }
//             }
//     }
//     console.log(filtered_data);
//     createTables();
  

// console.log(filteredData)

    var yearSet = new Set(data.map(row => row.YR));
    // console.log(yearSet);
    var trace1 = {
        //use filteredData.map below once you get it figured out how to get it filtered with the code above
        y: data.map(row => row.AVHPI),
        x: data.map(row => row.YEAR),
        name: "Avg HPI",
        type: "bar"
      };
    
    var test = [trace1]
    
    var layout = {
        title: "Home Price Index Since 1975",
        margin: {
          l: 100,
          r: 100,
          t: 100,
          b: 100
        }
      };
      console.log(trace1)
      // Render the plot to the div tag with id "plot"
      Plotly.newPlot('plot', test, layout);
    

})


// var labels = datafile.jsonarray.map(function(e) {
//     return e.MONTH + " " + e.YR;
//  });
//  var data = datafile.jsonarray.map(function(e) {
//     return e.HPI;
//  });;
 
//  var ctx = canvas.getContext('2d');
//  var config = {
//     type: 'bar',
//     data: {
//        labels: labels,
//        datasets: [{
//           label: 'HPI by Year',
//           data: data,
//           backgroundColor: 'rgba(0, 119, 204, 0.3)'
//        }]
//     }
//  };
 
//  var chart = new Chart(ctx, config);

 
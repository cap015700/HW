var svgWidth = 1500;
var svgHeight = 500;

var margin = {
  top: 20,
  right: 40,
  bottom: 80,
  left: 100
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Create an SVG wrapper, append an SVG group that will hold our chart,
//and shift the latter by left and top margins.
var svg = d3
  .select(".chart")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight)

// Append an SVG group
var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);;

// Initial Params
var chosenXAxis = "Rich"

// function used for updating x-scale var upon click on axis label
function xScale(moneyData, chosenXAxis) {
  // create scales
  var xLinearScale = d3.scaleLinear()
    .domain([d3.min(moneyData, d => d[chosenXAxis]*.5) ,
      d3.max(moneyData, d => d[chosenXAxis]) 
    ])
    .range([0, 1300])

  return xLinearScale

};

// function used for updating xAxis var upon click on axis label
function renderAxes(newXScale, xAxis) {
  var bottomAxis = d3.axisBottom(newXScale)

  xAxis.transition()
    .duration(1000)
    .call(bottomAxis)

  return xAxis
}

// function used for updating circles group with a transition to
// new circles

function renderTestGroup(testGroup, newXScale, chosenXaxis) {
  testGroup.transition()
  .duration(1000)
  .attr("x", d => newXScale(d[chosenXAxis]))

  return testGroup

}
function renderCircles(circlesGroup, newXScale, chosenXaxis) {

  circlesGroup.transition()
    .duration(1000)
    .attr("cx", d => newXScale(d[chosenXAxis]))

  return circlesGroup
};

// function used for updating circles group with new tooltip
function updateToolTip(chosenXAxis, circlesGroup) {

  if (chosenXAxis == "Rich") {
    var label = "% Single Income > 200K: "
  } else {
    var label = "% Family <10K: "
  }

  var toolTip = d3.tip()
    .attr("class", "tooltip")
    .offset([80, -60])
    .html(function (d) {
      return (`${d.State}<br>${label}<br>${d[chosenXAxis]}`);
    });

  circlesGroup.call(toolTip);

  circlesGroup.on("mouseover", function (data) {
      toolTip.show(data);
    })
    // onmouseout event
    .on("mouseout", function (data, index) {
      toolTip.hide(data);
    });

  return circlesGroup
}

// Retrieve data from the CSV file and execute everything below
d3.csv("./data/MoneyHappiness.csv", function (err, moneyData) {
  if (err) throw err;

  // parse data
  moneyData.forEach(function (data) {
    data.Rich = +data.Rich;
    data.Depressed = +data.Depressed;
    data.Poor = +data.Poor;
  });

  // xLinearScale function above csv import
  var xLinearScale = xScale(moneyData, chosenXAxis)
    
  // Create y scale function
  var yLinearScale = d3.scaleLinear()
    .domain([0, d3.max(moneyData, d => d.Depressed+2)])
    .range([height, 0]);

  // Create initial axis functions
  var bottomAxis = d3.axisBottom(xLinearScale);
  var leftAxis = d3.axisLeft(yLinearScale);

  // append x axis
  var xAxis = chartGroup.append("g")
    .classed("x-axis", true)
    .attr("transform", `translate(0, ${height})`)
    .call(bottomAxis)

  // append y axis
  chartGroup.append("g")
    .call(leftAxis)

  // append initial circles
  var circlesGroup = chartGroup.selectAll("circles")
    .data(moneyData)
    .enter()
    .append("circle")
    .attr("cx", d => xLinearScale(d[chosenXAxis]))
    .attr("cy", d => yLinearScale(d.Depressed))
    .attr("r", 14)
    .attr("fill", "skyblue")

  var testGroup = chartGroup.selectAll("circles")
    .data(moneyData)
    .enter()
    .append("text")
    .text(function (d) {
      return (d.Abbrev);
    })
    .attr("x", function (d) {
      return xLinearScale(d[chosenXAxis]);
    })
    .attr("y", function (d) {
      return yLinearScale(d.Depressed);
    })
    .attr("font-size", "10px")
    .attr("text-anchor", "middle")
    .attr("class", "stateText")
    .attr("fill", "white")
   

  // Create group for  2 x- axis labels
  var labelsGroup = chartGroup.append("g")
    .attr("transform", `translate(${width/2}, ${height + 20})`)

  var richLabel = labelsGroup.append("text")
    .attr("x", 0)
    .attr("y", 20)
    .attr("text-anchor", "middle")
    .attr("value", "Rich") //value to grab for event listener
    .classed("active", true)
    .text("% Single and Rich");

  var poorLabel = labelsGroup.append("text")
    .attr("x", 0)
    .attr("y", 40)
    .attr("text-anchor", "middle")
    .attr("value", "Poor") //value to grab for event listener
    .classed("inactive", true)
    .text("% Poor with Family");

  // append y axis
  chartGroup.append("text")
  .attr("text-anchor", "middle")
    .attr("y", 0 - margin.left / 2)
    .attr("x", 0 - (height / 2))
    .attr("dy", "1em")
    .attr("transform", "rotate(-90)")
    .classed("axis-text", true)
    .text("% Depressed");

  // updateToolTip function above csv import
  var circlesGroup = updateToolTip(chosenXAxis, circlesGroup)

  // x axis labels event listener
  labelsGroup.selectAll("text")
    .on("click", function () {
      // get value of selection
      var value = d3.select(this).attr("value")
      if (value != chosenXAxis) {

        // replaces chosenXaxis with value
        chosenXAxis = value;

        // console.log(chosenXAxis)

        // functions here found above csv import
        // updates x scale for new data
        xLinearScale = xScale(moneyData, chosenXAxis);

        // updates x axis with transition
        xAxis = renderAxes(xLinearScale, xAxis);

        // updates circles with new x values
        circlesGroup = renderCircles(circlesGroup, xLinearScale, chosenXAxis);
        testGroup = renderTestGroup(testGroup, xLinearScale, chosenXAxis);
        // updates tooltips with new info
        circlesGroup = updateToolTip(chosenXAxis, circlesGroup);

        // changes classes to change bold text
        if (chosenXAxis == "Poor") {
          poorLabel
            .classed("active", true)
            .classed("inactive", false)
          richLabel
            .classed("active", false)
            .classed("inactive", true)
        } else {
          poorLabel
            .classed("active", false)
            .classed("inactive", true)
          richLabel
            .classed("active", true)
            .classed("inactive", false)
        };
      };
    });
});
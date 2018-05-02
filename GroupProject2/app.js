function buildPlot() {
    /* data route */
    var url = "/api/pals";
    Plotly.d3.json(url, function (error, response) {

        console.log(response);

        var data = response

        var layout = {
            scope: "usa",
            title: "US Housing Market",
            showlegend: true,
            height: 600,
            // width: 980,
            geo: {
                scope: "usa",
                projection: {
                    type: "albers usa"
                },
                showland: true,
                landcolor: "rgb(217, 217, 217)",
                subunitwidth: 1,
                countrywidth: 1,
                subunitcolor: "rgb(163, 226, 211)",
                countrycolor: "rgb(255,255,255)"
            },
        };

        Plotly.newPlot("plot", data, layout);
    });
}

buildPlot();

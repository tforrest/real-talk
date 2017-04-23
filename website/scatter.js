window.onload = function () {
  var chart = new CanvasJS.Chart("chartContainer", {
    title: {
      text: "Mood to Sleep Comparison",
      fontSize: 20
    },
    animationEnabled: true,
    axisX: {
      title: "Hours of Sleep",
      titleFontSize: 18

    },
    axisY: {
      title: "Mood",
      titleFontSize: 16
    },
    legend: {
      verticalAlign: 'bottom',
      horizontalAlign: "center"
    },

    data: [
    {
      type: "scatter",
      markerType: "square",
      toolTipContent: "<span style='\"'color: {color};'\"'><strong>{name}</strong></span><br/><strong> Hours of Sleep</strong> {x} <br/><strong> Mood</strong></span> {y}",

      name: "Good Sleep",
      showInLegend: true,
      dataPoints: [

      { x: 12, y: 5 },
      { x: 8.5, y: 4 },
      { x: 7, y: 5 },
      { x: 8, y: 4 },
      { x: 6, y: 2 },
      { x: 8, y: 3 },
      { x: 9.5, y: 3 },
      { x: 4, y: 4 },
      { x: 10, y: 3 },
      { x: 8, y: 5 },
      { x: 7, y: 5 },
      { x: 5, y: 5 },
      { x: 9.5, y: 4 },
      { x: 9, y: 2 }

      ]
    },
    {
      type: "scatter",
      name: "Bad Sleep",
      markerType: "triangle",
      showInLegend: true,
      toolTipContent: "<span style='\"'color: {color};'\"'><strong>{name}</strong></span><br/><strong> Hours of Sleep</strong> {x} <br/><strong> Mood</strong></span> {y}",

      dataPoints: [
      { x: 4, y: 2 },
      { x: 6.5, y: 3 },
      { x: 5, y: 2 },
      { x: 7, y: 4 },
      { x: 6, y: 3 },
      { x: 9, y: 1 },
      { x: 5.5, y: 4 },
      { x: 7, y: 2 },
      { x: 6, y: 2 },
      { x: 7.5, y: 4 },
      { x: 7, y: 3 },
      { x: 9.5, y: 1 },
      { x: 8, y: 3 },
      { x: 10, y: 2 }

      ]
    }
    ],
    legend: {
      cursor: "pointer",
      itemclick: function (e) {
        if (typeof (e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
          e.dataSeries.visible = false;
        }
        else {
          e.dataSeries.visible = true;
        }
        chart.render();
      }
    }
  });

  chart.render();
}

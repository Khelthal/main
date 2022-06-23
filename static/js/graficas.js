var areaOptions;

function initAreaOptions(series, categories) {
  areaOptions = {
     series: [
       {
         name: "series1",
         data: series,
       },
     ],
     chart: {
       height: 350,
       type: "area",
     },
     dataLabels: {
       enabled: false,
     },
     stroke: {
       curve: "smooth",
     },
     xaxis: {
       type: "datetime",
       categories: categories,
     },
     tooltip: {
       x: {
         format: "dd/MM/yy HH:mm",
       },
     },
   };  

  var chart = new ApexCharts(document.querySelector('#chart'), areaOptions)
  chart.render()  
}

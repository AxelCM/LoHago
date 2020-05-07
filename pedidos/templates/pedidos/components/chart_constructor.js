<script type="text/javascript">

var fecha = []
var parser = []
var maximo = 0
var defaultData = [{%for counter in default%} '{{counter}}',{%endfor%}];
var labels = [{%for label in labels%}'{{label}}', {%endfor%}];
for(var i=0; i<defaultData.length;i++){
  parser[i] = parseInt(defaultData[i], 10);
  }
maximo = Math.max.apply(null, parser);

$.ajax({
  method: "GET",
  success: function(data){
    setChart()
  },
  error: function(error_data){
      console.log("error")
      console.log(error_data)
  }
})

function setChart(){
  var types = document.getElementById('type_chart').value;
  var ctx = document.getElementById('myChart');
  var myChart = new Chart(ctx, {
      type: types,
      data: {
        is3D: true,
          labels: labels,
          datasets: [{
              label: "ORDEN",
              data: defaultData,
              borderColor: [
                  'rgba(255, 99, 132, 1)',
                  'rgba(255, 206, 86, 1)',
                  'rgba(54, 162, 235, 1)',
                  'rgba(255, 206, 86, 1)',
                  'rgba(54, 162, 235, 1)',
                  'rgba(75, 192, 192, 1)',
                  'rgba(153, 102, 255, 1)',
                  'rgba(255, 159, 64, 1)',
                  'rgba(75, 192, 192, 1)',
                  'rgba(75, 192, 192, 1)',
                  'rgba(255, 99, 132, 1)',
                  'rgba(255, 206, 86, 1)',
              ],
              pointStyle: 'circle',
              borderWidth: 3,
              borderDash :[0] ,

          }]
      },

          options: {
            title: "GRAFICA",
              scales: {
                    yAxes: [{
                      ticks: {
                          steps: 1,
                          max: maximo + 2,
                          beginAtZero: true

                      }
                  }]
              }
            }
  })

}
</script>

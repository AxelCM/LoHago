// function getType() {
//   var items;
//     selected = document.getElementById('cat');
//     id= selected.options[selected.selectedIndex].value
//     items = [{%for mark in marks%}'{{mark.name}}',{%endfor%}];
//   var str = ""
//   for (var item of items) {
//     str += "<option>" + item + "</option>"
//   }
//   document.getElementById("mark").innerHTML = str;
// }
// document.getElementById("cat").addEventListener("onchange", getType)
// dicto = {
//   {%for mark in marks%}
//   '{{mark.category.pk}}':'{{mark.name}}',
//   {%endfor%}
// }

$(document).ready(function(){
    loadmark();
      $('#cat').change(function(){
          loadmark();
      });
})

function loadmark(){
  var token = '{{csrf_token}}';
  $.ajax({
    headers: { "X-CSRFToken": token },
    type:"POST",
    url:"{%url "get_types"%}",
    data:"cat=" + $('#cat').val(),
    success:function(r){
        $('#mark').html(r);
    }
  });
}

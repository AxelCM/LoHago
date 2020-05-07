Swal.fire({
  title : "{%for message in messages%}{{message}}{%endfor%}",
  icon: 'success'
});

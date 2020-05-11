Swal.fire({
  title: '<strong>LOHAGO APP</u></strong>',
  icon: 'success',
  html:
    '<p>Te damos la Bienvenida <b>{{request.user.first_name}}</b>,</p> ' +
    '<a class="btn btn-warning" href={%url "clean_cart"%}>ENTENDIDO!</a>',
  showConfirmButton:false,

})

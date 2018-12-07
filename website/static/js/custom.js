form = document.getElementsByClassName("form-control")
btn  =  document.getElementsByTagName("button")

const url = window.location.href + "feedback"

function isEmpty(input) {
    return input =="";
  }

function send(){
    form_data = Object.values(form).reduce((obj,field) => { obj[field.name] = field.value; return obj }, {})
    if (Object.values(form_data).some(isEmpty)) {
        Swal({
            type: 'error',
            title: 'Oops...',
            text: 'Please fill all the fields'
        })
    }
    else{
        axios({
            method: 'post',
            url: url,
            data : {
                "form": form_data
            }
        })
        .then(data=>console.log(data))
        .catch(err=>console.log(err))
        Swal({
            position: 'center',
            type: 'success',
            title: 'Thank you. We received your message',
            showConfirmButton: false,
            timer: 1500
          })
    }
}
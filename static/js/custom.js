form = Array.from(document.getElementsByClassName("form-control"))

function check_form(){
    form.every(function(item){ 
        return item.value != ""
    })
}
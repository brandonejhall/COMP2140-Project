window.onload=function(){

    $(document).ready(function(){
        let rescheduleSubmit= document.querySelector('#reschedule-submit');

        rescheduleSubmit.addEventListener("click",function(e){
            e.preventDefault();
            clearErrors();
    
            let reference = document.querySelector('#reference');
            let id= document.querySelector('#id');
    
            if (!isReference(reference.value.trim())){
                validationFailed =true;
                reference.style.border="2px solid red";
                displayErrorMessage(reference, "*Invalid reference #*")
            }else{
                reference.style.removeProperty("border");
            }
    
            if (!isValidID(id.value.trim())){
                validationFailed=true;
                id.style.border="2px solid red";
                displayErrorMessage(id,"*Invalid ID*");
            }else{
                id.style.removeProperty("border");
    
            }
        })
    })

    $(document).ready(function(){
        let homesubmit=document.querySelector("#form-submit");

        homesubmit.addEventListener("click",function(e){
            e.preventDefault();
            clearErrors();
    
            let name= document.querySelector("#name");
            let id=document.querySelector("#id");
            let email=document.querySelector("#email");
    
            
            if (isEmpty(name.value.trim())){
                validationFailed=true;
                name.style.border="2px solid red";
                displayErrorMessage(name,"*You must fill in your Full Name*");
            }else{
                name.style.removeProperty("border");
            }
    
    
            if (!isValidID(id.value.trim())){
                validationFailed=true;
                id.style.border="2px solid red";
                displayErrorMessage(id,"*Invalid ID*");
            }else{
                id.style.removeProperty("border");
            }
            
            if (!isValidEmail(email.value.trim())){
                validationFailed=true;
                email.style.border="2px solid red";
                displayErrorMessage(email,"*Invalid email address*");
            }else{
                email.style.removeProperty("border");
            }
        })
    
    })

    
    
}

function isEmpty(elementValue) {
    if (elementValue.length == 0) {
      // Or you could check if the value == ""
      console.log('field is empty');
      return true;
    } 
    return false;
}

function isValidID(id) {
    return /^\d{9}$/.test(id);
}

function isReference(ref){
    return /^\d{13}$/.test(ref);
}

function isValidEmail(emailAddress) {
    return /^[-a-z0-9~!$%^&*_=+}{\'?]+(\.[-a-z0-9~!$%^&*_=+}{\'?]+)*@([a-z0-9_][-a-z0-9_]*(\.[-a-z0-9_]+)*\.(aero|arpa|biz|com|coop|edu|gov|info|int|mil|museum|name|net|org|pro|travel|mobi|[a-z][a-z])|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,5})?$/.test(emailAddress);
}

function insertAfter(element, newNode) {
    element.parentNode.insertBefore(newNode, this.nextSibling);
}

function clearErrors() {
    var elementsWithErrors = document.querySelectorAll('.error');
    //console.log(elementsWithErrors);
    for (var x = 0; x < elementsWithErrors.length; x++) {
      elementsWithErrors[x].setAttribute('class', '');
      elementsWithErrors[x].parentNode.removeChild(elementsWithErrors[x].nextElementSibling);
      //console.log(elementsWithErrors[x].nextElementSibling);
    } 
}

function displayErrorMessage(formField, message) {
    formField.setAttribute('class', 'error');
    var errorMessageText = document.createTextNode(message);
    var errorMessage = document.createElement('span');
    errorMessage.setAttribute('class', 'error-message');
    errorMessage.appendChild(errorMessageText);
    //formField.insertAfter(errorMessage);
    insertAfter(formField, errorMessage);
}
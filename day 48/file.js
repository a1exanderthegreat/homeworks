const obj = {}

const form = document.getElementById("form")
const btn = document.getElementById("submit")

form.addEventListener("submit" , function(e){
    e.preventDefault();
    
    username = form.elements.username.value
    password = form.elements.password.value

    if(username.length >= 5 && password.length >= 8){
        obj.username = username
        obj.password = password
    }else {
        alert("Failed to register!")
    }
    console.log(obj)
})
let userNumber = prompt("Enter Your Number: ")

console.log(typeof(userNumber))                     
let convertedNumber = Number(userNumber)            
console.log(typeof(convertedNumber)) 

console.log(userNumber + convertedNumber)           
console.log(Number(userNumber) + convertedNumber)  




let temp = prompt("Enter the temperature of your room: ")

    //Logical Operators
if (temp <= 0 && temp >= -15) {
    console.log("Low Temperature.")

} else if (temp <= -16 || temp >= 50) {
    console.log("Wild Temperature.")

}else {
    console.log("Good Weather.")
}
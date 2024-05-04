let tickets = Number(prompt("How many tickets would you like to buy?"))

for(let i = 0; i < tickets; i++) {
    let name = prompt("Enter your Name: ")
    let surname = prompt("Enter your Surname: ")
    let age = prompt("Enter your Age: ")
}


let ticketCode = []
const abc = ["A" , "B" , "D" , "E" , "0" , "1" , "2" , "3" , "4" , "5"]

let ticketCodeGenerator = {
    random: function() {
        ticketCode = Math.random(abc)
    }
}
ticketCodeGenerator.random()

console.log(ticketCodeGenerator.random)
console.log("Active")

let true_answers = document.querySelectorAll(".true_answer")
let false_answer1s = document.querySelectorAll(".false_answer1")
let false_answer2s = document.querySelectorAll(".false_answer2")
let false_answer3s = document.querySelectorAll(".false_answer3")

let answersEl = document.querySelectorAll("ul")


console.log(true_answers[0].value, false_answer1s[0].value, false_answer2s[0].value, false_answer3s[0].value)

let first = [true_answers[0].value, false_answer1s[0].value, false_answer2s[0].value, false_answer3s[0].value]
first = randomize(first)

first.forEach(option => {
    let choice = document.createElement("li")
    choice.innerHTML = option
    answersEl[0].appendChild(choice)
})

function randomize(answers) {
    return answers.sort(() => Math.random() - 0.5)
}

console.log(randomize(first))
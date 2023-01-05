console.log("Active");

let btn = document.getElementById('btn');
let radioButtons = document.querySelectorAll('input[name="answer"]');

let true_answers = document.querySelectorAll(".true_answer");
let false_answer1s = document.querySelectorAll(".false_answer1");
let false_answer2s = document.querySelectorAll(".false_answer2");
let false_answer3s = document.querySelectorAll(".false_answer3");

btn.addEventListener('click', () => {
    let selectedAnswer;
    let score = 0
    for (let i=0; i< true.answers.length; i++) {

    }
    for (let radioButton of radioButtons) {
        if (radioButton.checked) {
            selectedAnswer = radioButton.value;
            if (selectedAnswer = true_answers) {
                score++
            }
            break;
        }
    }  
});



for (let i=0; i<true_answers.length; i++) {
    let answersEl = document.querySelectorAll("ul")
    let currentAns = [true_answers[i].value, false_answer1s[i].value, false_answer2s[i].value, false_answer3s[i].value]  
    currentAns = randomize(currentAns)
    currentAns.forEach(option => {
        let choice = document.createElement("li")
        choice.innerHTML = "<input type= 'radio' name= 'text' value= '"+ option + "'><span>"+ option +"</span>"
        answersEl[i].appendChild(choice)
    })
};

function randomize(answers) {
    return answers.sort(() => Math.random() - 0.5)
};

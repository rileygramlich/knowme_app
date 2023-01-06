console.log("Active");

let btn = document.getElementById('btn');

let true_answers = document.querySelectorAll(".true_answer");
let false_answer1s = document.querySelectorAll(".false_answer1");
let false_answer2s = document.querySelectorAll(".false_answer2");
let false_answer3s = document.querySelectorAll(".false_answer3");

for (let i=0; i<true_answers.length; i++) {
    let answersEl = document.querySelectorAll("ul")
    let currentAns = [[true_answers[i].value, 't'], [false_answer1s[i].value, 'f'], [false_answer2s[i].value, 'f'], [false_answer3s[i].value, 'f']]  
    currentAns = randomize(currentAns)
    currentAns.forEach(option => {
        let choice = document.createElement("li")
        choice.innerHTML = `<input type= 'radio' name= 'text' class= ${option[1]} value= ${option[0]}><span>${option[0]}</span>`
        answersEl[i].appendChild(choice)
    })
};

let radioButtons = document.querySelectorAll('input[name="text"]');
console.log(radioButtons)

function randomize(answers) {
    return answers.sort(() => Math.random() - 0.5)
};

let userAnswers = Array.from({ length: radioButtons.length / 4 })
Array.from(radioButtons).forEach(radioButton => {
    radioButton.addEventListener('change', (e) => {
        let question = e.target.parentNode.parentNode.parentNode.id
        userAnswers[question] = e.target.classList.contains('t')
    })
});

let score = 0
btn.addEventListener('click', () => {
    score = userAnswers.filter(answer => answer == true).length
    let resultEl = document.getElementById("results")
    let result = document.createElement("span")
    let percentage = Math.floor(score / userAnswers.length * 100)
    if (percentage >= 80) {
        result.innerHTML = `You got ${percentage}% (${score}/${userAnswers.length}) correct - You know me so well!`
    } else if (percentage >= 60) {
        result.innerHTML = `You got ${percentage}% correct - We need to hangout more!`
    } else if (percentage >= 40) {
        result.innerHTML = `You got ${percentage}% correct - Oh boy... We really need to talk more...`
    } else if (percentage >= 20) {
        result.innerHTML = `You got ${percentage}% correct - That's a little sad...`
    } else if (percentage >= 0)
    result.innerHTML = `You got ${percentage}% correct - Dang... Friendship Cancelled...`
    resultEl.appendChild(result)
});
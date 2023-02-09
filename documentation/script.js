let input = document.getElementById("text2acii_input");
let output = document.getElementById("text2acii_output")

input.addEventListener("input", function() {
    translate(input.value);
});

function translate(text) {
    let translated = ""

    var temp = text.split(" ").join("")
    console.log(temp)

    if(!isNaN(temp)){
        text = text.split(" ")
        for(let i = 0; i < text.length; i++){
            translated = translated + " " + String.fromCharCode(text[i])
        }

        output.innerHTML = "<b>Результат: </b>" + translated
    }

    else{
        for(let i = 0; i < text.length; i++){
            translated = translated + " " + text[i].charCodeAt(0)
        }

        output.innerHTML = "<b>Результат: </b>" + translated
    }

}
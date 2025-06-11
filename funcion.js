function insertToDisplay(data){
    document.querySelector('.display').value += data
}

function allclean(){
    document.querySelector('.display').value = ''
}

function clean(){
    const display = document.querySelector('.display')
    display.value = display.value.slice(0, -1)
}

function result(){
    const display = document.querySelector('.display')
    
    try{
        display.value = eval(display.value)
    }catch{
        display.value = "Error"
    }
}

function porcento(){
    const display = document.querySelector('.display').value;
    document.querySelector('.display').value = parseFloat(display)*0.01;
}

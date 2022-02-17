let btn = document.querySelector('#btn1')
let text1 = document.querySelector('#text1')
let result = document.querySelector('#result')

btn.addEventListener("click",() => {
  let num1 = parseInt(text1.value)

  if(num1 % 3 == 0 && num1 % 7 == 0){
    result.innerHTML = 'it is divisible by 3 and 7'
  }
  else if(num1 % 3 == 0){
    result.innerHTML = 'divisible only by 3'
  }
  else if(num1 % 7 == 0){
    result.innerHTML = 'divisible only by 7'
  }
  else{
    result.innerHTML = 'divisible by neither'
  }

})

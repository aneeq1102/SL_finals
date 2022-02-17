let btn = document.querySelector('#btn1')
let text1 = document.querySelector('#text1')
let text2 = document.querySelector('#text2')


let ip1 = document.querySelector('#num1')
let ip2 = document.querySelector('#num2')

btn.addEventListener("click",(e) => {
  ip1.innerHTML = text1.value
  ip2.innerHTML = text2.value
  e.preventDefault()
})

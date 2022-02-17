console.log('testing')

let res = document.querySelector('#result')
let mul = document.querySelector('#multiplication')
let add = document.querySelector('#addition')
let in1 = document.querySelector('#in1')
let in2 = document.querySelector('#in2')
console.log(res,mul,add,in1,in2)

mul.addEventListener("click",() => {
  res.innerHTML = "Result:"
  let num1 = parseInt(in1.value)
  let num2 = parseInt(in2.value)

  res.innerHTML += (num1 * num2)
})

add.addEventListener("click",() => {
  res.innerHTML = "Result:"
  let num1 = parseInt(in1.value)
  let num2 = parseInt(in2.value)

  res.innerHTML += (num1 + num2)
})

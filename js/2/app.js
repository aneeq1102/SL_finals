let btn1 = document.getElementById("btn_1")

btn1.addEventListener("click",() => {
  alert('triggerred by first click event listener')
})

btn1.addEventListener("click",() => {
  alert('triggered by second click event listener')
})

let tbox = document.getElementById('tbox')

tbox.addEventListener("mouseover",() => {
  tbox.style.background = "red"
})

tbox.addEventListener("mouseout",() => {
  tbox.style.background = "blue"
})

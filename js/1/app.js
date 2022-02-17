let btn1 = document.getElementById("btn_1")

btn1.addEventListener("click",() => {
  alert('triggerred by first click event listener')
})

btn1.addEventListener("click",() => {
  alert('triggered by second click event listener')
})

document.querySelectorAll('.food').forEach(item => {
  item.addEventListener("click",(e) => {
    alert(`${e.target.innerHTML}`)
  })
})

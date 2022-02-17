document.querySelector('#blu_btn').addEventListener("click",() => {
  document.querySelector('body').style.background = "blue"
})

document.querySelector('#grn_btn').addEventListener("click",() => {
  document.querySelector('body').style.background = "green"
})

let tb = document.querySelector('#changingtb')

document.onkeydown = function(e) {
            switch (e.keyCode) {
                case 37:
                    tb.style.background = "yellow"
                    break;
                case 38:
                    tb.style.background = "purple"
                    break;
                case 39:
                    tb.style.background = "orange"
                    break;
                case 40:
                    tb.style.background = "red"
                    break;
            }
}

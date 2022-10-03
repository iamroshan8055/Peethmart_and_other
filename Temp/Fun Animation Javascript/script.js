const boxes = document.querySelectorAll('.box')

window.addEventListener('scroll', checkBoxes)

checkBoxes()

function checkBoxes() {
    const triggerBottom = window.innerHeight / 5 * 4

    boxes.forEach(abc => {
        const boxTop = abc.getBoundingClientRect().top

        if(boxTop < triggerBottom) {
            abc.classList.add('show')
        } else {
            abc.classList.remove('show')
        }
    })
}
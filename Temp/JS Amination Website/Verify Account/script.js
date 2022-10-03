const codes = document.querySelectorAll('.code')

codes[0].focus()
console.log(codes)
codes.forEach((code, idx) => {
    code.addEventListener('keydown', (e) => {
        
        if(e.key >= 0 && e.key <=9) {
            codes[idx].value = ''
            setTimeout(() => codes[idx + 1].focus(), 10)
        } else if(e.key === 'Backspace') {
            setTimeout(() => codes[idx - 1].focus(), 10)
        }
    })
})


$('#xyz').on('keyup',function(){
    var value = $(this).val()
    console.log('Value:', value)


fetch("otp.json")
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {
        // console.log("==================",data.data[0].price.length)
        for (i=0; i<data.data.length; i++){
            if (parseInt(data.data[i].otp)==value){
                // document.getElementById("xyz").setAttribute("maxlength", data.data[0].price.length);
                document.getElementById("suc").innerHTML="Success!"
            } else {
                document.getElementById("suc").innerHTML=""
            }
            data.data[i].price="100";
            console.log("try",data.data[i]);
            // set(data.data[i]);
        }
    })
    .catch((error) =>{
        console.log(error);
    });
})

var hours = 24
var now = new Date().getTime();
var stepTime = localStorage.getItem('stepTime');

if(stepTime == null){
    localStorage.setItem('stepTime',now)

} else {
    if(now - stepTime > hours *60*60*1000){
        localStorage.clear();
        localStorage.setItem('stepTime',now);
    }
}

// const inpkey = documentz('#language');




// const inpButton = document.getSelection('.cards1');
// const inpkey = document.getSelection("languages");





// var languages = JSON.parse(localStorage.getItem('languages'));
//     console.log(localStorage.getItem('languages'))
//     // // var total = localStorage.getItem('total');
    
//     if(languages == null || languages == undefined){
//         localStorage.setItem('languages',JSON.stringify([]));
    
//         languages = JSON.parse(localStorage.getItem('languages'))
//         alert("Your data is stored");
//     }


var cart= document.querySelector("#cart")






// jQuery(function() {
//     jQuery('#car').change(function() {
//         this.form.submit();
//     });
// });

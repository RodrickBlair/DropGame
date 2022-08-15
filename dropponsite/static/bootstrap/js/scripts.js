function currentTime() {
  let date = new Date();
  let hh = date.getHours();
  let mm = date.getMinutes();
  let ss = date.getSeconds();
  let session = "AM";

  if(hh === 0){
      hh = 12;
  }
  if(hh > 12){
      hh = hh - 12;
      session = "PM";
   }

   hh = (hh < 10) ? "0" + hh : hh;
   mm = (mm < 10) ? "0" + mm : mm;
   ss = (ss < 10) ? "0" + ss : ss;

   let time = hh + ":" + mm + ":" + ss + " " + session;

  document.getElementById("clock").innerText = time;
  let t = setTimeout(function(){ currentTime() }, 1000);
}

let date = new Date();
let mi = date.getMinutes();
let ho = date.getHours();
if(ho <= 8 && mi <= 26){
    console.log('8:30AM Early Bird Draw')
}else if(ho <= 10 && mi <= 26){
    console.log('10:30AM Morning Draw')
}else if(ho <= 10 && mi <=25){
    console.log('1:00PM Midday Draw')
}else if(ho <= 15){
    console.log('3:00PM Mid Afternoon Draw')
}else if(ho <= 17){
    console.log('5:00PM Drive Time Draw')
}else if(ho <= 20 && mi <= 25){
    console.log('8:25PM Evening Draw')
}else{
    console.log('Prepare for tomorrow')
}


currentTime();

// GET TIME
// CHECK IF TIME IS BETWEEN 1AM & 8:25AM
// CHECK IF TIME IS BETWEEN 8:30AM & 10:25AM
// CHECK IF TIME IS BETWEEN 10:30AM & 12:55PM
// CHECK IF TIME IS BETWEEN 1:00AM & 2:55PM
// CHECK IF TIME IS BETWEEN 3:00PM & 4:55PM
// CHECK IF TIME IS BETWEEN 5:00PM & 8:20PM


window.onload = function(){
    // 60
    var oGreen = document.getElementById('green');
    //30
    var oYellow = document.getElementById('yellow');
    // 10
    var oRed = document.getElementById('red');
    var flag = 0, timerC = 0;
    var time_out = 200;
    function Increase(){
        if(flag<=60){
            oGreen.style.width = flag + '%';
            timerC = setTimeout(Increase, time_out);
            time_out -= 2;
            flag++;
        }
        else if(flag>=60&&flag<=90){
            oYellow.style.width = flag-60 + '%';
            timerC = setTimeout(Increase, time_out);
            time_out -= 1;
            flag++;
        }
        else{
            oRed.style.width = flag-90 + '%';
            timerC = setTimeout(Increase, time_out);
            time_out -= 0.5;
            flag++;
            if(flag == 101){
                clearTimeout(timerC);
                flag=0;
            }

        }
    }
    Increase();
}

var num = 0;
var click_count = 0;

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms))
}
function secret(){

    if(num<2){
        num++;
    }
    else{
        window.open("/manager/");
        num = 0;
    }


    sleep(1500).then(() => {
        // 这里写sleep之后需要去做的事情
        num = 0;
    })

}
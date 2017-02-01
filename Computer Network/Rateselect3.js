var Buf_now; // calculate buffer occupancy
var Rate_prev;  // Select first bit rate
var cu;
var r;
var arr1;
var arr2;
var BW;  // get real-time bandwidth
var prediction;
var pre_count;



function RateSelectInitialize(){
    Buf_now = 0;
    Rate_prev = 0.5;
    cu = 100;
    r = 50;
    arr1 = [];
    arr2 = [];
    prediction = [];
    pre_count = 0;
}

function Predict(prediction, Rate_next){
    if (prediction.length < 20){
        prediction.push(Rate_next);
    }
    else{
        if (Math.std(prediction) >= 5){
            Rate_next = 2;
            pre_count += 1;
        }
        else if (Math.std(prediction) > 2 && Math.std(prediction) < 5){
            Rate_next = 8;
            pre_count += 1;
        }
        else{
            pre_count = 0;
            prediction = [];
        }
    }
    if (pre_count > 50){
        prediction = [];
        pre_count = 0;
    }
}





function func(Buf_now){
    result = 35.74 * Math.exp((-((Buf_now)-170)/65) ** 2);
    return result;
}



function RateSelect(Rate_prev, Buf_now, r, cu, arr1, arr2, BW)
{
    if (Buf_now > 50){
        if (BW > 0 && BW < 2){
            Rate_next1 = 0.5;
        }
        else if (BW >= 2 && BW < 5){
            Rate_next1 = 2;
        }   
        else if (BW >= 5 && BW < 15){
            Rate_next1 = 8;
        }
        else if (BW >= 15){
            Rate_next1 = 20;
        }
        else{
            Rate_next1 = 0.5;
        }
    }
    else{
        Rate_next1 = 0.5;
    }
        
    if (Rate_prev == R_max){
        Rate_plus = R_max;
    }
    else{
        for (var i=0;i<R_i.length;i++){
            if (R_i[i] > Rate_prev){
                arr1.push(R_i[i]);
            }
        Rate_plus = Math.min(arr1);
        arr1 = [];
        }
    }
    if (Rate_prev == R_min){
        Rate_minus = R_min;
    }
    else{
        for (var i=0;i<R_i.length;i++){
            if (R_i[i] < Rate_prev){
                arr1.push(R_i[i]);
            }
        Rate_minus = Math.max(arr1);
        arr1 = [];
        }
    }
    
    
    if (Buf_now <= r){
        Rate_next2 = R_min;
    }
    else if (Buf_now >= (r+cu)){
        Rate_next2 = R_max;
    }
    else if (func(Buf_now) >= Rate_plus){
        for (var i=0;i<R_i.length;i++){
            if (R_i[i] < func(Buf_now)){
                arr2.push(R_i[i]);
            }
        Rate_next2 = Math.max(arr2);    
        arr2 = [];    
        }
    }
    else if (func(Buf_now) <= Rate_minus){
        for (var i=0;i<R_i.length;i++){
            if (R_i[i] > func(Buf_now))
                arr2.push(R_i[i]);
        Rate_next2 = Math.min(arr2);
        arr2 = [];
        }
    }
    else{
        Rate_next2 = Rate_prev;
    }
    return Math.min(Rate_next1, Rate_next2)
}
    

    
    
    
    
    
    
    
    
    
    
    
        
        
        
    
}
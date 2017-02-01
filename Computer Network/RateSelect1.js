/*
This is algorithm 1
Video Rate Adaptation Algorithm
*/



var Buf_now = 110; //The current buffer occupancy, seconds
var r = 90;       //The size of reservoir , seconds
var cu = 60;      //The size of cushion, seconds

var Rate_prev = 500; // The previously used video rate, bps
var R_max = 20000;   //Maximum video rate, bps
var R_min = 500; // Minimum video rate, bps

var R_i = [500, 2000, 8000, 20000];  
var arr1 = []; // empty list
var arr2 = []


fucntion func(Buf_now) {
    result = 35.74 * Math.exp(-((Buf_now-182.9)/43.23)^2);
    return result;
}


function algorithm1 (Rate_prev, Buf_now, r, cu) 
{
    if (Rate_prev === R_max){
        Rate_+ = R_max;
    }
    else{
        for (var i=0; i<R_i.length;i++)
            {
                if (R_i[i]>Rate_prev){
                    arr1.push(R_i[i]);
                }
            }
        Rate_+ = Math.min(arr1);
        arr1 = [];
    }
    if (Rate_prev === R_min){
        Rate_ = R_min
    }
    else{
        for (var i=0;i<R_i.length;i++){
            if (R_i[i] < Rate_prev){
                arr1.push(R_i[i]);
            }
        }
        Rate_ = Math.max(arr1);
        arr1 = [];
        }
    
    
    if (Buf_now <= r){
        Rate_next = R_min;
    }
    else if (Buf_now >= (r+cu))
        {
            Rate_next = R_max;            
        }
    else if (func(Buf_now) >= Rate_+){
             for (var i=0;i<R_i.length;i++){
        if (R_i[i] < func(Buf_now)){
            arr2.push(R_i[i]);
        }  
    }
             Rate_next = Math.max(arr2);
             arr2 = [];
             }
    else if (func(Buf_now) <= Rate_){
        for (var i=0;i<R_i.length;i++){
            if (R_i[i] > func(Buf_now)){
                arr2.push(R_i[i]);
            }
        }
        Rate_next = Math.min(arr2);
        // R_i : R_i > f(Buf_now)
    }
    else{
        Rate_next = Rate_prev;
    }
    
    return Rate_next;   
}



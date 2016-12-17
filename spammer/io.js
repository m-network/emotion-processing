var PORT = 9000;
var HOST = '192.168.1.5';
var LOCAL = "192.168.1."+(Math.round(Math.random()*120)+8);
var endpoint = "/shake/"

var osc = require('node-osc');
var client = new osc.Client(HOST, PORT);

var count = 0;
var frequency = 30;

function randomMultiplier(num){
  return (Math.random()*-2) + num;
}

function pulse(num){
  return Math.sin(num)+1;
}

function varyFrequency(){
  return Math.ceil(Math.random()*5000)+100;
}


function composeMessage(conn){
  // count++;
    // /gyro/192.168.1.25 {"v0":"-0.01021847", "v1":"0.1135909", "v2":"0.00504617"}
    // var dummydata = {
    //   v0:pulse(count+0.1),
    //   v1:pulse(count-0.05),
    //   v2:pulse(count-0.1),
    // }

    var dummydata = 1;


    conn.send(endpoint+LOCAL.toString(), dummydata, function () {
      console.log("--");
    });
}

var myfreq = 100;
setInterval(function(){

  if(myfreq %10 == 0){
    console.log("mod 10")
    myfreq = Math.ceil(Math.random()*5000)+100;
  }
  myfreq++;

  composeMessage(client);
  console.log('send',myfreq)
},1000);

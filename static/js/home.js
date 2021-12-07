/*
    Author : Thom Guillot
    Mail : thom.guillot@telecomnancy.eu
    Date : 7/12/2021
*/

// Help button functionalities

document.getElementById("helpbut").onclick = function() {
      
    document.getElementById("help").style.display = "block";
    document.getElementById("cand").style.display = "none";
    document.getElementById("helpbut").disabled = true;
    document.getElementById("candbut").disabled = false;

}

// Candidates button functionalities

document.getElementById("candbut").onclick = function() {

    document.getElementById("help").style.display = "none";
    document.getElementById("cand").style.display = "block";
    document.getElementById("helpbut").disabled = false;
    document.getElementById("candbut").disabled = true;

}
function myFunction() {
    var x = document.getElementById("myTab");
    if (x.className === "tab") {
      x.className += " responsive";
    } else {
      x.className = "tab";
    }
  }

 
function showForm() {
  var location = document.getElementById("location").value;
  var nagpurForm = document.getElementById("nagpurForm");
  var pimpriForm = document.getElementById("pimpriForm");

  nagpurForm.style.display = "none";
  pimpriForm.style.display = "none";

  if (location === "nagpur") {
    nagpurForm.style.display = "block";
  } else if (location === "pimpri") {
    pimpriForm.style.display = "block";
  }
}


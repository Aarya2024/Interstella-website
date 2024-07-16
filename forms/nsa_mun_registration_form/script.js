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

document.getElementById("phone").addEventListener("input", function (e) {
  this.value = this.value.replace(/[^0-9]/g, "").slice(0, 10);
});

document.getElementById("name").addEventListener("input", function (e) {
  this.value = this.value.replace(/[^a-zA-Z]/g, "");
});

document.getElementById("age").addEventListener("input", function (e) {
  let age = parseInt(this.value);
  if (age < 1 || age > 100) {
    this.value = "";
  }
});

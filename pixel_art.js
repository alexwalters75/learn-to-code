// Select color input
var colorPicker = document.getElementById('colorPicker');

// Select size input
var inputWidth = document.getElementById('inputWidth').value;
var inputHeight = document.getElementById('inputHeight').value;
var pixelCanvas = document.getElementById('pixelCanvas');
var sizePicker = document.getElementById('sizePicker');

// When size is submitted by the user, call makeGrid()
sizePicker.submit(function (event) {
  event.preventDefault();
  makeGrid(inputWidth, inputHeight);
});

// Your code goes here!
function makeGrid(inputWidth, inputHeight) {
  for (var x = 1; x<=inputWidth; x++) {
    var row = pixelCanvas.insertRow(-1);
    for (var y = 1; y<=inputHeight; y++) {
      var cell = row.insertCell(-1);
    }
  }
}

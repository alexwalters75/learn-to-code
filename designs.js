// Select color input
var colorPicker = document.getElementById('colorPicker');

// Select size input
var inputWidth = document.getElementById('inputWidth');       // create a variable for the width
var inputHeight = document.getElementById('inputHeight');     // create a variable for the height
var pixelCanvas = document.getElementById('pixelCanvas');
var sizePicker = document.getElementById('sizePicker');

// When size is submitted by the user, call makeGrid()

sizePicker.addEventListener('submit', function (event) {    // create an event listener when user clicks 'submit'
  event.preventDefault();
  makeGrid(inputWidth.value, inputHeight.value);            // call the makeGrid function
});

// Your code goes here!
function makeGrid(inputWidth, inputHeight) {    // define the makeGrid function
  pixelCanvas.innerText="";                     // empty the grid
  for (var y = 1; y<=inputHeight; y++) {
    var row = pixelCanvas.insertRow(-1);        // insert n rows where n = Grid Height
    for (var x = 1; x<=inputWidth; x++) {
      var cell = row.insertCell(-1);            // insert n cells where n = Grid Width
      cell.addEventListener('click', function(event) {        // fill the cell with the value of the color selected
        event.target.style.backgroundColor = colorPicker.value
      });
    }
  }
}

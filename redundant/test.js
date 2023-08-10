/*
let fileContents;

fetch('imageFile.txt')
  .then(response => response.text())
  .then(text => {
    fileContents = text;
    // You can perform further operations with the file contents here
    console.log(fileContents);
  })
  .catch(error => {
    // Handle any errors that occurred during the fetch
    console.error('Error:', error);
  });
  */

  /*
  const fs = require('fs');

  fs.readFile('/path/to/file.txt', 'utf8', (err, data) => {
    if (err) {
      console.error('Error:', err);
      return;
    }
    
    // File contents are available in the 'data' variable
    const fileContents = data;
    
    // You can perform further operations with the file contents here
    console.log(fileContents);
  });

  console.log(fileContents);
  */

const fs = require('fs');

function readFileWithCallback(filePath, callback) {
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      console.error('Error:', err);
      return;
    }

    callback(data);
  });
}

var str = ""

// Usage:
readFileWithCallback('imageFile.txt', fileContents => {
  // You can use the fileContents variable here
  //console.log(fileContents);
  str = fileContents;
});

console.log(str);

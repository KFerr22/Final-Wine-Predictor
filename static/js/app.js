// from data.js
var tableData = data;
// Select the buttons
var button = d3.select("#button");
var button2 = d3.select("#button2");

// Select the form
var form = d3.select("#form");

// Create event handlers 
button.on("click", run_prediction);


//When the winemaker enters all the characteristics of their new wine call this function to get a quality vlaue
//************************************************ */
function run_prediction() {
//************************************************ */
var fixed_acidity = d3.select("#fixed_acidity");
var fixed_acidity_value = fixed_acidity.property("value");
console.log("fixed_acidity_value", fixed_acidity_value)

var volatile_acidity = d3.select("#volatile_acidity");
var volatile_acidity_value = volatile_acidity.property("value");
console.log("volatile_acidity", volatile_acidity_value)

var citric_acid = d3.select("#citric_acid");
var citric_acid_value = citric_acid.property("value");
console.log("citric_acid_value", citric_acid_value)

var residual_sugar = d3.select("#residual_sugar");
var residual_sugar_value = residual_sugar.property("value");
console.log("residual_sugar_value", residual_sugar_value)

var chlorides = d3.select("#chlorides");
var chlorides_value = chlorides.property("value");
console.log("chlorides_value", chlorides_value)

var total_sulfur_dioxide = d3.select("#total_sulfur_dioxide");
var total_sulfur_dioxide_value = total_sulfur_dioxide.property("value");
console.log("total_sulfur_dioxide_value", total_sulfur_dioxide_value)

var free_sulfur_dioxide = d3.select("#free_sulfur_dioxide");
var free_sulfur_dioxide_value = free_sulfur_dioxide.property("value");
console.log("free_sulfur_dioxide_value", free_sulfur_dioxide_value)

var density = d3.select("#density");
var density_value = density.property("value");
console.log("density_value", density_value)

var pH = d3.select("#pH");
var pH_value = pH.property("value");
console.log("pH_value", pH_value)

var sulphates = d3.select("#sulphates");
var sulphates_value = sulphates.property("value");
console.log("sulphates_value", sulphates_value)

var alcohol = d3.select("#alcohol");
var alcohol_value = alcohol.property("value");
console.log("alcohol_value", alcohol_value)

var csv = [fixed_acidity_value, volatile_acidity_value,citric_acid_value,residual_sugar_value,total_sulfur_dioxide_value,free_sulfur_dioxide_value,density_value,pH_value,sulphates_value,alcohol_value]
console.log(csv)
 }
// Allow user to see all the value_ranges when on page load
//************************************************ */
function showallcharacterictics() {
//************************************************ */
console.log('showallcharacteristics')
  // Prevent the page from refreshing
  //d3.event.preventDefault();
   
console.log(tableData);   //debug to check what data is retrieved

  // Use D3 to select the table body
  var tbody = d3.select("tbody");

// Use D3 to select the table
  var table = d3.select("table");

// Use D3 to set the table class to `table table-striped`
  table.attr("class", "table table-striped");
  tableData.forEach(({characteristic,min,max}) => {
        
    // Append one table row per sighting
    var row = tbody.append("tr");
  
    // append one cell for each of the sighting attributes
    row.append("td").text(characteristic);
    row.append("td").text(min);
    row.append("td").text(max);
  });
};
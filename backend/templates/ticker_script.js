$(document).ready(function() {
    // Display buffering page for 0.5 seconds
    setTimeout(function() {
        $('#cardContainer').fadeIn();
    }, 500);
    
    // Show the textarea after buffer ends
    setTimeout(function() {
        $('.hidden-textarea').fadeIn();
    }, 1000); // Adjust the delay time as needed
});
// Function to display data for the selected ticker
function displayData() {
    var selectedTicker = document.getElementById("ticker").value; // Get the selected ticker value
    var tickerDataDiv = document.getElementById("tickerData"); // Get the div where data will be displayed

    // Display selected company's data
    var dataHTML = `
        <div class="tickerCard">
            <div class="tickerLogo">
                <img src="${getLogoURL(selectedTicker)}" alt="${selectedTicker} Logo" class="logoImage">
            </div>
            <div class="tickerInfo">
                <h2 class="tickerName">${selectedTicker}</h2>
                <div class="tickerPlot">
                    <img src="${getImageURL(selectedTicker)}" alt="${selectedTicker} Plot" class="plotImage">
                </div>
                <div class="tickerTextData">
                    <p>${getTextData(selectedTicker)}</p>
                </div>
            </div>
        </div>
    `;

    tickerDataDiv.innerHTML = dataHTML; // Update the div with the data HTML
    tickerDataDiv.style.display = "flex"; // Show the tickerDataContainer
}

document.getElementById("tickerData").style.display = "block";
document.getElementById("textDataTextarea").style.display = "block";


// Function to fetch and return text data for the selected ticker
function getTextData(ticker) {
    // Assuming you're using jQuery for simplicity
    $.ajax({
        url: "../Display/" + ticker.replace(/\s+/g, '_') + ".txt",
        success: function(data) {
            // Assuming you have a textarea with id "textDataTextarea"
            $("#textDataTextarea").val(data); // Set the fetched text data in the textarea
        },
        error: function(xhr, status, error) {
            console.log("Error fetching text data:", error);
        }
    });
}


// Function to get the logo image URL for the selected ticker
function getLogoURL(ticker) {
    // Update the file path based on the selected ticker
    return "../Display/" + ticker.replace(/\s+/g, '_') + "_logo.png";
}

// Function to get the plot image URL for the selected ticker
function getImageURL(ticker) {
    // Update the file path based on the selected ticker
    return "../Display/" + ticker.replace(/\s+/g, '_') + "_plot.jpeg";
}

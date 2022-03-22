var sliderIndex = 0;
showSlides();

function showSlides() {
  var i;
  var slides = document.getElementsByClassName("slide");     //get slides items
  let indicators = document.getElementsByClassName("indicator");    //get indicators
  
  //slides display order
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";   //disable slides
  }
  sliderIndex++;
  if (sliderIndex > slides.length) {sliderIndex = 1}    
  for (i = 0; i < indicators.length; i++) {
    indicators[i].className = indicators[i].className.replace(" active-indicator", "");
  }
  slides[sliderIndex-1].style.display = "block";     //display slides

  indicators[sliderIndex-1].className += " active-indicator";
  setTimeout(showSlides, 5000); // Change image every 5 seconds
}
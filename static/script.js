// Initialize Swiper
var swiper = new Swiper('.swiper-container', {
    loop: true,
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
  });
  
  // Background selection
  var backgroundSelect = document.getElementById('background-select');
  if (backgroundSelect) {
    backgroundSelect.addEventListener('change', function() {
      var backgroundId = this.value;
      var slides = document.querySelectorAll('.swiper-slide img');
      slides.forEach(function(img) {
        var imageFilename = img.getAttribute('data-image');
        img.src = '/combined_image/' + encodeURIComponent(imageFilename) + '/' + backgroundId;
      });
    });
  }
  
let currentImageIndex = 0;
const images = document.querySelectorAll('.slider-image');
const intervalTime = 5000; 
function showImage(index) {
  images.forEach(img => img.style.display = 'none');
  images[index].style.display = 'block';
}

function nextImage() {
  currentImageIndex = (currentImageIndex + 1) % images.length;
  showImage(currentImageIndex);
}

function prevImage() {
  currentImageIndex = (currentImageIndex - 1 + images.length) % images.length;
  showImage(currentImageIndex);
}

function startSlider() {
  setInterval(nextImage, intervalTime);
}

startSlider(); 

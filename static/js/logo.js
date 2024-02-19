function load_image() {
    fetch('/get_store_image')
        .then(response => response.blob())
        .then(blob => {
            // Create a URL for the blob data and set it as the image source
            const imageUrl = URL.createObjectURL(blob);
            document.getElementById('image').src = imageUrl;
        })
        .catch(error => console.error('Error:', error));
}

load_image();

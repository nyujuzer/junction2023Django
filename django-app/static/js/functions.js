const readFile = () => {
  const fileInput = document.getElementById("video_file");
  const videoDisplay = document.getElementById("fileContainer");
  const allowed_exts = ["mp4"];
  // Check if a file is selected
  if (fileInput.files.length > 0) {
    const file = fileInput.files[0];
    const ext = file.name.split(".")[1]
    if (allowed_exts.includes(ext)) {
      const reader = new FileReader();

      // Read the content of the file
      reader.onload = (event) => {
        const content = event.target.result;
        videoDisplay.src = content;
        videoDisplay.load();
      };

      // Handle errors during file reading
      reader.onerror = (event) => {
        console.error("Error reading the file:", event.target.error);
      };

      // Start reading the file as a data URL
      reader.readAsDataURL(file);
    } else{
    alert("We don't support that file extention")
    fileInput.value = ""
  }
}else {
      // Reset the video display if no file is selected
      videoDisplay.src = "";
    }
  
};

document.getElementById("video_file").addEventListener("change", function (e) {
  readFile(e.target);
});

const diseaseInfo = {
    'Early blight': 'Fungal disease causing dark brown spots with concentric rings on leaves. Can lead to defoliation and reduced yields.',
    'Late blight': 'Severe fungal disease causing large, dark brown patches on leaves and stems. Can destroy entire crops in favorable conditions.',
    'Yellow Leaf Curl Virus': 'Viral disease transmitted by whiteflies causing yellowing and curling of leaves, stunted growth, and significant yield loss.',
    'Healthy': 'Plant shows normal growth patterns with no visible signs of disease. Leaves are green and properly developed.',
};

document.getElementById("uploadForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const fileInput = document.getElementById("fileInput");
    const file = fileInput.files[0];

    if (!file) {
        alert("Please select a file first!");
        return;
    }

    // Show image preview
    const imagePreview = document.getElementById("imagePreview");
    const predictionResult = document.getElementById("predictionResult");

    imagePreview.innerHTML = ''; // Clear previous preview
    const img = document.createElement("img");
    img.src = URL.createObjectURL(file);
    imagePreview.appendChild(img);
    predictionResult.classList.remove("hidden");

    const formData = new FormData();
    formData.append("file", file);

    try {
        const response = await fetch("/predict", {
            method: "POST",
            body: formData,
        });

        if (!response.ok) {
            const errorText = await response.text();
            throw new Error(`Failed to get prediction: ${errorText}`);
        }

        const result = await response.json();
        
        if (result.error) {
            throw new Error(result.error);
        }

        // Update prediction result
        document.getElementById("prediction").innerText = `Class: ${result.class}`;
        const tooltipText = document.querySelector('.tooltip-text');
        tooltipText.textContent = diseaseInfo[result.class] || 'No information available for this class';
        const confidenceBar = document.getElementById("confidenceBar");
        confidenceBar.style.width = `${result.confidence * 100}%`;
        confidenceBar.textContent = `${(result.confidence * 100).toFixed(1)}%`;
    } catch (error) {
        console.error("Error:", error);
        alert("Error: " + error.message);
    }
});

// Preview image when file is selected
document.getElementById("fileInput").addEventListener("change", (e) => {
    const file = e.target.files[0];
    if (file) {
        const imagePreview = document.getElementById("imagePreview");
        const predictionResult = document.getElementById("predictionResult")

        imagePreview.innerHTML = '';
        const img = document.createElement("img");
        img.src = URL.createObjectURL(file);
        imagePreview.appendChild(img);
        imagePreview.classList.remove("hidden");
        predictionResult.classList.add("hidden")
    }
});

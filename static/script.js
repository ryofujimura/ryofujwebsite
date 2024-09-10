// Function to show the preview in the center horizontally at the height of the hovered link
function showPreview(event, projectId) {
    const previewContainer = document.getElementById('preview-' + projectId);
    previewContainer.style.display = 'block';

    // Calculate the center position for the preview container horizontally
    const windowWidth = window.innerWidth;
    const previewWidth = previewContainer.offsetWidth;
    const centerX = (windowWidth - previewWidth) / 2;

    // Position the preview container at the same height as the hovered link
    const rect = event.target.getBoundingClientRect();
    const linkTop = rect.top + window.scrollY; // Vertical position of the hovered link

    // Set the position of the preview container
    previewContainer.style.top = `${linkTop}px`;
    previewContainer.style.left = `${centerX + window.scrollX}px`;

    // Load preview content dynamically if needed
    previewContainer.innerHTML = `
        <h3>Project Title: ${projectId}</h3>
        <p>Some sneak peek content for the project...</p>
    `; // Replace this with actual content or make an AJAX call to fetch content dynamically

    // Add mouseover and mouseout event listeners to the preview to keep it visible
    previewContainer.addEventListener('mouseover', () => {
        previewContainer.style.display = 'block';
    });

    previewContainer.addEventListener('mouseout', () => {
        previewContainer.style.display = 'none';
    });
}

// Function to hide the preview when the mouse moves away from the link or preview
function hidePreview(event) {
    const previewContainers = document.querySelectorAll('.preview-container');
    previewContainers.forEach(container => {
        container.style.display = 'none';
    });
}

// Attach event listeners for hover to each project link
document.addEventListener('DOMContentLoaded', function() {
    const projectLinks = document.querySelectorAll('.project-link');

    projectLinks.forEach(link => {
        const projectId = link.getAttribute('href').split('project_id=')[1]; // Extract project ID from URL
        link.addEventListener('mouseover', (event) => showPreview(event, projectId));
        link.addEventListener('mouseout', hidePreview);
    });
});

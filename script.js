function updateTime() {
    var timeText = document.querySelector("#timeElement");
    if (timeText) {
        timeText.innerHTML = new Date().toLocaleString();
    }
}
updateTime();

setInterval(updateTime, 1000);

// Set initial position after DOM load
document.addEventListener("DOMContentLoaded", () => {
    const welcomeDiv = document.getElementById("welcome");
    welcomeDiv.style.left = "50%";
    welcomeDiv.style.top = "50%";
    welcomeDiv.style.transform = "translate(-50%, -50%)";
});

// Initialize dragging on the correct element
dragElement(document.getElementById("welcome"));

function dragElement(element) {
    let pos1 = 0,
        pos2 = 0,
        pos3 = 0,
        pos4 = 0;

    // Use the header element for dragging
    const header = document.getElementById(element.id + "header");
    if (header) {
        header.onmousedown = dragMouseDown;
    } else {
        element.onmousedown = dragMouseDown;
    }

    function dragMouseDown(e) {
        e = e || window.event;
        e.preventDefault();

        // Get initial mouse position
        pos3 = e.clientX;
        pos4 = e.clientY;

        // Store initial element position
        const rect = element.getBoundingClientRect();
        pos1 = rect.left;
        pos2 = rect.top;

        // Remove centering transform
        element.style.transform = "none";

        document.onmouseup = closeDragElement;
        document.onmousemove = elementDrag;
    }

    function elementDrag(e) {
        e = e || window.event;
        e.preventDefault();

        // Calculate new position
        const newX = pos1 + (e.clientX - pos3);
        const newY = pos2 + (e.clientY - pos4);

        // Set new position
        element.style.left = newX + "px";
        element.style.top = newY + "px";
    }

    function closeDragElement() {
        document.onmouseup = null;
        document.onmousemove = null;
    }
}

var welcomeScreen = document.querySelector("#welcome");

function closeWindow(element) {
    element.style.display = "none";
}

function openWindow(element) {
    element.style.display = "flex";
}

var welcomeScreenClose = document.querySelector("#welcomeclose");

var welcomeScreenOpen = document.querySelector("#welcomeopen");

welcomeScreenClose.addEventListener("click", function () {
    closeWindow(welcomeScreen);
});

welcomeScreenOpen.addEventListener("click", function () {
    openWindow(welcomeScreen);
});

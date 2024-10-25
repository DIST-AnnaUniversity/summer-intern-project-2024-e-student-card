<script>
    document.addEventListener('DOMContentLoaded', () => {
        if (window.history.replaceState) {
            window.history.replaceState(null, null, window.location.href);
        }
    });

    function changeButtonContent() {
        var button = document.getElementById("unlockButton");
        // Change the content of the button and its color
        if (button.innerText === "Click to Unlock") {
            button.innerText = "Unlocked";
            button.style.backgroundColor = "green"; // Set the button color to green
        } else {
            button.innerText = "Click to Unlock";
            button.style.backgroundColor = ""; // Reset to original color
        }
    }

    function changeFreezeButtonContent() {
        var button = document.getElementById("freezebutton");

        // Show confirmation alert
        var confirmAction = confirm("Are you sure you want to AUTHORIZE?");

        if (confirmAction) {
            // If user confirms, change content and color
            button.innerText = "AUTHORIZED";
            button.style.backgroundColor = "green"; // Set the button color to green

//            // Delay reload to allow user to see the change
//            setTimeout(() => {
//                location.reload(true);
//            }, 1000);  // 1 second delay before page reload
        }
    }

    function refresh() {
        location.reload(true);
    }
</script>



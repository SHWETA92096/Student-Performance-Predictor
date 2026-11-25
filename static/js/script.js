
// Fill the form with sample student information
const sampleButton = document.getElementById("sampleButton");

sampleButton.addEventListener("click", function () {
    document.getElementById("study_hours").value = 6;
    document.getElementById("attendance").value = 75;
    document.getElementById("previous_marks").value = 60;
});

// Validate the form before submission
const predictionForm = document.getElementById("predictionForm");

predictionForm.addEventListener("submit", function (event) {

    const studyHours = Number(
        document.getElementById("study_hours").value
    );

    const attendance = Number(
        document.getElementById("attendance").value
    );

    const previousMarks = Number(
        document.getElementById("previous_marks").value
    );

    if (
        studyHours < 0 || studyHours > 24 ||
        attendance < 0 || attendance > 100 ||
        previousMarks < 0 || previousMarks > 100
    ) {
        event.preventDefault();
        alert("Please enter valid academic information.");
    }
});

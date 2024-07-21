// Function to create member fields dynamically
function createMemberFields(numMembers) {
    const membersContainer = document.getElementById('membersContainer');
    membersContainer.innerHTML = ''; // Clear previous fields

    for (let i = 1; i <= numMembers; i++) {
        const memberBox = document.createElement('div');
        memberBox.classList.add('member-box');

        const memberHeading = document.createElement('div');
        memberHeading.classList.add('member-heading');
        memberHeading.textContent = `Member ${i}`;
        memberBox.appendChild(memberHeading);

        const nameLabel = document.createElement('label');
        nameLabel.textContent = `Name:`;
        memberBox.appendChild(nameLabel);

        const nameInput = document.createElement('input');
        nameInput.type = 'text';
        nameInput.name = `member${i}Name`;
        nameInput.required = true;
        memberBox.appendChild(nameInput);

        const collegeLabel = document.createElement('label');
        collegeLabel.textContent = `College:`;
        memberBox.appendChild(collegeLabel);

        const collegeInput = document.createElement('input');
        collegeInput.type = 'text';
        collegeInput.name = `member${i}College`;
        collegeInput.required = true;
        memberBox.appendChild(collegeInput);

        membersContainer.appendChild(memberBox);
    }
}

// Add event listener to the form submission
document.getElementById('registrationForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const teamName = document.getElementById('teamName').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const numMembers = document.querySelectorAll('#membersContainer .member-box').length;
    let members = [];

    if (!/^\d{10}$/.test(phone)) {
        alert('Please enter a valid 10-digit phone number.');
        return;
    }

    for (let i = 1; i <= numMembers; i++) {
        const memberName = document.querySelector(`input[name="member${i}Name"]`).value;
        const memberCollege = document.querySelector(`input[name="member${i}College"]`).value;
        members.push({ name: memberName, college: memberCollege });
    }

    if (teamName && email && phone && numMembers && members.length === parseInt(numMembers)) {
        // Process registration (e.g., send data to a server)

        // Show success message
        document.getElementById('successMessage').classList.remove('hidden');

        // Reset the form
        document.getElementById('registrationForm').reset();
        document.getElementById('membersContainer').innerHTML = '';
    } else {
        alert('Please fill in all fields.');
    }
});

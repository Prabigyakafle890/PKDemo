function hideAllPopups() {
  document.querySelectorAll('.popup').forEach(p => p.style.display = 'none');
}

function openGuest() {
  hideAllPopups();
  document.getElementById('guest-popup').style.display = 'block';
}

function openInstitutional() {
  hideAllPopups();
  document.getElementById('institutional-role').style.display = 'block';
}

function selectInstitutionalRole(role) {
  hideAllPopups();
  document.getElementById('institutional-login').style.display = 'block';
}

function goToDepartment() {
  const email = document.getElementById('institutional-email').value;
  if (!email.endsWith("@college.edu.np")) {
    alert("Please use your official institutional email.");
    return;
  }
  hideAllPopups();
  document.getElementById('department-select').style.display = 'block';
}

function continueToChatbot() {
  hideAllPopups();
  document.getElementById('chatbot-page').style.display = 'block';
}

function goHome() {
  hideAllPopups();
  document.getElementById('landing-page').style.display = 'block';
}

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


function toggleDepartment() {
  const userType = document.getElementById('user-type').value;
  const deptInput = document.getElementById('department');
  deptInput.style.display = userType === 'student' ? 'inline-block' : 'none';
}

function sendMessage() {
  const userInput = document.getElementById('user-input');
  const message = userInput.value.trim();
  const userType = document.getElementById('user-type').value;
  const department = document.getElementById('department').value.trim();
  const chatArea = document.getElementById('chat-area');

  if (message === '') return;

  // Show user's message
  const userMsg = document.createElement('div');
  userMsg.className = 'user-message';
  userMsg.textContent = "You: " + message;
  chatArea.appendChild(userMsg);

  // Send to backend
  fetch('http://127.0.0.1:5000/chat', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      message: message,
      user_type: userType,
      department: department
    })
  })
    .then(response => response.json())
    .then(data => {
      const botMsg = document.createElement('div');
      botMsg.className = 'bot-message';
      botMsg.textContent = "Bot: " + data.response;
      chatArea.appendChild(botMsg);
      chatArea.scrollTop = chatArea.scrollHeight;
    })
    .catch(error => {
      console.error('Error:', error);
    });

  userInput.value = '';
}

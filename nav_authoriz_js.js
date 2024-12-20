fetch('nav_authorization.html')
.then(response => response.text())
.then(navigation => document.getElementById('navbar_authoriz').innerHTML = navigation);
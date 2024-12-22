fetch('navigation.html')
.then(response => response.text())
.then(navigation => document.getElementById('navbar').innerHTML = navigation);
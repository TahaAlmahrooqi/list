var xhr = new XMLHttpRequest();
xhr.open("GET", "file.php");
xhr.send();

xhr.onreadystatechange = function() {
if (xhr.readyState === 4 && xhr.status === 200) {
	var content = xhr.responseText;
	document.getElementById("content").innerHTML = content;
	}
};



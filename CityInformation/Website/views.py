from django.shortcuts import render
from django.http import HttpResponse

# Home Page
def index(request):
    return HttpResponse("""<html>
	<head>
		<link rel="stylesheet" type="text/css" href="style.css">
	</head>
	<body>
		<div id="wrapper">
			<div id="title">
			<img src="http://www.adstockglobal.com/wp-content/uploads/2016/02/City-Info.png">
			</div>
			<div id="regologin">
				<input type="submit" value="Register">
				<input type="submit" value="Login">
			</div>
			<div id="main">
			I AM THE MAIN THINGO
			</div>
		</div>
	
	
	</body>


</html>

 """)

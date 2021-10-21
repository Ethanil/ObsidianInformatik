import fetch from 'node-fetch'
//async function to handle data fetching
async function getData () {
	//try catch block to handle promises and errors
	try {
		const calendarId ='n06fb7tj201kr2v8bkgg6irp9k@group.calendar.google.com'
		const myKey = 'AIzaSyCbd-KIxslp5wBams5m-yyplG63SL8Zlvw'
		//using await and fetch together as two standard ES6 client side features to extract the data
		let apiCall = await fetch('https://www.googleapis.com/calendar/v3/calendars/' + calendarId+ '/events?key=' + myKey)
		//response.json() is a method on the Response object that lets you extract a JSON object from the response
		//response.json() returns a promise resolved to a JSON object
		let apiResponse = await apiCall.json()
		console.log(apiResponse)
	} catch (error) {
	console.log(error)
	}
}
getData()

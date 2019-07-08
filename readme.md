## Ok ... I needed to figure out how to re-format Adobe Sign related "form data"

Adobe Sign returns "form data" as a csv formatted string.  This is really a problem for use in things like MS flow, zappier, ifttt, nintex and other workflow platforms. 

Soooo since I'm a huge fan of python and open source, I wrote this GCP Function to use the API token(oAuth or integration key), the "shard"(geolocation), the sender's email address, and the API related agreement ID to get the csv data and convert it to JSON.  It then returns this JSON which can be used by most of these workflow platforms.

#### The setup

Open a GCP Account.  Create a new function and set it up something like this:
![Setup Screen-Shot](https://www.evernote.com/shard/s517/sh/5fc307f9-b24e-4d8c-a494-f660c543862a/65be11a295780c42/res/140c36ab-0e6a-4544-beb1-9799a2675a44/skitch.png)

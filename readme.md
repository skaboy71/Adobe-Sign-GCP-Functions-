## Ok ... I needed to figure out how to re-format Adobe Sign related "form data"

Adobe Sign returns "form data" as a csv formatted string.  This is really a problem for use in things like MS flow, zappier, ifttt, nintex and other workflow platforms. 

Soooo since I'm a huge fan of python and open source, I wrote this GCP Function to use the API token(oAuth or integration key), the "shard"(geolocation), the sender's email address, and the API related agreement ID to get the csv data and convert it to JSON.  It then returns this JSON which can be used by most of these workflow platforms.

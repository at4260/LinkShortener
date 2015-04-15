# LinkShortener
Link shortener like bitly
Input link to shorten or input shortened link to access.

Getting Set Up
---
Create and activate a new, empty virtual environment.

`virtualenv env`
`source env/bin/activate`

Use pip to install the packages required in requirements.txt.

`pip install -r requirements.txt`

Start the application by running controller.py.
Navigate to http://localhost:5000 and start exploring the app.

(The following are notes from Chris Palmer.)
To Shorten A URL
---
Given a request to shorten a long URL called url:

Validate it. To validate it, call urlparse.urlparse(url) and ensure that the returned object has a valid scheme (http or https, no others) and a valid hostname (not localhost or other private name; not a private IP address like those in the RFC 1918 space like 192.168/16). Also reject URLs that are longer than some reasonable maximum, like 512 bytes.

Shorten it. Take a cryptographic hash of the URL with hashlib.sha256(url).digest(), truncate the digest byte-string to more than 10 but fewer than 17 bytes (see below for why) then encode the truncated digest byte-string somehow (hexadecimal, base-64, human-readable base-32, or the like). Call the result shortened.

Check for duplicates. Store all shortened -> url mappings in a dictionary called shortened_urls. Check if shortened is in the dictionary already; if so, check the value to see if we have found a hash collision. If not (as is likely), simply return the value.

Store and return the new shortened URL. If it was not a duplicate, set shortened_urls[shortened] = url, and then also database_file.write("%s%s\n" % (shortened, url)). (See below.) Return "https://foo.ly/%s" % (shortened).

To Retrieve A Long URL
---
Given a request to resolve a shortened URL into the corresponding long URL:

Extract the shortened ID from the request. Assuming the path part is the ID as in step 4 above, just take the path. Check that it is the right length, given the encoding scheme in step 2 above. If it's not the right length, fail.

Return the long URL, or 404. return shortened_urls[shortened].

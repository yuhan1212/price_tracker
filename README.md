# eBay Price Tracking

This program will automatically track the chosen product price,<br/>
and send an email to alert user when the latest price meets the target price.

### Features

* Scraped information from product page using BeautifulSoup and Requests libraries.
* Created price converter function and time interval setting, automated price checking system.
* Extracted pricing data and automatically sent customized notification email using smtplib module.

### Requirements

To automatically send and email, we need one of the following to be done:

* Allow Less Secure Apps to Access Your Gmail Account
* Enable Two-Factor Authentication, and generate a new app password for Mail
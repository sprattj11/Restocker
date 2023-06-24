# Jason Spratt
This is a python script to email me when the Ninja Creami product has come in stock.
It parses the html code div "product-availability ng-star-inserted", this class's text contains the stock status.
If the stock status is not "Out of Stock", it will send me an email with the link to the product.
It runs every 30 minutes via crontab job scheduler.
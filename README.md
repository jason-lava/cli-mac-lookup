# cli-mac-lookup

Here is a handy CLI tool to find the company manufacturer for any mac address. All you have to do is download, run a quick one-liner in the CLI, and hit enter. 

# Pre-requisites:
* you have python3 installed > 
    * sudo apt install python3
    * confirm version with >
    * python3 --version

# How To Use:
In the command line, type:
* python3 mac-lookup.py [paste mac address here without brackets]

# How It's Made:
Tech used:

* Python3
* CLI

This CLI tool was made to quickly look up any mac-address manufacturer. I added the argument section so you can lookup direct from cli. The program then pings a website with your mac address, reads/decodes the content, finds the web section for the manufacturer/company, and finally prints it to you.

# Lessons Learned:

No one method fits every bill. Scraping the data from JS was not going to work, Java too cumbersome, but attacking with Python proved to be the best tool for the job.
I enjoyed being able to use Python versus trying to make another Language work. 

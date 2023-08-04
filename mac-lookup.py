import sys
from urllib.request import urlopen

macAddress = sys.argv[1]

url = "https://www.ipchecktool.com/tool/macfinder?oui={}".format(macAddress)
page = urlopen(url)
htmlContent = page.read().decode("utf-8")

startIndex = htmlContent.find("<th>Vendor:</th>") + len("<th>Vendor:</th><td>") + 1
endIndex = htmlContent.find("<th>Address:</th>") - len("<th>Address:</th>")

company = htmlContent[startIndex:endIndex]

print(company)

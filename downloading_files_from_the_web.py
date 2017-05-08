from urllib import request

real_estate_url = 'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'

def download_real_estate_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'real_estate.csv'
    fx = open(dest_url, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_real_estate_data(real_estate_url)
from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/get_price/<product_name>')
def get_price(product_name):
    """run command: scrapy crawl command with -o -a options
    the output.json is read and displayed on http://localhost:5000/<product_name>
    """
    spider_name = 'price'
    # calls 'scrapy' as a subprocess
    subprocess.check_output(['scrapy', 'crawl', spider_name,
                             "-o", "output.json",
                             "-a", "product_name=" + product_name])

    # read output.json
    with open("output.json") as items_file:
        return items_file.read()


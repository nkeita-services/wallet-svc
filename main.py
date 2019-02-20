from flask import Flask, send_from_directory
import swagger
import logging

app = Flask(__name__)
app.config.from_envvar('APP_SETTINGS')

app.register_blueprint(swagger.swaggerui_blueprint, url_prefix=swagger.SWAGGER_URL)

handler = logging.FileHandler('app.log')
handler.setLevel(logging.ERROR)
app.logger.addHandler(handler)


@app.route('/docs/<file_name>')
def send_doc(file_name):
    return send_from_directory(
        'docs',
        file_name
    )

from flask import Flask, request, abort
import json
from regex import framework_detector
from framework_data import languages
app = Flask(__name__)



@app.route('/', methods=['POST'])
def hello_world():
    if request.method == 'POST':

        a = request.get_json()

        code_string = a['line']
        filename = a['filename']

        if ".py" in filename:
            framework_detector(code_string)

        # elif ".java" in filename:
        #
        #
        # elif ".scala" in filename:
        #
        #
        # elif ".cpp" in filename:
        #
        #
        # elif ".rb" in filename:
        #
        #
        # elif ".rb" in filename:
        #
        #
        # elif ".go" in filename:
        #
        #
        # elif ".php" in filename:
        #
        #
        # elif ".swift" in filename:
        #
        #
        # elif ".kt" in filename:

        else:
            abort(404)


    return json.dumps('ok', ensure_ascii=False)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)










from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import logging
import sys
from app import *
from config import *

app = Flask(__name__)
CORS(app)

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/api/embed', methods=['GET'])
def createEmbed():
    if request.method == "GET":
        if not is_dir_empty(f"{UPLOAD_FILE_PATH}"):
            load_index()
            return jsonify({'status':'OK','message':'Created embeddings successfully!'}),200
        else:
            return jsonify({'status':'Error','message':'No documents found to create embeddings, Please upload and invoke this method'}),200



@app.route('/api/upload', methods=['POST'])
def upload():
    if request.method == "POST":
        files = request.files.getlist("file")
        for file in files:
            file.save(os.path.join(f"{UPLOAD_FILE_PATH}", file.filename))
    return jsonify({'status':'OK','message':'File(s) uploaded successfully!'}),200

@app.route('/api/question', methods=['POST'])
def post_question():
    json = request.get_json(silent=True)
    question = json['question']
    user_id = json['user_id']
    logging.info("post question `%s` for user `%s`", question, user_id)
    if not is_dir_empty(f"{UPLOAD_FILE_PATH}"):
        resp = chat(question, user_id)
        data = jsonify({'answer':resp})
        return data, 200

if __name__ == '__main__':
    init_llm()
    init_index()
    if not is_dir_empty(f"{INDEX_STORAGE_PATH}"):
        init_query_engine()
    else:
        logging.info("No index available, skipping inti_engine_query() initialization")

    app.run(host='0.0.0.0', port=HTTP_PORT, debug=False)
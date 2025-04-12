## We will develop a Document Summarization application leveraging an Advanced RAG pipeline, using embedding models, Large Language Models (LLMs), post-processing techniques, and re-ranking models.
### Advanced RAG Pipeline
<img width="1262" alt="Screenshot 2025-04-12 at 6 38 42 PM" src="https://github.com/user-attachments/assets/bce82b9d-8314-400a-a415-8df9d491cac5" />

- #### Step1: RAG - Retrieval Aguemented Generation
  ##### Get familiar with RAG (Retrieval Augmented Generation) and its applications. This article covers the fundamentals of Basic RAG and delves into Advanced RAG techniques: https://ekluvtech.com/2025/03/16/rag-retrieval-agumented-generation/
- #### Step2: Setup Ollama and Qdrant
  ##### In this setup, LLM model and Embedding model will be run using Ollama ecosystem. These models will help in creating embeddings and final response from the users.
- #### Step3: Project Setup
  - ##### Since we’re using PyTorch dependencies, which currently support Python up to version 3.10, please ensure you’re using a compatible version. If you’re using a higher version, set up your environment with Python 3.10 using the following command
        python3.10 -m venv docusum                  
        source docusum/bin/activate
  - ##### Install the dependencies using the following command
        pip install -r requirements.txt 
  - ##### Before running app.py, ensure that the LLM and Embed Model are running in the Ollama ecosystem and that the Qdrant vector store is set up, configure all the parameters in the config.py
        python api.py
  - ##### If you encounter issues with requirements.txt, run the following commands to uninstall dependencies and install all the dependencies manually.
        #Uninstall all the dependencies
        pip uninstall -r requirements.txt

        #install dependencies
        pip install flask-cors
        pip install tiktoken
        pip install unstructured
        pip install Flask==2.0.1
        pip install llama-index
        pip install llama-index-vector-stores-qdrant
        pip install llama-index-llms-ollama
        pip install llama-index-embeddings-ollama
        pip install torch sentence-transformers
        pip install qdrant-client
        pip install Werkzeug==2.2.2
  - ##### Output after successful execution
  - <img width="1653" alt="Screenshot 2025-04-12 at 6 45 05 PM" src="https://github.com/user-attachments/assets/c3b1ae06-c3fa-499c-8458-fc95fb8354a4" />
  - #### The server will run on http://localhost:7654
  - #### The available APIs are
  - #### **/api/upload**: Please upload documents to the 'docs' folder
        
        curl --location 'http://localhost:7654/api/upload' \
        --form 'file=@"/path/to/file"'
    
  - #### <img width="735" alt="Screenshot 2025-04-12 at 6 59 53 PM" src="https://github.com/user-attachments/assets/c629befb-6efc-4a99-b58d-69451e1c1535" />

  - #### **/api/embed**: This process will generate embeddings and store them in the Qdrant vector database.
        
        curl --location --request GET 'http://localhost:7654/api/embed' \
        --header 'Content-Type: application/javascript' \
        --data '{
        }'
   - #### <img width="627" alt="Screenshot 2025-04-12 at 6 59 59 PM" src="https://github.com/user-attachments/assets/1ce4ccf5-9f32-493d-a32f-370d6f9f017b" />

  - #### **/api/question**: This will retrieve a response from the LLM (Large Language Model) running on local Ollama.
        
        curl --location 'http://localhost:7654/api/question' \
        --header 'Content-Type: application/json' \
        --data '{
          "question": "List out OWASP top 10 ",
          "user_id": "docusum"
        }'
    
  - #### <img width="628" alt="Screenshot 2025-04-12 at 7 00 08 PM" src="https://github.com/user-attachments/assets/25fae00a-98a5-4328-bca0-fa68710ac5b5" />

  - #### <img width="632" alt="Screenshot 2025-04-12 at 7 00 13 PM" src="https://github.com/user-attachments/assets/df57a1fd-55cb-4bab-80c2-dad0e504ef68" />
  


       

# Privacy.ai - Document Analysis and Q&A System

Privacy.ai is an AI-powered web application that allows users to **upload documents, extract insights, and interact with them via a Q&A system**. Using **FAISS for vector storage** and **Google Generative AI**, this tool enables users to ask questions about their documents and receive AI-generated responses.

## 🚀 Features
- 📂 **Upload Files**: Supports PDF uploads.
- 🧠 **AI-Powered Q&A**: Ask questions and receive responses based on document content.
- 🔍 **Smart Search**: Uses FAISS for efficient document similarity search.
- ⚡ **Google Generative AI**: Provides intelligent and context-aware answers.
- 🎨 **Modern UI**: Built with TailwindCSS for a sleek and responsive design.

---

## 🛠️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/privacy-ai.git
cd privacy-ai
```

### 2️⃣ Create and Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file in the root directory and add:
```ini
GOOGLE_API_KEY=your-google-api-key
```

### 5️⃣ Apply Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Run the Server
```bash
python manage.py runserver
```

The app will be available at: **http://localhost:8000/**

---

## 🔧 Usage Guide

### Uploading Documents
1. Click on **Upload Files**.
2. Select a **PDF** file and submit.
3. The file will be processed, and embeddings will be stored.

### Asking Questions
1. Enter a question in the **Chat with Your Document** section.
2. The system will find relevant document content and generate a response.
3. The AI-generated answer will be displayed instantly.

---

## 🏗️ Project Structure
```
privacy-ai/
# Valentius_DocuCruncher

Valentius_DocuCruncher is an AI-powered web application that enables users to upload documents, extract insights, and interact with them via a Q&A system. Leveraging FAISS for vector storage and Google Generative AI, users can ask questions about their documents and receive intelligent, context-aware responses.

## 🚀 Features
- **📂 Upload Files:** Supports PDF uploads.
- **🧠 AI-Powered Q&A:** Ask questions and receive responses based on document content.
- **🔍 Smart Search:** Uses FAISS for efficient document similarity search.
- **⚡ Google Generative AI:** Provides intelligent and context-aware answers.
- **🎨 Modern UI:** Built with TailwindCSS for a sleek and responsive design.

## 🛠️ Installation

1. **Clone the Repository**
	```sh
	git clone https://github.com/YOUR_GITHUB_USERNAME/privacy-ai.git
	cd privacy-ai
	```
2. **Create and Activate Virtual Environment**
	```sh
	python -m venv venv
	# On macOS/Linux
	source venv/bin/activate
	# On Windows
	venv\Scripts\activate
	```
3. **Install Dependencies**
	```sh
	pip install -r requirements.txt
	```
4. **Set Up Environment Variables**
	- Create a `.env` file in the root directory and add:
	  ```env
	  GOOGLE_API_KEY=your-google-api-key
	  ```
5. **Apply Database Migrations**
	```sh
	python manage.py makemigrations
	python manage.py migrate
	```
6. **Run the Server**
	```sh
	python manage.py runserver
	```
	The app will be available at: [http://localhost:8000/](http://localhost:8000/)

## 🔧 Usage Guide

### Uploading Documents
- Click on **Upload Files**.
- Select a PDF file and submit.
- The file will be processed, and embeddings will be stored.

### Asking Questions
- Enter a question in the **Chat with Your Document** section.
- The system will find relevant document content and generate a response.
- The AI-generated answer will be displayed instantly.

## 🏗️ Project Structure
```
Valentius_DocuCruncher/
├── EULA/
│   └── chatappv1/
│       ├── app1/
│       │   ├── templates/
│       │   │   └── frontend.html
│       │   ├── utils.py
│       │   ├── forms.py
│       │   ├── models.py
│       │   ├── views.py
│       │   ├── urls.py
│       │   └── ...
│       ├── chatappv1/
│       │   ├── settings.py
│       │   ├── urls.py
│       │   └── ...
│       ├── faiss_index/
│       │   ├── index.faiss
│       │   └── index.pkl
│       ├── media/
│       │   └── pdfs/
│       │       └── ...
│       └── manage.py
├── another_eula.docx
├── README.md
└── ...
```

## 🛠️ Troubleshooting

### 1. FAISS index not found
- Ensure you've uploaded a file before asking questions.
- Try deleting `faiss_index/` and re-uploading.

### 2. No AI response or errors in terminal
- Check `.env` for a valid `GOOGLE_API_KEY`.
- Restart the server after setting the API key.

### 3. Django migration issues
- Run:
  ```sh
  python manage.py makemigrations
  python manage.py migrate --run-syncdb
  ```

### 4. ModuleNotFoundError
- Activate your virtual environment.
- Run `pip install -r requirements.txt` to install dependencies.

## 🤝 Contributing
Contributions are welcome! Feel free to fork this repo and submit pull requests.

**To Contribute:**
1. Fork the repository.
2. Create a feature branch:
	```sh
	git checkout -b feature-name
	```
3. Commit changes:
	```sh
	git commit -m "Added new feature"
	```
4. Push to branch:
	```sh
	git push origin feature-name
	```
5. Submit a Pull Request.

## 🌟 Acknowledgments
- Django for backend framework.
- FAISS for efficient vector searching.
- Google Generative AI for text embeddings and Q&A.
- TailwindCSS for styling.



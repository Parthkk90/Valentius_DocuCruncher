# Valentius_DocuCruncher
Privacy.ai is an AI-powered web application that allows users to upload documents, extract insights, and interact with them via a Q&amp;A system. Using FAISS for vector storage and Google Generative AI, this tool enables users to ask questions about their documents and receive AI-generated responses.

🚀 Features
📂 Upload Files: Supports PDF uploads.
🧠 AI-Powered Q&A: Ask questions and receive responses based on document content.
🔍 Smart Search: Uses FAISS for efficient document similarity search.
⚡ Google Generative AI: Provides intelligent and context-aware answers.
🎨 Modern UI: Built with TailwindCSS for a sleek and responsive design.
🛠️ Installation
1️⃣ Clone the Repository
git clone https://github.com/YOUR_GITHUB_USERNAME/privacy-ai.git
cd privacy-ai
2️⃣ Create and Activate Virtual Environment
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Set Up Environment Variables
Create a .env file in the root directory and add:

GOOGLE_API_KEY=your-google-api-key
5️⃣ Apply Database Migrations
python manage.py makemigrations
python manage.py migrate
6️⃣ Run the Server
python manage.py runserver
The app will be available at: http://localhost:8000/

🔧 Usage Guide
Uploading Documents
Click on Upload Files.
Select a PDF file and submit.
The file will be processed, and embeddings will be stored.
Asking Questions
Enter a question in the Chat with Your Document section.
The system will find relevant document content and generate a response.
The AI-generated answer will be displayed instantly.
🏗️ Project Structure
privacy-ai/
├── myproject/
│   ├── settings.py  # Django project settings
│   ├── urls.py      # Global URL routing
├── myapp/
│   ├── templates/
│   │   ├── frontend.html  # Main frontend UI
│   ├── static/  # CSS/JS (if required)
│   ├── utils.py  # Text extraction, embedding, and AI functions
│   ├── forms.py  # File upload and question forms
│   ├── models.py  # Database models
│   ├── views.py  # Django views (backend logic)
│   ├── urls.py  # App-specific URL routing
├── media/  # Stores uploaded files
├── manage.py  # Django management script
├── .env  # API keys and environment variables
🛠️ Troubleshooting
Common Issues & Fixes
1️⃣ FAISS index not found

Ensure you've uploaded a file before asking questions.
Try deleting faiss_index/ and re-uploading.
2️⃣ No AI response or errors in terminal

Check .env for a valid GOOGLE_API_KEY.
Restart the server after setting the API key.
3️⃣ Django migration issues

python manage.py makemigrations
python manage.py migrate --run-syncdb
4️⃣ ModuleNotFoundError

Activate your virtual environment (source venv/bin/activate).
Run pip install -r requirements.txt to install dependencies.
🤝 Contributing
Contributions are welcome! Feel free to fork this repo and submit pull requests.

To Contribute:
Fork the repository.
Create a feature branch: git checkout -b feature-name
Commit changes: git commit -m "Added new feature"
Push to branch: git push origin feature-name
Submit a Pull Request.
🌟 Acknowledgments
Django for backend framework.
FAISS for efficient vector searching.
Google Generative AI for text embeddings and Q&A.
TailwindCSS for styling.
About
No description, website, or topics provided.
Resources
 Readme
 Activity
Stars
 0 stars
Watchers
 1 watching
Forks
 0 forks
Report repository
Releases
No releases published
Packages
No packages published
Languages
Python
65.4%
 
HTML
34.6%
Footer

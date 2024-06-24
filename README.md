## How to Use

### Setting Up

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your_username/chat-with-dms.git
   cd chat-with-dms

   ## Setup Environment Variables

1. **Create .streamlit folder:**
   - Create a `.streamlit` folder in the root directory of your project.

2. **Create secrets.toml file:**
   - Inside `.streamlit`, create a `secrets.toml` file to store sensitive data (similar to `.env` in other setups).

3. **Add OpenAI API key:**
   - Add your OpenAI API key to `secrets.toml`:
     ```toml
     # secrets.toml
     OPENAI_API_KEY = "your_openai_api_key_here"
     ```

## Configure Database (Optional)

- By default, the app is configured to save chat history using PostgreSQL provided by Supabase.
- If you prefer not to use Supabase, follow these steps:

  - Comment out the code in `database.py` related to database functions.
  - Replace the commented code with `pass` statements.

## Running the App

### Initialize Vector Database

1. **Run `run_first.py`:**
   - Execute `run_first.py` to create the vector database of your embeddings.
   - Provide the folder containing your JSON files as an argument:
     ```bash
     python run_first.py /path/to/your/json/files
     ```

### Launch the App

2. **Start Streamlit app:**
   - Use the following command to launch the Streamlit app:
     ```bash
     streamlit run app.py
     ```

### Enjoy Conversing with Your DMs

- Once launched, the app enables you to chat with your DMs, retrieve chat histories, and receive gift suggestions based on your conversations.

## Additional Notes

- **Contributions:** Contributions are welcome! Feel free to fork the repository, make improvements, and submit pull requests.
- **Feedback:** If you encounter any issues or have suggestions for improvements, please open an issue on GitHub.




# Resume LLM

- **Resume Upload:** Submit your resume for analysis.
- **Target Job Profile:** Specify the job profile you are targeting.
- **Strengths and Weaknesses Analysis:** Get a detailed analysis of your resume, highlighting strengths and weaknesses against the target job profile.
- **Enhanced Resume Output:** Receive an improved, simplified version of your resume, tailored to impress potential employers.

## Technical Setup:

### Setting Environment Variables

Before running the application, include the following environment variables:

```bash
export OPENAI_API_KEY='your_openai_api_key'
export MIXTRAL_API_KEY='your_mixtral_api_key'
```

### Local Setup

To run locally, follow these steps:

1. **Clone Repository:**
   ```bash
   git clone https://github.com/abhinav16aero/resumellm.git
   ```

2. **Navigate to AI_hackathon Directory:**
   ```bash
   cd resumellm
   ```

3. **Create Conda Environment:**
   ```bash
   python -m venv venv
   
   source venv\bin\activate
   ```

4. **Install Requirements:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run Streamlit Application:**
   ```bash
   streamlit run home.py
   ```

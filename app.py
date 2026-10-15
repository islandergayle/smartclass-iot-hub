import os
from google import genai

# --- GEMINI AI ASSISTANT MODULE ---
st.markdown("---")
st.markdown("### 🤖 SmartClass AI Copilot (Powered by Gemini)")
st.write("Type a natural language command to control the classroom environment automatically.")

user_prompt = st.text_input("Enter command:", placeholder="e.g., Prepare the room for a presentation at 21 degrees")

if st.button("Execute AI Command"):
    if user_prompt:
        try:
            # Initialize Gemini Client (reads from Streamlit secrets or environment variables)
            # You can set st.secrets["GEMINI_API_KEY"] in Streamlit Cloud settings
            api_key = st.secrets.get("GEMINI_API_KEY", os.environ.get("GEMINI_API_KEY"))
            
            if not api_key:
                st.error("Please configure your Gemini API Key in Streamlit Secrets.")
            else:
                client = genai.Client(api_key=api_key)
                
                prompt = f"""
                You are an intelligent IoT classroom assistant. Parse the user's request into a JSON-like action summary.
                User Request: "{user_prompt}"
                
                Provide a short, professional confirmation message explaining what classroom adjustments were made (e.g., AC temperature, lights brightness).
                """
                
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                )
                
                st.success("AI Action Executed Successfully!")
                st.markdown(f"**Response:** {response.text}")
                
        except Exception as e:
            st.error(f"Error connecting to Gemini API: {e}")
    else:
        st.warning("Please type a command first.")


import streamlit as st
from google import genai
from google.genai import types
from datetime import date

st.set_page_config(
    page_title="CampusClarity AI",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 CampusClarity AI")
st.caption("From college notices to clear next steps.")

st.info("Upload a notice. Find out what matters, what to do, and by when.")

uploaded_file = st.file_uploader(
    "Upload a college notice",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded notice", width="stretch")

    if st.button("Find my next steps", type="primary"):
        with st.spinner("Finding important actions and deadlines..."):
            try:
                client = genai.Client(
                    api_key=st.secrets["GEMINI_API_KEY"]
                )

                prompt = f"""
Today is {date.today().strftime('%d %B %Y')}.

Analyze this college notice for a student.
Keep the entire response under 120 words.

Use exactly these sections:

### What matters
State the main point in one sentence.

### Your next steps
List only concrete actions the student should take.
If no action is required, say so.

### Deadline and urgency
Give the exact deadline if stated.
Classify it as PAST, URGENT (within 48 hours),
UPCOMING, or NO DEADLINE STATED.
Use the current date above. Never invent a deadline.
If the date is ambiguous, say so.

### Important unknowns
Mention only missing information that could affect
the student's decision or next action.

Be concise. Do not repeat the whole notice.
Distinguish facts from assumptions. Never invent details.
"""

                response = client.models.generate_content(
                    model="gemma-4-26b-a4b-it",
                    contents=[
                        prompt,
                        types.Part.from_bytes(
                            data=uploaded_file.getvalue(),
                            mime_type=uploaded_file.type
                        )
                    ]
                )

                st.subheader("Your action plan")
                st.markdown(response.text)

                st.caption(
                    "AI-generated guidance. Verify critical dates "
                    "and requirements against the original notice."
                )

            except Exception as e:
                st.error(f"Analysis failed: {e}")

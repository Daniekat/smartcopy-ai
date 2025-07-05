import os, streamlit as st, openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

TEMPLATES = {
    "Facebook Ad": "Write a concise Facebook ad in {language} for a {business_type} selling {product}. Emphasise {usp}. CTA: {cta}",
    "WhatsApp Broadcast": "Compose a friendly WhatsApp marketing message in {language} for {business_name}. Offer: {offer}.",
    "Lead-Gen Post": "Craft an engaging social-media post in {language} that asks prospects a question about {pain_point} and invites them to click {link}."
}

st.title("SmartCopy AI")

language      = st.selectbox("Language / Taal", ["English", "Afrikaans"])
template_name = st.selectbox("Template", list(TEMPLATES.keys()))
business_type = st.text_input("Business type (e.g. bakery)")
product       = st.text_input("Product / service")
usp           = st.text_input("Unique selling point")
cta           = st.text_input("Call-to-action", "Order via WhatsApp")
offer         = st.text_input("Offer / promotion")
pain_point    = st.text_input("Pain point")
link          = st.text_input("Link / URL")

if st.button("Generate"):
    prompt = TEMPLATES[template_name].format(
        language=language, business_type=business_type, product=product,
        usp=usp, cta=cta, business_name=business_type, offer=offer,
        pain_point=pain_point, link=link
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=180
    )
    text = response.choices[0].message.content
    st.text_area("Result", text, height=200)
    st.download_button("Download .txt", text, file_name="copy.txt")

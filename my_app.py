import streamlit as st

st.write("Hello World: Getting Bore, Hello Brother!!")
st.title("Display Title use st.title()")
st.write("To write text st.write()")
st.header("I am header to write header use st.header()")
st.subheader("I am subheader to write subheader use st.subheader()")
st.text(" Hey I am simple text to write simple test use st.text()")
# to create hyperlink
st.markdown("[Streamlit](https://streamlit.io/)")
st.markdown("[streamlit CheatSheet](https://cheat-sheet.streamlit.app/)")
st.success("Succsess!")
st.info("Information")
st.warning("This is a warning")
st.error("This is an error")


from PIL import Image
img = Image.open("smj.jpg")
st.image(img,width=300, caption="Satyamev Jayate")

video_file = open("vid.mp4","rb")
video_bytes=video_file.read()
st.video(video_bytes)

st.video("https://www.youtube.com/watch?v=2v8urSwf8TI")
st.video("https://youtu.be/XvsQlwJJKwI?si=4ysmDLL5t8jeiZe2")



audio_file=open("song.mp3","rb")
audio_bytes=audio_file.read()
st.audio(audio_bytes, format="audio/mp3")

st.button("play")
st.header("Button widgets")


if st.button("play1"):
    st.text("Hello World") 

    
if st.button("play2"):
    st.text("Enjoy Music")
    st.video("https://www.youtube.com/watch?v=2v8urSwf8TI")
    
if st.checkbox("checkbox"):
    st.text("checkbox selected")
    st.video("https://youtu.be/a7gAiQQHIj8?si=cLVm_RWH2IB-XPBZ")
     
        
    












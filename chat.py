import streamlit as st

st.title('AI assistant for learning project')

with st.sidebar:
    st.text_input('Email: ')
    st.text_input('Password', type= 'password')
    st.text_input('Project: ')
    st.text_input('Name: ')

# st.write(st.session_state)

if 'messages' not in st.session_state.keys():
    st.session_state['messages'] = [{'role': 'assistant', 'content': 'How can I have you'}]

# st.write(st.session_state)

for message in st.session_state['messages']:
    with st.chat_message(message['role']):
        st.write(message['content'])

if promt:= st.chat_input('Input:'):
    st.session_state['messages'].append({'user': 'user', 'content': promt})
    with st.chat_message('user'):
        st.write(promt)

if st.session_state['messages'][-1]['role'] == 'user':
    with st.chat_message('assistant'):
        with st.spinner('Loading: '):
            respone = callable
            st.write(respone)
    st.session_state['message'].append({'role': 'assistant', 'content': respone})

 
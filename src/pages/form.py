import streamlit as st
import datetime as dt

form = st.form(key='sample_form')
with form:
    name = st.text_input('名前')
    address = st.text_input('住所')

    age_category = st.selectbox(
        '年齢層',
        (
            '10歳未満',
            '20代',
            '30代',
            '40代',
            '50代',
            '60歳以上'
        )
    )

    gender = st.radio(
        '性別',
        (
            '男性',
            '女性',
            '回答なし'
        )
    )

    hobby = st.multiselect(
        '趣味',
        (
            'スポーツ',
            '読書',
            'プログラミング',
            'アニメ',
            '映画',
            '釣り',
            '料理'
        )
    )

    mail_subscribe = st.checkbox('メールマガジンを受け取る')

    start_date = st.date_input(
        '開始日',
        dt.datetime.now()
    )

    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')

    if submit_btn:
        st.text(f'ようこそ！{name}さん！{address}に書籍を送りました！')
        st.text(f'年齢層: {age_category}')
        st.text(f'性別: {gender}')
        st.text(f'趣味: {", ".join(hobby)}')
        st.text(f'メールマガジンを受け取る: {mail_subscribe}')
        st.text(f'開始日: {start_date}')

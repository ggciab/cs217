import streamlit as st
from ner import SpacyDocument
from annotated_text import annotated_text, annotation
import matplotlib.pyplot as plt

text = st.text_area('Please enter text to process', "")
st.button('run')
sd = SpacyDocument(text)

with st.expander("Annotated Entities"):
    with st.form("Entities_form"):
        # Get which entities are wanted for annotation.
        entities = sd.get_entities()
        entitiy_labels = list(set([l for s, e, l, t in entities]))
        desired_entities = st.multiselect("Select which entities you'd like annotated:",
                                          entitiy_labels)
        all_labels = st.checkbox("Select all entities")
        if all_labels:
            desired_entities = entitiy_labels

        submitted = st.form_submit_button("Submit")
        if submitted:
            # Output annotated entities text
            annotated_entities = sd.get_entities_for_annotated_text(desired_entities)
            annotated_text(*annotated_entities)
            st.write("\n")

with st.expander("Chart: Percentage of Characters per Entities"):
    # Draw pie chart of Entities
    labels, percents = sd.get_percentages_for_labels()
    fig1, ax1 = plt.subplots()
    ax1.pie(percents, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')  # Draw pie as a circle
    st.pyplot(fig1)

with st.expander("Annotated POS Tags"):
    with st.form("POS_tags_form"):
        pos_tags = sd.get_pos_tags()

        desired_POS_tags = st.multiselect("Select which POS tags you'd like annotated:",
                                          list(set(pos_tags)))
        all_tags = st.checkbox("Select all POS tags")
        if all_tags:
            desired_POS_tags = list(set(pos_tags))
        submitted = st.form_submit_button("Submit")
        if submitted:
            annotated_POS_tags = sd.get_POS_tags_for_annotated_text(desired_POS_tags)
            annotated_text(*annotated_POS_tags)
            st.write("\n")
            # st.write("\n\nPOS tags", {tok: pos
            #                           for tok, pos in zip(sd.get_tokens(), pos_tags)
            #                           if pos in desired_POS_tags})

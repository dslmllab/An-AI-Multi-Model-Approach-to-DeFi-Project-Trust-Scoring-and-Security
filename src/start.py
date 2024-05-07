import streamlit as st
import requests
import requests
from textwrap import fill
import pandas as pd
import os
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import getDeFiProjectData
import summaryLLM
#projects_df = pd.read_csv("DeFi Projects.csv")
projects_df = pd.read_json("defillama_export.json")

project_names = projects_df["name"].tolist()

def main():
    st.set_page_config(page_title="DeFi Projects Analyzer")

    with open("style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    st.markdown("""
    <div class="title">
        <h1>DeFi Project Analyzer</h1>
    </div>
    """, unsafe_allow_html=True)


    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    st.sidebar.markdown('<h2 class="sidebar-title">DeFi Projects</h2>', unsafe_allow_html=True)
    #selected_project = st.sidebar.selectbox("Select a project", projects_df["Project"].tolist(),index=None,placeholder="Choose an option")
    selected_project = st.sidebar.selectbox("Select a DeFi project", project_names)
    githuburl = st.sidebar.text_input("Paste DeFi project or smart contract Address")


    code = st.sidebar.text_area("Paste code here", height=300, )
    st.sidebar.markdown('</div>', unsafe_allow_html=True)

    if selected_project or githuburl or code:

        if code:
            source_code = code
            contract_name = "Manually pasted code"

        elif selected_project:
            #project_data = projects_df[projects_df["Project"] == selected_project].iloc[0]
            project_data = projects_df[projects_df["name"] == selected_project].iloc[0]
            #contract_address = project_data["Smart Contract Address (Ethereum Mainnet)"]
            contract_address = project_data["address"]
            tokenid = project_data["gecko_id"]


            source_code, contract_name, compiler_version = getDeFiProjectData.get_contract_info(contract_address)

            contract_abi, contract_transactions = getDeFiProjectData.get_contract_details(contract_address)
            #st.write(project_data)
            st.header(project_data["name"])
            st.image(project_data['logo'])
            st.write("URL:", project_data["url"])
            st.write("Chain:", project_data["chain"])
            st.write("Category:", project_data["category"])
            st.write("Description:", project_data["description"])
            st.write("TVL:", project_data["tvl"])

            st.subheader("Chain TVLs")
            st.json(project_data["chainTvls"])



        elif githuburl:
            contract_address = githuburl

            source_code, contract_name, compiler_version = getDeFiProjectData.get_contract_info(contract_address)
            contract_abi, contract_transactions = getDeFiProjectData.get_contract_details(contract_address)

        if source_code:
            #project_data = 'code'
            summaryLLM.start_summary(tokenid,project_data,source_code,contract_name,compiler_version,contract_abi,contract_transactions)
            #analysisllmsm =  summaryLLM.start_summary_sc(source_code)

            #with st.expander('Smart contract LLM'):
            #st.markdown(analysisllmsm)



        else:
            st.warning("Failed to fetch contract information from Etherscan.")


if __name__ == "__main__":
    main()
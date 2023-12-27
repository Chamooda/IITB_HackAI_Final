# HackAI Documentation

## Introduction
This project aims to provide a solution for screening and matching resumes with job description using Fetch AI's UAgents LangChain, ChatGPT, Natural Language Processing(NLP) and Machine Learning. The system analyzes resumes to extract relevant information, match skills, and evaluate the suitability of candidates for a given job description.

## Assumptions
- Resumes are provided in PDF format.
- The system uses LangChain and ChatGPT for natural language processing(NLP).
- Fetch AI's UAgents forms the base of the project for enhancing and working of the entire system.
  
## Pre-Requisites
- Python 3.11 preffered
- ### Dependencies:
  - These are the Python libraries and frameworks used in this project. You can install them using the provided package manager or by running:
    ``` bash
     pip install <package_name>
    ```

  - ### OpenAI API
    - ### Description:
       Powerful language model developed by OpenAI.
    - ### Website:
       https://platform.openai.com/
    - ### Installation:
      ``` bash
      pip install openai
      ```

  - ### PyPDF2
    - ### Description:
       A Pure-Python library built as a PDF toolkit.
    - ### Website:
       https://pypi.org/project/PyPDF2/
    - ### Installation:
      ``` bash
      pip install PyPDF2
      ```

  - ### Fecth AI uAgents Library
    - ### Description:
       Library for interacting with Fetch.ai's intelligent agents.
    - ### Website:
       https://fetch.ai/
    - ### Installation:
      ``` bash
      pip install uagents
      ```
  

## Working
The following flowchart indicates how Alice, Bob and Converter operates:
## Run the main Script
* To run the project and its agents:
```bash
python bob.py
```
Upon running this file it will ask for job tittle and job description. This will create a jobs.json file which will contain the data entered. 

```bash
cd src
python main.py
```
This will check through all of the resumes in the given folder and will give approximate score on how much match with the given job description. 
The job description will be matched through jobs.json.


![image](https://github.com/Ayancodes2003/hackAIdocumentation/assets/119226120/4df31806-e479-4ef0-8583-131d386dcb70)


## Video Demo
```bash
https://drive.google.com/file/d/1U2HxZTIH6He51norlsVEY4m3EDDGU6ya/view?usp=sharing
```

## Future Scope
- Integration with additional AI models for enhanced resume analysis.
- Improved user interface and user experience meeting industry standards to smoothen the hiring process.
- Support for more file formats and data sources.
- Integration with other recruitment tools and platforms.

## Shortcomings
- There will be a delay of 20 secs between every response
- The only accepted file format is PDF as of now. 

## Contact us
- For any queries/doubts feel free to contact
  pushpak.agrawal2022@vitstudent.ac.in

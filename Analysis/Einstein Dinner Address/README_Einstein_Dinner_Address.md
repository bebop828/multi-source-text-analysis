
# Einstein_Address.ipynb 

*"The war is won, but the peace is not."* — Albert Einstein
## Overview

This Jupyter Notebook explores Albert Einstein’s powerful speech delivered at the **5th Nobel Anniversary Dinner on December 10, 1945**. The speech, given shortly after the end of World War II and the atomic bombings, is a reflection on the ethical responsibilities of scientists, the dangers of geopolitical division, and the need for global peace and justice.

## Contents


- **Audio Source**: [YouTube link](https://www.youtube.com/watch?v=twLxPG75k-8) — Duration: 9:09.
- **Summary and Interpretation**:
  - Moral reflections on the development and use of nuclear weapons.
  - Condemnation of ongoing injustices, particularly towards European Jews.
  - Call for a shift in political attitudes to avoid the collapse of civilization.
  - Use of **ethos**, **pathos**, and **logos** in the speech.

## Purpose

This notebook aims to:

- Highlight the **historical and ethical implications** of his message.

To achieve this, a combination of **natural language processing (NLP)** and **visual analysis techniques** were used:

- Analyze the **rhetorical strategies** Einstein employed.
- **Sentiment Analysis**: Tools such as NLTK and TextBlob were employed to extract and visualize emotional tone.
- **N-Gram Modeling**: To identify recurring word patterns and themes across the speech.
- **Topic Modeling (LDA)**: Used to uncover latent thematic structures in Einstein’s address.
- **Word Clouds**: Created to highlight the most frequently used terms visually, helping infer central topics at a glance.
- **Named Entity Recognition & Frequency Analysis**: Provided deeper context into whom and what Einstein emphasized.

These analytical steps contribute to both the **qualitative** and **quantitative** understanding of Einstein’s message.

## Usage

This notebook is best used for:
- Educational purposes in history, rhetoric, ethics, and political science.
- Classroom discussions on post-WWII geopolitics and scientific responsibility.
- Analytical writing and speech analysis practice.

## Requirements

The following Python libraries are required to run this notebook, along with brief explanations of their purpose:

- `nltk`: Natural language toolkit used for tokenization, stopwords, sentiment analysis, and n-gram modeling.
- `textblob`: Provides simple API for common NLP tasks like sentiment and noun phrase extraction.
- `gensim`: Used for topic modeling with Latent Dirichlet Allocation (LDA).
- `matplotlib.pyplot` and `seaborn`: For data visualization and styling of plots.
- `pandas`: To manipulate and analyze tabular data efficiently.
- `re`: Regular expressions used for text cleaning and preprocessing.
- `collections.Counter`: For counting word or token frequencies.
- `wordcloud.WordCloud, STOPWORDS`: For generating visually compelling word clouds.


Ensure you’ve downloaded the NLTK resources before use:
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')
```

## Project Workflow & Acknowledgments

The project began by extracting the original audio of Einstein's address from YouTube and converting it to an `.mp3` format.

To transcribe the speech:
- I used **AssemblyAI**, a powerful speech-to-text service, to convert the `.mp3` file into a structured `.csv` transcription.

Once the transcription was available:
- The `.csv` file was read into a **Python Jupyter Notebook** where the textual analysis and visualizations were performed.

Throughout the project:
- I leveraged AI-assisted tools including **ChatGPT**, **Perplexity**, and **Liner** for research, coding support, and refinement of analysis methods and explanations.


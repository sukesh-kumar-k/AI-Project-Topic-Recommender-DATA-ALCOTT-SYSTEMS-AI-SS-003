# AI Project Topic Recommender

## AI & Data Science Internship – Task AI-SS-003

## Project Overview

The **AI Project Topic Recommender** is a Python-based recommendation system developed as part of the **AI & Data Science Internship** at **Data Alcott Systems**.

The system recommends suitable project topics to students based on their interests, skills, academic background, and experience level.

It uses **Natural Language Processing (NLP)**, **TF-IDF Vectorization**, **Cosine Similarity**, and **Content-Based Filtering** to compare student profiles with available project topics and generate personalized recommendations.

---

## Task Details

- **Task ID:** AI-SS-003
- **Task Name:** AI Project Topic Recommender
- **Domain:** Student Support & Internship Management NLP
- **Technology Stack:** Python, NLP, TF-IDF, Content-Based Filtering
- **Company:** Data Alcott Systems
- **Student:** Sukesh Kumar K
- **Student Code:** DAS006290
- **Status:** Completed

---

## Objectives

The main objectives of this project are:

- To understand NLP fundamentals
- To perform text preprocessing
- To use TF-IDF Vectorization
- To calculate Cosine Similarity
- To match student interests and skills with project topics
- To generate personalized project recommendations
- To rank project topics according to their relevance
- To filter recommendations based on difficulty level

---

## Key Features

### 1. Student Interest Profile

The system uses student information such as:

- Student ID
- Name
- Interests
- Skills
- Academic Background
- Experience Level

### 2. Project Topic Database

Project topics are stored in `projects.csv`.

The dataset contains:

- Topic ID
- Project Title
- Domain
- Description
- Technology Stack
- Difficulty
- Duration

### 3. Text Preprocessing

The system performs NLP preprocessing including:

- Lowercase conversion
- Removal of special characters
- Tokenization
- Stopword removal
- Lemmatization

### 4. TF-IDF Vectorization

TF-IDF (Term Frequency–Inverse Document Frequency) is used to convert text data into numerical vectors.

This allows the system to compare student profiles with project topics.

### 5. Cosine Similarity

Cosine Similarity is used to calculate how closely a student's profile matches each project topic.

A higher similarity score indicates a stronger match.

### 6. Top-N Recommendations

The system ranks project topics based on their similarity scores and displays the **Top 5 recommendations**.

### 7. Difficulty Filtering

The system allows users to filter project recommendations according to:

- Beginner
- Intermediate
- Advanced

---

## Technologies Used

- Python
- Pandas
- NumPy
- NLTK
- Scikit-learn
- TF-IDF
- Cosine Similarity
- Content-Based Filtering
- CSV

---

## Project Structure

AI-Project-Topic-Recommender/
│
├── projects.csv
├── recommendation.py
├── requirements.txt
└── students.csv

### File Description

| File | Description |
|------|-------------|
| `recommendation.py` | Main Python program containing the recommendation system |
| `projects.csv` | Contains the available project topics |
| `students.csv` | Contains sample student profiles |
| `requirements.txt` | Contains the required Python libraries |

---

## Dataset Information

### projects.csv

The `projects.csv` file contains project topic information with the following columns:

- `topic_id`
- `title`
- `domain`
- `description`
- `tech_stack`
- `difficulty`
- `duration`

The project contains topics from different areas such as:

- Artificial Intelligence
- Natural Language Processing
- Machine Learning
- Data Science
- Computer Vision
- Education
- Agriculture

### students.csv

The `students.csv` file contains student profile information with the following columns:

- `student_id`
- `name`
- `interests`
- `skills`
- `academic_background`
- `experience_level`

The dataset contains sample students with different interests, skills, academic backgrounds, and experience levels.

---

## How the System Works

The recommendation process follows these steps:

1. Student profile is selected.
2. Student interests and skills are collected.
3. Text preprocessing is performed.
4. Project topic information is loaded from `projects.csv`.
5. Project text is preprocessed.
6. TF-IDF Vectorization converts the text into numerical vectors.
7. Cosine Similarity calculates the similarity between the student profile and project topics.
8. Project topics are ranked according to similarity scores.
9. Top 5 project recommendations are displayed.
10. The user can optionally apply a difficulty filter.

---

## Installation

### Step 1: Install Python

Make sure Python 3.x is installed on your computer.

Check the Python version using:

    python --version

### Step 2: Open the Project

Open the `AI-Project-Topic-Recommender` folder in Visual Studio Code.

### Step 3: Install Required Libraries

Open the VS Code terminal and run:

    pip install -r requirements.txt

### Step 4: Run the Program

Run:

    python recommendation.py

---

## How to Use

When the program starts, it displays the available students.

Example:

    Available Students:

    S001 - Alice - Beginner
    S002 - Bob - Intermediate
    S003 - Charlie - Advanced
    S004 - Diana - Intermediate
    S005 - Eve - Beginner
    S006 - Frank - Advanced
    S007 - Grace - Intermediate
    S008 - Henry - Beginner

Enter a Student ID when prompted:

    Enter Student ID (example: S001): S001

The system then displays the student's profile and generates personalized project recommendations.

---

## Test Case 1 – Beginner Student

### Student Selected

    Student: Alice
    Interests: AI NLP Chatbot Student Support
    Skills: Python NLP NLTK

### Recommended Projects

1. **AI Chatbot for Student Support**
   - Topic ID: T001
   - Domain: AI
   - Difficulty: Beginner
   - Duration: 3 weeks
   - Tech Stack: Python NLP NLTK Flask
   - Match Score: 65.35%

2. **Voice Assistant Using NLP**
   - Topic ID: T013
   - Domain: NLP
   - Difficulty: Intermediate
   - Duration: 5 weeks
   - Tech Stack: Python NLP Speech Recognition
   - Match Score: 22.71%

3. **Sentiment Analysis of Social Media**
   - Topic ID: T006
   - Domain: NLP
   - Difficulty: Beginner
   - Duration: 3 weeks
   - Tech Stack: Python NLP NLTK Scikit-learn
   - Match Score: 22.36%

4. **Fake News Detection**
   - Topic ID: T003
   - Domain: NLP
   - Difficulty: Intermediate
   - Duration: 4 weeks
   - Tech Stack: Python NLP TF-IDF Scikit-learn
   - Match Score: 16.31%

5. **Student Performance Prediction**
   - Topic ID: T010
   - Domain: Education
   - Difficulty: Beginner
   - Duration: 3 weeks
   - Tech Stack: Python Pandas Scikit-learn Machine Learning
   - Match Score: 15.49%

### Beginner Difficulty Filter

The Beginner difficulty filter was tested successfully.

    Projects matching Beginner difficulty:
    - AI Chatbot for Student Support (65.35%)
    - Sentiment Analysis of Social Media (22.36%)
    - Student Performance Prediction (15.49%)

    Recommendation process completed.

---

## Test Case 2 – Advanced Student

### Student Selected

    Student: Charlie
    Interests: Computer Vision AI Images
    Skills: Python OpenCV TensorFlow

### Recommended Projects

1. **Traffic Sign Recognition**
   - Topic ID: T014
   - Domain: Computer Vision
   - Difficulty: Advanced
   - Duration: 7 weeks
   - Tech Stack: Python OpenCV TensorFlow CNN
   - Match Score: 57.78%

2. **Smart Attendance System**
   - Topic ID: T004
   - Domain: Computer Vision
   - Difficulty: Advanced
   - Duration: 6 weeks
   - Tech Stack: Python OpenCV Face Recognition
   - Match Score: 28.95%

3. **Plant Disease Detection**
   - Topic ID: T008
   - Domain: Agriculture
   - Difficulty: Advanced
   - Duration: 7 weeks
   - Tech Stack: Python TensorFlow OpenCV Deep Learning
   - Match Score: 22.20%

4. **Sales Prediction System**
   - Topic ID: T007
   - Domain: Data Science
   - Difficulty: Beginner
   - Duration: 4 weeks
   - Tech Stack: Python Pandas Scikit-learn Regression
   - Match Score: 8.97%

5. **Weather Prediction Using Machine Learning**
   - Topic ID: T012
   - Domain: Data Science
   - Difficulty: Intermediate
   - Duration: 5 weeks
   - Tech Stack: Python Pandas Scikit-learn Time Series
   - Match Score: 7.11%

### Advanced Difficulty Filter

The Advanced difficulty filter was tested successfully.

    Projects matching Advanced difficulty:
    - Traffic Sign Recognition (57.78%)
    - Smart Attendance System (28.95%)
    - Plant Disease Detection (22.20%)

    Recommendation process completed.

---

## Recommendation Method

This project uses **Content-Based Filtering**.

The system compares the student's interests and skills with the descriptions and technology stacks of available project topics.

### TF-IDF Vectorization

TF-IDF stands for **Term Frequency–Inverse Document Frequency**.

It is used to convert text data into numerical vectors and helps identify important words in student profiles and project topics.

### Cosine Similarity

Cosine Similarity is used to measure the similarity between the student profile and project topic vectors.

The formula is:

    Cosine Similarity = (A · B) / (||A|| × ||B||)

A higher similarity score indicates a stronger match between the student's profile and the project topic.

---

## Sample Student Profile

Example:

    Student ID       : S001
    Name             : Alice
    Interests        : AI NLP Chatbot Student Support
    Skills           : Python NLP NLTK
    Experience Level : Beginner

Based on this information, the system identifies project topics related to AI, NLP, chatbots, Python, and student support.

---

## Requirements

The project requires:

- Python 3.x
- pandas
- numpy
- scikit-learn
- nltk

All required libraries are listed in `requirements.txt`.

The program also uses the following NLTK resources:

- Stopwords
- WordNet

These resources are downloaded automatically when required by the program.

---

## Learning Outcomes

Through this project, I learned:

- Natural Language Processing fundamentals
- Text preprocessing
- Stopword removal
- Lemmatization
- TF-IDF Vectorization
- Cosine Similarity
- Content-Based Recommendation
- Working with CSV datasets using Pandas
- Creating personalized recommendation systems
- Ranking project recommendations using similarity scores
- Filtering recommendations based on difficulty

---

## Future Improvements

The system can be further enhanced with:

- Project topic clustering
- Topic trend analysis
- Domain-based filtering
- Advanced topic modeling
- User feedback and ratings
- Flask or Django web interface
- Project topic visualization
- BERT or Transformer-based recommendations
- Larger student and project datasets

---

## Conclusion

The **AI Project Topic Recommender** successfully recommends suitable project topics based on student interests, skills, academic background, and experience level.

The system uses **Natural Language Processing**, **TF-IDF Vectorization**, **Cosine Similarity**, and **Content-Based Filtering** to identify and rank relevant project topics.

The implemented system supports **Top 5 project recommendations** and **difficulty-based filtering** for Beginner, Intermediate, and Advanced projects.

The project demonstrates a practical application of **Artificial Intelligence and Natural Language Processing in the Student Support domain**.

---

## Internship Information

- **Company:** Data Alcott Systems
- **Task ID:** AI-SS-003
- **Task Name:** AI Project Topic Recommender
- **Domain:** Student Support & Internship Management NLP
- **Technology Stack:** Python, NLP, TF-IDF, Content-Based Filtering
- **Student:** Sukesh Kumar K
- **Student Code:** DAS006290

---

## Author

**Sukesh Kumar K**

MCA Student

AI & Data Science Internship

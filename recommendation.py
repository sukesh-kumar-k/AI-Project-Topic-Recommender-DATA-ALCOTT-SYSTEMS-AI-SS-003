# AI Project Topic Recommender
# Data Alcott Systems - AI & Data Science Internship
# Task ID: AI-SS-003

import pandas as pd
import numpy as np
import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Download required NLTK resources
nltk.download("stopwords")
nltk.download("wordnet")


class ProjectTopicRecommender:

    def __init__(self):

        # NLP tools
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words("english"))

        # Load datasets
        self.projects_df = pd.read_csv("projects.csv")
        self.students_df = pd.read_csv("students.csv")

        # Prepare project text
        self.projects_df["combined_text"] = (
            self.projects_df["title"].fillna("") + " " +
            self.projects_df["domain"].fillna("") + " " +
            self.projects_df["description"].fillna("") + " " +
            self.projects_df["tech_stack"].fillna("")
        )

        # Clean project text
        self.projects_df["clean_text"] = (
            self.projects_df["combined_text"]
            .apply(self.preprocess_text)
        )

        # Create TF-IDF vectorizer
        self.vectorizer = TfidfVectorizer(
            stop_words="english"
        )

        # Create vectors for all projects
        self.project_vectors = self.vectorizer.fit_transform(
            self.projects_df["clean_text"]
        )

    # -----------------------------------------
    # TEXT PREPROCESSING
    # -----------------------------------------

    def preprocess_text(self, text):

        text = str(text).lower()

        # Remove special characters and numbers
        text = re.sub(r"[^a-zA-Z\s]", " ", text)

        # Split text into words
        words = text.split()

        # Remove stopwords and short words
        words = [
            word for word in words
            if word not in self.stop_words and len(word) > 2
        ]

        # Lemmatization
        words = [
            self.lemmatizer.lemmatize(word)
            for word in words
        ]

        return " ".join(words)

    # -----------------------------------------
    # GET STUDENT
    # -----------------------------------------

    def get_student(self, student_id):

        student = self.students_df[
            self.students_df["student_id"] == student_id
        ]

        if student.empty:
            return None

        return student.iloc[0]

    # -----------------------------------------
    # RECOMMEND PROJECTS
    # -----------------------------------------

    def recommend_projects(self, student_id, top_n=5):

        student = self.get_student(student_id)

        if student is None:
            return None

        # Combine student information
        student_profile = (
            str(student["interests"]) + " " +
            str(student["skills"]) + " " +
            str(student["academic_background"])
        )

        # Preprocess student profile
        clean_profile = self.preprocess_text(student_profile)

        # Convert student profile into TF-IDF vector
        student_vector = self.vectorizer.transform(
            [clean_profile]
        )

        # Calculate cosine similarity
        similarity_scores = cosine_similarity(
            student_vector,
            self.project_vectors
        )[0]

        # Get highest similarity indexes
        top_indexes = np.argsort(
            similarity_scores
        )[::-1][:top_n]

        recommendations = []

        for index in top_indexes:

            project = self.projects_df.iloc[index]

            recommendations.append({
                "topic_id": project["topic_id"],
                "title": project["title"],
                "domain": project["domain"],
                "difficulty": project["difficulty"],
                "duration": project["duration"],
                "tech_stack": project["tech_stack"],
                "score": round(
                    similarity_scores[index] * 100, 2
                )
            })

        return recommendations

    # -----------------------------------------
    # FILTER BY DIFFICULTY
    # -----------------------------------------

    def filter_by_difficulty(
        self,
        recommendations,
        difficulty
    ):

        return [
            project
            for project in recommendations
            if project["difficulty"].lower()
            == difficulty.lower()
        ]

    # -----------------------------------------
    # FILTER BY DOMAIN
    # -----------------------------------------

    def filter_by_domain(
        self,
        recommendations,
        domain
    ):

        return [
            project
            for project in recommendations
            if project["domain"].lower()
            == domain.lower()
        ]

    # -----------------------------------------
    # DISPLAY RECOMMENDATIONS
    # -----------------------------------------

    def display_recommendations(
        self,
        recommendations
    ):

        if not recommendations:
            print("No recommendations found.")
            return

        print("\n" + "=" * 70)
        print("🎯 RECOMMENDED PROJECT TOPICS")
        print("=" * 70)

        for number, project in enumerate(
            recommendations,
            start=1
        ):

            print(f"\n{number}. {project['title']}")
            print(f"   Topic ID   : {project['topic_id']}")
            print(f"   Domain     : {project['domain']}")
            print(f"   Difficulty : {project['difficulty']}")
            print(f"   Duration   : {project['duration']}")
            print(f"   Tech Stack : {project['tech_stack']}")
            print(f"   Match Score: {project['score']}%")

        print("\n" + "=" * 70)


# =====================================================
# MAIN PROGRAM
# =====================================================

if __name__ == "__main__":

    print("\n" + "=" * 70)
    print("💡 AI PROJECT TOPIC RECOMMENDER")
    print("=" * 70)

    # Create recommender
    recommender = ProjectTopicRecommender()

    print("\nAvailable Students:")

    for _, student in recommender.students_df.iterrows():

        print(
            f"{student['student_id']} - "
            f"{student['name']} - "
            f"{student['experience_level']}"
        )

    # Ask user for student ID
    student_id = input(
        "\nEnter Student ID (example: S001): "
    ).strip().upper()

    # Generate recommendations
    recommendations = recommender.recommend_projects(
        student_id,
        top_n=5
    )

    if recommendations is None:

        print("\n❌ Student not found.")

    else:

        student = recommender.get_student(student_id)

        print(
            f"\nStudent: {student['name']}"
        )

        print(
            f"Interests: {student['interests']}"
        )

        print(
            f"Skills: {student['skills']}"
        )

        # Display recommendations
        recommender.display_recommendations(
            recommendations
        )

        # Difficulty filter
        print("\n🔍 Difficulty Filter")
        difficulty = input(
            "Enter difficulty "
            "(Beginner/Intermediate/Advanced) "
            "or press Enter to skip: "
        ).strip()

        if difficulty:

            filtered = recommender.filter_by_difficulty(
                recommendations,
                difficulty
            )

            print(
                f"\nProjects matching "
                f"{difficulty} difficulty:"
            )

            if filtered:

                for project in filtered:

                    print(
                        f"- {project['title']} "
                        f"({project['score']}%)"
                    )

            else:

                print("No matching projects found.")

    print("\n✅ Recommendation process completed.")
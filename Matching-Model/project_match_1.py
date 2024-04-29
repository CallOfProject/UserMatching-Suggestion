# Kullanıcı sınıfı tanımı
class User:
    def __init__(self, user_id, username, universities, user_tags, experiences):
        self.user_id = user_id
        self.username = username
        self.universities = universities
        self.user_tags = user_tags
        self.experiences = experiences


# Proje sınıfı tanımı
class Project:
    def __init__(self, project_id, project_name, project_tags):
        self.project_id = project_id
        self.project_name = project_name
        self.project_tags = project_tags

# user-id, username,     

# Daha fazla kullanıcı örnek verisi
users = [
    User(1, "alice", ["Harvard", "Stanford", "MIT"], ["Python", "Machine Learning", "Data Science", "AI"], ["Data Scientist", "Analyst", "Researcher"]),
    User(2, "bob", ["MIT", "Caltech", "UC Berkeley", "Stanford"], ["Python", "Deep Learning", "Software Engineering"], ["Software Engineer", "Full Stack Developer", "Data Engineer"]),
    User(3, "charlie", ["Stanford", "Oxford", "Cambridge"], ["Data Analysis", "Machine Learning", "Big Data"], ["Researcher", "Data Analyst", "Statistician"]),
    User(4, "david", ["Harvard", "Yale", "Princeton"], ["Data Science", "Machine Learning", "Artificial Intelligence"], ["Data Scientist", "AI Researcher", "ML Engineer"]),
    User(5, "eve", ["Caltech", "Stanford", "UC Berkeley"], ["Quantum Computing", "Physics", "Python"], ["Quantum Researcher", "Physicist", "Engineer"]),
    User(6, "frank", ["Harvard", "UC Berkeley", "Oxford"], ["Python", "AI", "Statistics", "Data Science"], ["Statistician", "Data Scientist", "Analyst"]),
    User(7, "grace", ["Yale", "Oxford", "Princeton"], ["AI", "Deep Learning", "Robotics"], ["AI Engineer", "Robotics Engineer", "Software Engineer"]),
    User(8, "test", ["Yale", "Oxford", "Princeton"], ["Web", "Java", "Robotics"], ["AI Engineer", "Robotics Engineer", "Software Engineer"]),
]

# Daha fazla proje örnek verisi
projects = [
    Project(101, "AI Research", ["Machine Learning", "Deep Learning", "Artificial Intelligence"]),
    Project(102, "Data Analysis Tool", ["Data Analysis", "Python", "Statistics"]),
    Project(103, "Software Development", ["Software Engineering", "Python", "JavaScript"]),
    Project(104, "Quantum Computing", ["Quantum Computing", "Physics", "Python"]),
    Project(105, "Robotics and AI", ["Robotics", "AI", "Deep Learning"]),
    Project(106, "Big Data Analytics", ["Big Data", "Data Analysis", "Statistics"]),
    Project(107, "AI in Healthcare", ["AI", "Machine Learning", "Healthcare"]),
    Project(108, "Call-of-Project", ["Java", "Spring Boot", "Restful Service"]),
]

# Proje önerisi fonksiyonu
def recommend_projects_for_user(user, projects):
    recommended_projects = []

    for project in projects:
        common_tags = set(user.user_tags).intersection(set(project.project_tags))

        if common_tags:
            recommended_projects.append({
                "project_name": project.project_name,
                "common_tags": list(common_tags),
            })

    return recommended_projects

# Kullanıcı öneri algoritmaları
def recommend_users_by_tags(target_user, all_users):
    recommended_users = []

    for user in all_users:
        if user.user_id == target_user.user_id:
            continue

        common_tags = set(target_user.user_tags).intersection(user.user_tags)

        if common_tags:
            recommended_users.append({
                "username": user.username,
                "common_tags": list(common_tags),
            })

    return recommended_users


def recommend_users_by_universities(target_user, all_users):
    recommended_users = []

    for user in all_users:
        if user.user_id == target_user.user_id:
            continue

        common_universities = set(target_user.universities).intersection(user.universities)

        if common_universities:
            recommended_users.append({
                "username": user.username,
                "common_universities": list(common_universities),
            })

    return recommended_users


def recommend_users_by_experiences(target_user, all_users):
    recommended_users = []

    for user in all_users:
        if user.user_id == target_user.user_id:
            continue

        common_experiences = set(target_user.experiences).intersection(user.experiences)

        if common_experiences:
            recommended_users.append({
                "username": user.username,
                "common_experiences": list(common_experiences),
            })

    return recommended_users

# Hedef kullanıcı ve proje önerileri
target_user = users[7]  # Alice
recommended_projects = recommend_projects_for_user(target_user, projects)

# Önerilen projeleri yazdır
print("Proje önerileri:")
for rec in recommended_projects:
    print(f"Önerilen Proje: {rec['project_name']}, Ortak Etiketler: {rec['common_tags']}")

# Üniversitelere göre öneri
print("\nÜniversitelere göre öneriler:")
recommendations_by_universities = recommend_users_by_universities(target_user, users)
for rec in recommendations_by_universities:
    print(f"Önerilen Kullanıcı: {rec['username']}, Ortak Üniversiteler: {rec['common_universities']}")
    
# İşyerlerine göre öneri
print("\nİşyerlerine göre öneriler:")
recommendations_by_experiences = recommend_users_by_experiences(target_user, users)
for rec in recommendations_by_experiences:
    print(f"Önerilen Kullanıcı: {rec['username']}, Ortak Deneyimler: {rec['common_experiences']}")

# User Tags'e göre öneri
print("User Tags'e göre öneriler:")
recommendations_by_tags = recommend_users_by_tags(target_user, users)
for rec in recommendations_by_tags:
    print(f"Önerilen Kullanıcı: {rec['username']}, Ortak Etiketler: {rec['common_tags']}")